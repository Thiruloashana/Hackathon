
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
for key,value in n_ndist.items():
    print(n_ndist[key]['distances']) 
f.close()

def traverse(visited,min_ind,minn,c):
    c+=1
    if(c==20):
        visited.append('r0')
        print(visited)
        for i in range(1,len(visited)-1):
            visited[i]=str(visited[i])
            y='n'+ visited[i]
            visited[i]=y
        '''paths=[]
        paths.append(visited[0])
        for i in range(1,len(visited)-1):
            y='n'
            y+=str(visited[i])
            paths[i].append(y)
        paths.append(visited[21])'''

        '''for p,q in paths.items():
            print(p,q)'''
        print(visited)
        v0 = {"path": visited}
        output_dict = {"v0": v0}
        with open("level0_output.json", "w") as outfile:
            json.dump(output_dict, outfile) 
        f.close()    
        exit(0)

    for i in range(n_neigh):
        for j,k in n_ndist.items():
            if j==min_ind:
                    m=n_ndist[min_ind]['distances'][0]
                    for i in range(len(n_ndist[min_ind]['distances'])):
                        if m>n_ndist[min_ind]['distances'][i] and n_ndist[min_ind]['distances'][i]!=0:
                            m=n_ndist[min_ind]['distances'][i]
                    m_ind=n_ndist[min_ind]['distances'].index(m)
                    x=[]
                    x=n_ndist[min_ind]['distances']
                    while m_ind in visited:
                        x=[ele for ele in x if x.index(ele) not in visited]
                        m=x[0]
                        for i in range(len(x)):
                            if m>x[i] and x[i]!=0:
                                m=x[i]                             
                        m_ind=n_ndist[min_ind]['distances'].index(m)                    
                    visited.append(m_ind)
                    traverse(visited,m_ind,m,c)
                                     
c=0
visited=[]
visited.append('r0')
minn=min(r_ndist)
min_ind=r_ndist.index(minn)
visited.append(min_ind)
traverse(visited,min_ind,minn,c)
