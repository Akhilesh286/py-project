#!/data/data/com.termux/files/usr/bin/python3
import os 
import sys
def project_creater (project_name):
  file = open(f"templates/{project_name}.html","w")
  file.write("""<!DOCTYPE html>
  <html>
    <head>
      <meta http-equiv="content-type" content="text/html; charset=utf-8" />
      <meta name="" content="">
      <title></title>
      <link rel="stylesheet" href="//code.jquery.com/ui/1.13.2/themes/base/jquery-ui.css">
  <link rel="stylesheet" href="/resources/demos/style.css">
    </head>
    <body>
    <style type="text/css" media="all">
    </style>
    <!-- code here -->
    <!-- javascript files -->
      <script src="https://code.jquery.com/jquery-3.6.0.js"></script>
  <script src="https://code.jquery.com/ui/1.13.2/jquery-ui.js"></script>
  
      <script src="{{ url_for('static',filename='js/"""+project_name+""".js' )}}" type="text/javascript" charset="utf-8"></script>
    </body>
  </html>
  """)
  file.close()
  file = open(f"static/js/{project_name}.js","w")
  file.write("""$(document).ready(function(){
  //--- write your code here ----
  })
  """)
  file.close()
  
  with open("app.py", "r") as f:
      contents = f.readlines()
  
  contents.insert(4, f'\n#{project_name}\n@app.route("/{project_name}")\ndef {project_name} () :\n\treturn render_template("{project_name}.html")\n#done {project_name}\n\n')
  
  with open("app.py", "w") as f:
      contents = "".join(contents)
      f.write(contents)

def delete_line (file,delete_text):
  with open(file) as f:
      content_list = f.readlines()
  # print the list
  #print(content_list)
  # remove new line characters
  content_list = [x.strip() for x in content_list]
  deleted_lines = []
  count = 0
  for i in content_list:
    if i in delete_text:
      deleted_lines.append(count)
    count+=1
  #print (count,deleted_lines)
  
  # read file
  with open(file, 'r') as fp:
      # read an store all lines into list
      lines = fp.readlines()
  
  with open(file, 'w') as fp:
      # iterate each line
      for number, line in enumerate(lines):
          #print (number,line)
          # delete line 5 and 8. or pass any Nth line you want to remove
          # note list index starts from 0
          if number not in deleted_lines:
            fp.write(line)
  return f"deleted {delete_text} in {deleted_lines}"
#print (delete_line("test.txt",["hello","hai"]))



try :
  if sys.argv[1] == "-c":
    project_name = input("name of you project: ")
    project_creater(project_name)
    print ("run the file using ")
    print (f"http://127.0.0.1:8000/{project_name}")
    
  elif sys.argv[1] == "-d":
    try:
      project_name = input("project name: ")
      delete_line("app.py",[f"#{project_name}",f'@app.route("/{project_name}")',f'def {project_name} () :',f'return render_template("{project_name}.html")',f'#done {project_name}','\n'])
      
      os.chdir("templates")
      os.remove(f"{project_name}.html")
      #deleted html file going to js file
      os.chdir("../static/js")
      os.remove(f"{project_name}.js")
      
      
      
      print("done...")
    except FileNotFoundError:
      print("file not found in this name")
except IndexError:
  print ("no argument is give -c for creating a project and -d for delete the project ")