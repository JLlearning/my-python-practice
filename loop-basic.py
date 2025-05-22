# while 迴圈
#n=1
#while True:
#    print(n)
#    n+=1
#上面這個程式是正確的，但沒有盡頭，是無窮迴圈

#n=1
#while n<=3:
#    print(n)
#    n+=1
#上面這個程式就是有盡頭的，會印出1,2,3，然後結束

#1+2+3+...+10用while迴圈呈現
sum=0 #紀錄累加的結果
n=1
while n<=10:
    sum=sum+n #注意縮排，縮排內代表迴圈內的結構，縮排外代表迴圈外的結構
    n+=1
print(sum)


#for迴圈
for x in [5,8, 10]:  #x的值取自於列表中的值
    print(x) #印出列表中的值

for x in "apple":  #x的值取自於字串
    print(x) #印出字串中的值

for x in range(5):  #x的值取自於range內的列表：0, 1, 2, 3, 4，但不含5
    print(x) 

for x in range(5, 10):  #x的值取自於range內的列表：5, 6, 7, 8, 9，但不含10
    print(x) 


#1+2+3+...+10用for迴圈呈現
sum=0
for x in range(1, 11):  #x的值取自於range內的列表：5, 6, 7, 8, 9，但不含10
    sum=sum+x 
print(sum) 