import array as array
import array as myarr
balance = array.array('i',[300,200,100])
balance.insert(2, 150)
print(balance)
balance.insert(4,5)
print(balance)
print("after insertion",balance.insert(4,6))

first = myarr.array('b',[20,25,30])
first.pop(2)
print(first)

no = myarr.array('b',[10,4,5,5,7])
del no[4]
print(no)

number = myarr.array('b',[2,3,3,3,4,5,6])
print(number.index(3))

num = myarr.array('b',[1,2,3])
num.reverse()
print(num)

p = array.array('u',[u'\u0050',u'\u0059'])
print(p)
q = p.tounicode()
print(q)

n = myarr.array('b',[2,3,5,4,3,3,3])
print(n.count(3))

bal = array.array('i',[300,200,100])
for x in balance:
    print(x)
