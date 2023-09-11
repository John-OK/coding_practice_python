import string
def digital_cipher(message, key):
    encoded_message = [] # result that will be returned
    alphabet = string.ascii_lowercase # the alphabet (lowercase) as a string 
    letter_dict = {letter: index for index, letter in enumerate(alphabet, 1)} # map a unique number to each letter in order starting at 1
    key = str(key) # make key a string so each "digit" (now, a character) can be itertated over

    for index, letter in enumerate(message):
        letter_value = letter_dict[letter]
        encode_value = int(key[index % len(key)]) # get encoding value and turn it back to an integer
        encoded_message.append(letter_value + encode_value)
    return encoded_message

result = digital_cipher("masterpiece", 1939)
correct_answer = [14, 10, 22, 29, 6, 27, 19, 18, 6, 12, 8]
print(str(result) + ": calculated encoding")
print(str(correct_answer) + ": correct encoding")
print("\nResult is correct?")
print(result == correct_answer)