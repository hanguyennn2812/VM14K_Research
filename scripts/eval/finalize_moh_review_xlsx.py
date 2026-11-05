"""Add native internal links: artifact-tool's HYPERLINK evaluator is a stub.

Only the missing hyperlink feature is patched; all values/styles/formulas are authored by
artifact-tool. Uses standard OOXML and stdlib ZIP, never round-trips the workbook via openpyxl.
"""
import sys
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

NS = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
ET.register_namespace("x", NS)
ET.register_namespace("r", "http://schemas.openxmlformats.org/officeDocument/2006/relationships")


def finalize(path):
    path = Path(path)
    with zipfile.ZipFile(path) as source:
        sheet = ET.fromstring(source.read("xl/worksheets/sheet1.xml"))
        links = ET.Element(f"{{{NS}}}hyperlinks")
        for row in range(2, 62):
            ET.SubElement(links, f"{{{NS}}}hyperlink", ref=f"I{row}", location=f"'Đoạn gốc'!A{row}")
        old = sheet.find(f"{{{NS}}}hyperlinks")
        if old is not None:
            sheet.remove(old)
        following = {"printOptions", "pageMargins", "pageSetup", "headerFooter", "rowBreaks", "colBreaks",
                     "customProperties", "cellWatches", "ignoredErrors", "smartTags", "drawing", "legacyDrawing",
                     "legacyDrawingHF", "picture", "oleObjects", "controls", "webPublishItems", "tableParts", "extLst"}
        position = next((i for i, node in enumerate(sheet) if node.tag.rsplit("}", 1)[-1] in following), len(sheet))
        sheet.insert(position, links)
        temp = path.with_suffix(".links.tmp")
        with zipfile.ZipFile(temp, "w", zipfile.ZIP_DEFLATED) as dest:
            for info in source.infolist():
                dest.writestr(info, ET.tostring(sheet, encoding="utf-8", xml_declaration=True)
                              if info.filename == "xl/worksheets/sheet1.xml" else source.read(info.filename))
    temp.replace(path)
    print("Added 60 native links to source passages.")


if __name__ == "__main__":
    finalize(sys.argv[1])
