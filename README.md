# Python CSV Tool

A Python CLI tool to work with CSV files. It reads a CSV, lets you filter rows based on conditions, rename columns, and save the result to a new file.

## Project Structure

- `csv_loader.py` - loads CSV files safely.
- `transform.py` - filter and rename columns in any CSV.
- `cli.py` - handles command-line arguments for filters and renames.
- `main.py` - runs the tool, applies filters and renames, logs actions, and writes the output.

## How It Works

1. Load your CSV file.
2. Apply filters if you want (it will skip filters for columns that don't exist).
3. Apply renames if needed (it will skip renames for columns that don't exist).
4. Save the transformed CSV.

You can chain multiple filters and renames. It works with any CSV as long as the columns exist. If a column doesn’t exist, the tool will skip it and continue.

## Usage

### Run with Python

Put your CSV in the same folder as the code and run:

```bash
python main.py [SOURCE_FILE] [OUTPUT_FILE] --filter "[CONDITION]" --rename "[OLD_NAME:NEW_NAME]"
````

### Run with Podman (Containerized)

You can also run the tool in a container using Podman:

```bash
podman run --rm -v .:/app:Z csv-engineering-tool [SOURCE_FILE] [OUTPUT_FILE] --filter "[CONDITION]"
```

If the CSV doesn’t have some columns mentioned in filters or renames, the tool will show messages like:

```bash
Column 'score' does not exist in CSV. Skipping this filter.
Column 'old_name' does not exist in CSV. Skipping this rename.
Saved 3 rows to 'output.csv'.
```

This makes it safe to run with any CSV and still get results for the columns that exist.

## Why This Way

* Code is modular, easy to maintain, and easy to reuse.
* Filters and renames work for any CSV.
* Logging keeps you informed about each step.

## Future Ideas

* Support multiple conditions in one filter (AND/OR).
* Detect automatically if columns are numbers or strings for smarter filtering.
* Export to other formats like JSON.
