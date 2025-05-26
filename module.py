#載入模組的基本語法：import 模組名稱  or  import 模組名稱 as 模組別名
#使用模組：模組名稱或別名.函式名稱(參考資料) or 模組名稱或別名.變數名稱

#載入內建的sys模組，並取得資訊
# import sys
# print(sys.platform) #印出作業系統的名稱
# print(sys.maxsize) #印出系統的最大整數大小

# import sys as s #載入sys模組，並將模組命名為s
# print(s.platform)
# print(s.maxsize) 


#建立geomestry模組，載入使用：
#要建立新的頁面去建立模組，然後在這個頁面中載入模組
# import geometry
# result=geometry.distance(1, 1, 5, 5)
# print(result) #印出兩點之間的距離
# result=geometry.slope(1, 1, 5, 5)
# print(result) #印出兩點之間的斜率



#調整搜尋模組的路徑
import sys
#print(sys.path) #印出目前的模組搜尋路徑

#當我把我自己設定的模組放入module資料夾，程式搜尋路徑就找不到了，因此需要修改搜尋路徑
import sys
sys.path.append("modules") #在模組的搜尋路徑列表中新增路徑   #append代表增補
print(sys.path)

import geometry
result=geometry.distance(1, 1, 5, 5)
print(result)
