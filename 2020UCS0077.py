# 2020UCS0077 ARYAN CS PROJECT-1
# THIS CONTAINS 21 UTILITY FUNCTIONS.
# ALL THE FUNCTIONS ARE USEFUL AND HAVE UTILITY, NONE ARE IRRELEVANT.
# Utility of each function is given above each function as a comment.

print('                    ******************WELCOME******************')
para__ = ''                                                          # This wil obtain user input
temp = input('Enter the text/Paste it here: \n')                     # used to halt the loop once input is entered
while temp:                                                          # Loop will help obtaining multiple line input
    para__ += temp + '\n'
    temp = input()


# #1 line counter
def count_line(para_):
    para_list = para_.split('\n')
    num_lines = len(para_list)
    print('Passed text contains ' + str(num_lines-1) + ' lines')
    return num_lines


# #2 character counter (including spaces, special characters and punctuation)
def count_char(para_):
    num_total_char = len(para_)
    print('Passed text contains a total of ' + str(num_total_char) + ' characters')
    return num_total_char


# #3 Word and space counter ( will count single white space in the entire text)
def count_words(para_):
    num_words = len(para_.split())
    num_spaces = num_words - count_line(para_)
    print('Passed text contains a total of ' + str(num_words) + ' words')
    print('Passed text contains ' + str(num_spaces) + ' spaces')
    return num_words, num_spaces


# #4 Extra WhiteSpace (more than 1 space, will be contracted to single space) Remover
def rem_extra_whitespaces(para_):
    line_split = para_.split('\n')
    new_para = ''
    for i in range(len(line_split)):
        line_word_split = line_split[i].split()
        line_word_rem_space = []
        clear_line = ''
        for j in line_word_split:
            if j[0] != ' ':
                line_word_rem_space.append(j)
        for m in line_word_rem_space:
            clear_line += m + ' '
        if i != len(line_split) - 1:
            new_para += clear_line + '\n'
        else:
            new_para += clear_line
    return new_para


# #5 Capitalizing First Letter Of Each Line
def cap_first_letter_each_line(para_):
    line_split = para_.split('\n')
    new_para = ''
    new_line_lst = []
    for i in range(len(line_split) - 1):
        if 97 <= ord(line_split[i][0]) <= 122:
            new_line_lst.append(chr(ord(line_split[i][0]) - 32) + line_split[i][1:])
        else:
            new_line_lst.append(line_split[i])
    for j in range(len(new_line_lst)):
        if j != len(new_line_lst):
            new_para += new_line_lst[j] + '\n'
        else:
            new_para += new_line_lst[j]
    return new_para


# #6 Capitalizing All Letters In The Text
def all_caps(para_):
    new_para = ''
    line_split = para_.split('\n')
    for i in range(len(line_split)):
        for j in line_split[i]:
            if 97 <= ord(j) <= 122:
                new_para += chr(ord(j)-32)
            else:
                new_para += j
        if i != len(line_split) -1:
            new_para += '\n'
    return new_para


# #7 Lowercase-ing All Letters In The Text
def all_small(para_):
    new_para = ''
    line_split = para_.split('\n')
    for i in range(len(line_split)):
        for j in line_split[i]:
            if 65 <= ord(j) <= 90:
                new_para += chr(ord(j)+32)
            else:
                new_para += j
        if i != len(line_split) - 1:
            new_para += '\n'
    return new_para


# #8 Capitalizing First Letter Of Each Word In The Text
def cap_first_letter_each_word(_para):
    new_para = ''
    line_split = _para.split('\n')
    for i in range(len(line_split)):
        word_split = line_split[i].split()
        for j in range(len(word_split)):
            if 97 <= ord(word_split[j][0]) <= 122:
                new_word = ''
                new_word += chr(ord(word_split[j][0])-32) + word_split[j][1:]
                word_split[j] = new_word
        new_line = ''
        for k in word_split:
            new_line += k + ' '
        if i != len(line_split) - 1:
            new_para += new_line + '\n'
        else:
            new_para += new_line
    return new_para


# #9 Counting how many times a specific word exists in the text
def count_specific_word(para_):
    word_split = para_.split()
    to_find = input('Enter the word you want to find: ')
    count = 0
    for i in word_split:
        if to_find == i:
            count += 1
    print(to_find, 'Occurs', count, 'times in the entire text')


# #10 Finding where (all line numbers in which the given word occurs at least once) In The Text Does The Word Exist
def word_line_locator(para_):
    line_split = para_.split('\n')
    to_find = input('Enter the word you want to find: ')
    word_location = {}
    line_no = []
    for i in range(len(line_split)):
        word_split = line_split[i].split()
        if to_find in word_split:
            line_no.append(i+1)
        word_location[to_find + ' occurs in line no.(s) '] = line_no
    print(word_location)


