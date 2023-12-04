won_points = 0

def remove_empty_elements(l):
    for i, element in enumerate(l):
        if len(element) == 0:
            l.pop(i)
    return l
            
with open("input.txt", encoding="utf-8") as cards:
    for card in cards:
        numbers = card.split(": ")[1].strip()

        winning_numbers = numbers.split(" | ")[0]
        winning_numbers = winning_numbers.split(" ")
        winning_numbers = remove_empty_elements(winning_numbers)

        your_numbers = numbers.split(" | ")[1]
        your_numbers = your_numbers.split(" ")
        your_numbers = remove_empty_elements(your_numbers)

        matching_numbers = []
        for your_number in your_numbers:
            if your_number in winning_numbers:
                matching_numbers.append(your_number)

        points = 0
        for matching_number in matching_numbers:
            if points == 0:
                points = 1
            else:
                points *= 2

        won_points += points

print(won_points)
