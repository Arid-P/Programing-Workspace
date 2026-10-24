#!/bin/python3
"""
7 3
Tsi
h%x
i #
sM 
$a 
#t%
ir!
"""
import math
import os
import random
import re
import sys

add_space: bool = True
def not_alnum () -> str :
    if add_space :
        return " "
    else :
        return ""


def decode_matrix (matrix: list[str], cols: int, rows: int) -> str :
    global add_space
    
    str_matrix: list[str] | str = []
    for col in range(cols) :
        for row in range(rows) :
            try :
                str_matrix.append(matrix[row][col])
            except IndexError :
                str_matrix.append(" ")
    
    special_idx = 0
    for i in range(-1, -len(str_matrix), -1) :
        if str_matrix[i].isalnum() :
            special_idx = i-1
            break
    
    special_idx = len(str_matrix) + special_idx + 2
    
    
    answer: str = ""
    for i in range(special_idx) :
        answer +=  str_matrix[i] if  str_matrix[i].isalnum() else not_alnum()
        add_space =  str_matrix[i].isalnum()
    
    answer += ''.join(str_matrix[special_idx : ])
    
    return answer
    
    
"""{
    s_ptr: int = 0
    e_ptr:int = 1
    is_last: bool = False
    
    while e_ptr <= len(str_matrix) :
         str_matrix[i] = str_matrix[s_ptr:e_ptr]
        #print(f"{s_ptr=}    {e_ptr=}    { str_matrix[i] = }    {length=}")
        if not  str_matrix[i].isalnum() :
            org_e_ptr = e_ptr
            
            if  not is_last :
                for i in range(s_ptr+1, len(str_matrix)) :
                    if str_matrix[i].isalnum() :
                        e_ptr = i
                        break
                
            if e_ptr != org_e_ptr :
                to_replace_substr = str_matrix[s_ptr: e_ptr]
                str_matrix = str_matrix.replace(to_replace_substr, " ")
            else :
                is_last = True
            
            #print(f'{to_replace_substr = }       {str_matrix = }')
        
        s_ptr += 1
        e_ptr = s_ptr + 1
    
    
    return str_matrix
    #}"""




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

result: str = decode_matrix(matrix, m, n)
print(result)
# print()
# if result != "This is Matrix#  %!" :
#     result = set( result.split() )
#     correct_result = set( "This is Matrix#  %!".split() )
#     print(correct_result.intersection(result))