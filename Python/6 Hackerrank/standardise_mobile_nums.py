
def wrapper(f):
    def fun(li):
        nums: list[str] = []
        for num in li :
            if len(num) > 10 :
                num = num[:: -1]
                mobile_num = num[0 : 10]
                mobile_num = mobile_num[:: -1]
                mobile_num = f"+91 {mobile_num[ : 5]} {mobile_num[5 :]}"
                nums.append(mobile_num)
            else :
                mobile_num = f"+91 {num[ : 5]} {num[5 :]}"
                nums.append(mobile_num)
            
        
        
        f(nums)
    
    return fun

@wrapper
def sort_phone(li):
    print(*sorted(li), sep='\n')

if __name__ == '__main__':
    li = [input() for _ in range(int(input()))]
    sort_phone(li) 


