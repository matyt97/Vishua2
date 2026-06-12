video_section = """<!-- Video Showcase Section -->
<section class="py-xl bg-slate-950 dark:bg-black text-white">
<div class="max-w-[1280px] mx-auto px-4 md:px-8">
<div class="text-center mb-lg">
<h2 class="font-headline-lg text-headline-lg uppercase mb-4">Nuestro Trabajo en Terreno</h2>
<p class="font-body-md text-slate-400 max-w-2xl mx-auto">Conozca de cerca nuestros procesos, la implementación de tecnología y el compromiso de nuestro equipo humano en el día a día.</p>
</div>
<div class="relative max-w-4xl mx-auto bg-slate-800 rounded-xl overflow-hidden aspect-video shadow-2xl border border-slate-700 group cursor-pointer">
<img class="w-full h-full object-cover opacity-60 group-hover:opacity-40 transition-opacity duration-500" data-alt="Industrial working environment video thumbnail showing an active mining operation with safety personnel" src="https://lh3.googleusercontent.com/aida-public/AB6AXuAwUqA2nC3H09FDE57WdXYb1bBovmU0pT5E5kE5k9G1F8G6xO19f0XvA9V50Q-D4Hq2nC1bY8rU7o4eQ3pXv1r6TqBf11y8gB1sM3QW7D8FwBqA2wF2c5R4mU9jTqR5c8r2G6M9vH4bL8fX1G4wH5bE3sQ8fV7nE4bC3sV8cE2jQ1wT5gB9yN8kV7bL0dZ6pX2cV4bE3vN7gZ9oK1rL4qZ0wM5c" />
<div class="absolute inset-0 flex items-center justify-center">
<div class="w-20 h-20 bg-secondary-container hover:bg-orange-500 text-white rounded-full flex items-center justify-center transition-transform transform group-hover:scale-110 shadow-[0_0_30px_rgba(252,119,40,0.5)]">
<span class="material-symbols-outlined text-4xl" data-icon="play_arrow">play_arrow</span>
</div>
</div>
<div class="absolute bottom-6 left-6 right-6">
<p class="font-label-md uppercase tracking-widest text-slate-300 mb-2">Próximamente</p>
<h3 class="font-headline-md">Video Corporativo VISHUA SpA</h3>
</div>
</div>
</div>
</section>
"""

with open('index.html', 'r', encoding='utf-8') as f:
    index_lines = f.readlines()

# Extract Equipamiento Tecnico (lines 200-242, which is index 199 to 242)
equipamiento_block = index_lines[199:242]

# Replace in index.html
new_index_lines = index_lines[:199] + [video_section] + index_lines[242:]
with open('index.html', 'w', encoding='utf-8') as f:
    f.writelines(new_index_lines)

# Insert into productos.html
with open('productos.html', 'r', encoding='utf-8') as f:
    prod_lines = f.readlines()

# We insert before <!-- Product Grid -->, let's find that line
insert_idx = -1
for i, line in enumerate(prod_lines):
    if "<!-- Product Grid -->" in line:
        insert_idx = i
        break

if insert_idx != -1:
    new_prod_lines = prod_lines[:insert_idx] + equipamiento_block + prod_lines[insert_idx:]
    with open('productos.html', 'w', encoding='utf-8') as f:
        f.writelines(new_prod_lines)
    print("Successfully moved section and inserted video placeholder.")
else:
    print("Could not find <!-- Product Grid --> in productos.html")
