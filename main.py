from utils import minimum_coin_bottom_up

total = 12
coins = [1, 2, 5]


if __name__ == '__main__':
    coins = minimum_coin_bottom_up(total, coins)

    if coins is not None:
        print(f"total of {len(coins)} coins with values: {coins}")
    else:
        print("No solution is possible")
