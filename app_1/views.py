from django.shortcuts import render, redirect
from django.core.mail import send_mail as sm
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse
import re
# from django.core.mail import send_mail as sm
# Create your views here.

def home(request):
    
    return render(request, 'index.html')

def send_me(request):
    msg=''
    re_msg=''
    if request.method == 'POST':
        user_name = request.POST['name']
        send_to_email = request.POST['email']
        user_contact = request.POST['phone']
        query = request.POST['query']
        
        if user_name =="" and send_to_email == "" and user_contact =="" and query=="":
            re_msg = "Please fill all details"

        elif user_name !="" and send_to_email == "" and user_contact =="" and query=="":
            re_msg = "Error!! Please re-fill all details you missed this field(User_mail-id, Phone Number, user_query)"

        elif user_name =="" and send_to_email != "" and user_contact =="" and query=="":
            #error_message = 
            re_msg = "Error!! Please re-fill all details you missed this field(User_name, Phone Number, user_query)"

        elif user_name =="" and send_to_email == "" and user_contact !="" and query=="":
            #error_message = 
            re_msg = "Error!! Please re-fill all details you missed this field(User_name, User_mail-id, user_query)"

        elif user_name =="" and send_to_email == "" and user_contact=="" and query!="":
            #error_message = 
            re_msg = "Error!! Please re-fill all details you missed this field(User_name, User_mail-id, Phone Number)"

        elif user_name =="":
            re_msg = "Please enter the your name"

        elif send_to_email =="":
            re_msg = "Please enter the your mail-id"
            #error_message = 

        elif user_contact=="":
            re_msg = "Please fill the Phone Number "
            #error_message = 

        elif query=="":
            #error_message = 
            re_msg = "Please your query"
        

        if(re.search("^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$",send_to_email)):
            if re.match(r'[789]\d{9}$', user_contact):
                if user_name.isalpha():
                    # For clients
                    client_subject  = 'Vote of thanks'
                    message = 'Thanks for visiting our website here you '
                    from_mail = 'settings.EMAIL_HOST_USER'
                    recipient_list = [send_to_email, ]
                    sm(client_subject, message, from_mail, recipient_list, fail_silently=False)
                    
                    # For Admin
                    admin_subject: "Contact details from the user with a query"
                    message_for_admin = 'Greatings Admin, \nYou have recived an recived an new query from: \nName: '+ user_name +'\nMail-Id: '+ send_to_email +'\nStating the Query as:\n \n<!-- Query Start`s from here -->\n'+ query +'\n<!-- Query end`s here -->\n \nKindley replay to him\n \n \n Thank You \n \tBy: Top-Ui.'
                    send_to_admin = ['aravindmurugan100@gmail.com', ]
                    sm(admin_subject, message_for_admin, from_mail, send_to_admin, fail_silently=False)
                    msg =  'Thanks '+send_to_email+' for your valuable feedback...'  
                else:
                    re_msg = "Invalid Name"
            else:
                re_msg = "Invalid contact number"
        else:
            re_msg="Invalid Email-Id"

            

    return render(request, 'index.html', {'success_message': msg, 'error_message':re_msg, })
