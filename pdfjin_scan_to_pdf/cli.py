import sys, argparse
from pathlib import Path
try:
    from .core import scan_to_pdf
    from . import __version__
except (ImportError, ValueError):
    from pdfjin_scan_to_pdf.core import scan_to_pdf
    from pdfjin_scan_to_pdf import __version__


def main():
    p = argparse.ArgumentParser(prog="pdfjin-scan-to-pdf", description="Compile scanned photos into a PDF.")
    p.add_argument("images", nargs="+", help="Scanned image files")
    p.add_argument("-o", "--output", required=True, help="Destination PDF file")
    p.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    args = p.parse_args()
    try:
        scan_to_pdf(args.images, output=args.output)
        print(f"Scanned PDF saved -> {args.output}")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr); sys.exit(1)


if __name__ == "__main__":
    main()
