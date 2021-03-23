from hanapin import Bing

g = Bing("alone alan walker", count=3)

for i in g.results():
    print(i)