import operator
import typing
"""
10
Jake Jake 42 M
Jake Kevin 57 M
Jake Michael 91 M
Kevin Jake 2 M
Kevin Kevin 44 M
Kevin Michael 100 M
Michael Jake 4 M
Michael Kevin 36 M
Michael Michael 15 M
Micheal Micheal 6 M
"""
def person_lister(f: callable):
    def inner(people):
        people = sorted(people, key = lambda person: int(person[2]) )
        print("Sorted People")
        print_list(people)
        result: list[str] = []
        for person in people :
            result.append(f(person))
        
        return result
    
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

def print_list(li: list[any]) -> None :
    for el in li :
        print(el)

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print_list(people)
    print(*name_format(people), sep='\n')