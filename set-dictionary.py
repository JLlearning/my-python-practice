#集合set的運算
s1={3, 4, 5}
print(3 in s1) #判斷3有沒有在集合中，True or False
print(10 in s1)
print(10 not in s1)


s1={3, 4, 5}
s2={4, 5, 6, 7}
s3=s1&s2 #交集&，取相同部分
print(s3)

s3=s1|s2 #聯集|，取兩集合中所有資料，但不重複取
print(s3)

s3=s1-s2 #差集-，從s1中減去與s2重疊的部分
print(s3)

s3=s2-s1 #差集-，從s2中減去與s1重疊的部分
print(s3)

s3=s1^s2 #反交集^，取兩集合中不重疊的部分
print(s3)


 #set(字串)，把字串中的字母拆解成集合，並且不重複
s=set("Hello") #set(字串)
print(s) # {'H', 'e', 'l', 'o'}，集合沒有順序性，所以得出的結果有可能是隨興的且排除重複的部分
print("e" in s)
print("p" in s)


#字典的運算
#字典的運算，字典是無順序的，所以不能用index來取值，key:value
#取值用key來取值
dic={"apple":"蘋果", "bug":"蟲"}
print(dic["bug"])

dic["apple"]="青蘋果" #改變字典中的值
print(dic["apple"])

dic={"apple":"蘋果", "bug":"蟲"}
print("bug" in dic) #判斷key有沒有在字典中，True or False
# in 跟 not in判斷的對象只有key值，不是value值

dic={"apple":"蘋果", "bug":"蟲"}
print(dic)
del dic["bug"] #刪除字典中的key，但是刪的時候會將整個鍵值對一起刪除
print(dic)


#特殊語法 for...in... 
#dic={x:x*2 for x in 列表} →→字典推導式，x值可以寫成任何代號，x是列表中的值乘以2
dic={x:x*2 for x in [1, 2, 3, 4, 5]}
print(dic)
#以列表中的資料去產生字典
