# https://adventofcode.com/2023/day/2



# def day_2():
#     total = 0
#     possible_game = {
#         "red" : 12,
#         "green" : 13,
#         "blue" : 14
#     }
#     for line in open("day_2/data.txt", "r"):
#         line = line.split(": ")
#         game_id = line[0].split(" ")
#         game_id = game_id[1]
#         line = line[1].split("; ")
#         add = True
#         for set in line:
#             games_dict = {}

#             sub_set = set.split(", ")
#             for color in sub_set:
#                 sub_color = color.split()
#                 if sub_color[1] in possible_game:
#                     games_dict[sub_color[1]] = int(sub_color[0]) + games_dict.get(sub_color[1], 0)

#             for game in possible_game:
#                 if games_dict.get(game,0) > possible_game[game]:
#                     add = False
#         if add:
#             total += int(game_id)

    

#     return total


# print(day_2())


def day_2():
    total = 0
    possible_game = {"red","green","blue"}
    for line in open("day_2/data.txt", "r"):
        line = line.split(": ")
        line = line[1].split("; ")
        games_dict = {}
        for set in line:
            sub_set = set.split(", ")
            for color in sub_set:
                sub_color = color.split()
                if sub_color[1] in possible_game:
                    games_dict[sub_color[1]] = max(int(sub_color[0]), games_dict.get(sub_color[1], 0))
        sub_total = 1
        for val in games_dict.values():
            sub_total *= val
        total += sub_total

    return total


print(day_2())
