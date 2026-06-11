"""
ATM Simulation System
Developed by Anshika Batham
"""

# Default ATM Data
original_pin = 1234
balance = 10000

print("Welcome to Apna Bank ATM 🏦")

# Prompt user for PIN authentication
user_pin = int(input("Please enter your 4-digit PIN: "))

# Validate user credentials
if user_pin == original_pin:
    print("Login Successful! Welcome Anshika.\n")
    
    # Main ATM transaction loop
    while True:
        print("=== ATM Menu ===")
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Exit")
        
        # Prompt user for operation choice
        choice = int(input("Enter your choice (1-4): "))
        
        # Process user choice
        if choice == 1:
            print(f"Your current balance is: ₹{balance}\n")
            
        elif choice == 2:
            # Handle Cash Withdrawal
            withdraw_amt = int(input("Enter amount to withdraw: ₹"))
            if withdraw_amt > 0 and withdraw_amt <= balance:
                balance = balance - withdraw_amt
                print(f"Success! Please collect your cash: ₹{withdraw_amt}")
                print(f"Updated balance: ₹{balance}\n")
            else:
                print("Error: Insufficient funds or invalid amount!\n")
                
        elif choice == 3:
            # Handle Cash Deposit
            deposit_amt = int(input("Enter amount to deposit: ₹"))
            if deposit_amt > 0:
                balance = balance + deposit_amt
                print(f"Success! ₹{deposit_amt} deposited safely.")
                print(f"Updated balance: ₹{balance}\n")
            else:
                print("Error: Please enter a valid amount.\n")
                
        elif choice == 4:
            print("Thank you for using Apna Bank. Goodbye! 👋")
            break  # This stops the while loop and exits the ATM
            
        else:
            print("Invalid choice. Please select from 1-4.\n")

else:
    print("Wrong PIN! Transaction Cancelled.")