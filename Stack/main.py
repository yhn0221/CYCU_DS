def reverse_string_with_stack(s):

    stack = list(s)
    
    reversed_string = ''
    while stack:
        reversed_string += stack.pop()
        # print(reversed_string)
    
    return reversed_string

user_input = input("請輸入一段文字: ")

print("反轉後的文字是:", reverse_string_with_stack(user_input))
