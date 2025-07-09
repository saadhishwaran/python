def lastd():
    dict1 = dict1.popitem()
    print(dict1)

def get():
    dict2 = dict1.get()
    print(dict2)

def value():
    dict2 = dict1.values()
    print(dict2)

def delent():
    dict1.clear()
    print("the dict has been droped")
    
def addnew():
    dict1.update()
    print(dict1)

dict1 = {"k1":'v1','k2':'v2'}