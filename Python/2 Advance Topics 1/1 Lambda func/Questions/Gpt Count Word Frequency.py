from functools import reduce

def apply_conditions(occurrences: list[tuple]) -> list[tuple]:
    # Filter words whose occurrences are more than 1
    occurrences = filter(lambda tup: tup[1] > 1, occurrences)
    
    # Sort by frequency (descending) and then alphabetically (ascending)
    occurrences = sorted(occurrences, key=lambda tup: (-tup[1], tup[0]))
    
    return occurrences

def main() -> None:
    # The given list
    parts_sentence: list[str] = ["apple banana apple", "banana orange apple", "orange banana", "kiwi banana banana"]
    
    # The sum of all elements in the given list
    sentence: str = reduce(lambda part1_sentence, part2_sentence: part1_sentence + " " + part2_sentence, parts_sentence)
    
    # Unique words in the list
    words: list[str] = list(set(sentence.split(" ")))
    
    # Store the occurrences of a word in (word, occurrence) tuple
    occurrences: list[tuple] = [(word, sentence.count(word)) for word in words]
    
    # Apply conditions to filter and sort
    occurrences = apply_conditions(occurrences)
    
    print(occurrences)

if __name__ == "__main__":
    main()