import pickle
import json
class Foo(object):
    def __init__(self):
        self.x = 1
        self.y = 2

fobj=Foo()
s=json.dumps(fobj.__dict__)
print(s)
g=pickle.load(open('results.p','rb'))
print(json.dumps(g.__dict__))