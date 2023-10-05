#!/bin/python3

# Starter Code for Project 1 Phase 2 of UPRM CIIC 3015 Fall 2023 

# Repeated symbol count for header messages
BORDER_COUNT = 25
# Repeats the symbol for formatted text borders
starborder = "*" * BORDER_COUNT
dashborder = "-" * BORDER_COUNT

# Menu options to compare with choice
DEPOSIT_FUNDS_MENU_CHOICE = "1"
WITHDRAW_FUNDS_MENU_CHOICE = "2"
VIEW_BALANCE_MENU_CHOICE = "3"
CLOSE_ACCOUNT_MENU_CHOICE = "4"
# Only shown if balance is greater than or equal to zero
CLOSE_ACCOUNT_MENU_CHOICE = "4"

# Counters
penalty_cnt = 0
withdrawal_cnt = 0
deposit_cnt = 0

print("\n" + starborder + "\nWelcome to Banco Popular!\n" + starborder)
#
# Setup Account
#Balance loop
print("\n" + dashborder + "\nAccount Setup\n" + dashborder + "\n")
accent = input("Account name: ")
#The starting balance input is put in a while loop so if a person inputs a number that isnt valid to the system it repeats the input. It was also added try and except for if the user enters a number or text invalid to the system.
while True:
    try:
        startbal= input("Starting balance: $")
        floatstartbal= float(startbal)
        if floatstartbal > 0:
            if startbal == format((floatstartbal), '.0f') or startbal == format((floatstartbal), ".2f"):
                break
        else:
            pass
    except ValueError:
        pass
#startbal is equal to floatstartbal due to startbal was a string and I didnt wanna change all the variables in the code.
startbal = floatstartbal
#This variable was named for the close account initial balance.
initialbal = startbal
print("\nWelcome new account member!\n"
    f"Account {accent} created with starting balance: ${startbal:.2f}")

# TODO: implement setup account logic here building off phase 1 logic

#
# Main Account Menu
#
# TODO: add loop with menu selection and menu actions from phase 1 here
#Loop is added so the user can hit a choice and be continuously given the option until "4" is entered.
while True:
    if startbal < 0:
        n=input(
            "\nSelect option:\n"
            "(1) Deposit funds\n"
            "(2) Withdraw funds\n"
            "(3) View bank account balance\n")
    else:
        n = input(
        "\nSelect option:\n"
        "(1) Deposit funds\n"
        "(2) Withdraw funds\n"
        "(3) View bank account balance\n"
        "(4) Close account\n")
