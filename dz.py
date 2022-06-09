#  # Задание 1 Написать программу вычисления арифметического выражения заданного строкой. Используются операции +,-,/,*. приоритет операций стандартный. 


# input_string = '1+4/2-2'
# result = 0
# counter = -1
# for ch in range(len(input_string)):
#     if counter == ch:
#         continue
#     if input_string[ch] in ['-', '+', '/', '*']:
#         next_value = int(input_string[ch+1])
#         if input_string[ch] == '-':
#             result -= next_value
#             counter = ch+1
#         elif input_string[ch] == '+':
#             result += next_value
#             counter = ch+1
#         elif input_string[ch] == '*':
#             result *= next_value
#             counter = ch+1
#         elif input_string[ch] == '/':
#             result /= next_value
#             counter = ch+1
#     else:
#         result = int(input_string[ch])

# print(result)

# Задание 2  Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных файлах (в одном файлике отрывок из какой-то книги, а втором файлике — сжатая версия этого текста).

with open('file.txt', 'r') as data:
    my_text = data.read()

def encode_rle(ss):
    str_code = ''
    prev_char = ''
    count = 1
    for char in ss:
        if char != prev_char:
            if prev_char:
                str_code += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    return str_code

            
str_code = encode_rle(my_text)
print(str_code)

with open('file.txt', 'r') as data:
    my_text2 = data.read()

def decoding_rle(ss:str):
    count = ''
    str_decode = ''
    for char in ss:
        if char.isdigit():
            count += char 
        else:
            str_decode += char * int(count)
            count = ''
    return str_decode

str_decode = decoding_rle(my_text2)
print(str_decode)