from threading import Thread
from time import sleep
from datetime import datetime
'''
def hai (arg):
  print ("arg:",arg)
  sleep(arg)

date = datetime.now()
for i in range(5):
  number = int (input ("number: "))
  t1 = Thread(target=hai, args=(number,))
  t1.start()
t1.join()
print (datetime.now ()-date)
'''
class Employee():
    def get_salary (self):
      return "100000"
    def get_name(self):
        return self.get_salary()


# ✅ instantiate class first
emp1 = Employee()

# ✅ call method on class instance
print(emp1.get_name())  # 👉️ "Alice"