#If 1 is entered by user the code will loop due to it only accepts the input of 2 decimal points or no decimal points entered.
#The code uses try and except for the input
#It preps the user for if they enter a number greater than 0 to run the deposit and if the contrary it done it gives an error message
    if n == "1":
        # Dashborder makes it look nice :).
        print("\n" + dashborder + "\nDeposit funds\n" + dashborder + "\n")
        try:
            dpfunds = input("Amount to deposit: $")
            floatdpfunds = float(dpfunds)
            if floatdpfunds > 0:
                if format((floatdpfunds), '.0f') == dpfunds or format((floatdpfunds), '.2f')== dpfunds:
                # This is for the closing account when one closes the account and shows deposit amounts.
                    deposit_cnt += 1
                    dpfunds = floatdpfunds
                    startbal += dpfunds
                    print(f"Account Name: {accent}\nDeposit Amount: ${dpfunds:.2f}\nNew Balance: ${startbal:.2f}" + "\n")
                    continue
                # If the user chooses a number equal to or less than 0, the system fails the transaction and ends the loop.
                else:
                    print("Transaction failed: Invalid deposit amount.")
            else:
                print("Transaction failed: Invalid deposit amount.")
                # If the user chooses a number greater than 0, it deposits funds into the user's bank account.
        except ValueError:
            print("Transaction failed: Invalid deposit amount.")
            pass
    #
    # Withdrawal
    #

    # TODO: Implement the logic for the withdrawal action here
    # If the user chooses 2, it allows the user to withdraw money from their account.
    #The code is in a try and except for the data validation which was already previously explained.
    #The code has all option for penalty and change dispenser described below
    elif n == "2":
        print("\n" + dashborder + "\nWithdraw Funds\n" + dashborder)
        try:
            withdraw = input("\nAmount to withdraw: $")
            floatwithdrawfunds = float(withdraw)
            # If the user inputs a number less than or equal to 0, the system will print a transaction error and break the loop.
            if floatwithdrawfunds <= 0:
                print("Transaction failed: Invalid withdrawal amount.")
            # If the user inputs a number greater than 0, the system will print the account name, withdrawal amount, penalties, new balance, and a thank you message.
            elif floatwithdrawfunds > 0:
                if format((floatwithdrawfunds), '.0f') == withdraw or format((floatwithdrawfunds), '.2f') == withdraw:
                    startbal -= floatwithdrawfunds
                    withdraw = floatwithdrawfunds
                    withdrawal_cnt += 1
                    penalamt = 0
                    #This part of the code was focused on out dispensary assigment.
                    # Convert the dollar amount to cents and work with integers
                    cents = int(withdraw * 100 + 0.5)  # Round to the nearest cent
                    # Calculate the number of each denomination
                    hundreddollar = cents // 10000
                    cents %= 10000
                    fiftydollar = cents // 5000
                    cents %= 5000
                    twentydollar = cents // 2000
                    cents %= 2000
                    tendollar = cents // 1000
                    cents %= 1000
                    fivedollar = cents // 500
                    cents %= 500
                    dollars = cents // 100
                    cents %= 100
                    quarters = cents // 25
                    cents %= 25
                    dimes = cents // 10
                    cents %= 10
                    nickels = cents // 5
                    pennies = cents % 5
                    #If user balance is greater than 0 the code will run the following
                    if startbal > 0:
                        print(
                            f"Account name: {accent}\nWithdrawal Amount: ${floatwithdrawfunds:.2f}\nPenalties: ${penalamt:.2f}\nNew Balance: ${startbal:.2f}")
                        print("Currency withdrawn:")
                        #The code below is for the change dispensary so it inputs the correct sums of each bill or coin withdrawn.
                        if hundreddollar > 0:
                            print(f"$100s: {hundreddollar}")
                        if fiftydollar > 0:
                            print(f"$50s: {fiftydollar}")
                        if twentydollar > 0:
                            print(f"$20s: {twentydollar}")
                        if tendollar > 0:
                            print(f"$10s: {tendollar}")
                        if fivedollar > 0:
                            print(f"$5s: {fivedollar}")
                        if dollars > 0:
                            print(f"$1s: {dollars}")
                        if quarters > 0:
                            print(f"quarters: {quarters}")
                        if dimes > 0:
                            print(f"dimes: {dimes}")
                        if nickels > 0:
                            print(f"nickels: {nickels}")
                        if pennies > 0:
                            print(f"pennies: {pennies}")
                    # If the user inputs a number that would make their bank account balance reach or exceed -100, no action will be taken.
                    elif 0 >= startbal >= -100:
                        print(
                            f"Account name: {accent}\nWithdrawal Amount: ${floatwithdrawfunds:.2f}\nPenalties: ${penalamt:.2f}\nNew Balance: ${startbal:.2f}")
                        print("Currency withdrawn:")
                        if hundreddollar > 0:
                            print(f"$100s: {hundreddollar}")
                        if fiftydollar > 0:
                            print(f"$50s: {fiftydollar}")
                        if twentydollar > 0:
                            print(f"$20s: {twentydollar}")
                        if tendollar > 0:
                            print(f"$10s: {tendollar}")
                        if fivedollar > 0:
                            print(f"$5s: {fivedollar}")
                        if dollars > 0:
                            print(f"$1s: {dollars}")
                        if quarters > 0:
                            print(f"quarters: {quarters}")
                        if dimes > 0:
                            print(f"dimes: {dimes}")
                        if nickels > 0:
                            print(f"nickels: {nickels}")
                        if pennies > 0:
                            print(f"pennies: {pennies}")
                    # If the user inputs a number that would make their bank account balance fall between -100 and -1000, the user will be charged a 1% fee on the amount withdrawn.
                    elif -100 > startbal > -1000:
                        #penalty_cnt is added for if the user closes the account it gives the total sum of times there was a penalty
                        penalty_cnt += 1
                        penalamt = floatwithdrawfunds * 0.01
                        startbal -= penalamt
                        print(
                            f"Withdrawal amount is greater than account balance. Overdraft penalty of 1% applied.\nAccount name: {accent}\nWithdrawal Amount: ${floatwithdrawfunds:.2f}\nPenalties: ${penalamt:.2f}\nNew Balance: ${startbal:.2f}")
                        print("Currency withdrawn:")
                        if hundreddollar > 0:
                            print(f"$100s: {hundreddollar}")
                        if fiftydollar > 0:
                            print(f"$50s: {fiftydollar}")
                        if twentydollar > 0:
                            print(f"$20s: {twentydollar}")
                        if tendollar > 0:
                            print(f"$10s: {tendollar}")
                        if fivedollar > 0:
                            print(f"$5s: {fivedollar}")
                        if dollars > 0:
                            print(f"$1s: {dollars}")
                        if quarters > 0:
                            print(f"quarters: {quarters}")
                        if dimes > 0:
                            print(f"dimes: {dimes}")
                        if nickels > 0:
                            print(f"nickels: {nickels}")
                        if pennies > 0:
                            print(f"pennies: {pennies}")
                    # If the user inputs a number that would make their bank account balance fall between -1000 and -5000, the user will be charged a 3% fee on the amount withdrawn.
                    elif -1000 >= startbal > -5000:
                        # penalty_cnt is added for if the user closes the account it gives the total sum of times there was a penalty
                        penalty_cnt += 1
                        penalamt = floatwithdrawfunds * 0.03
                        startbal -= penalamt
                        print(
                            f"Withdrawal amount is greater than account balance. Overdraft penalty of 3% applied.\nAccount name: {accent}\nWithdrawal Amount: ${floatwithdrawfunds:.2f}\nPenalties: ${penalamt:.2f}\nNew Balance: ${startbal:.2f}")
                        print("Currency withdrawn:")
                        if hundreddollar > 0:
                            print(f"$100s: {hundreddollar}")
                        if fiftydollar > 0:
                            print(f"$50s: {fiftydollar}")
                        if twentydollar > 0:
                            print(f"$20s: {twentydollar}")
                        if tendollar > 0:
                            print(f"$10s: {tendollar}")
                        if fivedollar > 0:
                            print(f"$5s: {fivedollar}")
                        if dollars > 0:
                            print(f"$1s: {dollars}")
                        if quarters > 0:
                            print(f"quarters: {quarters}")
                        if dimes > 0:
                            print(f"dimes: {dimes}")
                        if nickels > 0:
                            print(f"nickels: {nickels}")
                        if pennies > 0:
                            print(f"pennies: {pennies}")
                        # If the user inputs a number that would make their bank account balance fall below -5000, the system will display a transaction error.
                    elif startbal <= -5000:
                        # in this part i add the float withdraw funds + the startbal due too in the code once 2 is inputed it does startbal - floatwithdrawfunds.
                        withdrawal_cnt -=1
                        startbal += floatwithdrawfunds
                        print("Transaction failed: withdrawal amount exceeds overdraft limit.")
                else:
                    print("Transaction failed: Invalid withdrawal amount.")
            #This space was put due to the tester having to spaces I couldnt use a "\n" because it woul addd 2 spaces instead of the 1 I was missing.
            print("")
        except ValueError:
            print("Transaction failed: Invalid withdrawal amount.")
            pass
    #
    # View balance
    #

    # TODO: Implement the logic for the view balance action here
    # If the user chooses 3, it allows the user to see the current balance from their account.
    elif n == "3":
            print("\n" + dashborder + "\nAccount balance\n" + dashborder)
            print(f"Account name: {accent}\nBalance: ${startbal:.2f}")
    #
    # Close account
    #

    # TODO: Implement the logic for the close account action here
    # If the user chooses 4, the system prints TODO and it allows the user to close the account and breaks loop.
    # TODO: support close account menu action
    elif n == "4":
        #if the start bal is greater than 0 it will show the following this is due to the fact that it needs to due the opposite if the startbal is less than 0
        if startbal >= 0:
            print("\n" + starborder + "\nClosing Account\n" + starborder)
            print("\n" + dashborder + "\nFinal Account Statement\n" + dashborder)
            #The balance was rounded due to it kept giving me a result that was incorrect
            startbal = round((startbal), 2)
            finalbal =float((startbal - initialbal) / initialbal) * 100
            #Here we focus on the final bal if its greater or equal to 0 that is because it has to have a (+0.00%)
            if finalbal >= 0:
                print(f"Account name: {accent}\nInitial balance: ${initialbal:.2f}\nFinal balance: ${startbal:.2f} (+{finalbal:.2f}%)")
            #The else is focused on if the code is negative so it wont have the plus sign in front.
            else:
                print(f"Account name: {accent}\nInitial balance: ${initialbal:.2f}\nFinal balance: ${startbal:.2f} ({finalbal:.2f}%)")
            #These prints are all accumalators that you can see throughout the code.
            #The accumulators are used for when one pressed "1" or "2" or if they have a penalty the code will take the accumulator variable and add 1 so the user can see how many times he had done what and his penalt
            # ies.
            print(f"Deposit count: {deposit_cnt}")
            print(f"Withdrawal count: {withdrawal_cnt}")
            print(f"Overdraft penalty count: {penalty_cnt}")
            print("\n" + "Thank you for banking with Banco Popular!")
            break
        else:
            pass
