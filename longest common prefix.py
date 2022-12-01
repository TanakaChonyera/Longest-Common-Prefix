def list_traversal(strs, icp, letter, letter_index, letter_counter):
    word_iterator = 1
    while word_iterator <= len(strs) - 1:
        if letter_index > len(strs[word_iterator]) - 1:
            return icp
        elif letter != strs[word_iterator][letter_index]:
            return icp
        else:
            letter_counter += 1
        word_iterator += 1
    return letter_counter


def longest_common_prefix(strs):

    icp = ''
    letter_index = 0

    for letter in strs[0]:

        letter_counter = 0
        letter_counter = list_traversal(strs, icp, letter, letter_index, letter_counter)

        if letter_counter == len(strs) - 1:
            icp += letter
        letter_index += 1

    return icp

strs = ["cir", "car"]
print(longest_common_prefix(strs))




