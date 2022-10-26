cart = {
    "Яблоко": 23, 
    "Апельсин": 47, 
    "Банан": 10
}

for fruit, count in cart.items():  
    print(fruit)
    print("Количество:", count)
    print()

total_count = sum(cart.values())  
print("Общее количество фруктов:", total_count)