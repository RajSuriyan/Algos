def caesarCipher(s, k):
    # Write your code here
    n=""
    for i in s:
        if(i.isalpha()):
            if(i.islower()):
                k=k%26
                d=0
                d=ord(i)+k
                if(d>122):
                    d=d-122+96
                    n=n+chr(d)                    
                else:                    
                    n=n+chr(d)                    
            else:
                c=0                    
                k=k%26
                c=ord(i)+k                
                if(c>90):
                    c=ord(i)+k-91+65
                    print(c)
                    n=n+chr(c)
                    c=0
                else:
                    n=n+chr(c)
                    c=0            
        else:
            n=n+i
            print(n)
    return n
