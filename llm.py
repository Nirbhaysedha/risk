import os
from llama_index.llms.openai import OpenAI
def OPenai(question):
    key= ""
    os.environ["OPENAI_API_KEY"] = key
    llm = OpenAI(model="gpt-4o-mini",)
    resp = llm.complete(question)
    return resp.text
from reportlab.lib.pagesizes import A4

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (SimpleDocTemplate, Spacer, Table, TableStyle,
                                Paragraph, PageBreak, Image, Frame, PageTemplate)


import json



LOGO_PATH = "/Users/nirbhaysedha/Desktop/AI-Assess-Tool/ai_risk_assessment/riskapp/static/img/KPMG_logo.svg.png"
OUTPUT_FILE = "AI_Risk_Assessment_Report.pdf"
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle, Image, PageBreak

import json

# File paths
KPMG_LOGO_PATH = "/Users/nirbhaysedha/Desktop/AI-Assess-Tool/ai_risk_assessment/riskapp/static/img/KPMG_logo.svg.png"

# Load JSON data
def load_json(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

# Footer function
def footer(canvas, doc):
    canvas.saveState()
    width, height = A4
    logo = Image(KPMG_LOGO_PATH, width=80, height=30)
    logo.drawOn(canvas, width - 100, 20)
    canvas.setFont("Helvetica", 8)
    canvas.drawString(30, 20, "© KPMG - All Rights Reserved")
    canvas.restoreState()

# PDF generation function
def create_pdf(filename, matrix, pii, rcm, riq, rtq):
    doc = SimpleDocTemplate(filename, pagesize=A4)
    elements = []
    styles = getSampleStyleSheet()
    
    # Title
    title_style = ParagraphStyle(   
    name="TitleStyle",
    fontSize=22,  # Increased font size for emphasis
    alignment=TA_CENTER,
    spaceAfter=15,  # Added more spacing after the title
    textColor=colors.darkblue,
    fontName="Helvetica-Bold"  # Making it bold
)
    elements.append(Paragraph("AI Risk Assessment Report", title_style))
    elements.append(Spacer(1, 20))
    
    # Tester details
    tester_info = Paragraph("<b>Tested by:</b>Nirbhay Sedha <br/><br/><b>Organization:</b> KPMG <br/><br/><b>Email:</b> nirbhaysedha@kpmg.com <br/><br/><b>Contact:</b> +91 XXXXXXXXXX <br/><br/><b>Role:</b> Senior Developer", styles['Normal'])
    elements.append(tester_info)
    elements.append(Spacer(1, 40))
    
    # Table of Contents
    toc_style = ParagraphStyle(name="TOCStyle", fontSize=14, textColor=colors.black, spaceAfter=10)
    elements.append(Paragraph("<b>Table of Contents</b>", toc_style))
    toc = [
        ["1.", "Introduction"],
        ["2.", "AI Risk Matrix"],
        ["3.", "PII Considerations"],
        ["4.", "Risk Control Measures"],
        ["5.", "Risk Impact Quantification"],
        ["6.", "Risk Tolerance Quantification"],
    ]
    table = Table(toc, colWidths=[30, 400])
    table.setStyle(TableStyle([
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.darkblue),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
    ]))
    elements.append(table)
    elements.append(PageBreak())
    
    # Sections
    sections = [
        ("AI Risk Matrix", matrix),
        ("PII Considerations", pii),
        ("Risk Control Measures", rcm),
        ("Risk Impact Quantification", riq),
        ("Risk Tolerance Quantification", rtq),
    ]
    for title, content in sections:
        elements.append(Paragraph(f"<b>{title}</b>", styles['Heading2']))
        elements.append(Spacer(1, 10))
        elements.append(Paragraph(content, styles['Normal']))
        elements.append(Spacer(1, 20))
    
    # Build PDF
    doc.build(elements, onFirstPage=footer, onLaterPages=footer)
    print(f"PDF '{filename}' created successfully!")

# Load Data



# Load JSON data
matrix_d = load_json("/Users/nirbhaysedha/Desktop/AI-Assess-Tool/ai_risk_assessment/riskapp/templates/riskapp/data/matrix.json")
pii_d = load_json("/Users/nirbhaysedha/Desktop/AI-Assess-Tool/ai_risk_assessment/riskapp/templates/riskapp/data/pii.json")
rcm_d = load_json("/Users/nirbhaysedha/Desktop/AI-Assess-Tool/ai_risk_assessment/riskapp/templates/riskapp/data/rcm.json")
riq_d = load_json("/Users/nirbhaysedha/Desktop/AI-Assess-Tool/ai_risk_assessment/riskapp/templates/riskapp/data/riq.json")
rtq_d = load_json("/Users/nirbhaysedha/Desktop/AI-Assess-Tool/ai_risk_assessment/riskapp/templates/riskapp/data/rtq.json")


matrix = OPenai(f"Provide a comprehensive, well-structured analysis of {matrix_d}. The response should be formal, professional, and assertive, avoiding hedging language like 'it appears' or 'the data suggests.' Instead, deliver clear and confident statements. The content should be formatted as a cohesive document with well-formed paragraphs, ensuring smooth transitions between sections. Avoid bullet points, numbered lists, or hashes. Cover all critical aspects thoroughly with in-depth insights.")

pii = OPenai(f"Provide a thorough and professionally written analysis of {pii_d}. Ensure the response is structured as a cohesive and authoritative document with clear, confident statements. Avoid using bullet points, hashes, or structured headers, and instead, present the information in well-formed paragraphs with logical flow. The response should be detailed, insightful, and cover all essential aspects comprehensively.")

rcm = OPenai(f"Deliver a structured and professional analysis of {rcm_d}. The response should be assertive and direct, avoiding speculative phrases and ensuring clarity in presenting key points. Format the content as a formal document with well-organized paragraphs, ensuring seamless transitions between ideas. Avoid bullet points or lists, and provide a detailed and insightful discussion of all critical elements.")

riq = OPenai(f"Provide a confident and well-articulated analysis of {riq_d}. The response should be structured as a professionally written document, with clear and decisive statements. Avoid bullet points, numbered lists, or hashes, and instead, maintain a fluid and formal writing style. Ensure that all critical aspects are covered comprehensively, with in-depth discussion and clarity.")

rtq = OPenai(f"Deliver a well-structured, confident, and detailed analysis of {rtq_d}. The response should be written in a formal and professional tone, avoiding hesitant phrases like 'it seems' or 'it appears.' Instead, state findings with certainty and clarity. Format the content as a cohesive document with smooth paragraph transitions, avoiding lists or structured headers. Ensure the discussion is thorough, insightful, and comprehensive.")

create_pdf("output.pdf", matrix, pii, rcm, riq, rtq)