# #11 Finding and Counting Unique Words
def unique_words(para_):
    word_split = para_.split()
    unique = []
    for i in word_split:
        if i not in unique and i[:-1] not in unique:
            if i[-1] in [',', '.', '!', '?']:
                unique.append(i[:-1])
            else:
                unique.append(i)
    print(unique)
    print(len(unique), 'UNIQUE WORDS FOUND')


# #12 Grammar Correction (Punctuation Formatting) Near Full Stop
def full_stop_correction(para_):
    new_para = ''
    new_para2 = ''
    punc_lst = [',', '!', '?', '(', ')', '\\', '/', '-', '_', '@', '&', '*']
    for i in range(len(para_)):
        if para_[i] == ' ':
            if para_[i+1] != '.':
                new_para += ' '
        if para_[i] == '.':
            if para_[i+1] != ' ':
                new_para += '. '
            else:
                new_para += '.'
        if 65 <= ord(para_[i]) <= 90 or 97 <= ord(para_[i]) <= 122 or para_[i] == '\n' or para_[i] in punc_lst:
            new_para += para_[i]
        if not 65 <= ord(para_[i]) <= 90 and 97 <= ord(para_[i]) <= 122 and para_[i] == '\n':
            new_para += para_[i]

    line_split = new_para.split('\n')
    for i in range(len(line_split)):
        full_stop_split = line_split[i].split('. ')
        rectified_full_stop_list = []
        for j in full_stop_split:
            if j != '' and 97 <= ord(j[0]) <= 122:
                rectified_full_stop_list.append(chr(ord(j[0]) - 32) + j[1:])
            else:
                rectified_full_stop_list.append(j)
        new_line = ''
        for k in rectified_full_stop_list:
            if rectified_full_stop_list.index(k) != len(rectified_full_stop_list) -1 and len(k) > 0:
                new_line += k + '. '
            else:
                new_line += k
        if i != len(line_split) - 1:
            new_para2 += new_line + '\n'
        else:
            new_para2 += new_line
    return new_para2


# #13 Grammar (Punctuation Formatting) Comma Correction
def comma_correction(para_):
    punc_lst = ['.', '!', '?', '(', ')', '\\', '/', '-', '_', '@', '&', '*']
    new_para = ''
    for i in range(len(para_)):
        if para_[i] == ' ':
            if para_[i+1] != ',':
                new_para += ' '
        if para_[i] == ',':
            if para_[i+1] != ' ':
                new_para += ', '
            else:
                new_para += ','
        if 65 <= ord(para_[i]) <= 90 or 97 <= ord(para_[i]) <= 122 or para_[i] == '\n' or para_[i] in punc_lst:
            new_para += para_[i]
        if not 65 <= ord(para_[i]) <= 90 and 97 <= ord(para_[i]) <= 122 and para_[i] == '\n':
            new_para += para_[i]
    return new_para


# #14 Capitalize Selected Word
def cap_sel_word(para_):
    new_para = ''
    to_cap = input('Enter a word as it appears in text that you want to capitalize: \n')
    cap_ver = ''
    for i in range(len(to_cap)):
        if 97 <= ord(to_cap[i]) <= 122:
            cap_ver += chr(ord(to_cap[i]) - 32)
        else:
            cap_ver += to_cap[i]

    line_split = para_.split('\n')
    for i in range(len(line_split)):
        word_split = line_split[i].split()
        for j in range(len(word_split)):
            if word_split[j] == to_cap or word_split[j][:-1] == to_cap or word_split[j][1:] == to_cap:
                word_split[j] = cap_ver
        new_line = ''
        for k in word_split:
            new_line += k + ' '
        if i != len(line_split) - 1:
            new_para += new_line + '\n'
        else:
            new_para += new_line
    return new_para


# #15 Capitalize First Letter Of A Selected Word
def cap_first_sel(para_):
    new_para = ''
    to_cap = input('Enter a word as it appears in text that you want to capitalize: \n')
    cap_ver = ''
    if 97 <= ord(to_cap[0]) <= 122:
        cap_ver += chr(ord(to_cap[0]) - 32) + to_cap[1:]
    else:
        cap_ver += to_cap[0] + to_cap[1:]

    line_split = para_.split('\n')
    for i in range(len(line_split)):
        word_split = line_split[i].split()
        for j in range(len(word_split)):
            if word_split[j][:-1] == to_cap or word_split[j][1:] == to_cap or word_split[j] == to_cap :
                word_split[j] = cap_ver
        new_line = ''
        for k in word_split:
            new_line += k + ' '
        if i != len(line_split):
            new_para += new_line + '\n'
        else:
            new_para += new_line
    return new_para


