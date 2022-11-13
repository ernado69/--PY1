from random import randint

def get_unique_list_numbers() -> list[int]:
        # TODO написать функцию для получения списка уникальных целых чисел
    list = []
    start, end = -10, 10
    for i in range(15):
        num = randint(start, end)
        if num not in list:
            list.append(num)
    return list

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
