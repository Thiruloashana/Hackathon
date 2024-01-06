
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

def traverse(visited,min_ind,minn,c):
    c+=1
    if(c==19):
        exit(0)
    print("minn",minn)
    print("min_ind",min_ind)
    for i in range(n_neigh):
        for j,k in n_ndist.items():
            print(j,min_ind)
            if j==min_ind:
                    m=n_ndist[min_ind]['distances'][0]
                    for i in range(len(n_ndist[min_ind]['distances'])):
                        if m>n_ndist[min_ind]['distances'][i] and n_ndist[min_ind]['distances'][i]!=0:
                            m=n_ndist[min_ind]['distances'][i]
                    print("m",m)
                    m_ind=n_ndist[min_ind]['distances'].index(m)
                    print("m_ind",m_ind)
                    x=[]
                    x=n_ndist[min_ind]['distances']
                    while m_ind in visited:
                        x=[ele for ele in x if x.index(ele) not in visited]
                        print(index)
                        m=x[0]
                        for i in range(len(x)):
                            if m>x[i] and x[i]!=0:
                                m=x[i]                             
                        m_ind=n_ndist[min_ind]['distances'].index(m)                    
                    visited.append(m_ind)
                    print("visited: ",visited)
                    traverse(visited,m_ind,m,c)
                                     

c=0
visited=[]
minn=min(r_ndist)
min_ind=r_ndist.index(minn)
visited.append(min_ind)
traverse(visited,min_ind,minn,c)
