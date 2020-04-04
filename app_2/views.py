from django.shortcuts import render
from django.http import HttpResponse
import pytesseract
from PIL import Image

Html_content=""

# Create your views here.
def startup_function(request):
    return render(request, 'App0.html', {})

def upload_function(request):
    for count, x in enumerate(request.FILES.getlist("files")):
        def process(f):
            with open('./static/img/upload_img/Temp_Img_' +str(count)+ '.png', 'wb+') as Destination:
                for chunk in f.chunks():
                    Destination.write(chunk)
        process(x)

    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
    img=Image.open('./static/img/upload_img/Temp_Img_0.png')
    text = pytesseract.image_to_string(img)
    #print(text)
    words=text.split()
    print(words)
    #num=len(words)
    #print(words[0][0:5])

    words=text.split()
    #print(words)
    #print(" ")
    #print(words[0][0:5])

    new_list=[]
    for word in words:
        new_list.append(word.lower())

    #print(new_list)
    #print(" ")
    Html_content=""
    count=len(new_list)

    for i in range(0, len(new_list)):
        #print(new_list[i])
        if "ho1-" in new_list[i]:
            Html_content= Html_content+'<h1>'+new_list[i][4:]+'</h1><br/>\n'
        elif "lbl-" in new_list[i]:
            Html_content= Html_content+'<label>'+new_list[i][4:]+'</label>'
        elif "txt-" in new_list[i]:
            Html_content= Html_content+'<input type="text" name="'+new_list[i][4:]+'" id="" placeholder="'+new_list[i][4:]+'"><br/>\n'
        elif "ext-" in new_list[i]:
            Html_content= Html_content+'<input type="password" name="'+new_list[i][4:]+'" id="" placeholder="'+new_list[i][4:]+'"><br/>\n'
        elif "mxt-" in new_list[i]:
            Html_content= Html_content+'<input type="email" name="'+new_list[i][4:]+'" id="" placeholder="'+new_list[i][4:]+'"><br/>\n'
        elif "txa-" in new_list[i]:
            Html_content= Html_content+'<textarea name="'+new_list[i][4:]+'" id="" cols="30" rows="10" placeholder="'+new_list[i][4:]+'"></textarea><br/>\n'
        elif "btn-" in new_list[i]:
            Html_content= Html_content+'<input type="submit" value="'+new_list[i][4:]+'">\n'
    
    return render(request, 'App0.html', {'message':'file is been uploaded!!', 'label1':'the code is been given below', 'list_of_items':words, 'img':'./static/img/upload_img/Temp_Img_0.png', 'Get_code':'Get-Code', 'html_web_content':Html_content, 'copy':'Copy to the Clipboard', 'label_of_predect':'The list of predicted items:'})

def texteditor_function(request):
    return render(request, 'App1.html',)