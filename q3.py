def wordCount(file_path):
    word_dict = {}

    with open('q3.txt', 'r') as file:
        for line_number, line in enumerate(file, start=1):
            words = line.strip().split()
            for word in words:
                word = word.lower()  # Converting to lowercase to treat case-insensitive words
                if word not in word_dict:
                    word_dict[word] = [line_number]
                else:
                    word_dict[word].append(line_number)

    return word_dict

file_path = 'q3.txt'
result = wordCount(file_path)

# Printing  the result
for word, line_numbers in result.items():
    print(f"{word}: {line_numbers}", end=" ")
