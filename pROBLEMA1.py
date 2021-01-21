with open("input.txt",'r') as x:
    list1=list(eval(x.readline()))
print(list1)
list2=sorted(list1)
print(list2)
revers=sorted(list1)
revers.sort(reverse=True)
print(revers)
print('numărul de elemente din listă = ',len(list1))
print('elementul maximum = ',max(list1))
print('elementul minimum = ',min(list1))
list3=list1
list3.append(111)
print(list3)
list4=list1
list4.insert(1,222)
list4=list4[0:len(list4)-1]
print(list4)