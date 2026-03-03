import argparse

def parse_args():
    """
    Handle CLI argument parsing.
    Returns args object.
    """
    parser = argparse.ArgumentParser(description="Filter and transform CSV files.")
    parser.add_argument("input_csv", help="Path to input CSV file")
    parser.add_argument("output_csv", help="Path to output CSV file")
    parser.add_argument("--filter", nargs="+", help="Filter conditions, e.g., 'age>=18 score>50'")
    parser.add_argument("--rename", nargs="+", help="Rename columns, e.g., 'city:location name:full_name'")

    return parser.parse_args()