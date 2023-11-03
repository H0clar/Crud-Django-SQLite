from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib import colors
from io import BytesIO

def generar_pdf(datos, razon_social, rut, num_boleta, fecha_emision, total, iva):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=landscape(A4))
    story = []

    # Información de la boleta
    info = f"RAZON SOCIAL {razon_social}\nRUT: {rut}\nBOLETA ELECTRONICA No. {num_boleta}\nFECHA EMISION: {fecha_emision}"

    style = getSampleStyleSheet()["Title"]
    story.append(Paragraph(info, style))
    story.append(Spacer(1, 20))

    # Tabla de productos
    columnas = ["CANTIDAD", "DESCRIPCION", "VALOR"]
    datos.insert(0, columnas)
    col_widths = [doc.width / 3.0] * 3
    tabla = Table(data=datos, colWidths=col_widths)

    # Aplicar estilos a la tabla
    tabla.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
        ('BOX', (0, 0), (-1, -1), 2, colors.black),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ]))

    story.append(tabla)
    story.append(Spacer(1, 10))

    # Resumen
    resumen = f"TOTAL: ${total}\n\nEL IVA DE ESTA BOLETA ES: ${iva}"
    story.append(Paragraph(resumen, style))

    doc.build(story)
    buffer.seek(0)
    return buffer
