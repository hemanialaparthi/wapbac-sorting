import random

# Spaghetti code that replaces the text at a given position in a CSV file with replacement_text
# The replacement is done with a given percentage chance
# Currently not finished just a proof of concept thought for the time being for work in the future.


def replace_text_master(file_path, replacement_text, attribute_pos, percentage=50, output_file=None):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    modified_lines = []
    for line in lines:
        if random.random() < percentage / 100.0:  # Replace with the given percentage chance
            parts = line.split(',')  
            if len(parts) < attribute_pos:
                modified_line = line
            else:
                for part in len(parts):
                    if part == attribute_pos:
                        parts[part] = replacement_text
                    if part == 0:
                        modified_lines = parts[part] + ','
                    if part == len(parts):
                        modified_lines += parts[part]
                    modified_lines = modified_lines + parts[part] + ','
        else:
            modified_line = line  # If not selected, keep the line as is
        modified_lines.append(modified_line)

    output_path = output_file if output_file else file_path
    with open(output_path, 'w', encoding='utf-8') as file:
        file.writelines(modified_lines)