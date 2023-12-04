digits = list(map(str, list(range(10))))
gear_ratios = []

def get_part_numbers(line, gear_index):
    part_numbers = []
    adjacent_indexes = [gear_index - 1, gear_index, gear_index + 1]

    for i, char in enumerate(line):
        if char not in digits:
            continue
        # Continue if not the first digit in number
        elif i > 0 and line[i - 1] in digits:
            continue
        elif char in digits:
            current_number = [char]
            current_number_length = 1
            current_number_indexes = [i]
            forward_i = i + 1
            next_char = line[forward_i]
            while next_char in digits:
                current_number.append(next_char)
                current_number_indexes.append(forward_i)
                current_number_length += 1
                forward_i += 1
                try:
                    next_char = line[forward_i]
                except IndexError:
                    break
            current_number_joined = "".join(current_number)

            for index in current_number_indexes:
                if index in adjacent_indexes:
                    part_numbers.append(int(current_number_joined))
                    break

    return part_numbers

with open("input.txt", encoding="utf-8") as schematic:
    lines = schematic.readlines()
    for i, line in enumerate(lines):
        lines[i] = lines[i].strip()

    for line_i, line in enumerate(lines):
        current_line = lines[line_i]
        if line_i == 0:
            previous_line = "".join(["."]*len(current_line))
        else:
            previous_line = lines[line_i - 1]
        if line_i == len(lines) - 1:
            next_line = "".join(["."]*len(current_line))
        else:
            next_line = lines [line_i + 1]

        for char_i, char in enumerate(current_line):
            if char != "*":
                continue

            part_numbers = []
            part_numbers.append(get_part_numbers(previous_line, char_i))
            part_numbers.append(get_part_numbers(current_line, char_i))
            part_numbers.append(get_part_numbers(next_line, char_i))
            
            part_numbers_flattened = []
            for part_list in part_numbers:
                for part in part_list:
                    part_numbers_flattened.append(part)

            if len(part_numbers_flattened) == 2:
                gear_ratio = part_numbers_flattened[0] * part_numbers_flattened[1]
                gear_ratios.append(gear_ratio)

answer = sum(gear_ratios)
print(answer)

