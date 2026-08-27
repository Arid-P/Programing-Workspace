def main() -> None:
    para: str = "apple banana apple orange banana apple grape orange orange"

    words: list = para.split(' ')

    uniq_words = {}
    for word in words:
        if word not in uniq_words:
            occurrence = para.count(word)
            uniq_words[word] = occurrence
        else:
            continue
    
    # Sort by occurrences (values) in descending order and create a new dictionary
    uniq_words = {key: val for key, val in sorted(uniq_words.items(), key=lambda item: item[1], reverse=True)}

    print(f"{uniq_words}")

if __name__ == "__main__":
    main()