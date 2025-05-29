#Python文字檔案的讀取和儲存

    #開啟基本語法：檔案物件= open(檔案路徑, mode=開啟模式, encoding=編碼格式)
        #開啟模式：
            #r：讀取模式，預設值，檔案必須存在
            #w：寫入模式，檔案不存在則建立，存在則覆蓋
            #r+：讀取和寫入模式，檔案必須存在
        #encoding=編碼格式：
            #如果不寫encoding，預設語言就是英文
            #如果要寫中文，編碼為"utf-8"（中文）或"big5"（繁體中文）

    #讀取檔案：
        #基本語法：檔案物件.read()  ===>讀取檔案內容，回傳字串
        #一次讀取一行：for 變數 in 檔案物件  ===>從檔案依序讀取每行文字到變數中
    #讀取JSON格式檔案：
        #基本語法：import json
        #讀取到的資料=json.load(檔案物件)



#開啟/儲存檔案
# file=open("data.text", mode="w", encoding="utf-8") #建立/開啟一個檔案（如果這個檔案不存在，Python會自動幫你新建一個檔案；存在則覆蓋）
# file.write("中文測試\nSecond line") #把文字寫進去
# file.close() #關閉（資料在寫入後，真正存到硬碟上是需要關閉檔案才會完成的。）

#開啟/儲存檔案的最佳實務寫法：with開頭的寫法，就不需要close，系統會自動幫我們安全關閉檔案
# with open("data.text", mode="w", encoding="utf-8") as file: #開啟檔案
#     file.write("中文測試\nSecond line") #寫入檔案

#讀取檔案：檔案物件.read()  ===>一次讀取檔案內容
# with open ("data.text", mode="r", encoding="utf-8") as file:
#     data=file.read()
# print(data) #讀取檔案內容，回傳字串




#如果資料是數字，而我想要在讀取時做一些動作呢？例如加法
# with open("data.text", mode="w", encoding="utf-8") as file:
#     file.write("5\n3") 
# #一次讀取一行：for 變數 in 檔案物件  ===>從檔案依序讀取每行文字到變數中
# sum=0
# with open ("data.text", mode="r", encoding="utf-8") as file:
#     for line in file: #把資料一行一行讀出來
#         sum+=int(line)     #把字串轉成數字，再加總
# print(sum)



#使用JSON格式讀取、複寫檔案
import json
#從檔案中讀取json格式的資料，放入變數data中
with open("config.json", mode="r") as file:
    data=json.load(file) 
print(data) #data是一個字典資料
data["name"]="New name" #我想要修改data中的資料
#然後再覆寫入檔案中
with open("config.json", mode="w") as file:
    json.dump(data, file) #把 Python 資料寫入 JSON 檔案中