def main():
    coke_value = 50
    coins_allowed = [25, 10, 5]
    inserted_coins = 0

    while inserted_coins < coke_value:
        print(f"Amount Due: {coke_value - inserted_coins}")
        coins = int(input("Insert Coin: "))
        if coins in coins_allowed:
            inserted_coins += coins
        else:
            print(f"Amount Due: {coke_value - inserted_coins}")
            coins = int(input("Insert Coin: "))
    else:
            print(f"Change Owed: {inserted_coins - coke_value}")

main()
