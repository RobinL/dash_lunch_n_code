thousandList = list(range(1,1000))
sumList = []
for i in thousandList:
    if i % 3 == 0 or i % 5 ==0:
        sumList.append(i)
        
answer = sum(sumList)
print(answer)