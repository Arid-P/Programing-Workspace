from collections import Counter as cnt

def main () -> None :
    #raise ValueError('main not implemented')

    nums = [1, 1, 1, 2, 2, 3]
    n=2
    count_nums = cnt(nums)

    count_nums = dict(sorted(count_nums.items(), key = lambda k_v: -k_v[1] ))

    count_nums_keys = list(count_nums.keys())
    answer = [count_nums_keys[i] for i in range(n)]

    print(f"{answer=}")

    return

if __name__ == "__main__" :
    main()