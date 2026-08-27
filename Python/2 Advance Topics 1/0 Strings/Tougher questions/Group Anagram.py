from collections import defaultdict
import time  # Import the time module

class gpt:
    @staticmethod
    def main(words: list[str]) -> None:
        # Dictionary to store groups of anagrams, key is the sorted word
        anagram_groups = defaultdict(list)
        
        for word in words:
            # Sort the word to get the key
            sorted_word = ''.join(sorted(word))
            
            # Append the word to the list corresponding to the sorted word
            anagram_groups[sorted_word].append(word)
        
        # Convert dictionary values (lists of anagrams) to a sorted list of lists
        all_anagrams = list(anagram_groups.values())
        
        # Sort by the length of anagram groups, largest group first
        all_anagrams = sorted(all_anagrams, key=lambda group: -len(group))
        
        

class mine:
    @staticmethod
    def is_anagram(word1: str, word2: str) -> bool:
        # Check if both words have the same characters in any order
        if len(word1) != len(word2):
            return False
        for chr_ in word1:
            if word1.count(chr_) != word2.count(chr_):
                return False
        return True

    def main(self, words: list[str]) -> None:
        all_anagrams = []
        
        for word in words :
            checked_anagrams: list[str] = []
            
            for check_word in words :
                if self.is_anagram(word, check_word) :
                    checked_anagrams.append(check_word)
            
            for checked_word in checked_anagrams :
                words.remove(checked_word)
            
            all_anagrams.append(checked_anagrams)
        
        all_anagrams = list( sorted(all_anagrams, key=lambda anagrams: -len(anagrams) ))
        
        if words :
            for word in words :
                all_anagrams.append([word])
        
        # Sort by the length of anagram groups (largest first)
        all_anagrams = sorted(all_anagrams, key=lambda anagrams: -len(anagrams))
        
        

def calculate_time(func, words: list[str]) -> float:  # Function to calculate time taken by another function
    start_time = time.time()  # Start time
    func(words)  # Call the function with words list
    end_time = time.time()  # End time
    return end_time - start_time  # Return the time taken

if __name__ == "__main__":
    words_list = [
    "eat", "tea", "ate", "tan", "nat", "bat", "tab", "pat", "tap", "pan", 
    "nap", "rat", "tar", "art", "bar", "bra", "ear", "rae", "silent", 
    "listen", "enlist", "tinsel", "slinte", "evil", "vile", "veil", "live", 
    "save", "vase", "seva", "seav", "lives", "elves", "rescue", "secure", 
    "recuse", "stare", "rates", "tears", "aster", "ears", "raze", "bare", 
    "beer", "race", "care", "acer", "cafe", "face", "faced", "scare", "cries", 
    "sire", "rise", "ires", "ices", "fair", "fiar", "arif", "fir", "fri", "rif", 
    "least", "stale", "teals", "slate", "tales", "steal", "vials", "basil", 
    "sail", "ails", "lisa", "salt", "last", "tals", "lats", "alts", "stal", 
    "gains", "sign", "sing", "gin", "grins", "ring", "grin", "grange", "bored", 
    "robed", "adore", "doer", "redo", "roar", "air", "ear", "era", "reap", 
    "pare", "pear", "rape", "rape", "teas", "seat", "stare", "rates", "steer", 
    "reset", "tense", "sent", "nest", "tone", "note", "tone", "cone", "once", 
    "lions", "noils", "loins", "snail", "slain", "flames", "femals", "amles", 
    "bakes", "beaks", "skate", "steak", "takes", "vates", "vates", "saves", 
    "saves", "salve", "vials", "sail", "ails", "lisa", "sang", "gnas", "angs", 
    "stag", "gats", "taps", "pat", "tap", "gaps", "pats", "spat", "spat", "rains", 
    "nails", "sail", "airs", "rains", "scare", "grapes", "grape", "gapes", 
    "sew", "wes", "ews", "sew", "beta", "teab", "bate", "beat", "mate", "team", 
    "seam", "same", "moat", "atom", "moat", "math", "tham", "hat", "chat", 
    "that", "whats", "stat", "tats", "cats", "act", "cat", "tac", "cat", 
    "rat", "tar", "art", "lase", "sale", "seal", "seals", "seal", "case", 
    "aces", "east", "seat", "etas", "bats", "stab", "tabs", "bats", "tsar", 
    "arts", "stars", "sart", "raster", "stare", "stear", "sear", "tear", 
    "lair", "liar", "rail", "grape", "graps", "gasp", "pats", "spat", "pas", 
    "pat", "pass", "salt", "slat", "last", "atlas", "riles", "lisle", "leis", 
    "leis", "lien", "sile", "lip", "pip", "liar", "trial", "tail", "tale", 
    "tales", "teal", "lead", "lade", "dale", "deal", "ladle", "lase", "ale", 
    "bake", "beak", "sane", "seen", "neat", "neat", "stane", "notes", "stone"
]

    # Calculate time taken by both functions and print them
    mine_time = calculate_time(mine().main, words_list)
    print(f"Time taken by mine approach: {mine_time:.6f} seconds")
    
    gpt_time = calculate_time(gpt.main, words_list)
    print(f"Time taken by gpt approach: {gpt_time:.6f} seconds")
    
    
