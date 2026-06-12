import glob

html_files = glob.glob('*.html')
old_img = 'https://lh3.googleusercontent.com/aida/ADBb0uiIxQg7rRdhsxJxpp4FU0xknkhF7dMRQw7D_dDKkRD7SZtoVEOl3Xra6msEN-_cufI10aOUrl-9aYvmU3jjj6YLELvuS0GcNll60ynabEEk84nf1vsWGzFsrKItOsCunmm8DAxZ4VgZonQ1s_JdEZJU7u5Qo2BER-gAj4vNJ1VCrwqL9hpFnzWbYAzF9YfSsVgCl4KhTSzUp8vDkjbNtBzfgVZtDdG6xoAyuZv6PdbvME7j5j9Bqy-5S2JrKjFr0EYF7bFfEnYzY_o'
new_img = 'logo.png'

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    if old_img in content:
        content = content.replace(old_img, new_img)
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Updated logo path to logo.png in {f}")
