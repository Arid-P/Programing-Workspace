from set_one_solution import Solution

sol = Solution()
passed = 0
failed = 0

def check(problem, func, got, expected, input_desc):
    global passed, failed
    if got == expected:
        print(f"✅ {problem} — PASSED")
        passed += 1
    else:
        print(f"❌ {problem} — FAILED")
        print(f"   Input:    {input_desc}")
        print(f"   Got:      {got}")
        print(f"   Expected: {expected}")
        failed += 1

# ─────────────────────────────────────────
# P1 — find_second_largest
# ─────────────────────────────────────────
check("P1 basic",          sol.find_second_largest, sol.find_second_largest([3,7,1,9,4]),     7,    "[3,7,1,9,4]")
check("P1 duplicates",     sol.find_second_largest, sol.find_second_largest([5,5,5]),         5,    "[5,5,5]")
check("P1 two elements",   sol.find_second_largest, sol.find_second_largest([10, 3]),         3,    "[10,3]")
check("P1 negatives",      sol.find_second_largest, sol.find_second_largest([-1,-5,-2,-3]),   -2,   "[-1,-5,-2,-3]")

# ─────────────────────────────────────────
# P2 — is_palindrome
# ─────────────────────────────────────────
check("P2 true odd",       sol.is_palindrome, sol.is_palindrome([1,2,3,2,1]),   True,  "[1,2,3,2,1]")
check("P2 true even",      sol.is_palindrome, sol.is_palindrome([1,2,2,1]),     True,  "[1,2,2,1]")
check("P2 false",          sol.is_palindrome, sol.is_palindrome([1,2,3,4,5]),   False, "[1,2,3,4,5]")
check("P2 single",         sol.is_palindrome, sol.is_palindrome([42]),          True,  "[42]")

# ─────────────────────────────────────────
# P3 — rotate_right
# ─────────────────────────────────────────
check("P3 basic",          sol.rotate_right, sol.rotate_right([1,2,3,4,5], 2),       [4,5,1,2,3],  "[1,2,3,4,5], k=2")
check("P3 k > len",        sol.rotate_right, sol.rotate_right([1,2,3,4,5], 7),       [4,5,1,2,3],  "[1,2,3,4,5], k=7")
check("P3 k = 0",          sol.rotate_right, sol.rotate_right([1,2,3,4,5], 0),       [1,2,3,4,5],  "[1,2,3,4,5], k=0")
check("P3 k = len",        sol.rotate_right, sol.rotate_right([1,2,3,4,5], 5),       [1,2,3,4,5],  "[1,2,3,4,5], k=5")
check("P3 single",         sol.rotate_right, sol.rotate_right([1], 3),               [1],          "[1], k=3")

# ─────────────────────────────────────────
# P4 — pair_sum (unordered, (a,b) == (b,a))
# normalise each pair to (min, max) before comparing
# ─────────────────────────────────────────
def norm(pairs):
    return sorted([tuple(sorted(p)) for p in pairs])

r4a = norm(sol.pair_sum([1,2,3,4,5], 5))
check("P4 basic",          sol.pair_sum, r4a,  norm([(1,4),(2,3)]),           "[1,2,3,4,5], target=5")

r4b = norm(sol.pair_sum([1,1,2,3], 4))
check("P4 with dupe vals", sol.pair_sum, r4b,  norm([(1,3)]),                 "[1,1,2,3], target=4")

r4c = norm(sol.pair_sum([1,2,3], 10))
check("P4 no pairs",       sol.pair_sum, r4c,  [],                            "[1,2,3], target=10")

r4d = norm(sol.pair_sum([-1,1,0,2], 1))
check("P4 negatives",      sol.pair_sum, r4d,  norm([(-1,2),(0,1)]),          "[-1,1,0,2], target=1")

# ─────────────────────────────────────────
# P5 — two_sum (return indices)
# ─────────────────────────────────────────
check("P5 basic",          sol.two_sum, sorted(sol.two_sum([2,7,11,15], 9)),   [0,1],  "[2,7,11,15], target=9")
check("P5 not first pair", sol.two_sum, sorted(sol.two_sum([3,2,4], 6)),       [1,2],  "[3,2,4], target=6")
check("P5 negatives",      sol.two_sum, sorted(sol.two_sum([-3,4,3,90], 0)),   [0,2],  "[-3,4,3,90], target=0")
check("P5 same index?",    sol.two_sum, sorted(sol.two_sum([3,3], 6)),         [0,1],  "[3,3], target=6")

# ─────────────────────────────────────────
print(f"\n{'─'*40}")
print(f"  {passed} passed | {failed} failed out of {passed+failed} tests")
print(f"{'─'*40}")
