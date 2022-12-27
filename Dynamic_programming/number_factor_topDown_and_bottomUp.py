def number_factor_topDown(n, temp_dict):
    if n in (0, 1, 2):
        return 1
    elif n == 3:
        return 2
    else:
        if n not in temp_dict:
            subP1 = number_factor_topDown(n-1, temp_dict)
            subP2 = number_factor_topDown(n-3, temp_dict)
            subP3 = number_factor_topDown(n-4, temp_dict)
            temp_dict[n] = subP1 + subP2 + subP3
        return temp_dict[n]


print(number_factor_topDown(5, {}))


def number_factor_bottomUP(n):
    temp_arr = [1, 1, 1, 2]
    for i in range(4, n+1):
        temp_arr.append(temp_arr[i-1] + temp_arr[i-3] + temp_arr[i-4])
    return temp_arr[n]


print(number_factor_bottomUP(5))
