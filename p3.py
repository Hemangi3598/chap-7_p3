d1 = [10, 30, 10, 20, 40, 25, 10, 14]

print(d1.count(10))
print(d1.count(11))

print(d1.index(30))
print(d1.index(20))
#index functn will show their index position in list
# print(d1.index(21))

print(d1)
d1.reverse()
print(d1)
# reverse functn will simply reverse the data as given

d1.sort()
print(d1)
# sort functn will arrange the data in ascending order

d1.sort(reverse=True)
print(d1)
# If we have to arrange data in descending order then first sort data and then use sort(reverse=True)




