import sys
import random
try:
    print(f"first argument {sys.argv[1]}")
    args = sys.argv
    random.shuffle(args)
    print(f"Random argument {args[0]}")
except IndexError as err:
    print(f"Error:no arguments, provide atleast one({err})")
    sys.exit(1)
except (NameError,KeyError) as err1:
    print(f"Eror: module not loaded ({err1})")
    sys.exit(1)
else:
    print("this is else part")
finally:
    print("final execution phase")
