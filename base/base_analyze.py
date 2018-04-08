import os,yaml

def yml(file_name):
    file_path = os.getcwd()+os.sep+"data"+os.sep+file_name+".yml"
    with open(file_path,"r",encoding="utf-8") as r:
        return yaml.load(r)