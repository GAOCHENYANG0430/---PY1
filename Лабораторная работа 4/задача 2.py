students_dict = {
    'Саша': 27,
    'Кирилл': 52, 
    'Маша': 14, 
    'Петя': 36, 
    'Оля': 43, 
}
min_age = 18  
 
students_list = []
 
for student in students_dict:
    if students_dict[student] > min_age:
        students_list.append(student)
 
print('Саша', 'Кирилл', 'Петя', 'Оля', students_list)

students_list.sort()
print('Кирилл', 'Оля', 'Петя', 'Саша', students_list)