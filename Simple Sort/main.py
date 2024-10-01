##自all_sort導入sort函式
from all_sort import bubblesort_increasing, bubblesort_decreasing, insertsort_increasing, insertsort_decreasing, selectsort_increasing, selectsort_decreasing


##輸入數字資料
user_input = input("請輸入數字，用逗號和空格分隔，如 2, 3, 1: ")
numbers_str_list = user_input.split(', ')
numbers = [int(number.strip()) for number in numbers_str_list]

##設定選擇的sort方法
sortmode=0

while sortmode not in [1, 2, 3]:
    try:
        sortmode= int(input("請輸入數字，bubble sort請按1，insert sort請按2，select sort請按3: "))
    except ValueError:
        print("輸入有效數字")
    if sortmode not in [1, 2, 3]:
        print("輸入的數字不是1, 2, 或 3。請再試一次。")


##設定遞減或遞增
resulttype=0
while resulttype not in [1, 2]:
    try:
        resulttype= int(input("請輸入數字，遞增請按1，遞減請按2: "))
    except ValueError:
        print("輸入有效數字")
    if resulttype not in [1, 2]:
        print("輸入的數字不是1 or 2。請再試一次。")

##輸出結果選擇哪個
if sortmode==1:
    if resulttype==1:
        print("使用 bubblesort_increasing")
        result= bubblesort_increasing(numbers)
    else:
        print("使用 bubblesort_decreasing")
        result=bubblesort_decreasing(numbers)    
else:
    if sortmode==2:
        if resulttype==1:
            print("insertsort_increasing")
            result=insertsort_increasing(numbers)
        else:
            print("insersort_decreasing")
            result=insertsort_decreasing(numbers)

    else:
        if resulttype==1:
            print("selectsort_increasing")
            result=selectsort_increasing(numbers)
        else:
            print("selectsort_decreasing")
            result=selectsort_decreasing(numbers) 
print(result) 
