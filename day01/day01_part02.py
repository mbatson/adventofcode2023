digits = list(map(str, list(range(10))))
digit_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
calibration_values = []

def word_to_digit(word):
    for i, digit_word in enumerate(digit_words, start=1):
        if word == digit_word:
            return str(i)

with open("input.txt", encoding="utf-8") as values:
    for value in values:
        digits_found = []

        for i, char in enumerate(value):
            if char in digits:
                digits_found.append(char)
            else:
                if i < (len(value) - 5):
                    if (next_5_chars := value[i:(i + 5)]) in digit_words:
                        digits_found.append(next_5_chars)
                    elif (next_4_chars := value[i:(i + 4)]) in digit_words:
                        digits_found.append(next_4_chars)
                    elif (next_3_chars := value[i:(i + 3)]) in digit_words:
                        digits_found.append(next_3_chars)
                elif i < (len(value) - 4):
                    if (next_4_chars := value[i:(i + 4)]) in digit_words:
                        digits_found.append(next_4_chars)
                    elif (next_3_chars := value[i:(i + 3)]) in digit_words:
                        digits_found.append(next_3_chars)
                elif i < (len(value) - 3):
                    if (next_3_chars := value[i:(i + 3)]) in digit_words:
                        digits_found.append(next_3_chars)

        for i, digit_found in enumerate(digits_found):
            if digit_found in digit_words:
                digits_found[i] = word_to_digit(digit_found)

        first_last_digits = [digits_found[0], digits_found[-1]]
        calibration_value = "".join(first_last_digits)
        calibration_values.append(int(calibration_value))

answer = sum(calibration_values)
print(answer)
