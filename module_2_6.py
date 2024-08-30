
def password(digit):
    result = str()
    numbers_pair = []
    for i in range (1, digit):
        temp_list= []
        for a in range (2 , digit):
            if i >= digit / 2:
                break
            elif digit % (i + a) == 0 and i != a:
                temp_list.append([i, a])

        if temp_list == []:
            break
        else:
            numbers_pair.append(temp_list)
            
    for lists in numbers_pair:
        for pair in lists:
            for digits in pair:
                result += str(digits)
    
    return result
print(password(4))
print(password(7))
print(password(13))
