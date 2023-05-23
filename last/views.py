from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.conf import settings
from django.views.decorators.csrf import csrf_protect
import time
from django.db import connection

'''urlRoute="""
"""'''
curl=settings.CURRENT_URL
def home(request):
    return render(request,"home.html",{'curl':curl})
def about(request):
    return render(request,"about.html",{'curl':curl})
def contact(request):
    return render(request,"contact.html",{'curl':curl})
def service(request):
    return render(request,"service.html",{'curl':curl})
def register(request):
    if request.method=='GET':
        return render(request,"register.html",{'curl':curl,'msg':''})
    else:
        name=request.POST.get("name")
        username=request.POST.get("username")
        password=request.POST.get("password")
        mobile=request.POST.get("mobile")
        address=request.POST.get("address")
        city=request.POST.get("city")
        gender=request.POST.get("gender")
        info=time.asctime(time.localtime(time.time()))
        #create a query to insert record in database
        sql="insert into register values(NULL,'%s','%s','%s','%s','%s','%s','%s','user',1,'%s')"%(name,username,password,mobile,address,city,gender,info)
        #execute query using cursor instance
        cursor=connection.cursor()
        cursor.execute(sql)


        return render(request,"register.html",{'curl':curl,'msg':'form submitted'})
def login(request):
    if request.method=='GET':
        return render(request,"login.html",{'curl':curl,'msg':''})
    else:
        username=request.POST.get("username")
        password=request.POST.get("password")
        print(username)
        print(password)
        # query to fetch user details from database
        sql="select * from register where username='%s' and password='%s' and status=1"%(username,password)
        cursor=connection.cursor()
        cursor.execute(sql)
        #fetch record from cursor
        userDetails=cursor.fetchone()
        print(userDetails)
        if userDetails!=None:
            if userDetails[8]=="user":
                return redirect(curl+'user/')
            else:
                return redirect(curl+'myadmin/')
        else:
            return render(request,"login.html",{'curl':curl,'msg':'invalid user please login again'})
def adminhome(request):
    return render(request,"adminhome.html",{'curl':curl})
def userhome(request):
    return render(request,"userhome.html",{'curl':curl})       

