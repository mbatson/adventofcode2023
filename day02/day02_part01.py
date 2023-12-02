max_red_cubes = 12
max_green_cubes = 13
max_blue_cubes = 14
possible_game_ids = []

def check_game_results(game_results):
    for result in game_results.split("; "):
        for sub_result in result.split(", "):
            cube_count = sub_result.split(" ")[0]
            cube_colour = sub_result.split(" ")[1]
            if cube_colour == "red" and int(cube_count) > max_red_cubes:
                return False
            elif cube_colour == "green" and int(cube_count) > max_green_cubes:
                return False
            elif cube_colour == "blue" and int(cube_count) > max_blue_cubes:
                return False
    return True

with open("input.txt", encoding="utf-8") as games:
    for game in games:
        game_id = game.split(":")[0]
        game_id = game_id.split(" ")[1]

        game_results = game.split(":")[1].strip()
        if check_game_results(game_results):
            possible_game_ids.append(int(game_id))

answer = sum(possible_game_ids)
print(answer)
