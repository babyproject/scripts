import argparse

#function
def calc():
    x=input("enter x:")
    y=input("enter y:")
    return x**2+y**2

parser=argparse.ArgumentParser()
parser.add_argument("-D", "--daemon", help="enable daemon mode", action="store_true")
parser.add_argument("-B", "--background",  help="fork into background", action="store_true")
group=parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", help="show details", action="store_true")
group.add_argument("-q", "--quiet", action="store_true", help="enable quiet mode")
parser.add_argument("-w", "--welcome", type=str, help= "show greeting")
parser.add_argument("-o", "--options", type=str, choices=["kiss", "kissme", "kissmeagain"], help="show options")
parser.add_argument("-m", "--math", action="store_true", help="simple math")
args=parser.parse_args()
if args.daemon:
    print("daemon mode enabled")
if args.background:
    print("running in background")
if args.verbose:
    print("running '{}'".format(__file__))
if args.welcome:
    print("welcome here, {}".format(args.welcome))
if args.options=="kiss":
    print("then just kiss")
elif args.options=="kissme":
    print("there you go")
elif args.options=="kissmeagain":
    print("baby one more time")
if args.math:
    anwser=calc()
    print ("the anwser is: {}".format(anwser))

