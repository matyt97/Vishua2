import os
import re

files = [
    'productos.html',
    'clientes.html',
    'representacion.html',
    'servicios.html',
    'novedades.html',
    'tobogan.html',
    'contacto.html',
    'nosotros.html'
]

# Read index.html to extract the unified header and footer
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

header_match = re.search(r'<header class="fixed top-0 w-full z-\[60\] flex flex-col">.*?</header>', index_content, re.DOTALL)
if not header_match:
    print('Header not found in index.html')
    exit(1)
new_header = header_match.group(0)

footer_match = re.search(r'<footer.*?</footer>', index_content, re.DOTALL)
if not footer_match:
    print('Footer not found in index.html')
    exit(1)
new_footer = footer_match.group(0)

for file in files:
    if not os.path.exists(file):
        print(f'File {file} not found')
        continue
    
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Create a base header where all links are inactive
    active_class = 'text-orange-500 border-b-2 border-orange-500 pb-1'
    inactive_class = 'text-slate-300 hover:text-white transition-colors'
    base_header = new_header.replace(f'class="{active_class}"', f'class="{inactive_class}"')
    
    # Make the current file's link active
    file_header = base_header.replace(
        f'class="{inactive_class}" href="{file}"',
        f'class="{active_class}" href="{file}"'
    )
    
    # Replace header/nav area
    # Old files might have <!-- TopAppBar --> ... </nav> or <header> ... </nav>
    # Let's replace from <!-- TopAppBar --> or <header ... fixed ...> to </nav>
    content = re.sub(r'<!-- TopAppBar -->.*?</nav>', file_header, content, flags=re.DOTALL)
    
    # Some files might not have <!-- TopAppBar --> but have <header> ... </nav>
    if file_header not in content:
         content = re.sub(r'<header.*?</nav>', file_header, content, flags=re.DOTALL)

    # Replace footer
    content = re.sub(r'<footer.*?</footer>', new_footer, content, flags=re.DOTALL)

    # Update specific broken links in main content
    content = content.replace('href="/contacto"', 'href="contacto.html"')
    content = content.replace('href="/servicios"', 'href="servicios.html"')
    content = content.replace('href="/productos"', 'href="productos.html"')
    
    # Ensure main has enough padding to account for the new header
    content = re.sub(r'<main class="[^"]*"', '<main class="pt-[160px] md:pt-[120px]"', content)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Processed {file}')
