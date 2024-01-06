
import json

f = open('level0.json')
data = json.load(f)
r_ndist=[]
rest={}
n_ndist={}
index=0
for key,value in data.items():
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
f.close()

def traverse(visited,min_ind):
    for i in range(n_neigh):
        for j,k in n_ndist.items():
            if j==min_ind:
                for z in range(len(n_ndist[j]['distances'])):
                    m=min(n_ndist[j]['distances'][z])
                    m_ind=n_ndist[j]['distances'][z].index(m)
                    while m_ind in visited:
                        n_ndist[j]['distances'][z].remove(m)
                        m=min(n_ndist[j]['distances'][z])     
                        m_ind=n_ndist[j]['distances'][z].index(m)                    
                    visited.append(m_ind)
                    traverse(visited,m_ind)
                                     


visited=[]
minn=min(r_ndist)
min_ind=r_ndist.index(minn)
visited.append(min_ind)
#traverse(visited,min_ind)
print(n_ndist[j]['distances'][0])