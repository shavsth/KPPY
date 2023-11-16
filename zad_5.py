import json
#from functools import reduce

#def source_update(a, value):
#    if 'source' in a and a['source'].find("### Ćwiczenie") == 0:
#        value['outputs'] = "[]"
#    return value

def ipynbErase(file_name):
    file_name = file_name if ".ipynb" not in file_name else file_name.replace(".ipynb","")

    file = open(file_name + ".ipynb", "rb")
    dane = json.load(file)

    dane['cells'] = list(map(lambda value: value.update({'outputs': "[]"}) or value, dane['cells']))
    #dane['cells'] = reduce(source_update, dane['cells'], {})

    file.close()

    file2_text = json.dumps(dane)

    file2 = open(file_name + ".czysty.ipynb", "w")
    file2.write(file2_text)

    return file_name + ".czysty.ipynb"

f = input("Nazwa pliku .ipynb do oczyszczenia >> ")

print("Czysty plik {} utworzony.".format(ipynbErase(f)))
