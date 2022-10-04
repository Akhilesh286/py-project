#!/data/data/com.termux/files/usr/bin/python
import os
import sys
import datetime
import getYourColor
# total arguments

package = "javaCodes"

cl = getYourColor


# run time class 
def run (argument):
  
  file = str(argument.split(".")[0])
  
  startTime = datetime.datetime.now()
  
  os.system(f"javac -d . {argument}")
  
  os.system(f"java {package}.{file}")
  
  time = str(datetime.datetime.now()-startTime)
  
  print ("")
  timeInSecond = time.split(":")
  
  print (
    cl.getColors.blue("<--"+timeInSecond[2]+"s-->")
    )
  
  file_size = os.stat(argument)
  
  print("Size of file :", cl.getColors.pink(
    str(file_size.st_size)), "bytes")




# create a class 
def createClass ():
  className = input ("class Name: ")
  
  code = """ {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        //---------Code-----------//
    }
}
"""

  Class = className.split(".")[0]
  f = open(f"{className}.java", "a")
  
  f.write(f"""package {package};
import java.util.Scanner;
class {Class} {code}
  """)
  
  f.close()
  
  print (cl.getColors.purple("Your Class is Done.."))
  
  
  
  
  
try:
  argument = sys.argv[1]
  
  if argument == "-c":
    createClass()
  else:
    run(argument)
    
except IndexError:
  print ("""
-c for creating a class 
<file> to run the class 
  """)
