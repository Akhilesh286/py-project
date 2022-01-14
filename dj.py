#! /data/data/com.termux/files/usr/bin/python
import os
import sys
from color import colors as cl
r=cl.r
print (cl.fgCyan+"hello"+r)
def temp ():
  filename = input ("File Name : ")
  with open(filename,'w') as f:
    f.write("""
{% extends 'main.html' %}
{% block head %}
<title></title>
{% endblock %}
{% block body %}
<h1>html file </h1>
{% endblock %}
""")
def App (pname):
  app_name = input ("Ender"+cl.fgBlue+"App"+r+"Name : ")
  print (cl.fgCyan+os.getcwd()+r)
  os.chdir(pname)
  os.system (f"django-admin startapp {app_name}")
  with open ('runserver','w') as f:
    f.close()
  os.mkdir("action")
  os.chdir("action/")
  with open (f'{app_name}.py' , "w") as f:
    f.write("""
def action ():
  data = {
    'hai':"hai action",
    'hello':'Hello'
  }
  return data
""")
  os.chdir("../")
  os.chdir(app_name)
  os.mkdir("templates")
  os.chdir("templates")
  f = open("index.html", "w")
  f.write("""{% extends 'main.html' %}
{% block head %}
<title>hello world</title>
{% endblock %}
{% block body %}
<h1 class="text">{{hello}}</h1>
<h1>{{hai}}</h1>
<button type="button" class="btn btn-secondary" onclick="but()">Secondary</button>
{% endblock %}""")
  with open ('main.html','w') as f:
    f.write ("""
<!DOCTYPE html>
<html>
  <head>
    {% load static %}
    <meta http-equiv="content-type" content="text/html; charset=utf-8" />
    <meta name="" content="">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <link rel="stylesheet" href="{% static 'css/style.css' %}" type="text/css" media="all" />
{% block head %}
{% endblock %}
  </head>
  <body>
    {% block body %}
    {% endblock %}
    <script
  src="https://code.jquery.com/jquery-3.6.0.slim.min.js"
  integrity="sha256-u7e5khyithlIdTpu22PHhENmPcRdFiHRjhAuHcs05RI="
  crossorigin="anonymous"></script>
    <script src="{% static 'js/script.js' %}" type="text/javascript" charset="utf-8"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.10.2/dist/umd/popper.min.js" integrity="sha384-7+zCNj/IqJ95wo16oMtfsKbZ9ccEh31eOz1HGyDuCQ6wgnyJNSYdrPa03rtR1zdB" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.min.js" integrity="sha384-QJHtvGhmr9XOIpI6YVutG+2QOK9T+ZnN4kzFN1RtK3zEFEIsxhlmWl5/YESvpZ13" crossorigin="anonymous"></script>

  </body>
</html>
""")
  os.chdir("../")
  os.mkdir("static")
  os.chdir("static")
  os.mkdir("js")
  os.mkdir("css")
  os.chdir("css")
  with open ("style.css", "w") as f:
    f.write("""
.text {
  color: #0b191d;
}""")
  os.chdir("../")
  os.chdir("js")
  with open ("script.js", "w") as f:
    f.write("""function but() {
  alert("hello")
}""")
  print (cl.fgCyan+os.getcwd()+r)
  os.chdir("../")
  os.chdir("../")
  print (cl.fgCyan+os.getcwd()+r)
  # views
  src3=open("views.py","r") 
  fline3=f"""from django.shortcuts import render , redirect
from django.http import HttpResponse\n
from action import {app_name} 

def index (request):
  data = {app_name}.action()
  return render(request,'index.html',data)"""   #Prepending string 
  oline3=src3.readlines() 
#Here, we prepend the string we want to on first line 
  oline3.insert(1,fline3) 
  src3.close() 
 
 
