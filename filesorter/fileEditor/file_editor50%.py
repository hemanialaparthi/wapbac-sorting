import random

def replace_text_before_comma(file_path, replacement_text, percentage=100, output_file=None):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    modified_lines = []
    total_lines = len(lines)
    num_lines_to_replace = int((percentage / 100) * total_lines)

    # Randomly shuffle the lines and select the first `num_lines_to_replace` lines to modify
    lines_to_modify = random.sample(range(total_lines), num_lines_to_replace)

    for i, line in enumerate(lines):
        if i in lines_to_modify:
            parts = line.split(',', 1)  # Split at the first comma only
            if len(parts) > 1:
                modified_line = replacement_text + ',' + parts[1]
            else:
                modified_line = line  # If no comma, keep the line as is
        else:
            modified_line = line  # Keep the line unchanged
        modified_lines.append(modified_line)

    output_path = output_file if output_file else file_path
    with open(output_path, 'w', encoding='utf-8') as file:
        file.writelines(modified_lines)

# Example usage
replace_text_before_comma('input.txt', 'Cindy Burns', percentage=50, output_file='output.txt')
