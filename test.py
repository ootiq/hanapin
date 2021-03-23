from hanapin import Google

g = Google("something", count=3)

for i in g.results():
    print(i)