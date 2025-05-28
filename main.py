#主程式
#import 封包名稱.模組名稱（先把資料夾與模組叫出來）
import geometry.point
result=geometry.point.distance(3,4) #呼叫函式
print(result) 

import geometry.line
result=geometry.line.slope(1, 1, 5, 5) #呼叫函式
print(result) 

import geometry.line as line
result=line.slope(1, 1, 5, 5) #呼叫函式
print(result) 