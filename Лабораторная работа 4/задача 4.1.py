grades_list = [5, 5, 4, 3, 4, 5, 5]

graders_dict = {}

for grade in grades_list:
    if grade in graders_dict:
        graders_dict[grade] += 1  
    else:
        graders_dict[grade] = 1  

graders_dict