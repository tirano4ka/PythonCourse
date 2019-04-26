with open('rosalind_revc.txt', 'r') as file:    
    a=list(file.read())
for i in a:
  if i == 'A':
    i = 'T'
  elif i == 'T':
    i='A'
  if i == 'G':
    i = 'C'
  elif i == 'C':
    i='G'
a.reverse()    
b = ''.join(a)

print(b)
