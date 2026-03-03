from app.csv_loader import parse_csv
from app.transform import apply_filter, apply_rename
from app.cli import parse_args
import csv


def main():
    args = parse_args()
    input_path = args.input_csv
    output_path = args.output_csv

    # Load CSV
    data = parse_csv(input_path)
    if data is None or not data:
        print("No data to process.")
        return

    # Transformations
    filtered = data
    if args.filter:
        for f in args.filter:
            filtered = apply_filter(filtered, f)

    transformed = filtered
    if args.rename:
        for r in args.rename:
            transformed = apply_rename(transformed, r)

    # Save CSV
    try:
        with open(output_path, mode="w", newline="", encoding="utf-8") as file:
            if not transformed:
                print("No data to save.")
                return
            writer = csv.DictWriter(file, fieldnames=transformed[0].keys())
            writer.writeheader()
            for row in transformed:
                writer.writerow(row)
        print(f"Saved {len(transformed)} rows to '{output_path}'.")
    except Exception as e:
        print(f"Error writing CSV file: {e}")

if __name__ == "__main__":
    main()