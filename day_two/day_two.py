# # List out scores for 1 & 2
# part_1 = ["BX", "CY", "AZ", "AX", "BY", "CZ", "CX", "AY", "BZ"]
# part_2 = ["BX", "CX", "AX", "AY", "BY", "CY", "CZ", "AZ", "BZ"]
#
# # primary function for scoring
# def score(input_day_two):
#     with open("day_2_inputs") as input:
#         return sum(map(lambda pair: input_day_two.index(pair) + 1, map(lambda line: ''.join(line.strip().split()), input.readlines())))
#
# print(score(part_1))
# print(score(part_2))

# Here's what the above python is doing:
# 1. Open the file
# 2. Read all the lines
# 3. Strip the lines of whitespace
# 4. Split the lines into words
# 5. Join the words back together
# 6. Find the index of the word in the input list
# 7. Add 1 to the index
# 8. Sum all the indices

#13022

# Get the data

with open("day_2_inputs") as file:
    # create a list comprehension and iterate through the data
    # in my file each line read it, strip of extra characters and the split then by new lines
   rounds = [i.replace(" ", "") for i in file.read().strip().split("\n")]

# print(rounds)


# ---------------------------------------------
# LEFT VS RIGHT | OUT | RIGHT + OUTCOME = TOTAL
# ---------------------------------------------
# A vs X = DRAW = (1 + 3) = 4
# A vs Y = WIN  = (2 + 6) = 8
# A vs Z = LOSS = (3 + 0) = 3
# B vs X = LOSS = (1 + 0) = 1
# B vs Y = DRAW = (2 + 3) = 5
# B vs Z = WIN  = (3 + 6) = 9
# C vs X = WIN  = (1 + 6) = 7
# C vs Y = LOSS = (2 + 0) = 2
# C vs Z = DRAW = (3 + 3) = 6

# put everything into a dictionary
# outcomes = {
#     "AX":4, "AY":8, "AZ":3,
#     "BX":1, "BY":5, "BZ":9,
#     "CX":7, "CY":2, "CZ":6
# }
#
# total_points_part1 = 0
# for round in rounds:
#     total_points_part1 += outcomes[round]
#
# print(total_points_part1)

# part 2

desired_outcomes = {
    "AX":3, "AY":4, "AZ":8,
    "BX":1, "BY":5, "BZ":9,
    "CX":2, "CY":6, "CZ":7
}

total_points_part2 = 0
for round in rounds:
    total_points_part2 += desired_outcomes[round]

    print(total_points_part2)