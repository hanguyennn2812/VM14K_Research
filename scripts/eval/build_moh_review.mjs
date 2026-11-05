// Run with the supplied artifact-tool runtime linked at OUTPUT_DIR/node_modules.
import fs from 'node:fs/promises';
import path from 'node:path';
import { createRequire } from 'node:module';
import { pathToFileURL } from 'node:url';
import { fileURLToPath } from 'node:url';
import { execFileSync } from 'node:child_process';

const [input, output] = process.argv.slice(2);
if (!input || !output) throw new Error('Usage: node build_moh_review.mjs payload.json output.xlsx');
const outDir = path.dirname(path.resolve(output));
const require = createRequire(path.join(outDir, 'package.json'));
const { Workbook, SpreadsheetFile } = await import(pathToFileURL(require.resolve('@oai/artifact-tool')).href);
const data = JSON.parse(await fs.readFile(input, 'utf8'));
const wb = Workbook.create();
const review = wb.worksheets.add('Duyệt 60');
const source = wb.worksheets.add('Đoạn gốc');
const summary = wb.worksheets.add('Tổng kết');
const regression = wb.worksheets.add('BatDong_vong1');
const ratings = ['Đúng', 'Sai', 'Không rõ', 'Không lâm sàng'];
const tags = ['nhiều đáp án đúng', 'không khớp văn bản', 'lỗi font', 'câu mơ hồ',
  'tự lộ đáp án', 'hỏi câu chữ văn bản', 'nguồn tiếng Anh', 'đoạn không nêu tên bệnh', 'bảng vỡ', 'khác'];
const head = '#203B55', ink = '#182B3A';

function base(sheet, range) {
  sheet.showGridLines = false;
  sheet.getRange(range).format.font = { name: 'Arial', size: 11, color: ink };
  sheet.getRange(range).format.verticalAlignment = 'top';
  sheet.getRange(range).format.wrapText = true;
}
function header(sheet, range) {
  sheet.getRange(range).format.fill = head;
  sheet.getRange(range).format.font = { name: 'Arial', size: 11, bold: true, color: '#FFFFFF' };
  sheet.getRange(range).format.rowHeight = 36;
}
function d3(rec, answerIndex) {
  return rec ? `${rec.pred} (P đáp án: ${rec.probs[answerIndex].toFixed(2)})` : 'Chưa chạy';
}
function options(r) { return r.options.map((s, i) => `${'ABCD'[i]}. ${s}`).join('\n'); }
function answer(r) { return `${'ABCD'[r.answer_index]}. ${r.options[r.answer_index]}`; }

base(review, 'A1:M61');
const rows = data.items.map((r, i) => [i + 1, r.question, options(r), answer(r), r.evidence,
  '', '', '', '', r.id, d3(r.d3_own, r.answer_index), d3(r.d3_bare, r.answer_index), r.flag]);
review.getRange('A1:M61').values = [[ '#', 'Câu hỏi', 'Các phương án', 'Đáp án máy viết',
  'Trích dẫn nguyên văn', 'Đánh giá', 'Nhãn lỗi', 'Ghi chú', 'Đọc nguồn', 'Mã câu',
  'd3 có nguồn', 'd3 không nguồn', 'Cờ máy (tham khảo)' ], ...rows];
header(review, 'A1:M1');
for (const [col, width] of Object.entries({A:5, B:46, C:55, D:37, E:54, F:20, G:25, H:40, I:22, J:35, K:24, L:24, M:36})) {
  review.getRange(`${col}1:${col}61`).format.columnWidth = width;
}
review.getRange('A2:M61').format.rowHeight = 145;
review.getRange('F2:H61').format.fill = '#FFF4D4';
review.getRange('F2:F61').dataValidation = { rule: { type: 'list', values: ratings } };
review.getRange('G2:G61').dataValidation = { rule: { type: 'list', values: tags } };
review.getRange('F2:F61').conditionalFormats.addCustom('F2="Đúng"', { fill: '#E8F2E6' });
review.getRange('F2:F61').conditionalFormats.addCustom('AND(F2<>"",F2<>"Đúng")', { fill: '#FBE3DB' });
review.tables.add('A1:M61', true, 'Review60');
review.freezePanes.freezeRows(1);
review.tabColor = head;

