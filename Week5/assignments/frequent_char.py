def most_frequent_character(word_list):
    counter = {}
    for word in word_list:
        for char in word:
            counter[char] = counter.get(char, 0) + 1
    
    most_frequent = None
    frequent_count = 0
    for char, count in counter.items():
        if most_frequent is None or count > frequent_count:
            most_frequent = char
            frequent_count = count
    
    print(most_frequent)
    
word_list = input().split()
most_frequent_character(word_list)