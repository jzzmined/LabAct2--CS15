class LoadWallet:
    def __init__(self, owner_name,mob_number,start_balance=0.0):
        self.owner_name = owner_name
        self.mob_number = mob_number
        self.start_balance = float(start_balance)

    #TopUp Load
    def top_up(self, top_up_amount):
        if top_up_amount > 0:
            self.start_balance += top_up_amount
            print(f"Top-up successful. New balance: PHP {self.start_balance:.2f}")
        else:
            print("Invalid top-up amount. Please enter a positive value.")
        
    #Send Load
    def send_load(self, recipient_number, send_amount):
        if send_amount > 0 and send_amount <= self.start_balance:
            self.start_balance -= send_amount
            print(f"Load sent successfully!")
            print(f"\nNew balance: PHP {self.start_balance:.2f}")
        else:
            print("Invalid send amount. Please enter a positive value within your balance.")

    #Send Load with Fee
    def send_with_fee(self, recipient_number, send_amount, fee=2.00):
        total_amount = send_amount + fee
        if send_amount <= 0:
            print("Invalid send amount. Please enter a positive value.")
        elif total_amount > self.start_balance:
            print("Insufficient balance to cover the send amount and fee.")
        else: 
            self.start_balance -= total_amount
            print(f"Load sent successfully!!")
            print(f"\nNew balance: PHP {self.start_balance:.2f}")

    #Show Balance
    def show_balance(self):
        print("\n---WALLET INFORMATION---")
        print(f"Owner: {self.owner_name}")
        print(f"Mobile Number: {self.mob_number}")
        print(f"Balance: PHP {self.start_balance:.2f}")

    


    


