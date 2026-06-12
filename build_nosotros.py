import os

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

parts = content.split('<main class="pt-[160px] md:pt-[120px]">')
header = parts[0]
rest = parts[1]

footer_parts = content.split('<!-- Footer -->\n')
footer = '<!-- Footer -->\n' + footer_parts[1]

nosotros_match = content.find('<!-- Why Choose Us -->')
services_match = content.find('<!-- Services Section -->')
nosotros_section = content[nosotros_match:services_match]

hero = """<section class="relative h-[400px] flex items-center overflow-hidden">
<div class="absolute inset-0 z-0">
<img class="w-full h-full object-cover grayscale brightness-[0.25]" data-alt="team of engineers in safety gear inspecting industrial site" src="https://lh3.googleusercontent.com/aida-public/AB6AXuAW7SDEs1jCfPyfMtDTD9fP3Zxvos8Pj8S3jUVbGTOG8-4PKMv9eyIZxK_YOTceDrDmy2jzwnFNjPr3MN2QKU6gXSS8fpPx8PTNZ4VET1O-fG1MoPYOFAVfrGXPLhajlZY-SQVPfnI6xwFOshtulkVLTCjQpSSkvDcZDy-U1v5NVC5ht4hIpJDwQfIxSCBMwcKCdAtTkGzS5as-0dEHZyQ8p55WGpAVXZaWW91KCDdjrreTk_lcv-G1gCc8eM1kULzP17k5eh1NlMP6"/>
<div class="absolute inset-0 bg-gradient-to-r from-primary-container/90 to-transparent"></div>
</div>
<div class="relative z-10 max-w-[1280px] mx-auto px-8 w-full">
<div class="max-w-2xl border-l-4 border-tertiary-fixed-dim pl-8">
<span class="font-label-md text-label-md text-tertiary-fixed-dim uppercase tracking-widest block mb-4">Sobre Nosotros</span>
<h1 class="font-headline-xl text-headline-xl text-white mb-6">Conoce a VISHUA SpA</h1>
<p class="font-body-lg text-body-lg text-slate-300">Líderes en prevención de riesgos, comprometidos con la seguridad industrial y el bienestar de las personas.</p>
</div>
</div>
</section>
"""

nosotros_html = header + '<main class="pt-[160px] md:pt-[120px]">\n' + hero + nosotros_section + '</main>\n' + footer

with open('nosotros.html', 'w', encoding='utf-8') as f:
    f.write(nosotros_html)
print('Created nosotros.html')
