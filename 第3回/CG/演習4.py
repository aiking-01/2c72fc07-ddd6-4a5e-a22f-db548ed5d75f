class Prefecture:
 def __init__(s,n,p,a,c,f):s.n,s.p,s.a,s.c,s.f=n,p,a,c,f
 def show(s):print("\n府県名：",s.n,"\n人口：",s.p,"\n面積：",s.a,"\n府県庁所在地：",s.c,"\n府県の花：",s.f)
 def density(s):return s.p/s.a