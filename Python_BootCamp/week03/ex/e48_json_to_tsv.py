import json
import csv
import os
def json_to_tsv(Json, Tsv):
    if os.path.exists(Json):
        with open(Json) as f:
            j = json.load(f)
            with open(Tsv, 'w') as output_file:
                dw = csv.DictWriter(output_file, j[0], delimiter = '\t')
                dw.writeheader()
                dw.writerows(j)
                return 1
    else:
        return -1
json_to_tsv('example.json', 'example.tsv')
