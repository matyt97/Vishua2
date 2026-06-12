import os
import re

whatsapp_widget = """<!-- WhatsApp Button -->
<div id="whatsapp-widget" class="fixed bottom-8 right-8 z-[100] flex flex-col items-end gap-2 transition-all duration-300">
    <button onclick="document.getElementById('whatsapp-widget').style.display='none'" class="bg-white text-slate-500 hover:text-slate-800 rounded-full w-6 h-6 flex items-center justify-center shadow-md border border-slate-200" title="Cerrar">
        <span class="material-symbols-outlined text-[14px]">close</span>
    </button>
    <a class="w-16 h-16 bg-[#25D366] text-white rounded-full flex items-center justify-center shadow-2xl transition-transform hover:scale-110 active:scale-95 group relative" href="https://wa.me/56912345678" target="_blank">
        <svg class="w-8 h-8 fill-current" viewbox="0 0 24 24">
            <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L0 24l6.335-1.662c1.72.94 3.659 1.437 5.63 1.438h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"></path>
        </svg>
        <div class="absolute right-20 bg-slate-900 text-white px-4 py-2 text-xs font-bold uppercase rounded-sm opacity-0 group-hover:opacity-100 transition-opacity whitespace-nowrap shadow-xl pointer-events-none">Hable con un experto</div>
    </a>
</div>
"""

# HTML files to process
html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Step 1: Remove any existing WhatsApp Button completely
    # The old one might be from <!-- WhatsApp Button --> to </a> right before </body>
    # The new one is <!-- WhatsApp Button --> to </div> right before </body>
    # We will use regex to remove it
    
    # regex to match <!-- WhatsApp Button --> up to the last </body>
    pattern = re.compile(r'<!-- WhatsApp Button -->.*?(?=</body>)', re.DOTALL)
    
    if pattern.search(content):
        # Remove the old button
        content = pattern.sub('', content)
    else:
        # If no button, maybe it's not there.
        pass

    # Step 2: Insert the new widget right before </body>
    if '</body>' in content:
        content = content.replace('</body>', whatsapp_widget + '\n</body>')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Injected into {filepath}")
    else:
        print(f"Warning: no </body> found in {filepath}")
