from datetime import datetime
from re import sub
from pyperclip import paste

class Item:
    def __init__(self, oT, count):
        self.oT = oT
        self.count = count

fileLines = paste().split("\n")

newList = []
regexRemove = "[|Â•·\t,/\.”“]"
regexRemove2 = []

try:
    with open("ignoreList.txt", "r") as f:
        pass
except FileNotFoundError:
    with open("ignoreList.txt", "w") as f:
        pass

with open("ignoreList.txt", "r", encoding="utf8") as file:
    regexRemove2 = file.readlines()
    for i in range(len(regexRemove2)):
        regexRemove2[i] = sub("\\n", "", regexRemove2[i])  

for i in fileLines:
    i = sub(regexRemove, "", i)
    for ii in regexRemove2:
        i = sub(ii, "", i)

    i = i.strip()
    newList.append(i)

ignoist = ["", " ", "   "]
items = []
counter = 0
for i in newList:
    temp = i
    temp = sub("\d", "", temp).strip()

    if temp in ignoist:
        continue
    for ii in newList:
        temp2 = ii
        temp2 = sub("\d", "", temp2).strip()
        if temp == temp2:
            counter += 1

    ignoist.append(temp)
    items.append(
        Item(
            sub(regexRemove,"",i).strip(),
            counter
        )
    )
    counter = 0

items = sorted(items,key= lambda i: i.count, reverse=True)

now = datetime.now()
time = now.strftime("%I-%M-%S%p")


with open(f"output{time}.csv", "w") as file:
    for i in items:
        file.write("{0} instance{1} of {2}\n".format(i.count, "s" if i.count > 1 else " " , i.oT))
