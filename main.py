if __name__ == "__main__":
    owner_name = input("Enter owner name: ")
    mob_number = input("Enter mobile number: ")
    start_balance = float(input("Enter starting balance: "))

    wallet = LoadWallet(owner_name, mob_number, start_balance)

    while True:
        print("\n---MENU---")
        print("1.Top Up Load")
        print("2. Send Load (same network)")
        print("3. Send Load (with fee)")
        print("4. Show Balance")
        print("5. Exit")

        pili_ka = input("Enter your choice (1-5): ")

        if pili_ka == 1:
            top_up_amount = float(input("Enter top-up amount: "))
            wallet.top_up(top_up_amount)