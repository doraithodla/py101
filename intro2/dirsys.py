''' 
Print the directory of a module. It is easy to inspect a module and print out all the entries. We do that with the sys module in this little app with just a couple of lines of code
'''

import sys

for i in dir(sys):
    print(i)
