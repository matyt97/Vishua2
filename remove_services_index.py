with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Remove lines 200 to 294 (which is index 199 to 294)
new_lines = lines[:199] + lines[294:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Removed section from index.html successfully.")
