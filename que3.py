num = (1,2,3,4,5,6,7,8,9)
even = 0
odd = 0
for i in num :
    if i % 2 :
        even+= 1
    else :
        odd+= 1
print('total even no is',even)
print('total odd no is',odd)