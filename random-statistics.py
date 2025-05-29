#隨機模組
import random

#隨機選取
# data=random.choice([1, 5, 6, 10, 20])  #從列表中隨機選取
# print(data)

# data=random.sample([1, 5, 6, 10, 20], 3)  #從列表中一次隨機選取多筆資料，這邊是選3筆資料
# print(data)


#隨機調換順序shuffle（對資料本身直接調換，洗牌的概念）
# data=[1, 5, 8, 20]
# random.shuffle(data)
# print(data)


#隨機取得亂數
# data=random.random()  #random模組中的random函式呼叫，意思是0~1之間的隨機亂數
# print(data)

#上述寫法也相當於uniform的寫法
# data=random.uniform(0.0, 1.0)  #意思是0.0~1.0之間的隨機亂數，代表中間的數字出現的機率是相同的
# print(data)
# data=random.uniform(60, 100)  #意思是60~100之間的隨機亂數，這個寫法的好處是可以自訂開頭與結尾的數字
# print(data)


#取得常態分配亂數
# data=random.normalvariate(100, 10) #指定平均數100，標準差10，得到的資料大多數會在90~110之間
# print(data)
# data=random.normalvariate(0, 10) #指定平均數0，標準差10，得到的資料大多數會在-10~10之間
# print(data)




#統計模組
import statistics as stat
# data=stat.mean([1, 4, 5, 8])  #mean=平均數
# print(data)

# data=stat.median([1, 4, 5, 8, 11, 6, 60])  #median=中位數（會排除極端值）
# print(data)

data=stat.stdev([1, 4, 5, 8, 11, 6, 300])  #stdev=標準差 standard deviation，代表資料的散佈狀況，值的差距越大散佈越大
print(data)