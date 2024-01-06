
import json

f = open('level0.json')
data = json.load(f)
r_ndist=[]
rest={}
n_ndist={}
index=0
for key,value in data.items():
    print(key,value)

    n_neigh=data['n_neighbourhoods']
    print()

    if key=='neighbourhoods':
        for k,v in data[key].items():
            n_ndist[index]=v
            index+=1

    print()
    if key=='restaurants':
       for k1,v1 in data[key].items():
           if k1=='r0':
               rest=v1
               for k2,v2 in rest.items():
                   if k2=='neighbourhood_distance':
                       r_ndist=v2
print("R_NDIST")
print(r_ndist)
print("N_NDIST")
for key,value in n_ndist.items():
    print(n_ndist[key]['distances'])

visited={}


f.close()
