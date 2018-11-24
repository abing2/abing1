import os
def read():
    with open(os.getcwd()+os.sep+'Data'+os.sep+'doc.txt','r',encoding='utf-8')as f :
        list = []
        for line in f.readlines():
            list.append(tuple(line.strip().split(',')))
        return list


