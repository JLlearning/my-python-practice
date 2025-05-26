#參數的預設資料
# def power(base, exponent):
#     print(base**exponent) #印出base的exponent次方的結果
# power(3, 2) #3的2次方
# power(2, 3) #2的3次方

# power(4) 這樣寫，我們少給了一個exponent參數，會報錯
#如果在定義中改成exponent=0，代表如果沒有給exponent的參數的話，exponent預設值是0
# def power(base, exponent=0):
#     print(base**exponent) 
# power(5) #任何數字的0次方都會得到1



# #使用參數名稱對應
# def devide(n1, n2):
#     print(n1/n2)
# devide(2, 4)
# devide(n2=2, n1=4) #參數名稱對應



#無限/不定 參數資料
#def avg():  #我希望使用者無論輸入多少個數字，我都能幫他算出平均值
# def avg(*ns):  #*ns代表不定數量的參數，這個ns會變成一個list
#     print(ns) #ns會變成一個Tuple list，裡面有使用者輸入的所有數字

#如果要算平均數
def avg(*ns):
    sum=0
    for n in ns:
        sum=sum+n
    print(sum/len(ns)) #平均數的寫法：sum是所有數字的總和，len(ns)是數字的個數（代表列表的長度）
avg(3, 5, 10)
avg(-4, 20, -16, 8, 3)