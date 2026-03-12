class Account:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def __repr__(self):
        return f"Account({self.name!r}, balance={self.balance})"


class Ledger:
    """A simple double-entry ledger.

    Every transaction moves money FROM one account TO another.
    A debit decreases the source; a credit increases the destination.
    """

    def __init__(self):
        self.accounts = {}
        self.transactions = []

    def create_account(self, name, opening_balance=0):
        self.accounts[name] = Account(name, opening_balance)

    def get_balance(self, name):
        return self.accounts[name].balance

    def transfer(self, from_account, to_account, amount):
        """Transfer `amount` from `from_account` to `to_account`.

        Rules:
        - amount must be positive.
        - The source balance is decreased by `amount`.
        - The destination balance is increased by `amount`.
        - The transaction is recorded.
        """
        if amount <= 0:
            raise ValueError("Transfer amount must be positive")

        src = self.accounts[from_account]
        dst = self.accounts[to_account]

        # BUG: signs are inverted — adds to source and subtracts from destination
        src.balance += amount
        dst.balance -= amount

        self.transactions.append({
            "from": from_account,
            "to": to_account,
            "amount": amount,
        })

    def total_transferred(self):
        """Return the total amount of money that has moved through the ledger."""
        return sum(t["amount"] for t in self.transactions)

    def net_balance(self):
        """Return the sum of all account balances.

        In a correct system this should always equal the sum of all opening balances,
        since transfers just move money between accounts.
        """
        return sum(acc.balance for acc in self.accounts.values())
