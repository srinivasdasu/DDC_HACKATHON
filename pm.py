import argparse
import os
import new_projman.py

arg_parse=argparse.ArgumentParser()
arg_parse.add_argument("-t","--type",help="It indictaes type of the project need to create from a template")
arg_parse.add_argumenr("-p","--path",help="It provides path where we need to create our project ")
arg_parse.add_argument("SUBCMD",help="Enter type of operations which you want to do")
arg_parse.add_argument("NAME",help="Name of the project to create")
args=arg_parse.parse_args()
os.environ["PROJMAN_LOCATION"]="/Users/lenovo/PycharmProjects/projman/src/projman"
if args.type:
    print "t",args.type
if args.path:
    path=args.path
else:
    path=os.environ["PROJMAN_LOCATION"]

