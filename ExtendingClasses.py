#Wanting a list that wants you to append items are unique, like a set.
class UniqueList(list):
    def append(self,item):
        if item in self:
            return
        super().append(item)

uniqueList = UniqueList()
uniqueList.append(1)
uniqueList.append(2)
uniqueList.append(3)

print(uniqueList)