list = []
a = ""
while a != "!":
    a = input("Введите число, если хочешь закончить введите восклицательный знак:")
    list.append(a)


print(sum(list) / len(list))
