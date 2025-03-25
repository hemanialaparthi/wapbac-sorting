def replace_text_before_comma(file_path, replacement_text, output_file=None):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    modified_lines = []
    for line in lines:
        parts = line.split(',', 1)  # Split at the first comma only
        if len(parts) > 1:
            modified_line = replacement_text + ',' + parts[1]
        else:
            modified_line = line  # If no comma, keep the line as is
        modified_lines.append(modified_line)

    output_path = output_file if output_file else file_path
    with open(output_path, 'w', encoding='utf-8') as file:
        file.writelines(modified_lines)

# Example usage
replace_text_before_comma('input.txt', 'Cindy Burns', 'output.txt')