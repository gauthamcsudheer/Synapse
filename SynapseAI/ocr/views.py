import pytesseract
from PIL import Image
from django.shortcuts import render

def ocr_view(request):
    if request.method == "POST" and request.FILES.getlist("images"):
        uploaded_images = request.FILES.getlist("images")
        
        # Debug: Print uploaded images
        print("Uploaded images:", uploaded_images)
        
        # Combine extracted text
        extracted_texts = []
        for uploaded_image in uploaded_images:
            image = Image.open(uploaded_image)
            extracted_text = pytesseract.image_to_string(image)
            extracted_texts.append(extracted_text)
        
        combined_text = "\n\n".join(extracted_texts)
        return render(request, 'ocr/ocr_result.html', {'text': combined_text})
    
    return render(request, 'ocr/ocr_form.html')

