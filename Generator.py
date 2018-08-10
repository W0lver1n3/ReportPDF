#inclusione del file feedparser
import feedparserMik
from feedparserMik import feed_title
import time
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
 
doc = SimpleDocTemplate("report.pdf",pagesize=letter,
                        rightMargin=15,leftMargin=15,
                        topMargin=15,bottomMargin=15)
Story=[]
logo = "logo.jpg"
magName = "EarlyVariabile"
 
im = Image(logo, 204,103)
im.hAlign = 'LEFT'
Story.append(im)

styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
ptext = '<font size=12>%s</font>' % (feed_title)
Story.append(Paragraph(ptext, styles["Justify"]))
Story.append(Spacer(1, 12))

ptext = '<font size=12>Variabile di testo %s</font>' % (magName)
Story.append(Paragraph(ptext, styles["Justify"]))
Story.append(Spacer(1, 12))

ptext = '<font size=12>WOW</font>'
Story.append(Paragraph(ptext, styles["Normal"]))
Story.append(Spacer(1, 12))
doc.build(Story)