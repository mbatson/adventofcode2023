digits = list(map(str, list(range(10))))
calibration_values = []

with open("input.txt", encoding="utf-8") as values:
    for value in values:
        digits_found = []
        for char in value:
            if char in digits:
                digits_found.append(char)
        first_last_digits = [digits_found[0], digits_found[-1]]
        calibration_value = "".join(first_last_digits)
        calibration_values.append(int(calibration_value))

answer = sum(calibration_values)
print(answer)
