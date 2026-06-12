with open('index.html', 'r', encoding='utf-8') as f:
    index_lines = f.readlines()

with open('servicios.html', 'r', encoding='utf-8') as f:
    servicios_lines = f.readlines()

# Extract lines 200 to 294 from index.html (0-indexed: 199 to 294)
section_to_copy = index_lines[199:294]

# Replace lines 174 to 242 in servicios.html (0-indexed: 173 to 242)
new_servicios_lines = servicios_lines[:173] + section_to_copy + servicios_lines[242:]

with open('servicios.html', 'w', encoding='utf-8') as f:
    f.writelines(new_servicios_lines)

print("Section replaced successfully.")
