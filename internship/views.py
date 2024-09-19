from django.shortcuts import render,HttpResponse
from .models import Provider,Feedback,Contactus,Notice,ProgramDetails
from django.contrib import messages
def home(request):
    return render(request,"internship/html/home.html")

def about_internship(request):
    program_list=ProgramDetails.objects.all()
    program_contents={
        "program_data_key":program_list,
        "title":"MyHomePage"
    }
    return render(request,"internship/html/about_internship.html",program_contents)

def feedback(request):
    if request.method=="GET":

        return render(request,"internship/html/feedback.html")
    if request.method=="POST":
        fn=request.POST["name"]
        fe=request.POST["email"]
        fd=request.POST["date"]
        ft=request.POST["feedbacktext"]
        fr=request.POST["rating"]
        feedback_obj=Feedback(name=fn,email=fe,date=fd,feedbacktext=ft,rating=fr)
        feedback_obj.save()
        messages.success(request,"Thanks For Your Feedback")
        return render(request,"internship/html/feedback.html")
    
def contactus(request):
    if request.method=="GET":
        return render(request,"internship/html/contactus.html")
    if request.method=="POST":
        un=request.POST["username"]
        ue=request.POST["useremail"]
        up=request.POST["userphone"]
        uq=request.POST["userquery"]
        # ud=request.post["userdate"]
        contactus_obj=Contactus(name=un,email=ue,phone=up,question=uq)
        contactus_obj.save()
        messages.success(request,"your query is resolve shortly")
        return render(request,"internship/html/home.html")
      
           
# def needhelp(request):
#     return render(request,"internship/html/needhelp.html")
#     return render(request,"internship/html/needhelp.html")

# def login(request):
#     return render(request,"internship/html/login.html")   

def registration(request):
    if request.method == "GET":
        return render(request,"internship/internship_provider/provider_registration.html")
    
    if request.method == "POST":
        p_id=request.POST["providerid"]
        p_pass=request.POST["provpass"]
        o_name=request.POST["organizationname"]
        own_name=request.POST["ownername"]
        o_email=request.POST["email"]
        o_phone=request.POST["phonenumber"]
        o_add=request.POST["address"]
        o_city=request.POST["city"]
        o_domain=request.POST["domain"]
        o_about=request.POST["aboutorganisation"]
        print(p_id,p_pass)
        registration_obj=Provider(providerid=p_id,provpass=p_pass,organizationname=o_name,ownername=own_name,email=o_email,phonenumber=o_phone,address=o_add,city=o_city,domain=o_domain,aboutorganisation=o_about) 
        registration_obj.save()
        return render(request,"internship/html/login.html")
    
def notice(request):
    notice_object_list=Notice.objects.all()
    notice_contents={
        "notice_key":notice_object_list,
        "title":"MyHomePage"
    }
    return render(request,"internship/html/notice.html",notice_contents)
    
        
    



    

    
    
    

# Create your views here.
