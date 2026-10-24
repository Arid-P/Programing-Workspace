# ==============================================
# 🔵 ITERATORS & GENERATORS IN PYTHON (Notes)
# ==============================================

# -------------------------
# 🔹 What is an Iterator?
# -------------------------
# An iterator is an object that implements the __iter__() and __next__() methods.
# You can use it in a for-loop to get one value at a time.
# When there are no more values, it raises StopIteration.

class ReverseIterator:
    """
    A class-based iterator that counts backward from a given number down to 1.
    """
    def __init__(self, start: int) -> None:
        self.current = start

    def __iter__(self) -> 'ReverseIterator':
        # This method is called once at the start of iteration.
        return self

    def __next__(self) -> int:
        # This method is called repeatedly during iteration.
        # It must return the next item and raise StopIteration when done.
        if self.current >= 1:
            value = self.current
            self.current -= 1
            return value
        else:
            raise StopIteration

def run_iterator_example() -> None:
    it = ReverseIterator(5)
    for x in it:
        print(x)

# -------------------------
# 🔹 What is a Generator?
# -------------------------
# A generator is a special type of iterator that you write as a function using `yield`.
# Python automatically handles __iter__() and __next__() for you.

q

def reverse_generator(start: int) -> Generator[int, None, None]:
    """
    A generator function that yields numbers from 'start' down to 1.
    """
    while start >= 1:
        yield start  # Pauses and sends back value
        start -= 1   # Resumes from here on next call

def run_generator_example() -> None:
    for x in reverse_generator(5):
        print(x)

# -------------------------
# 🔸 Key Differences
# -------------------------
# ✅ Generators are simpler and require less code than iterators.
# ✅ Iterators are more flexible when you need to maintain complex state.

# -------------------------
# 🔸 Internal Working of for-loop
# -------------------------
# for x in iterable:
#     → Calls iter(iterable)  → __iter__()
#     → Repeatedly calls next(iterator)  → __next__()

# -------------------------
# 🔸 Summary
# -------------------------
# Iterator: Class with __iter__() and __next__()
# Generator: Function using yield (auto handles iteration)

# -------------------------
# 🔹 Run the examples
# -------------------------
if __name__ == "__main__":
    print("Iterator Output:")
    run_iterator_example()
    
    print("\nGenerator Output:")
    run_generator_example()