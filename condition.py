#判斷式
#if True:
#    print("True oooo")
#else:
#    print("False zzzz")


#x=input("請輸入一個數字:") #input()函數會將輸入的資料轉成字串型態，即便輸入數字，也還是字串的型態
    #使用者在終端輸入數字後會再去跑下面的的程式
#x=int(x) #將字串轉成整數型態
#if x>100:
#    print("大於100")
#else:
#    print("小於等於100")


#x=input("請輸入一個數字:")
#x=int(x)
#if x>200:
#    print("大於200")
#elif x>100:
#    print("大於100，小於等於200")
#else:
#    print("小於等於100")


#四則運算
#n1=int(input("請輸入第一個數字:")) #先輸入字串再馬上轉換成數字型態（合併寫）
#n2=int(input("請輸入第二個數字:"))
#print(n1+n2)

n1=int(input("請輸入第一個數字:")) 
n2=int(input("請輸入第二個數字:")) 
op=input("請輸入運算: +, -, *, /:")
if op=="+":
    print(n1+n2)
elif op=="-":
    print(n1-n2)
elif op=="*":
    print(n1*n2)
elif op=="/":
    print(n1/n2)
else:
    print("不支援運算")