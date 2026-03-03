def filter_adults(data):
    filtered = []
    for row in data:
        if int(row['age']) >= 18:
            filtered.append(row.copy())
    return filtered


def rename_column(data, old_key, new_key):
    transformed = []
    for row in data:
        new_row = row.copy()
        if old_key in new_row:
            new_row[new_key] = new_row.pop(old_key)
        else:
            print(f"Warning: Column '{old_key}' does not exist in a row. Skipping rename.")
    return transformed


def apply_filter(data, condition):
    if not condition or not data:
        return data

    key, op, value = None, None, None
    # Basic parser: splits on >=, <=, ==, >, <
    for operator in [">=", "<=", "==", ">", "<"]:
        if operator in condition:
            key, value = condition.split(operator)
            key = key.strip()
            value = value.strip()
            op = operator
            break
    if not op:
        print(f"Invalid filter condition: {condition}")
        return data

    # Column validation
    if key not in data[0]:
        print(f"Column '{key}' does not exist in CSV. Skipping this filter.")
        return data

    filtered = []
    for row in data:
        try:
            # Try numeric comparison first
            cell = int(row[key])
            comp = int(value)
        except (ValueError, KeyError):
            # Fallback to string comparison for non-numeric data
            cell = str(row[key])
            comp = str(value)

        if op == ">=" and cell >= comp:
            filtered.append(row.copy())
        elif op == "<=" and cell <= comp:
            filtered.append(row.copy())
        elif op == "==" and cell == comp:
            filtered.append(row.copy())
        elif op == ">" and cell > comp:
            filtered.append(row.copy())
        elif op == "<" and cell < comp:
            filtered.append(row.copy())
    return filtered


def apply_rename(data, rename_str):
    if not rename_str or not data:
        return data
    try:
        old_key, new_key = rename_str.split(":")
    except ValueError:
        print(f"Invalid rename format: {rename_str}")
        return data

    # Column validation
    if old_key.strip() not in data[0]:
        print(f"Column '{old_key.strip()}' does not exist in CSV. Skipping this rename.")
        return data

    # Pass to the helper function for transformation
    transformed = []
    for row in data:
        new_row = row.copy()
        if old_key.strip() in new_row:
            new_row[new_key.strip()] = new_row.pop(old_key.strip())
        transformed.append(new_row)
    return transformed
