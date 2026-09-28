
#Initialising some oftwn used variables
a_to_z: list[str] = [chr(ascii_value) for ascii_value in range(97, 123, 1)]
A_to_Z: list[str] = [chr(ascii_value) for ascii_value in range(65, 91, 1)]
zero_nine: list[str] = [str(num) for num in range(0, 10, 1)]
other_chrs: list[str] = ["_", "-"]



def fun(email: str):
    """
    return True if s is a valid email, else return False
    """
    try :
        email = email.split("@")
        email[1] = email[1].split(".")
        
        user, web, exe = email[0], email[1][0], email[1][1]
        #username, websitename, extension
    except IndexError :
        return False
    
    #checking if any one of them is empty
    if not (user and web and exe) :
        return False
    
    
    for chr_ in user :
        if  not(chr_ in a_to_z  or  chr_ in A_to_Z  or  chr_ in zero_nine  or chr_ in other_chrs) : 
            return False
    
    
    for chr_ in web :
        if  not(chr_ in a_to_z  or  chr_ in A_to_Z  or  chr_ in zero_nine) : 
            return False
    
    #checking if exe is under 4 chrs 
    if len(exe) > 3 :
        return False
    
    for chr_ in exe :
        if  not(chr_ in a_to_z  or  chr_ in A_to_Z) : 
            return False
    
    return True
    


def filter_mail(emails):
    return list(filter(fun, emails))


if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)