from typing import List


def minimum_coin_bottom_up(total: int, coins_list: List[int]):
    coins_list = sorted(coins_list, reverse=True)

    T: List = [0] * (total + 1)
    R: List = [0] * (total + 1)

    T[0] = 0
    for i in range(1, total):
        T[i] = 2**99
        R[i] = -1

    for j in range(0, len(coins_list) - 1):
        for i in range(1, total):
            if i >= coins_list[j]:
                if T[i - coins_list[j]] + 1 < T[i]:
                    T[i] = 1 + T[i - coins_list[j]]
                    R[i] = j

    return get_coin_combination(R, coins_list)


def get_coin_combination(R: List[int], coins_list: List[int]):
    if R[len(R) - 1] == -1:
        return

    coins: list[int] = []
    start: int = len(R) - 1

    while start != 0:
        j = R[start]
        coins.append(coins_list[j])
        start -= coins_list[j]

    return sorted(coins, reverse=True)
