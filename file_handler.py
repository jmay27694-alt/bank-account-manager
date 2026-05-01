import csv
import os

def save_account(filename: str, name: str, account_type: str, balance: float, deposit_count: int) -> None:
    """Save or update an account in a CSV file."""
    accounts = []

  
    print(f"DEBUG: Saving bank data to: {os.path.abspath(filename)}")

   
    if os.path.exists(filename):
        try:
            with open(filename, "r", newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    
                    if row.get("name"):
                        accounts.append(row)
        except Exception as e:
            print(f"DEBUG: Error reading file: {e}")

  
    updated = False
    for account in accounts:
        if account["name"].lower() == name.lower():
            account["account_type"] = account_type
            account["balance"] = str(balance)
            account["deposit_count"] = str(deposit_count)
            updated = True
            break

   
    if not updated:
        accounts.append({
            "name": name,
            "account_type": account_type,
            "balance": str(balance),
            "deposit_count": str(deposit_count)
        })

   
    try:
        with open(filename, "w", newline="") as file:
            fieldnames = ["name", "account_type", "balance", "deposit_count"]
            # AI used for Dictionary Writing syntax.
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(accounts)
        print("DEBUG: Bank account save successful.")
    except PermissionError:
        print("ERROR: CSV is open in Excel! Close it and try again.")
    except Exception as e:
        print(f"DEBUG: Write error: {e}")


def load_account(filename: str, name: str) -> dict[str, str] | None:
    """Load an account by name from a CSV file."""
    if not os.path.exists(filename):
        print(f"DEBUG: No bank file found at {filename}")
        return None

    try:
        with open(filename, "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row.get("name") and row["name"].lower() == name.lower():
                    return row
    except Exception as e:
        print(f"DEBUG: Error loading bank file: {e}")

    return None
