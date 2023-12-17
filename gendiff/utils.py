import json
from os import getcwd, path


def real_patch(file: str):
    if '/' in file:
        return file
    return path.join(getcwd(), file)


def generate_diff(path_file1, path_file2):
    json1 = json.loads(open(real_patch(path_file1)).read())
    json2 = json.loads(open(real_patch(path_file2)).read())
    keys = json1.keys() | json2.keys()
    result = {}
    for i in sorted(keys):
        if i in json1.keys() and i in json2.keys():
            if json1.get(i) == json2.get(i):
                result[i] = json1.get(i)
            else:
                result[f'- {i}'] = json1.get(i)
                result[f'+ {i}'] = json2.get(i)
        elif i in json1.keys():
            result[f'- {i}'] = json1.get(i)
        elif i in json2.keys():
            result[f'+ {i}'] = json2.get(i)
    print(str(json.dumps(result, indent=4)).replace('"', ''))
