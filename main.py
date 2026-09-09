from loadwallet import LoadWallet

#MAIN
def main():
    print("\nMabuhay! Mag-load kana!")
    owner_name = input("\nEnter owner name: ")
    mob_number = input("Enter mobile number: ")
    start_balance = float(input("Enter starting balance: "))

    wallet = LoadWallet(owner_name, mob_number, start_balance)

    while True:
        print("\n---MENU---")
        print("1.Top Up Load")
        print("2.Send Load (same network)")
        print("3.Send Load (with fee)")
        print("4.Show Balance")
        print("5.Exit")

        pili_ka = int(input("\nChoose an option (1-5): "))

        if pili_ka == 1:
            top_up_amount = float(input("Enter top-up amount: "))
            wallet.top_up(top_up_amount)
        elif pili_ka == 2:
            recipient_number = input("Enter recipient number: ")
            send_amount = float(input("Enter send amount: "))
            wallet.send_load(recipient_number, send_amount)
        elif pili_ka == 3:
            recipient_number = input("Enter recipient number: ")
            send_amount = float(input("Enter send amount: "))
            fee = float(input("Enter fee amount (default is 2.00): ") or 2.00)
            wallet.send_with_fee(recipient_number, send_amount, fee)
        elif pili_ka == 4:
            wallet.show_balance()
        elif pili_ka == 5:
            print("Humana tehhh....")
            break
        else:
            print("Invalid choice. Please paki usab, salamat!")

main()

        
