import getpass          

n = list(getpass.getpass('Word to be guessed:'))

i = 0
g = ''
seen = []

while i < len(n):       
    if n[i].isupper() or n[i].islower():
        g = g + '_'
    else:
        g = g + n[i]
    i = i + 1

g = list(g)                     

wrong = raw_input('Enter no. of lives: ')

i2 = 0
while n != g:
    m = raw_input('guess: ')

    if m in seen:       
        print ('!! You have already guessed this letter !!')


    i3 = 0
    while i3 < len(n):                  
        if n[i3] == m.lower() or n[i3] == m.upper():
            g[i3] = n[i3]
        i3 = i3 + 1

    if m not in n:
        if m not in seen:           
            i2 = i2 + 1
            print ('Lives:'), wrong - i2
    seen.append(m)

    if i2 == wrong:         
        break

if n == g:          
    print ('You Win:'), ('').join(n)
else:
    print ('You Lost:'), ('').join(n)
