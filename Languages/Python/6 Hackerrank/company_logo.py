#!/bin/python3

import math
import os
import random
import re
import sys


class Solution () : 
    def max_repeat_chr (self, s: str) -> str :
        chr_ocurrence_list: list[tuple[str, int]] = []
        listed_chrs: list[str] = []
        
        for chr_ in s :
            if chr_ not in listed_chrs :
                listed_chrs.append(chr_)
                
                chr_ocurr = (chr_, s.count(chr_))
                
                chr_ocurrence_list.append( chr_ocurr )
        
        #to sort it aphabetically
        chr_ocurrence_list = list( sorted(chr_ocurrence_list, key=lambda chr_ocurr: chr_ocurr[0] ) )
        #to sort it in desending order
        chr_ocurrence_list = list( sorted(chr_ocurrence_list, key=lambda chr_ocurr: -chr_ocurr[1] ) )
        
        max_chr = chr_ocurrence_list[0][0]
        max_chr_ocurr = chr_ocurrence_list[0][1]
        
        print(f"{max_chr} {max_chr_ocurr}")
        
        return s.replace(max_chr, "")



if __name__ == '__main__':
    s = input("Enter string:  ")
    sol = Solution()
    for i in range(3) :
        s = sol.max_repeat_chr(s)
