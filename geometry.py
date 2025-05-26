#在geometry模組中定義幾何運算功能（目前有兩個函式）
def distance(x1, y1, x2, y2): #計算平面幾何中兩點之間的距離
    return((x2-x1)**2+(y2-y1)**2)**0.5

def slope(x1, y1, x2, y2): #計算平面幾何中一個線段兩點之間的斜率
    return (y2-y1)/(x2-x1)