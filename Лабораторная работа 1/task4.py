import json

INPUT_FILE = "input.csv"

def csv_to_list_dict(filename) -> list[dict]:
    konv_a = []
    konv_b = []
    with open(filename, 'r') as f:
        res = f.readlines()
        headers = res[0].rstrip().split(sep=',')
        for row in res[1:]:
            konv_b.append(row.rstrip().split(sep=','))
        for element in konv_b:
            a = {k:v for k, v in zip(headers, element)}
            konv_a.append(a)

    return konv_a

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
