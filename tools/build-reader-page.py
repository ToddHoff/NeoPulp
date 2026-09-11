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
    "A neopulp is a book a person created, shaped and judged \u2014 and a machine wrote with them. "
    "The author is the one who takes responsibility for it: I created this, I shaped it, I judged it, "
    "and I stand behind it.",

    "Before the machine, trying an idea could cost years, so most ideas were never tried. The strange "
    "book stayed a note in a drawer. The machine removes that friction, and the strange book gets made. "
    "Pulp democratized publishing. Neopulp democratizes experimentation.",

    "The mark tells you what was done with that freedom: a human created this book, shaped it, judged "
    "it, and wouldn't sign it until every word was one they'd stand behind. It says so on the title "
    "page, without hedging, because a new medium is nothing to apologize for. Ask the camera.",

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

    # body: centred paragraphs flowing down from the top of the text block
    style = ParagraphStyle("body", fontName="Archivo-Regular", fontSize=9.2, leading=12.9,
                           alignment=TA_CENTER, textColor=BODY)
    width = W - 2 * MARGIN
    gap = 7.92
    paras = [Paragraph(t, style) for t in PARAS]
    body_h = sum(p.wrap(width, H)[1] for p in paras) + gap * (len(paras) - 1)

    # The 09-03 page filled the sheet: kicker 57.6 from the top, tagline 13.5 above the QR.
    # With less text, split the slack evenly above the kicker and below the tagline.
    TOP_KICKER, BODY_TOP, BODY_H_0903, TAGLINE_0903 = 590.4, 522.72, 295.38, 162.54
    dy = (BODY_H_0903 - body_h) / 2
    c.translate(0, -dy)

    # header
    tracked(c, KICKER, TOP_KICKER, "JetBrainsMono-Regular", 8, DIM, 3.2)
    c.setFillColor(INK); c.setFont("Archivo-Black", 24)
    c.drawCentredString(W / 2, 560.16, TITLE)
    c.setLineWidth(1.6); c.line(W / 2 - 21.6, 544.32, W / 2 + 21.6, 544.32)

    y = BODY_TOP
    for p in paras:
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
    c.translate(0, dy)

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
