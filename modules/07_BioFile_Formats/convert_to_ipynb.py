
import nbformat

def convert_to_ipynb(input_file, output_file):
    # Read the script
    with open(input_file, 'r') as f:
        lines = f.readlines()

    # Initialize notebook
    notebook = nbformat.v4.new_notebook()
    cells = []
    current_content = []
    current_type = None

    # Process each line
    for line in lines:
        line = line.rstrip()  # Remove trailing whitespace/newlines
        if line == '# %% [markdown]':
            if current_content:  # Save previous cell
                content_str = ''.join(current_content)
                if current_type == 'markdown':
                    cells.append(nbformat.v4.new_markdown_cell(source=content_str))
                elif current_type == 'code':
                    cells.append(nbformat.v4.new_code_cell(source=content_str))
            current_type = 'markdown'
            current_content = []
        elif line == '# %%':
            if current_content:  # Save previous cell
                content_str = ''.join(current_content)
                if current_type == 'markdown':
                    cells.append(nbformat.v4.new_markdown_cell(source=content_str))
                elif current_type == 'code':
                    cells.append(nbformat.v4.new_code_cell(source=content_str))
            current_type = 'code'
            current_content = []
        else:
            current_content.append(line + '\n')  # Preserve newlines

    # Add the final cell
    if current_content:
        content_str = ''.join(current_content)
        if current_type == 'markdown':
            cells.append(nbformat.v4.new_markdown_cell(source=content_str))
        elif current_type == 'code':
            cells.append(nbformat.v4.new_code_cell(source=content_str))

    # Attach cells to notebook
    notebook['cells'] = cells

    # Write to .ipynb file
    with open(output_file, 'w') as f:
        nbformat.write(notebook, f)
    print(f"Converted {input_file} to {output_file}")

# Example usage
input_file = 'Updated_assignment.py'  # Your input script
output_file = 'Updated_assignment.ipynb'  # Desired output notebook
convert_to_ipynb(input_file, output_file)