#We again open the file in WRITE mode  
  src3=open("views.py","w") 
  src3.writelines(oline3) 
  src3.close() 
  # urls
  #os.chdir("../")
  print (cl.fgCyan+os.getcwd()+r)
  with open ("urls.py" , "w") as f :
    f.write(f"""
from django.urls import path
from {app_name} import views 
urlpatterns = [
    path('', views.index),
]
""")
  os.chdir("../")
  os.chdir(f"{pname}/")
  print (cl.fgCyan+os.getcwd()+r)
  src=open("urls.py","r") 
  fline=f"""from django.urls import include \nfrom {app_name} import urls \n"""    #Prepending string 
  oline=src.readlines() 
#Here, we prepend the string we want to on first line 
  oline.insert(17,fline) 
  src.close() 
 
 
#We again open the file in WRITE mode  
  src=open("urls.py","w") 
  src.writelines(oline) 
  src.close() 
  #urlpatterns
  src2=open("urls.py","r") 
  fline2=f"    path('{app_name}/', include('{app_name}.urls')),\n"    #Prepending string 
  oline2=src2.readlines() 
#Here, we prepend the string we want to on first line 
  oline2.insert(22,fline2) 
  src2.close() 
 
 
#We again open the file in WRITE mode  
  src2=open("urls.py","w") 
  src2.writelines(oline2) 
  src2.close() 
  # settings
  #os.chdir("a/")
  print (cl.fgCyan+os.getcwd()+r)
  src1=open("settings.py","r") 
  fline1=f"    '{app_name}',\n"    #Prepending string 
  oline1=src1.readlines() 
#Here, we prepend the string we want to on first line 
  oline1.insert(39,fline1) 
  src1.close() 
 
 
#We again open the file in WRITE mode  
  src1=open("settings.py","w") 
  src1.writelines(oline1) 
  src1.close() 
  
  
  
  
  

def sapp ():
  app_name = input ("Ender App Name : ")
  print (cl.fgCyan+os.getcwd()+r)
  os.system (f"django-admin startapp {app_name}")
  os.chdir(app_name)
  os.mkdir("templates")
  os.chdir("templates")
  f = open("index.html", "w")
  f.write("<h1> Hello World </h1>")
  os.chdir("../")
  os.mkdir("static")
  os.chdir("static")
  os.mkdir("js")
  os.mkdir("css")
  os.chdir("css")
  with open ("style.css", "w") as f:
    f.write("")
  os.chdir("../")
  os.chdir("js")
  with open ("script.js", "w") as f:
    f.write("")
  print (cl.fgCyan+os.getcwd()+r)
  os.chdir("../")
  os.chdir("../")
  print (cl.fgCyan+os.getcwd()+r)
  with open ("urls.py" , "w") as f :
    f.write("""
from django.urls import path
from web import views 
urlpatterns = [
    path('', views.index),
]
""")
  
    

  
  
def project():
  project_name = input ("project name >>>")
  os.system(f"django-admin startproject {project_name}")
  print (f"""You need any App press : \033[92m Y \033[0m
or don't nedd App  press :\033[91m N \033[0m""")
  y_n=input("").upper()
  if y_n == "Y":
    App(project_name)
  elif y_n == "N":
    print (cl.red+"you pressed N"+r)
  else :
    print (cl.fgYellow+"You pressed another character"+cl.r)
try:
  if sys.argv[1] == "-p" or sys.argv[1] == "-project":
    project()
  elif sys.argv[1] == "-a" or sys.argv[1] == "-app":
    pname = input (cl.fgBlue+"ender project_name :"+cl.r)
    if pname == ".":
      sapp()
    else :
      App(pname)
  elif sys.argv[1] == "-t" or sys.argv == "-templates":
    temp()
  elif sys.argv[1]== "-h" or sys.argv[1] == "-help":
    print ("""
-h or -help :- 
     for help 
-a or -app :- 
     for Create App 
-p or -project :- 
     for Create Projects
-t or -templates :- 
     for Create Templates

    """)
  else :
    print (cl.red+"syntax error "+r)
    print (cl.fgBlue+"type -h or -help"+r)
    
  
except IndexError:
  print (cl.red+"Argument Is Null"+cl.r)
except FileNotFoundError: 
  print (cl.red+"no such director"+r)