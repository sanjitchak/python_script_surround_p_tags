with open('newpost.txt', 'r',encoding="utf8") as f:
    lines = f.readlines()

modified_lines = []
for line in lines:
    if not line.strip():  # ignore empty or whitespace-only lines
        continue
    if line.strip().startswith('<'):
        modified_lines.append(line)
    else:
        modified_lines.append('<p>' + line.strip() + '</p>')

with open('newfile.txt', 'w', encoding="utf8") as f:
    for line in modified_lines:
        f.write(line + '\n')
