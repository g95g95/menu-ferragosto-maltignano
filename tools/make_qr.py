#!/usr/bin/env python3
"""Rigenera il QR code del menù (SVG + PNG) verso l'URL passato come argomento.

Uso:
    python3 tools/make_qr.py "https://g95g95.github.io/menu-ferragosto-maltignano/"

Dipendenze: pip install qrcode pillow
"""
import os
import sys

import qrcode

DEFAULT_URL = "https://g95g95.github.io/menu-ferragosto-maltignano/"
INK = "#20301F"
CREAM = "#FBF6EC"
ASSETS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets")


def matrix_to_svg(matrix):
    """Un solo <path>: ogni riga di moduli accesi diventa un rettangolo orizzontale."""
    n = len(matrix)
    parts = []
    for y, row in enumerate(matrix):
        x = 0
        while x < n:
            if row[x]:
                start = x
                while x < n and row[x]:
                    x += 1
                parts.append(f"M{start} {y}h{x - start}v1h{-(x - start)}z")
            else:
                x += 1
    path = "".join(parts)
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {n} {n}" '
        f'width="512" height="512" shape-rendering="crispEdges" role="img" '
        f'aria-label="QR code menu Ferragosto">'
        f'<rect width="{n}" height="{n}" fill="{CREAM}"/>'
        f'<path d="{path}" fill="{INK}"/></svg>'
    )


def main():
    url = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_URL
    # border=4 moduli: la "quiet zone" richiesta dallo standard, inclusa nel disegno
    # così il codice resta leggibile anche se appoggiato su uno sfondo scuro.
    qr = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=1, border=4
    )
    qr.add_data(url)
    qr.make(fit=True)

    svg_path = os.path.normpath(os.path.join(ASSETS, "qr-menu.svg"))
    with open(svg_path, "w") as fh:
        fh.write(matrix_to_svg(qr.get_matrix()))

    png_path = os.path.normpath(os.path.join(ASSETS, "qr-menu.png"))
    qrcode.make(
        url, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=12, border=4
    ).save(png_path)

    print(f"QR v{qr.version} -> {url}")
    print(f"  {svg_path}")
    print(f"  {png_path}")


if __name__ == "__main__":
    main()