base(source, 'A1:C61');
source.getRange('A1:C1').values = [['#', 'Văn bản / mục / trang', 'Đoạn gốc đầy đủ (kể cả ngữ cảnh tiêu đề)']];
header(source, 'A1:C1');
source.getRange('A1:A61').format.columnWidth = 6;
source.getRange('B1:B61').format.columnWidth = 58;
source.getRange('C1:C61').format.columnWidth = 145;
data.items.forEach((r, i) => {
  const n = i + 2;
  // Only display whitespace is compacted. The JSONL retains original line breaks verbatim.
  const body = r.chunk_text.replace(/\s+/g, ' ').trim();
  source.getRange(`A${n}:C${n}`).values = [[i + 1,
    `${r.doc}\n\n${r.section || ''}\n\nTrang PDF ${r.page}\n${r.source_path}`, body]];
  source.getRange(`A${n}:C${n}`).format.rowHeight = 365;
  review.getRange(`I${n}`).values = [[`Đọc nguồn · trang ${r.page}`]];
  review.getRange(`I${n}`).format.font = { name: 'Arial', size: 11, color: '#1767A1' };
});
source.freezePanes.freezeRows(1);

base(summary, 'A1:C27');
summary.getRange('A1:C27').format.columnWidth = 31;
summary.getRange('C1:C27').format.columnWidth = 100;
summary.getRange('A1:C1').values = [['Duyệt pilot vòng 2', '03/11/2026', '60 câu mới. Năm câu bất đồng vòng 1 được giữ riêng.']];
header(summary, 'A1:C1');
summary.getRange('A3:C14').values = [
  ['Tổng số câu', 60, 'Chấm tại Duyệt 60, cột F. Cột G–H để ghi lỗi và cách sửa.'],
  ['Đã chấm hợp lệ', null, 'Chỉ bốn nhãn trong danh sách được tính.'],
  ['Đúng', null, 'Đúng lâm sàng, rõ bệnh/đối tượng, chỉ một đáp án đúng và nguồn hỗ trợ đầy đủ.'],
  ['Sai', null, 'Sai đáp án, có thêm đáp án đúng, sai liều/tuổi/thời gian hoặc thêm mức khẳng định.'],
  ['Không rõ', null, 'Thiếu ngữ cảnh, không đủ chứng cứ, câu mơ hồ hoặc nguồn không đọc chắc được.'],
  ['Không lâm sàng', null, 'Thủ tục, giám sát, biểu mẫu, phân công, thống kê hoặc hỏi câu chữ tài liệu.'],
  ['Tỷ lệ Đúng / 60', null, 'Mẫu số luôn là 60, kể cả khi mới chấm một phần.'],
  ['Ngưỡng duyệt', 0.9, 'Ít nhất 54/60 Đúng, phải chấm đủ 60 câu.'],
  ['Kết quả', null, 'Kết quả tự cập nhật theo các nhãn ông nhập.'],
  ['Sinh toàn bộ data', 'Chờ ông duyệt', 'Chỉ số máy và kết quả ĐẠT không tự chạy sinh data.'],
  ['Độ phủ văn bản', Object.keys(data.doc_counts).length, 'Tối đa 6 câu mỗi văn bản (10% bộ duyệt).'],
  ['Kiểm tra d3', data.d3_own_complete && data.d3_bare_complete ? 'Đủ hai lượt / 60 câu' : 'Chưa đủ hai lượt',
    'Điểm d3 và lượt kiểm tra của máy chỉ để tham khảo, không thay đánh giá của người duyệt.'],
];
summary.getRange('B4').formulas = [['=SUM(B5:B8)']];
ratings.forEach((v, i) => { summary.getRange(`B${i + 5}`).formulas = [[`=COUNTIF('Duyệt 60'!F2:F61,"${v}")`]]; });
summary.getRange('B9').formulas = [['=B5/B3']];
summary.getRange('B9:B10').setNumberFormat('0.0%');
summary.getRange('B11').formulas = [['=IF(B4<B3,"Chưa xong",IF(B9>=B10,"ĐẠT — chờ ông duyệt","CHƯA ĐẠT"))']];
summary.getRange('A16:C21').values = [
  ['Cách duyệt', '', 'Đọc câu hỏi, bốn phương án, đáp án và trích dẫn. Bấm Đọc nguồn để đọc toàn bộ đoạn.'],
  ['Kiểm cả bốn phương án', '', 'Đừng chỉ kiểm trích dẫn: tìm cả lựa chọn khác cũng đúng, khác nhóm tuổi hoặc khoảng liều chồng lấn.'],
  ['Tự lộ đáp án / câu chữ', '', 'Đánh dấu nếu câu hỏi nhắc lại đáp án hoặc chỉ hỏi nội dung được liệt kê; không chấp nhận vào data mới.'],
  ['Viết tắt', '', 'Tên bệnh phải rõ; ghi chú nếu viết tắt chưa được giải nghĩa hoặc làm câu khó hiểu.'],
  ['Năm câu cũ', '', 'Tab BatDong_vong1 giữ nguyên câu và đoạn gốc vòng 1. Chấm lại riêng, không tính vào 60 câu mới.'],
  ['Đối chiếu vòng 1', '', 'Hà: 47 Đúng, 1 Sai, 6 Không rõ, 6 Không lâm sàng (47/60 = 78,3%).'],
];
summary.getRange('A23:C23').values = [['Nguồn review vòng 1', '', data.ha_review.path]];
summary.getRange('A24:C24').values = [['SHA256 file Hà', '', data.ha_review.sha256]];
summary.getRange('A26:C26').values = [['Thay đổi vòng 2', '', 'Giữ tiêu đề/mục và trang; loại nguồn giám sát, tiếng Anh/font hỏng và trang có bảng; kiểm tên bệnh, trích dẫn, lộ đáp án và cả bốn lựa chọn.']];
summary.getRange('A27:C27').values = [['Giới hạn', '', 'Trang có bảng bị loại bảo thủ, chưa sửa OCR hay tái dựng bảng. Lượt kiểm tra riêng dùng cùng model viết câu, chưa phải xác nhận độc lập về y khoa.']];
summary.getRange('A3:C27').format.rowHeight = 44;
summary.getRange('A26:C27').format.rowHeight = 62;

