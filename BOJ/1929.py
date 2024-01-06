text=input()
text1=text.upper()
m=0
cnt=1

for i in range(len(text1)) :
    for j in range(26) :    
        if m<text1.count(chr(j+65)) :
            m=text1.count(chr(j+65))
            n=chr(j+65)
           
print(n)