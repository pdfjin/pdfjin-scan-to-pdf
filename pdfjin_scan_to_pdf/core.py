import io
from pathlib import Path
from typing import List, Union
from PIL import Image
import img2pdf


def scan_to_pdf(images: List[Union[str, Path, bytes]], output: Union[str, Path] = None) -> bytes:
    processed = []
    for item in images:
        raw = open(item, "rb").read() if isinstance(item, (str, Path)) else item
        img = Image.open(io.BytesIO(raw))
        if img.mode != "RGB":
            img = img.convert("RGB")
        buf = io.BytesIO()
        img.save(buf, format="JPEG", quality=92)
        processed.append(buf.getvalue())

    pdf_bytes = img2pdf.convert(processed)
    if output:
        Path(output).write_bytes(pdf_bytes)
    return pdf_bytes
