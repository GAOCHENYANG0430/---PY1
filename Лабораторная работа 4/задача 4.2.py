grades_list = [5, 5, 4, 3, 4, 5, 5]

graders_dict = {}
DEFAULT_COUNT = 0

for grade in grades_list:
    graders_dict[grade] = graders_dict.get(grade, DEFAULT_COUNT) + 1

graders_dict