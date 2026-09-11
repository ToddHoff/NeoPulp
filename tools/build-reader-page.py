#!/usr/bin/env python3
"""Build assets/neopulp-reader-page.pdf — the 6x9" one-ink "A note to the reader" page.

Usage:  python3 build-reader-page.py [--fonts DIR] [--qr PNG] [--out PDF]

Fonts (TTF): Archivo-Regular, Archivo-Bold, Archivo-Black, JetBrainsMono-Regular,
JetBrainsMono-Bold. Get them from Google Fonts / the Archivo and JetBrains Mono repos.

The wording is locked in book-page.html and assets/neopulp-reader-page.txt — change
all copies together (see claude/neopulp-book-page.md in the Neo Pulp project).
"""
import argparse, os
from reportlab.lib.colors import Color
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph

W, H = 432, 648  # 6 x 9 in
MARGIN = 48.96   # 0.68 in
INK = Color(.05, .047, .043)
BODY = Color(.25, .23, .2)
DIM = Color(.43, .42, .38)

KICKER = "A NOTE TO THE READER"
TITLE = "This book is a neopulp."
PARAS = [
    "A neopulp is a book a person created, shaped and judged — and a machine wrote with them. "
    "The author is the one who takes responsibility for it: I created this, I shaped it, I judged it, "
    "and I stand behind it.",

    "For all of history, the creative economy selected for ideas worth the cost of making. Every medium "
    "charged a price for trying the idea that probably wouldn't work, so most of those ideas were never "
    "tried. The strange book stayed a note in a drawer. That price just collapsed. Now we can select for "
    "ideas worth making — and when experimentation gets cheap, creativity becomes play again. The old "
    "pulps knew what to do with cheap: wild premises, new writers, another one next month. Pulp "
    "democratized publishing. Neopulp democratizes experimentation.",

    "Good work, in any medium, by any means, is a concentrated form of intention. That is what the mark "
    "on this book certifies: not that a human typed it, but that a human created it, shaped it, judged it, "
    "and wouldn't sign it until every word was one they'd stand behind. It says so on the title page, at "
    "byline scale, without hedging, because a new medium is nothing to apologize for. It never was. Ask "
    "the camera.",

    "A book isn't good because a human wrote every word, and it isn't bad because a machine wrote any of "
    "them. Judge the work first. The means of creation are not the measure of it. You will decide.",
]
PROMISE = "A human vision, perfected."
PROMISE_CAP = "THE PROMISE EVERY NEOPULP MAKES"
TAGLINE = "We create. We don't stop. Come make something."
SCAN = "SCAN THE CODE, OR GO TO"
URL = "neopulp.possibility.com"


def register_fonts(d):
    for n in ["Archivo-Regular", "Archivo-Bold", "Archivo-Black", "JetBrainsMono-Regular", "JetBrainsMono-Bold"]:
        pdfmetrics.registerFont(TTFont(n, os.path.join(d, n + ".ttf")))


def tracked(c, text, y, font, size, color, track):
    c.saveState()
    c.setFillColor(color)
    c.setFont(font, size)
    c.drawCentredString(W / 2, y, text, charSpace=track)
    c.restoreState()


def build(out, fonts, qr):
    register_fonts(fonts)
    c = canvas.Canvas(out, pagesize=(W, H))
    c.setAuthor("neopulp"); c.setCreator("neopulp.possibility.com")
    c.setTitle("A note to the reader — neopulp")

    # header
    tracked(c, KICKER, 590.4, "JetBrainsMono-Regular", 8, DIM, 3.2)
    c.setFillColor(INK); c.setFont("Archivo-Black", 24)
    c.drawCentredString(W / 2, 560.16, TITLE)
    c.setLineWidth(1.6); c.line(W / 2 - 21.6, 544.32, W / 2 + 21.6, 544.32)

    # body: centred paragraphs flowing down from a fixed top
    style = ParagraphStyle("body", fontName="Archivo-Regular", fontSize=9.2, leading=12.9,
                           alignment=TA_CENTER, textColor=BODY)
    width = W - 2 * MARGIN
    gap = 7.92
    y = 522.72  # top of the first paragraph (445.32 + 6 lines x 12.9 in the 09-03 build)
    for text in PARAS:
        p = Paragraph(text, style)
        _, h = p.wrap(width, H)
        y -= h
        p.drawOn(c, MARGIN, y)
        y -= gap
    y += gap  # bottom of the last paragraph

    # promise block, hung 22.32 below the body
    c.setFillColor(INK); c.setFont("Archivo-Black", 15.5)
    c.drawCentredString(W / 2, y - 22.32, PROMISE)
    tracked(c, PROMISE_CAP, y - 36.72, "JetBrainsMono-Regular", 6.8, DIM, 2.6)
    c.setFillColor(INK); c.setFont("Archivo-Bold", 10.5)
    c.drawCentredString(W / 2, y - 65.52, TAGLINE)

    # footer, fixed to the page bottom
    c.drawImage(qr, W / 2 - 32.4, 84.24, 64.8, 64.8, mask="auto")
    tracked(c, SCAN, 68.4, "JetBrainsMono-Regular", 6.8, DIM, 2.4)
    c.setFillColor(INK); c.setFont("JetBrainsMono-Bold", 9.5)
    c.drawCentredString(W / 2, 54, URL)

    c.showPage(); c.save()


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    ap = argparse.ArgumentParser()
    ap.add_argument("--fonts", default=os.path.join(here, "fonts"))
    ap.add_argument("--qr", default=os.path.join(here, "..", "assets", "png", "neopulp-qr.png"))
    ap.add_argument("--out", default=os.path.join(here, "..", "assets", "neopulp-reader-page.pdf"))
    a = ap.parse_args()
    build(a.out, a.fonts, a.qr)
    print("wrote", a.out)
