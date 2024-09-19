from django.shortcuts import render,redirect
from .models import Provider,ProgramDetails
from django.contrib import messages




def login(request):
    if request.method=="GET":
        return render(request,"internship/html/login.html")
    if request.method=="POST":
        p_id=request.POST["providerid"]
        p_pass=request.POST.get("provpass")
        print(p_id,p_pass)
        Provider_list=Provider.objects.filter(providerid=p_id,provpass=p_pass)
        length=len(Provider_list)

        if length>0:
            request.session["provider_key"]=p_id  
            
            #return redirect("login")
            provider_obj=Provider.objects.get(providerid=p_id)
#         print(provider_obj)
    
#       p_dict={"provider_data":provider_obj}
           
            return render(request,'internship/internship_provider/provider.html')
        else:
            return render(request,'internship/html/login.html')

def providercourse(request):
    if request.method == "GET":
        return render(request,"internship/internship_provider/providercourse.html")
    if request.method == "POST":

        p_id= request.session["provider_key"]
        print(p_id)
        provider_obj=Provider.objects.get(providerid=p_id)
        print(provider_obj)
        p_name=request.POST["program_name"]
        p_duration=request.POST["program_duration"]
        p_fees=request.POST["program_fees"]
        # p_sdate=request.POST["start_date"]
        # p_edate=request.POST["end_date"]
        p_perquisite=request.POST["program_per"]
        p_stipend=request.POST["program_sti"]
        # p_description=request.POST["program_des"]
        course_obj=ProgramDetails(Providerid=provider_obj,programname=p_name,duration=p_duration,fees=p_fees,perquisite=p_perquisite,stipend=p_stipend)
        course_obj.save()
        return render(request,"internship/internship_provider/providerprofile.html")
def providerviewcourse(request):
    provider_obj_list=Provider.objects.all()
    course_obj_list=ProgramDetails.objects.all()
    course_contents={
        "provider_key":provider_obj_list,
        "program_data_key":course_obj_list
    }
    return render(request,"internship/internship_provider/provider_viewcourse.html",course_contents)
        

    
    
    
    
        



def providerviewprofile(request):
        p_id= request.session["provider_key"]
        print(p_id)
        provider_obj=Provider.objects.get(providerid=p_id)
        print(provider_obj)
        p_dict={"provider_data":provider_obj}
        return render(request,"internship/internship_provider/providerprofile.html",p_dict)
    



    

# def providerviewprofile(request):
#     return render(request,"internship/internship_provider/providerprofile.html")
        
    
    #     employee_object_list=Employee.objects.all()
    # event_object_list=Event.objects.all()
    # employee_contents={
    #     "employee_key":employee_object_list,

    
    #     "event_key":event_object_list
    # }
    

    
    
    
    # return render(request,"myapp/html/home.html",employee_contents)

def providereditprofile(request):
    if request.method=="GET":
        p_id= request.session["provider_key"]
        print(p_id)
        provider_obj=Provider.objects.get(providerid=p_id)
        print(provider_obj)
        p_dict={"provider_data":provider_obj}
        return render(request,"internship/internship_provider/provider_editprofile.html",p_dict)
    if request.method=="POST":
        pe=request.POST["provideremail"]
        pp=request.POST["providernumber"]
        pa=request.POST["address"]
        pc=request.POST["city"]
        pd=request.POST["domain"]
        p_id= request.session["provider_key"]
        provider_obj=Provider.objects.get(providerid=p_id)
        provider_obj.email=pe
        provider_obj.phonenumber=pp
        provider_obj.address=pa
        provider_obj.city=pc
        provider_obj.domain=pd
        provider_obj.save()
        p_dict={"provider_data":provider_obj}
        return render(request,"internship/internship_provider/providerprofile.html",p_dict)
        
        




    
