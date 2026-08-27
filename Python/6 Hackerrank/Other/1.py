#for debugging
import inspect

def debug(*args):
    frame = inspect.currentframe().f_back  # Get caller's frame
    local_vars = frame.f_locals  # Get local variables in the function's scope
    
    output = []
    for arg in args:
        name = next((var for var, val in local_vars.items() if val is arg), "?")
        output.append(f"{name} = {repr(arg)}")  

    print(", ".join(output))  # Print formatted output
    print()


class Solution:
    def count_sq(self, s: str) -> int:
        """Counts the number of '[' in the string."""
        count = 0
        for el in s:
            if el == "[":
                count += 1
        return count
    
    def count_substr(self, s: str, ptr_sq1: int, info_str: list[int]) -> list[int]:
        """Extracts the number before '[' and updates info_str accordingly."""
        idx = ptr_sq1 - 1
        count = ""
        while True:
            try:
                if s[idx] in {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}:
                    count += s[idx]
                    idx -= 1
                else:
                    break
            except IndexError:
                break
        
        count = count[::-1]  # Reverse the extracted number
        info_str.append(len(count))
        info_str[0] = int(count)
        return info_str
    
    def bracket(self, s: str) -> list[int]:
        """Finds the positions of the last '[' and ']' and retrieves the preceding number."""
        ptr_sq1 = -1
        ptr_sq2 = -1
        info_str = [-1, -1, -1]  # Count, '[' index, ']' index

        for i in range(1, len(s) + 1):
            if s[-i] == ']':
                ptr_sq2 = -i
            if s[-i] == '[':
                ptr_sq1 = -i
                info_str[1] = ptr_sq1
                info_str[2] = ptr_sq2
                info_str = self.count_substr(s, ptr_sq1, info_str)
                break
        
        return info_str
    
    def decodedString(self, s: str) -> str:
        """Decodes the given encoded string based on the pattern 'number[string]'."""
        answer = ""
        result = ""
        count = self.count_sq(s)

        while count > 0:
            info_str = self.bracket(s)
            sub_str = s[info_str[1] + 1: info_str[2]]

            while info_str[0] > 0:
                result += sub_str
                info_str[0] -= 1
            
            
            if info_str[2] + 1 != 0:
                be_replace_sub_str = s[info_str[1] - info_str[3]: info_str[2] + 1]
            else:
                be_replace_sub_str = s[info_str[1] - info_str[3]:]
            
            sub = s.count(be_replace_sub_str) 
            s = s.replace(be_replace_sub_str, result)

            if count != 1:
                answer = result + answer
            else:
                answer = result

            result = ''
            count -= sub
        
        return s



#{  # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    #t = int(input())
    t=2
    for _ in range(t):
        print(f"Test case {_+1}")
        s = "11[b2[a]]"
        #s = "3[a3[b]1[ab]]"
        #s = input()

        ob = Solution()
        print(ob.decodedString(s))
        print("~")

# } Driver Code Ends





"""
Try 1
class Solution:
    def __init__ (self) :
        self.occurrence_w_part: list = []
    
    
    def find_no_sub_parts (self, s) -> int :
        no_sub_parts: int = 0
        for idx in range(1, len(s)+1) :
            if s[-1 * idx] == "]" :
                no_sub_parts += 1
        
        return no_sub_parts
    
    
    def sperate_parts(self, s) -> None :
        no_sub_parts: int = self.find_no_sub_parts(s)
        
        start_idx = no_sub_parts + 1
        
        str_part: str = ""
        while start_idx <= len(s) :
            if s[-1 * start_idx] != "[" :
                str_part += s[-1 * start_idx]
                start_idx += 1
            else :
                start_idx += 1
                str_part = str_part[ : : -1]
                self.occurrence_w_part.append( [ int(s[-1 * start_idx]), str_part ] )
                start_idx += 1
                str_part: str = ""
        
        return
    
    
    def generate_part (self, part, idx) -> None :
        result: str = ""
        
        for i in range(part[0]) :
            result += part[1]
        
        
        if idx+1 != len(self.occurrence_w_part) :
            part2 = self.occurrence_w_part[idx + 1]
            part2[1] += result
            
            self.occurrence_w_part[idx + 1] = part2
        else :
            part2 = self.occurrence_w_part[idx]
            part2[1] = result
            
            self.occurrence_w_part[idx] = part2
        
        
        return
    
    
    def decodedString(self, s):
        self.sperate_parts(s)
        
        for idx, part in enumerate(self.occurrence_w_part) :
            self.generate_part(part, idx)
        
        #print(self.occurrence_w_part)
        
        return self.occurrence_w_part[-1][1]
"""