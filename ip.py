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
#def iprange(x):
    ip,sub=x.split('/')
    octet=ip.split('.')
    sub=int(sub)
    count=32-sub
    count=2**count # count displays the usable IPs in the range 
    return count

#To display the subnet mask from above calc
def netmask(sub):
    total=[128,64,32,16,8,4,2,1]
    whole=int(sub/8)
    rem=int(sub%8)
    a=0
    b=0
    ran=[0,0,0,0]
    while a<whole:
        ran[a]=2**8-1
        a=a+1
    while b<rem:
        ran[a]=total[b]+ran[a]
        b=b+1
    return ran

# to find network id
def nid(x):
    ip,sub=x.split('/')
    octet=ip.split('.')
    sub=int(sub)
    bin1=[0,0,0,0]
    octets=[0,0,0,0]
    bin2=[0,0,0,0]
    for m in range(len(octet)):
        octets[m]=int(octet[m]) # octet = ['198', '167', '1', '1']
    for m in range(len(octets)): 
        bin1[m]=format(octets[m],'08b') # octets = [198, 167, 1, 1]
    binary='.'.join(bin1) #bin1 = ['11000110', '10100111', '00000001', '00000001']
    binjoin=''.join(bin1) # bin2= [11000110, 10100111, 1, 1]
    for m in range(len(bin1)): # binary = '11000110.10100111.00000001.00000001'
        bin2[m]=int(bin1[m])  #binjoin = '11000110101001110000000100000001'
    #to convert subnet ID to binary
    b=0
    c=0
    d=0
    binconv=[0]*32
    while b<32:
        while c<sub:
            binconv[c]=1
            c=c+1
        b=b+1
        binconv[c]=0
    l=[binconv[i:i+8] for i in range (0,len(binconv),8)]
    #convert list into single binary list
    d=0
    bv=[0,0,0,0]
    while d<4:
        s=[str(i) for i in l[d]]
        bv[d]=int("".join(s))
        d=d+1
    strings = [str(integer) for integer in bv]
    a_string = "".join(strings)
    final = int(a_string) # final = 11111111111111111111111111000000
    pro=[str(x) for x in bv] #pro= ['11111111', '11111111', '11111111', '11000000']
    prod='.'.join(pro) # prod = '11111111.11111111.11111111.11000000'
    
    #NETWORK CALCULATION
    nmid=[0,0,0,0]
    for i in range(len(octets)):
        nmid[i]=ran[i]&octets[i] # Range from previous class // NMID is the network ID 
        
    #Broadcast calc
    remainder=int(sub%8)
    subid=total[remainder-1]-1 # total  from previous class
    bid=octets
    bid[int(sub/8)]=subid
    div=int(sub/8)+1 # BID is the broadcast ID 
    while div<4:
        bid[div]=255
        div=div+1
    #FirstIP
    lastno=3
    firstip=nmid
    firstip[lastno]=1 # Displays the first usable IP
    #LastIP
    lastno=3
    lastip=bid
    lastip[lastno]=254 # Displays the last usable IP 
    #Amazon Alloted IPS
       

    

    
    
    

    
    
    
    
