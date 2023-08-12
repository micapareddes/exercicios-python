def is_it_a_palindrome(word):
    ind = len(word) - 1
    reversed_word = []
    word_list =[]
    ind_word = 0

    while ind_word < len(word):
        word_list.append(word[ind_word])
        ind_word += 1

    while ind >= 0:
        letter = word[ind]
        reversed_word.append(letter)
        ind -= 1
    return reversed_word == word_list

palavra = 'sol'
print(is_it_a_palindrome(palavra))

'''''
chatGPT

def is_it_a_palindrome(word):
    word_len = len(word)
    ind = 0

    while ind < word_len // 2:  # We only need to check the first half of the word
        # Compare the current character with the corresponding character from the end
        if word[ind] != word[word_len - ind - 1]:
            return False
        ind += 1

    return True  # All characters matched, the word is a palindrome

palavra = 'mim'
print(is_it_a_palindrome(palavra))

'''