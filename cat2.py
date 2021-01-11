from cat import Cat
baron = Cat("Барон", 2, "мальчик")
sem = Cat("Сэм", 2, "мальчик")
print("_"*20)
print(f"| Имя питомца: {baron.get_name()}", f"| Возраст: {baron.get_age()} года", f"| Пол: {baron.get_gen()}", sep="\n")
print("_"*20)
print(f"| Имя питомца: {sem.get_name()}", f"| Возраст: {sem.get_age()} года", f"| Пол: {sem.get_gen()}", sep="\n")
print("_"*20)
