import csv
import os


def save_account(filename: str, name: str, account_type: str, balance: float, deposit_count: int) -> None:
    """Save or update an account in a CSV file."""
    accounts = []

    if os.path.exists(filename):
        with open(filename, "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                accounts.append(row)

    updated = False

    for account in accounts:
        if account["name"].lower() == name.lower():
            account["account_type"] = account_type
            account["balance"] = str(balance)
            account["deposit_count"] = str(deposit_count)
            updated = True

    if not updated:
        accounts.append({
            "name": name,
            "account_type": account_type,
            "balance": str(balance),
            "deposit_count": str(deposit_count)
        })

    with open(filename, "w", newline="") as file:
        fieldnames = ["name", "account_type", "balance", "deposit_count"]
# AI used for Dictionary Writing syntax.                
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(accounts)


def load_account(filename: str, name: str) -> dict[str, str] | None:
    """Load an account by name from a CSV file."""
    if not os.path.exists(filename):
        return None

    with open(filename, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["name"].lower() == name.lower():
                return row

    return None