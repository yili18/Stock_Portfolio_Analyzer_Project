import csv
from pathlib import Path
import sys


def load_accounts():
    """Writes account information from CSV to list."""
    csvpath = Path('client_table.csv')
    accounts = []
    with open(csvpath, newline='') as csvfile:
        rows = csv.reader(csvfile)
        header = next(rows)
        for row in rows:
            pin = int(row[3])
            balance = float(row[4])
            account = {
                "pin": pin,
                "balance": balance
            }
            accounts.append(account)
        return accounts


def validate_pin(pin):
    """Verifies that PIN is 5 digits long."""

    # Verifies length of pin is 5 digits prints validations message and return True. Else returns False.
    if len(pin) == 5:
        print(f"The length of your PIN is valid")
        return True
    else:
        return False

import sys
# import fire
import questionary

def login():
    """Login to the Clienet Portal using an account PIN."""

    # Initial CLI asking user to input PIN
    pin = questionary.text("Please enter your 5 digit PIN number:").ask()

    # Calls validate_pin() function to confirm length.
    if not validate_pin(pin):
        sys.exit("Sorry, your account PIN is not valid. It must be 5 digits in length.")

    # If pin validates, calls load_accounts() and then verifies pin against accounts list. Returns account that matches pin.
    accounts = load_accounts()

    for account in accounts:
        if int(pin) == account["pin"]:
            return account

    # If no account was returned above, exit with an error
    sys.exit(
        "Sorry, your login was not successful. Your PIN does not link to an account. Please check your PIN and try again."
    )


def main_menu():
    """Dialog for the Client Portal Main Menu."""

    # Determines action taken by application.
    action = questionary.select(
        "Would you like to check your balance?",
        choices=["yes", "no"],
    ).ask()
    return action


def run():
    """The main function for running the script."""

    # Initiates login process. If pin verified, returns validated account.
    account = login()

    # Initiates client portal action: check balance.
    action = main_menu()

    # Processes the chosen action
    if action == "yes":
        sys.exit(f"Your current account balance is {account['balance']: .2f}")

    # Prints the adjusted balance.
    print(
        f"Thank you for your {action}. Your adjusted balance is ${account['balance']: .2f}."
    )

if __name__ == "__main__":
    run()

