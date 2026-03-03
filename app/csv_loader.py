import csv

def parse_csv(file_path):
    """
    Load a CSV file and return a list of dictionaries.
    """
    try:
        data = []
        with open(file_path, mode="r", newline="", encoding="utf-8") as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                data.append(row)
        return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except PermissionError:
        print(f"Error: Permission denied when accessing '{file_path}'.")
        return None
    except csv.Error as e:
        print(f"Error parsing CSV file: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None