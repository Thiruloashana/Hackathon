#level1a

import json

f = open('level1a.json')
data = json.load(f)
r_ndist=[]
rest={}
n_ndist={}
index=0
for key,value in data.items():
    n_neigh=data['n_neighbourhoods']

    if key=='neighbourhoods':
        for k,v in data[key].items():
            n_ndist[index]=v
            index+=1

    if key=='restaurants':
       for k1,v1 in data[key].items():
           if k1=='r0':
               rest=v1
               for k2,v2 in rest.items():
                   if k2=='neighbourhood_distance':
                       r_ndist=v2
    if key=='vehicles':
        cap=data[key]['v0']['capacity']
        capacity=cap
        print("capacity",cap)
    
f.close()
print("R_NDIST",r_ndist)

dist={}
for i in range(len(n_ndist)):
    dist[i]=n_ndist[i]['distances']

for x,y in dist.items():
    print(x,y)

paths={}
visited_track=[]
paths_f=[[]]
count=0
def traverse(visited,min_ind,cap,orders,c,paths,count):
    #print(visited)
    print(orders)
    c+=1
    if(len(set(orders))==1):
        '''print(visited_track)
        visited.append('r0')
        for i in range(1,len(visited)-1):
            visited[i]=str(visited[i])
            y='n'+ visited[i]
            visited[i]=y

        v0 = {"path": visited}
        output_dict = {"v0": v0}
        with open("level1_output.json", "w") as outfile:
            json.dump(output_dict, outfile) 
        f.close()''' 
        visited.append("r0")
        paths[count]=visited
        print(paths)
        exit(0)

    for i in range(n_neigh):
        for j,k in n_ndist.items():
            if j==min_ind:
                    m=n_ndist[min_ind]['distances'][0]
                    for i in range(len(n_ndist[min_ind]['distances'])):
                        if m>n_ndist[min_ind]['distances'][i] and n_ndist[min_ind]['distances'][i]!=0:
                            m=n_ndist[min_ind]['distances'][i]
                    m_ind=n_ndist[min_ind]['distances'].index(m)
                    print("m_ind m",m_ind,m)
                    x=[]
                    x=n_ndist[min_ind]['distances']
                    while m_ind in visited_track:
                        x=[ele for ele in x if x.index(ele) not in visited_track]
                        m=x[0]
                        for i in range(len(x)):
                            if m>x[i] and x[i]!=0:
                                m=x[i]                             
                        m_ind=n_ndist[min_ind]['distances'].index(m)                    
                    if cap>=orders[m_ind]:
                        visited.append(m_ind)
                        visited_track.append(m_ind)
                        cap-=orders[m_ind]
                        orders[m_ind]=0
                        print(cap) 
                    else:
                        cap=capacity
                        visited.append("r0")
                        paths[count]=visited
                        count+=1
                        print(paths)
                        visited.clear()
                        print(visited)
                        visited.append("r0")
                    
                    traverse(visited,m_ind,cap,orders,c,paths,count)
                                    
c=0
visited=[]
visited.append('r0')
minn=min(r_ndist)
min_ind=r_ndist.index(minn)
visited.append(min_ind)
visited_track.append(min_ind)
orders=[n_ndist[i]['order_quantity'] for i in range(len(n_ndist))]
print(orders)
orders[min_ind]=0
traverse(visited,min_ind,cap,orders,c,paths,count)
