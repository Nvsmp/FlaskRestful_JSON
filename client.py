import requests, json

def pergunta():
    return input("###############\n[0] EXIT \n[1] Get\n[2] Post\n[3] Delete\n###############\nOPCAO : ")

r = pergunta()

while( r != "0"):
    if r == "1":
        print(f"##### GET #####")
        response = requests.get("http://0.0.0.0:8080/get").json()
        chaves = response.keys()
        for chave in chaves:
            print(f"{chave} : {response[chave]}")
    elif r == "2":
        print(f"## POST/UPDATE ##")
        chave = input("CHAVE : ")
        valor = input("VALOR : ")
        response = requests.post(f"http://localhost:8080/post/{chave},{valor}")
        print(f" ### { str(response.text.upper()) } ###")

    elif r == "3":
        print(f"#### DELETE ####")
        chave = input("CHAVE : ")
        response = requests.delete(f"http://127.0.0.1:8080/delete/{chave}")
        print(f" ### {response.text.upper()} ###")
        

    r = pergunta()