#有序、可變動的列表 List
grades=[20, 50, 70, 90, 80]
print(grades)
print(grades[3]) #List的索引從0開始
print(grades[0:3]) #List的索引從0開始

grades[0]=55 #List的資料可以被改變：把列表中的第一個數字改為55
print(grades)

grades=[20, 50, 70, 90, 80]
grades[1:4]=[] #List的資料可以被改變：把列表中的編號1~4（但不包含）改為空白，刪除的意思
print(grades)

grades=[20, 50, 70, 90, 80]
grades=grades+[12, 33] #列表的串接，原來的列表加上新的列表
print(grades)

#取得列表的長度是length，用len(列表)表示
grades=[20, 50, 70, 90, 80]
length=len(grades) #取得列表的長度
print(length)


#巢壯列表：列表中放入另外的列表
data=[[3, 4, 5], [6, 7, 8]]
print(data[1])
print(data[1][2]) #取得巢狀列表中的資料，data[1]是第二個列表，data[1][2]是第二個列表中的第三個資料

data=[[3, 4, 5], [6, 7, 8]]
data[0][0:2]=[1, 1, 1] #把巢狀列表中的資料改為1, 1, 1
print(data[0])


#有序、不可變動的列表 Tuple
data=(3, 4, 5)
print(data[2])

#所有的操作都跟list一樣，唯獨無法換資料
data[0]=8 #錯誤，因為Tuple的資料無法被改變