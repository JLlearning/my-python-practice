#定義函式
# def multiply():
#     print(3*4)

#呼叫函式：函式內部的程式碼正確，但沒有被呼叫，就不會被執行
# multiply()

# def multiply(n1, n2):   #定義函式，n1, n2是參數，參數的存在可以讓程式碼更有彈性（例如不僅限於3*4，也可以是任意數相乘）
#     print(n1*n2)

# multiply(5, 6)
# multiply(12, 12)


#程式執行完畢後會得到甚麼資料，必須要看回傳值return，如果定義中沒有寫上return或者return後沒有給出具體回傳值，回傳值預設就是none
# def multiply(n1, n2):
#     print(n1*n2)
#     return n1*n2

# value=multiply(3, 7)
# print(value) 


#變化型
# def multiply(n1, n2):
#     print(n1*n2)
#     return n1*n2

# value=multiply(3, 7)+multiply(2, 10)
# print(value) 


#程式的包裝：重複的邏輯可以重複利用
#這是一個1+...+10的程式
# sum=0
# for x in range(1, 11):
#     sum=sum+x
# print(sum)

#如果從1+.....+x的動作需要重複好多次，這時候就可以把它包裝成一個函式
# def calculate():
#     sum=0
#     for x in range(1, 11):
#         sum=sum+x
#     print(sum)

# calculate()

def calculate(max):
    sum=0
    for x in range(1, max+1):
        sum=sum+x
    print(sum)
    return 100

value=calculate(10)
print(value)