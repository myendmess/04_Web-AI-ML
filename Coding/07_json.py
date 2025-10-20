import json

json_string = "{\"nome\": \"Luca\", \"cognome\": \"Rossi\", \"eta\": 20, \"corsi\": [\"Matematica\", \"Informatica\", \"Storia\"]}"
print(json_string)
json_parsed = json.loads(json_string)
edited_json_string = json.dumps(json_parsed, indent=4)
#formatted_info = f'nome: {json_parsed["nome"]}\ncognome: {json_parsed["cognome"]}\neta: {json_parsed["eta"]}\ncorsi: {json_parsed["corsi"]}'
print(edited_json_string)
#print(formatted_info)
print(f'''nome: {json_parsed["nome"]}
cognome: {json_parsed["cognome"]}
eta: {json_parsed["eta"]}
corsi: {json_parsed["corsi"]}''')
