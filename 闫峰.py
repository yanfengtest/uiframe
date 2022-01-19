
import copy
#浅拷贝
a = [[1,2,3],[4,5,6]]
b= a.copy()
b[0].append(10)
print("a:",a)
print("b:",b)
#深拷贝
c = [[1,2,3],[4,5,6]]
d = copy.deepcopy(c)
e = d
d[0].append(10)
print("c:",c)
print("d:",d)
print("e:",e)
print(id(e))
print(id(d))


