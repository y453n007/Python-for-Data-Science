import sys

if len(sys.argv) != 2:
    print("AssertionError: more than one argument is provided")
    sys.exit()
if sys.argv[1].lstrip('-').isdigit():  
    if int(sys.argv[1]) % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
        sys.exit()
else:
    print("AssertionError: argument is not an integer")
    sys.exit()