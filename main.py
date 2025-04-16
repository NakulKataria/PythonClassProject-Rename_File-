import os
import sys
from datetime import datetime

def rename_files(folder_path, rule='add_date_prefix'):
    try:
        if not os.path.exists(folder_path):
            raise FileNotFoundError("The specified folder does not exist.")

        files = os.listdir(folder_path)
        if not files:
            print("The folder is empty. No files to rename.")
            return

        for filename in files:
            old_path = os.path.join(folder_path, filename)

            # Skip directories
            if os.path.isdir(old_path):
                continue

            if rule == 'add_date_prefix':
                date_str = datetime.now().strftime("%Y-%m-%d")
                new_name = f"{date_str}_{filename}"
            elif rule == 'remove_spaces':
                new_name = filename.replace(" ", "_")
            elif rule == 'lowercase':
                new_name = filename.lower()
            else:
                raise ValueError("Invalid renaming rule specified.")

            new_path = os.path.join(folder_path, new_name)

            # Avoid overwriting existing files
            if os.path.exists(new_path):
                print(f"Skipped: {new_name} already exists.")
                continue

            os.rename(old_path, new_path)
            print(f"Renamed: {filename} ➜ {new_name}")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")

# Example usage:
if __name__ == "__main__":
    folder = input("Enter the path to the folder: ").strip()
    print("Choose a renaming rule:\n1. add_date_prefix\n2. remove_spaces\n3. lowercase")
    rule_input = input("Enter rule (e.g., add_date_prefix): ").strip()

    rename_files(folder, rule_input)
