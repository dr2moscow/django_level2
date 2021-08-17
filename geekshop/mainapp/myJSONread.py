# Читаем json-файл в python
import json
import pathlib

print(pathlib.Path.cwd())

with open('templates/mainapp/json/categories.json', encoding='utf-8') as json_file:
    data = json.load(json_file)
    print(data)



