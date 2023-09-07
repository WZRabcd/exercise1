def count_and_replace_words():
    count = 0
    with open('file_to_read.txt', 'r') as file:
        text = file.read()
        count = text.count('terrible')

        replaced_text = text.split()
        for i in range(len(replaced_text)):
            if replaced_text[i] == 'terrible':
                if (i + 1) % 2 == 0:
                    replaced_text[i] = 'pathetic'
                else:
                    replaced_text[i] = 'marvellous'

    with open('result.txt', 'w') as file:
        file.write(' '.join(replaced_text))

    return count


word_count = count_and_replace_words()
print(f"Total occurrences of the word 'terrible': {word_count}")