# #16 Replacing a given word by another given word in the entire text
def replace_word(para_):
    to_replace = input('Which word from the text would you like to replace: ')
    new_word = input('Enter a new word in replacement for ' + to_replace + ': ')
    while to_replace not in para_:
        print(to_replace, 'IS NOT FOUND IN THE PARAGRAPH')
        to_replace = input('Re-enter a word from the text(or press "N" to EXIT): ')
        if to_replace in para_ or to_replace == 'N':
            break

    new_para = ''
    line_split = para_.split('\n')
    for i in range(len(line_split)):
        word_split = line_split[i].split()
        for j in range(len(word_split)):
            if word_split[j] == to_replace or word_split[j][:-1] == to_replace or word_split[j][1:] == to_replace:
                word_split[j] = new_word
        new_line = ''
        for k in word_split:
            new_line += k + ' '
        if i != len(line_split) - 1:
            new_para += new_line + '\n'
        else:
            new_para += new_line
    return new_para


# #17 Removing all the punctuation marks
def rem_punc(para_):
    new_para = ''
    for i in para_:
        if 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122 or i == '\n' or i == ' ':
            new_para += i
    return new_para


# #18 Adding Ordered Numbering in front of each line, to represent individual one line sentences or a list of items
# Works Flawless with single line sentences in each line and is not meant to be used in
def numbered_list(para_):
    cap_first_letter_each_line(para_[:-1])
    line_split = para_.split('\n')
    for i in range(len(line_split)):
        if i < len(line_split) -1:
            new_line = ''
            new_line += str(i+1) + '.) ' + line_split[i] + '.'
            print(new_line)


# #19 Finding Palindrome from the entire text
def palindrome(para_):
    word_split = para_.split()
    count = []
    for i in word_split:
        if len(i) > 1:
            if i == i[::-1]:
                count.append(i)
    if len(count) != 0:
        print(count)
    else:
        print('NO Palindrome found! ')


# #20 Counting number of sentences (Incomplete sentences are those without full-stops)
def count_sent(para_):
    count = 0
    for i in range(len(para_)):
        if para_[i] == '.':
            if para_[i+1] == ' ' or 65 <= ord(para_[i+1]) <= 90 or 97 <= ord(para_[i+1]) <= 122:
                count += 1
    if count != 0:
        print('This text contains,', count, 'sentences')
    if count == 0:
        print('This text ONE incomplete sentence')


# #21 Check if a word is present, will return 'Yes' if present and 'NO' otherwise
def check_word(para_):
    to_find = input('Type the word to see if it is present in the text: ')
    word_split = para_.split()
    count = 0
    for i in word_split:
        if to_find == i or to_find == i[:-1]:
            count = 1
            break
    if count == 1:
        print('Yes, Its present.')
    else:
        print('NO, Its NOT present.')


feature = ['Count number of lines', 'Count number of characters', 'Count number of words & spaces',
           'Extra white space removal', 'Capitalizing first letter of each line', 'Capitalizing entire text',
           'Lower-casing entire text', 'Capitalize first letter of each word', 'Count a specific word',
           'Locate a word by line number', 'Find unique words from the entire text', 'Full stop Correction',
           'Comma correction', 'Capitalize a selected word in entire text',
           'Capitalize first letter of a selected word in entire text', 'Replace a word from entire text',
           'Remove punctuations', 'Create a numbered list of one line sentences per line eg. Grocery list',
           'Find Palindromes from the entire text', 'Count the number of sentences', 'Check if a word is in the text']

for i in range(len(feature)):
    print(str(i+1)+'.) ' + feature[i])

