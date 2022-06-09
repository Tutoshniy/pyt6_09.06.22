 # Задание 1 Написать программу вычисления арифметического выражения заданного строкой. Используются операции +,-,/,*. приоритет операций стандартный. 


input_string = '1+4/2-2'
result = 0
counter = -1
for ch in range(len(input_string)):
    if counter == ch:
        continue
    if input_string[ch] in ['-', '+', '/', '*']:
        next_value = int(input_string[ch+1])
        if input_string[ch] == '-':
            result -= next_value
            counter = ch+1
        elif input_string[ch] == '+':
            result += next_value
            counter = ch+1
        elif input_string[ch] == '*':
            result *= next_value
            counter = ch+1
        elif input_string[ch] == '/':
            result /= next_value
            counter = ch+1
    else:
        result = int(input_string[ch])

print(result)
