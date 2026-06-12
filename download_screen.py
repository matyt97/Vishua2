import urllib.request

url = "https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ8Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpbCiVodG1sX2JjNTg0Yzg0NzRmNTQyNTFiZTZiNjlkYzMzYzYwNGMwEgsSBxCtusjk2RcYAZIBJAoKcHJvamVjdF9pZBIWQhQxMTUzMzE1MDEyMjQ2ODQ0NzI2Nw&filename=&opi=89354086"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as response:
        html_content = response.read().decode('utf-8')
    with open('clientes_y_distribuidores.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("Downloaded successfully.")
except Exception as e:
    print(f"Error: {e}")
