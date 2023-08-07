s="1234"
li = {str(i): chr(i + 64) for i in range(1, 27)}
di={}

def decode(s,t):
    
    
    if s=="":
        print(t)
        return 1
    
    if s in di:
        return di[s]
    
    elif s[0]=="0":
        return 0

    
    
    if s[0]!="0":
        x1,x2=0,0
        x1=decode(s[1:],t+li[s[0]])
        if len(s)!=1:
            if int(s[0:2])<=26:
                x2=decode(s[2:],t+li[s[0:2]])
        
        di[s]=x1+x2
        return x1+x2


print(decode(s,""))