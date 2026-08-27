from icecream import ic 


def matchingStrings(stringList, queries):
    counter = [0] * len(queries)
    hashmap = {}
    
    for idx ,query in enumerate(queries):
        if query not in hashmap:
            hashmap[query] = [idx]
        else:
            hashmap[query].append(idx)
    
    for string in stringList:
        idc = hashmap.get(string)
        
        if idc is not None:
            for idx in idc:
                counter[idx] += 1
    
    return counter


if __name__ == '__main__':
    stringList_count = int(input().strip())

    stringList = []

    for _ in range(stringList_count):
        stringList_item = input()
        stringList.append(stringList_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)
    
    res = matchingStrings(stringList, queries)
    ic(res)