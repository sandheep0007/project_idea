from django.shortcuts import render
# import io
# from django.http import FileResponse
# from reportlab.pdfgen import canvas

# def generatePDF(request, id):
#     buffer = io.BytesIO()
#     x = canvas.Canvas(buffer)
#     x.drawString(100, 100, "Let's generate this pdf file.")
#     x.showPage()
#     x.save()
#     buffer.seek(0)
#     return FileResponse(buffer, as_attachment=True, filename='attempt1.pdf')
