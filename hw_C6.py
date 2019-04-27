with open('rosalind_subs.txt') as f:
    s=f.readline()
    t=f.readline()
    
a = []   

for i in range(0,len(s)):
 if s[i:i+9] == t[0:9]:
    a.append(i+1)
    
b = [str(r) for r in a]
c = ' '.join(b)
print(c)
