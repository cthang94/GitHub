adict = {}
mydict = dict()

mydict['red'] = 'rouge'
mydict['blue'] = 'bleu'
mydict['yellow'] = 'jaune'

print (mydict)
print (mydict['yellow'])
a = len(mydict)
print (a)

for a, b in mydict.items():
    print (a,b)

for x in sorted(set(mydict)):
    print (x)


freq = dict()
word = 'antidisestablishmentarianism'

for letter in word:
    freq[letter] = freq.get(letter,0) + 1

print (freq)

str = 'cat'
freq2 = dict()

for letter in str:
    if letter is not '':
        freq2[letter] = freq.get(letter,0) + 1
print (freq2)
