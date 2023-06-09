def hello(points,p,k):
    distance=[]
    for g in points:
      for xy in points[g]:
         ecudis = ((xy[0]-p[0])**2 + (xy[1]-p[1])**2)**0.5
         distance.append((ecudis,g))
    f1,f2=0,0
    for d in distance:
       if d[1]==0:
          f1 +=1
       elif d[1]==1:
          f2+=2
    return 0 if f1>f2 else 1
points ={
    1:[(1,1),(2,2),(3,1)],
    0:[(5,3),(4,4),(6,5)]
}
p=(1,2)
k=3
print(hello(points,p,k))