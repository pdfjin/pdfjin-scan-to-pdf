import io
from PIL import Image
from pdfjin_scan_to_pdf.core import scan_to_pdf


def test_scan_to_pdf():
    img = Image.new("RGB", (100, 100), color="white")
    buf = io.BytesIO()
    img.save(buf, format="JPEG")
    res = scan_to_pdf([buf.getvalue()])
    assert len(res) > 0
