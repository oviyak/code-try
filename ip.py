#to display class of a random IPv4 generated # 
from random import randint, choice
from string import hexdigits
def ipval(x):
    octets=[];
    if x==4:
        for a in range(4):
            octets.append(str(randint(0,255)))
            ip = ":".join(octets)
        for m in range(0,len(octets)):
            octets[m]=int(octets[m])
        print(octets)
    if octets[0]==0: print('Invalid')
    if octets[0]>0 and octets[0]<127: print('Class A')
    if octets[0]>127 and octets[0]<191: print('Class B')
    if octets[0]>191 and octets[0]<225: print('Class c')
    return ip


#To display the subnet count 
def iprange(x):
    ip,sub=x.split('/')
    octet=ip.split('.')
    sub=int(sub)
    count=32-sub
    count=2**count
    return count

#To display the subnet mask 
