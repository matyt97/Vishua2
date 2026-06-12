with open('clientes.html', 'r', encoding='utf-8') as f:
    clientes_lines = f.readlines()

# Extract from <!-- Clients Grid --> to the end of <!-- Global Capability Banner -->
start_idx = -1
end_idx = -1

for i, line in enumerate(clientes_lines):
    if "<!-- Clients Grid -->" in line:
        start_idx = i
    if "<!-- Global Capability Banner -->" in line:
        # find the end of this section which is before </main>
        for j in range(i, len(clientes_lines)):
            if "</main>" in clientes_lines[j]:
                end_idx = j
                break
        break

if start_idx != -1 and end_idx != -1:
    extracted_content = clientes_lines[start_idx:end_idx]
    
    with open('nosotros.html', 'r', encoding='utf-8') as f:
        nosotros_lines = f.readlines()
        
    main_end_idx = -1
    for i, line in enumerate(nosotros_lines):
        if "</main>" in line:
            main_end_idx = i
            break
            
    if main_end_idx != -1:
        new_nosotros_lines = nosotros_lines[:main_end_idx] + extracted_content + nosotros_lines[main_end_idx:]
        with open('nosotros.html', 'w', encoding='utf-8') as f:
            f.writelines(new_nosotros_lines)
        print("Successfully merged Clientes y Distribuciones into Nosotros.")
    else:
        print("Could not find </main> in nosotros.html")
else:
    print(f"Could not find boundaries in clientes.html. start: {start_idx}, end: {end_idx}")
