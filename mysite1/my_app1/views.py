from django.http import HttpResponse
from django.template import loader
from django import template
import datetime
from django.core.mail import send_mail
#from my_app1.models import formcontact
from my_app1.models import logindetails
from my_app1.models import signupdetails
from my_app1.models import carddetails
from my_app1.models import student
from my_app1.models import employee
#def form(request):
    #if request.method=="POST":
       # fname=request.POST['fname']  
        #lname=request.POST['lname']  
        #email=request.POST['email']  
        #phone=request.POST['phone']   
        #ins=formcontact(fname=fname,lname=lname,phone=phone,email=email)
        #ins.save()
        #print("Data Saved Successfully")
    #return render(request,'home.html')
def login(request):
    if request.method=="POST":
        name=request.POST['name']  
        email=request.POST['email']  
        password=request.POST['password'] 
       
        mobile=request.POST['mobile']   
        ins=logindetails(name=name,email=email,password=password,mobile=mobile)
        ins.save()
        print("Data Saved Sucessfully")
    return render(request,"home.html")
    errors=[]
    if request.method=="POST":
        if not request.POST.get('name',''):
            errors.append('Enter user name')
        if not request.POST.get('password','') or len(request.POST['password'])>6:
            errors.append('Enter a valid passsword')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mail address.')
        if not errors:
            send_mail(
                request.POST['name'],
                request.POST['password'],
                request.POST.get('email','noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/home/thanks')
    return render(request,'home.html',{
        'errors':errors,
        'number':request.POST.get('number',''),
        'passoword': request.POST.get('password',''),
        'email':request.POST.get('email',''),
    })
def signup(request):
    if request.method=="POST":
        email=request.POST['email']  
        password=request.POST['password'] 
        ins=signupdetails(email=email,password=password)
        ins.save()
        print("Data Saved Sucessfully")
    return render(request,'home1.html')
    errors=[]
    if request.method=="POST":
        if not request.POST.get('password','') or len(request.POST['password'])>6:
            errors.append('Enter a valid passsword')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mail address.')
        if not errors:
            send_mail(
                request.POST['password'],
                request.POST.get('email','noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/home/thanks')
    return render(request,'home1.html',{
        'errors':errors,
        'passoword': request.POST.get('password',''),
        'email':request.POST.get('email',''),
    })
def index1(request):
    return render(request,"Index1.html")
def product(request):
    return render(request,"Products.html")
def card(request):
    if request.method=="POST":
        name=request.POST['name']  
        email=request.POST['email']  
        address=request.POST['address'] 
        city=request.POST['city']
        state=request.POST['state']
        pincode=request.POST['pincode'] 
        pname=request.POST['pname']
        pid=request.POST['pid']
        quantity=request.POST['quantity']
        price=request.POST['price']
        cardnum=request.POST['cardnum']
        cardname=request.POST['cardname'] 
        edate=request.POST['edate'] 
        cvv=request.POST['cvv']   
        ins=carddetails(name=name,email=email,address=address,city=city,state=state,pincode=pincode,pname=pname,pid=pid,quantity=quantity,price=price,cardnum=cardnum,cardname=cardname,edate=edate,cvv=cvv)
        ins.save()
        print("Data Saved Sucessfully")
    return render(request,"cart.html")
def update(request):
    print("the method is",request)
    if request.method=="POST":  
        email=request.POST['email']
        newemail=request.POST['newemail']
        upd=logindetails.objects.get(email=email)
        upd.email=newemail
        upd.save()
        mobile=request.POST['mobile']
        newmobile=request.POST['newmobile']
        upd=logindetails.objects.get(mobile=mobile)
        upd.mobile=newmobile
        upd.save()
        print("Data updated successfully")  
    else:
        print("redirected")
    return render(request,'update1.html')
def delete(request):
    if request.method=="POST":
        email=request.POST['email']
        dele=logindetails.objects.get(email=email)
        dele.delete()
        print("Data deleted successfully")
    else:
        print("redirected")
    return render(request,'delete.html')
def title(request):
    str1={"name":"sandhiya"}
    return render(request,"contact1.html",str1)
from django.db.models.lookups import GreaterThan
from django.db.models import F
def details(request):
    if request.method=="POST":
        s_id=request.POST['s_id']  
        name=request.POST['name']  
        sub_mark1=request.POST['sub_mark1'] 
        sub_mark2=request.POST['sub_mark2'] 
        sub_mark3=request.POST['sub_mark3'] 
        total=int(sub_mark1)+int(sub_mark2)+int(sub_mark3)
        avg=int(total)/3
        ins=student(s_id=s_id,name=name,sub_mark1=sub_mark1,sub_mark2=sub_mark2,sub_mark3=sub_mark3,Total=total,avg=avg)
        ins.save()
        choice_query_set =student.objects.filter(avg=75)
        choice_list = list(choice_query_set.values())
        print(choice_list)
        return HttpResponse(" successfully retrieved  %s   " % choice_list)
    return render(request,"details.html")
from django.db.models import Sum
def employee1(request):
    if request.method=="POST":
        e_id=request.POST['e_id']  
        name=request.POST['name']  
        age=request.POST['age'] 
        address=request.POST['address']   
        salary=request.POST['salary'] 
        dept=request.POST['dept'] 
        ins=employee(e_id=e_id,name=name,age=age,address=address,salary=salary,dept=dept)
        ins.save()
        choice_query_set =employee.objects.annotate(Salary_sum=Sum('salary'))
        choice_list = list(choice_query_set.values())
        print(choice_query_set)
        return HttpResponse(" successfully retrieved  %s   " % choice_list)
    return render(request,"employee.html")
def index2(request):
	template=loader.get_template("index2.html")
	name={
		'person_name':'sandhiya',
		'email':'sandhiyad.19cse@kongu.edu',
        'phone':'9384454679',
        'experience':'2'
		}
	return HttpResponse(template.render(name))
def contact(request):
    errors=[]
    if request.method=="POST":
        if not request.POST.get('Name',''):
            errors.append('Enter a name')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mail address.')
        if not errors:
            send_mail(
                request.POST['name'],
                request.POST.get('email','noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    return render(request,'contact2.html',{
        'errors':errors,
        'name':request.POST.get('name',''),
        'email':request.POST.get('email',''),
    })
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
import re
def validate(request):
    errors=[]
    if request.method=="POST":
        if not request.POST.get('name',''):
            errors.append('Enter a name')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mail address')
        if not errors:
            send_mail(
                request.POST['name'],
                request.POST.get('email','noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('success')
    return render(request,'email.html',{
        'errors':errors,
        'name':request.POST.get('name',''),
        'email':request.POST.get('email',''),
    })
def success(request):
    return render(request,'success.html')