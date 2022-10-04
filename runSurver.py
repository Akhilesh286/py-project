# approach 2
# using stat function of os module

import os
 

file_size = os.stat('sample.java')

print("Size of file :", file_size.st_size, "bytes")

while True:
  file_size2 = os.stat('sample.java')
  if file_size > file_size2:
    print ("hello ")