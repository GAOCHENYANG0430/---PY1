DEFAULT_COUNT = 0
graders_dict = {
    3: 1, 
    4: 2, 
    5: 4
}

print(graders_dict.get(2))  
print(graders_dict.get(2, DEFAULT_COUNT)) 