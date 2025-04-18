from collections import UserDict


dictionary1 = UserDict({"list1":[1,2,3,4],"list2":[2,3,4,5]})
print(dictionary1.__getitem__("list1"))
print(dictionary1["list1"])


