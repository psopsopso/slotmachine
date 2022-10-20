MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1


def deposit():
    while True:
        amount = input("What would you like to deposit ? $ ")
        if amount.isdigit():
            amount = int(amount)
            if amount >= 0:
                break
            else:
                print("Amount must be greater than zero.")
        else:
            print("Please enter a valid number.")
    return amount


def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if lines in range(1, MAX_LINES+1):
                break
            else:
                print(f"Number of lines must be between 1 and {MAX_LINES}.")
        else:
            print("Please enter a valid number.")
    return lines


def get_bet():
    while True:
        amount = input("What would you like to bet ? $ ")
        if amount.isdigit():
            amount = int(amount)
            if amount in range(MIN_BET, MAX_BET + 1):
                break
            else:
                print(f"Amount must be between {MIN_BET} and {MAX_BET}.")
        else:
            print("Please enter a valid number.")
    return amount


def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(
                f"You do not have enough fund to bet that amount. Current balance: {balance}. Bet is {total_bet}.")
        else:
            break
    print(
        f"You are betting {bet}$ on {lines} lines. Total bet is equal to: {total_bet}$.")


main()
