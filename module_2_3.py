my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
while i < len(my_list):
    current_number = my_list[i]
    if current_number < 0:
        break
    if current_number == 0:
        i += 1
        continue
    print(current_number)
    i += 1