const oldHeaders = ['# vòng cũ', 'Câu hỏi cũ (giữ nguyên)', 'Các phương án', 'Đáp án máy viết', 'Trích dẫn',
  'd3 có nguồn (vòng 1)', 'Hà đánh giá / ghi chú', 'Đánh giá lại', 'Ghi chú mới', 'Đoạn gốc vòng 1', 'Mã câu'];
base(regression, 'A1:K6');
regression.getRange('A1:K6').values = [oldHeaders, ...data.historical.map((r, i) => [i + 1, r.question,
  options(r), answer(r), r.evidence, d3(r.d3_own, r.answer_index),
  [r.ha.rating, r.ha.tag, r.ha.note].filter(Boolean).join('\n') || 'Không thuộc mẫu Hà chấm', '', '', r.chunk_text, r.id])];
header(regression, 'A1:K1');
for (const [col, width] of Object.entries({A:10, B:48, C:55, D:40, E:55, F:27, G:38, H:22, I:40, J:140, K:38})) {
  regression.getRange(`${col}1:${col}6`).format.columnWidth = width;
}
regression.getRange('A2:K6').format.rowHeight = 330;
regression.getRange('H2:I6').format.fill = '#FFF4D4';
regression.getRange('H2:H6').dataValidation = { rule: { type: 'list', values: ratings } };
regression.freezePanes.freezeRows(1);
regression.tables.add('A1:K6', true, 'Historical5');

// Exercise the human-review gate, then restore every input before saving.
for (const [correct, rated, expected] of [[53,60,'CHƯA ĐẠT'], [54,60,'ĐẠT — chờ ông duyệt'],
  [54,59,'Chưa xong'], [0,0,'Chưa xong']]) {
  review.getRange('F2:F61').values = Array.from({length:60}, (_, i) => [i < correct ? 'Đúng' : i < rated ? 'Sai' : '']);
  wb.recalculate();
  const actual = summary.getRange('B11').values[0][0];
  if (actual !== expected) throw new Error(`Review gate: ${correct}/${rated}: ${actual} != ${expected}`);
}
review.getRange('F2:F61').values = Array.from({length:60}, () => ['']);
wb.recalculate();
console.log('Verified 4 review-gate scenarios; restored all 60 ratings to blank.');
console.log((await wb.inspect({ kind: 'table', range: "'Tổng kết'!A3:C14", include: 'values,formulas', tableMaxRows: 12, tableMaxCols: 3, maxChars: 2500 })).ndjson);
console.log((await wb.inspect({ kind: 'match', searchTerm: '#REF!|#DIV/0!|#VALUE!|#NAME\\?|#NUM!|#SPILL!|#CALC!', options: {useRegex:true,maxResults:20}, maxChars:1500 })).ndjson);
for (const [name, range, filename] of [['Duyệt 60','A1:H3','review'], ['Đoạn gốc','A1:C2','source'],
  ['Tổng kết','A1:C14','summary'], ['BatDong_vong1','A1:I2','historical']]) {
  const blob = await wb.render({sheetName:name,range,scale:1,format:'png'});
  await fs.writeFile(path.join(outDir, `${filename}.png`), new Uint8Array(await blob.arrayBuffer()));
}
const exported = await SpreadsheetFile.exportXlsx(wb);
await exported.save(output);
execFileSync(process.env.PYTHON || 'python', ['-X', 'utf8',
  fileURLToPath(new URL('./finalize_moh_review_xlsx.py', import.meta.url)), output], {stdio:'inherit'});
console.log(`Saved ${output}`);
