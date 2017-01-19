import sys

total = len(sys.argv)
name = "Welcome"
if(total == 2):
    name = str(sys.argv[1])

print("Hello, %s!" %name)