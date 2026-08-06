import sys


args = sys.argv
first = args.get(1, None)
if first == "1":
    print("1")
elif first == "2":
    print("2")
else:
    print("no router given.")
