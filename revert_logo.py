import os
import glob

html_files = glob.glob('*.html')

old_img = '<img src="https://lh3.googleusercontent.com/aida/ADBb0uiIxQg7rRdhsxJxpp4FU0xknkhF7dMRQw7D_dDKkRD7SZtoVEOl3Xra6msEN-_cufI10aOUrl-9aYvmU3jjj6YLELvuS0GcNll60ynabEEk84nf1vsWGzFsrKItOsCunmm8DAxZ4VgZonQ1s_JdEZJU7u5Qo2BER-gAj4vNJ1VCrwqL9hpFnzWbYAzF9YfSsVgCl4KhTSzUp8vDkjbNtBzfgVZtDdG6xoAyuZv6PdbvME7j5j9Bqy-5S2JrKjFr0EYF7bFfEnYzY_o" alt="VISHUA SpA Logo" class="h-12 object-contain" />'

new_logo = '<div class="flex items-center gap-2"><div class="w-10 h-10 bg-secondary-container rounded-lg flex items-center justify-center shadow-lg"><span class="material-symbols-outlined text-white text-2xl font-bold" data-icon="security">security</span></div><span class="font-headline-md text-white tracking-widest uppercase text-xl">VISHUA<span class="text-secondary-container text-2xl">.</span></span></div>'

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    if new_logo in content:
        content = content.replace(new_logo, old_img)
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Reverted logo in {f}")
