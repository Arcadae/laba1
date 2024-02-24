""""""
#Натуральные числа , состоящие из чётных и нечётных чередующихся цифр . Для каждого числа минимальную и максимальную цифру вывести прописью.ВАРИАНТ-20
""""""
import sys
    
book={
    0 : "zero",
    1 : "one",
    2 : "two",
    3 : "three",
    4 : "four",
    5 : "five",
    6 : "six",
    7 : "seven",
    8 : "eight",
    9 : "nine"
}

try:
    with open('lorem.txt') as file:
        string_with_symbols=file.read(1024)
except FileNotFoundError:
    sys.exit('<<NOT FOUND>>')

flag_of_digit=bool
if len(string_with_symbols)==0:
    sys.exit('Your file has not any symbols , please give another file')
elif len(string_with_symbols)==1:
    sys.exit('Your file has only one symbol , please give another file')
else:
    for elem in range(len(string_with_symbols)-1):
        if string_with_symbols[elem].isdigit() and string_with_symbols[elem+1].isdigit():
            flag_of_digit=True
            break
        else:
            flag_of_digit=False
if flag_of_digit:
    print('Your file is ready to work\n')
else:
    sys.exit('This string has not right number of digits to work')

string_with_symbols=string_with_symbols+' '
string_element=''
for element in range(len(string_with_symbols)):
    if string_with_symbols[element].isdigit() or (string_with_symbols[element]=='-' and string_with_symbols[element+1].isdigit()):
        string_element=string_element+string_with_symbols[element]
    else:
        string_element=string_element+' '
        
work_string=''
flag_of_minus=False
count_of_needed_digits = 0
for element in range(len(string_element)-1):
    if string_element[element]!=' ':
        work_string=work_string+string_element[element]
        if len(work_string)>=2 and string_element[element+1]==' ':
            if work_string[0]=='-':
                flag_of_minus=True
            rgh_string=''
            #print(work_string)
            #print(flag_of_minus)
            for number in range(len(work_string)):
                if flag_of_minus:
                    if number==0:
                        continue
                    elif number==1:
                       if int(work_string[number])%2 == int(work_string[number+1])%2:
                           break
                       else:
                           rgh_string += work_string[number]
                    else:
                       if int(work_string[number])%2 == int(work_string[number-1])%2:
                           break
                       else:
                           rgh_string += work_string[number]
                else:
                    if number==0:
                        if int(work_string[number])%2 == int(work_string[number+1])%2:
                            break
                        else:
                           rgh_string += work_string[number]
                    else:
                        if int(work_string[number])%2 == int(work_string[number-1])%2:
                           break
                        else:
                           rgh_string += work_string[number]
            if rgh_string != work_string and flag_of_minus==False:
                flag_of_minus =False
                continue
            else:
                #print(rgh_string)
                work_int=int
                if len(rgh_string)>=2:
                    work_int=int(rgh_string)
                    if flag_of_minus:
                        work_int *= -1
                    else:
                        work_int=work_int
                    print('We find a number=',work_int)
                    if flag_of_minus:
                        big_number=((work_int*-1)//10)
                    else:
                        big_number=work_int//10
                    while big_number>=10:
                        big_number=big_number//10
                    if flag_of_minus:
                        small_number=((work_int)*-1)%10
                    else:
                        small_number=work_int%10
                    print('The biggest element=',book[big_number],'\n''The smallest element=',book[small_number],'\n')
                work_string=str(work_int)
                flag_of_minus=False
                count_of_needed_digits += 1
    else:
        work_string=''
if count_of_needed_digits==0:
    print('This file has not needed digits')


            
