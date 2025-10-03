# Find the biggest coin that is less than the giving total number
# Add coin to the result and subtract from the total number
# if V is eqal to zero:
#   then print result
# else:
#   repeat step 2 and 3


def change_coin(total_number, coins):
    coins.sort()
    index = len(coins)-1

    while True:
        coin_value = coins[index]
        if coin_value <= total_number:
            print(coin_value)
            total_number = total_number - coin_value
        if coin_value > total_number:
            index -= 1
        if total_number == 0:
            break


coins = [1, 2, 5, 10, 20, 50, 100]
change_coin(333, coins)
