#words, count = open('enable1.txt', 'r').readlines(), 0
#for word in words:
#    aword = word[:-2]
#    if ''.join(sorted(aword)) == aword:
#        count += 1
#print count

words = open('enable1.txt', 'r').readlines()
count = 0
for word in words:
    aword = word.replace('\n', '').replace('\r', '')
    if ''.join(sorted(aword)) == aword:
        count += 1
print count 
