with open('clientes_y_distribuidores.html', 'r', encoding='utf-8') as f:
    c_lines = f.readlines()

start_extract = -1
end_extract = -1

for i, line in enumerate(c_lines):
    if "<!-- Socios Estratégicos" in line:
        start_extract = i
    if "<!-- Footer -->" in line:
        end_extract = i
        # We actually want to stop before </main>, let's find </main> around there
        for j in range(i, 0, -1):
            if "</main>" in c_lines[j]:
                end_extract = j
                break
        break

if start_extract != -1 and end_extract != -1:
    extracted = c_lines[start_extract:end_extract]
    
    with open('nosotros.html', 'r', encoding='utf-8') as f:
        n_lines = f.readlines()
        
    start_replace = -1
    end_replace = -1
    for i, line in enumerate(n_lines):
        if "<!-- Clients Grid -->" in line:
            start_replace = i
        if "</main>" in line:
            end_replace = i
            break
            
    if start_replace != -1 and end_replace != -1:
        new_n_lines = n_lines[:start_replace] + extracted + n_lines[end_replace:]
        with open('nosotros.html', 'w', encoding='utf-8') as f:
            f.writelines(new_n_lines)
        print("Successfully replaced with Clientes y Distribuidores content.")
    else:
        print("Could not find replacement boundaries in nosotros.html")
else:
    print("Could not find extraction boundaries in clientes_y_distribuidores.html")