res = 'y'
updated_para = para__
while res == 'y':
    feat = int(input('ENTER FEATURE NUMBER: '))
    print()
    if feat == 1:
        count_line(updated_para)
        print()
        x = input('Press "y" to make more changes OR Press any other key to Exit: ')
        if x == 'y':
            res = 'y'
        else:
            break
    if feat == 2:
        count_char(updated_para)
        print()
        x = input('PRESS "y" TO MAKE MORE CHANGES OR press any key to exit: ')
        if x == 'y':
            res = 'y'
        else:
            break
    if feat == 3:
        count_words(updated_para)
        print()
        x = input('PRESS "y" TO MAKE MORE CHANGES OR press any key to exit: ')
        if x == 'y':
            res = 'y'
        else:
            break
    if feat == 4:
        updated_para = rem_extra_whitespaces(updated_para)
        print(updated_para)
        print()
        x = input('PRESS "y" TO MAKE MORE CHANGES OR press any key to exit: ')
        if x == 'y':
            res = 'y'
        else:
            break
    if feat == 5:
        updated_para = cap_first_letter_each_line(updated_para)
        print(updated_para)
        print()
        x = input('PRESS "y" TO MAKE MORE CHANGES OR press any key to exit: ')
        if x == 'y':
            res = 'y'
        else:
            break
    if feat == 6:
        updated_para = all_caps(updated_para)
        print(updated_para)
        print()
        x = input('PRESS "y" TO MAKE MORE CHANGES OR press any key to exit: ')
        if x == 'y':
            res = 'y'
        else:
            break
    if feat == 7:
        updated_para = all_small(updated_para)
        print(updated_para)
        print()
        x = input('PRESS "y" TO MAKE MORE CHANGES OR press any key to exit: ')
        if x == 'y':
            res = 'y'
        else:
            break
    if feat == 8:
        updated_para = cap_first_letter_each_word(updated_para)
        print(updated_para)
        print()
        x = input('PRESS "y" TO MAKE MORE CHANGES OR press any key to exit: ')
        if x == 'y':
            res = 'y'
        else:
            break
    if feat == 9:
        count_specific_word(updated_para)
        print()
        x = input('PRESS "y" TO MAKE MORE CHANGES OR press any key to exit: ')
        if x == 'y':
            res = 'y'
        else:
            break
    if feat == 10:
        word_line_locator(updated_para)
        print()
        x = input('PRESS "y" TO MAKE MORE CHANGES OR press any key to exit: ')
        if x == 'y':
            res = 'y'
        else:
            break
    if feat == 11:
        unique_words(updated_para)
        print()
        x = input('PRESS "y" TO MAKE MORE CHANGES OR press any key to exit: ')
        if x == 'y':
            res = 'y'
        else:
            break
    if feat == 12:
        updated_para = full_stop_correction(updated_para)
        print(updated_para)
        print()
        x = input('PRESS "y" TO MAKE MORE CHANGES OR press any key to exit: ')
        if x == 'y':
            res = 'y'
        else:
            break
    if feat == 13:
        updated_para = comma_correction(updated_para)
        print(updated_para)
        print()
        x = input('PRESS "y" TO MAKE MORE CHANGES OR press any key to exit: ')
        if x == 'y':
            res = 'y'
        else:
            break
    if feat == 14:
        updated_para = cap_sel_word(updated_para)
        print(updated_para)
        print()
        x = input('PRESS "y" TO MAKE MORE CHANGES OR press any key to exit: ')
        if x == 'y':
            res = 'y'
        else:
            break
    if feat == 15:
        updated_para = cap_first_sel(updated_para)
        print(updated_para)
        print()
        x = input('PRESS "y" TO MAKE MORE CHANGES OR press any key to exit: ')
        if x == 'y':
            res = 'y'
        else:
            break
    if feat == 16:
        updated_para = replace_word(updated_para)
        print(updated_para)
        print()
        x = input('PRESS "y" TO MAKE MORE CHANGES OR press any key to exit: ')
        if x == 'y':
            res = 'y'
        else:
            break
    if feat == 17:
        updated_para = rem_punc(updated_para)
        print(updated_para)
        print()
        x = input('PRESS "y" TO MAKE MORE CHANGES OR press any key to exit: ')
        if x == 'y':
            res = 'y'
        else:
            break
    if feat == 18:
        numbered_list(updated_para)
        print()
        print('''        Any changes you make after this they
        will NOT BE made into the numbered list
        instead they'll be made in the previously obtained
        text (paragraph NOT numbered list).''')
        print()
        print()
        x = input('PRESS "y" TO MAKE MORE CHANGES OR press any key to exit: ')
        if x == 'y':
            res = 'y'
        else:
            break
    if feat == 19:
        palindrome(updated_para)
        print()
        x = input('PRESS "y" TO MAKE MORE CHANGES OR press any key to exit: ')
        if x == 'y':
            res = 'y'
        else:
            break
    if feat == 20:
        count_sent(updated_para)
        print()
        x = input('PRESS "y" TO MAKE MORE CHANGES OR press any key to exit: ')
        if x == 'y':
            res = 'y'
        else:
            break
    if feat == 21:
        check_word(updated_para)
        print()
        x = input('PRESS "y" TO MAKE MORE CHANGES OR press any key to exit: ')
        if x == 'y':
            res = 'y'
        else:
            break
print()
print(' After all the changes the final text is: ')
print()
print(updated_para)
