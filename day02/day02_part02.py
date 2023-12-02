powers_of_min_cubes = []

def check_game_results(game_results):
    min_red_cubes = 1
    min_green_cubes = 1
    min_blue_cubes = 1

    for result in game_results.split("; "):
        for sub_result in result.split(", "):
            cube_count = int(sub_result.split(" ")[0])
            cube_colour = sub_result.split(" ")[1]
            if cube_colour == "red" and cube_count > min_red_cubes:
                min_red_cubes = cube_count
            elif cube_colour == "green" and cube_count > min_green_cubes:
                min_green_cubes = cube_count
            elif cube_colour == "blue" and cube_count > min_blue_cubes:
                min_blue_cubes = cube_count

    return min_red_cubes, min_green_cubes, min_blue_cubes

with open("input.txt", encoding="utf-8") as games:
    for game in games:
        game_id = game.split(":")[0]
        game_id = game_id.split(" ")[1]

        game_results = game.split(":")[1].strip()
        min_red_cubes, min_green_cubes, min_blue_cubes = check_game_results(game_results)
        power_of_min_cubes = min_red_cubes * min_green_cubes * min_blue_cubes
        powers_of_min_cubes.append(power_of_min_cubes)
        

answer = sum(powers_of_min_cubes)
print(answer)
