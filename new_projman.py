'''
Author: Dasu Srinivas
'''
import yaml
import os
'''
Setting up default and environment variables
'''
per='0777'
os.environ["PROJMAN_TEMPLATES"]="/Users/lenovo/PycharmProjects/projman/src/projman/projman_template.yaml"+":/Users/lenovo/PycharmProjects/projman/src/projman/projman_template1.yaml"
os.environ["PROJMAN_LOCATION"]="/Users/lenovo/PycharmProjects/projman/src/projman"
path=os.environ["PROJMAN_LOCATION"]
type_d=all
name="HULK"

'''
Creation of Directory structure based on user input
'''
def create(path,type_d,name):
    s = yaml_parsing()
    if path is None:
        path=os.environ["PROJMAN_LOCATION"]
    if type_d is None:
        type_d=all
    if name is None:
        name="HULK"
    path=os.path.join(path,"projects",name)
    if not os.path.exists(path):
        os.makedirs(path)
    for i in range(0,len(s)):
        parsing_yaml(s[i],path,type_d,name)

'''
For parsing yaml file
'''
def yaml_parsing():
    st=os.environ["PROJMAN_TEMPLATES"]
    templates=st.split(':')
    print templates
    for i in range(0,len(templates)):
        with open(templates[i]) as stream:
            try:
                return yaml.load(stream)
            except yaml.YAMLError as exc:
                print exc

'''
For parsing nested lists
'''
def parsing_lis(folders,  path,type_d,name):
    for items in folders:
        parsing_yaml(items,  path,type_d,name)

'''
For parsing nested dictionaries
'''
def parsing_dic(folders, path,type_d,name):
    global per
    for fol in folders.keys():
        if fol == 'permission':
            per = folders[fol]
        elif fol == 'value':
            if (type(folders[fol])!=type({})):
                name=folders[fol]
                if per!='0777':
                    if not os.path.exists(os.path.join(path, name)):
                        try:
                            os.makedirs(os.path.join(path, name), per)
                        except:
                            os.makedirs(os.path.join(path, name), int(per))
                    #create_directory(path, folders[fol], per)
                    per='0777'
                else:
                    if not os.path.exists(os.path.join(path,name)):
                        os.makedirs(os.path.join(path,name))
            else:
                parsing_yaml(folders[fol], path,type_d,name)
        else:
            print per
            if per!='0777':
                if not os.path.exists(os.path.join(path, fol)):
                    try:
                        os.makedirs(os.path.join(path, fol), per)
                    except:
                        os.makedirs(os.path.join(path, fol), int(per))
                per='0777'
            else:
                if not os.path.exists(os.path.join(path,fol)):
                        os.makedirs(os.path.join(path,fol))
            path = os.path.join(path, fol)
            parsing_yaml(folders[fol], path,type_d,name)


def parsing_yaml(folders, path,type_d,name):
    if (type(folders) == type([])):
        parsing_lis(folders,  path,type_d,name)
    elif (type(folders) == type({})):
        parsing_dic(folders,  path,type_d,name)

emptyDirs = []
'''
list all files, folders and directories
'''
def list():
    for root, dirs, files in os.walk(os.getcwd()):
        print(root)
        print(dirs)

def deleteFiles(dirList, dirPath):
    for file in dirList:
        print "Deleting " + file
        os.remove(dirPath + "/" + file)

def removeDirectory(dirEntry):
    print "Deleting files in " + dirEntry[0]
    deleteFiles(dirEntry[2], dirEntry[0])
    emptyDirs.insert(0, dirEntry[0])
'''
Deleting all files and folders recursively
'''
def delete():
    tree = os.walk(os.getcwd())
    for directory in tree:
        removeDirectory(directory)

    for dir in emptyDirs:
        print "Removing " + dir
        os.rmdir(dir)
def describe():
    for root, dirs, files in os.walk(os.getcwd()):
        print(root)
        print(dirs)
        print(files)
def type():
    print "not implemented"
if __name__== '__main__':
    create(path,type_d,name)

#parsing_yaml(yd, path)
