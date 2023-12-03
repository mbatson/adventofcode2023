digits = list(map(str, list(range(10))))
part_numbers = []

with open("input.txt", encoding="utf-8") as schematic:
    lines = schematic.readlines()
    for i, line in enumerate(lines):
        lines[i] = lines[i].strip()

    for i, line in enumerate(lines):
        if i == 0:
            previous_line = "".join(["."]*10)
        else:
            previous_line = lines[i - 1]
        current_line = lines[i]
        if i == len(lines) - 1:
            next_line = "".join(["."]*10)
        else:
            next_line = lines [i + 1]

        for i, char in enumerate(current_line):
            if char not in digits:
                continue
            # Continue if not the first digit in number
            elif i > 0 and current_line[i - 1] in digits:
                continue
            elif char in digits:
                current_number = [char]
                current_number_length = 1
                forward_i = i + 1
                next_char = current_line[forward_i]
                while next_char in digits:
                    current_number.append(next_char)
                    current_number_length += 1
                    forward_i += 1
                    try:
                        next_char = current_line[forward_i]
                    except IndexError:
                        next_char = "."
                current_number_joined = "".join(current_number)

                adjacent_chars = []
                forward_i = i
                while forward_i < i + current_number_length:
                    adjacent_chars.append(previous_line[forward_i])
                    adjacent_chars.append(next_line[forward_i])
                    forward_i += 1
                if i != 0:
                    adjacent_chars.append(previous_line[i - 1])
                    adjacent_chars.append(current_line[i - 1])
                    adjacent_chars.append(next_line[i - 1])
                if i + current_number_length != len(current_line):
                    adjacent_chars.append(previous_line[i + current_number_length])
                    adjacent_chars.append(current_line[i + current_number_length])
                    adjacent_chars.append(next_line[i + current_number_length])

                for char in adjacent_chars:
                    if char != "." and char not in digits:
                        part_numbers.append(int(current_number_joined))
                        break

answer = sum(part_numbers)
print(answer)
