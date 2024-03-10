import json
from flask import Flask 
from flask_restful import Api, Resource

# FLASK RESTFUL
app = Flask(__name__)
api = Api(app)

# FUNCOES
# ler arquivo
# escrever arquivo


class Get(Resource):

    def get(self):
        try:
            # LE O ARQUIVO JSON
            data_r = open('data.json', 'r')  # ABRE O ARQUIVO PARA LEITURA (r)
            data = json.loads(data_r.read())
            data_r.close()  # FECHA O ARQUIVO
            return data
        except:
            return json({"deuerro":" :* "})

class Post(Resource):
    # POST SERVE COMO UPDATE POIS DIC PYTHON NAO PERMITE CHAVES DUPLICADAS
    def post(self, chave, valor):
        try:
            # SALVA O CONTEUDO DO ARQUIVO JSON #
            data_r = open("data.json", "r")  # ABRE O ARQUIVO JSON LEITURA (r)
            dic = json.loads(data_r.read())  # LE O CONTEUDO
            data_r.close()  # FECHA O ARQUIVO JSON
            dic[chave] = valor # ATUALiZA O DICIONARIO

            # RE-ESCREVE O ARQUIVO JSON #

            data_w = open("data.json", "w")  # ABRIR O ARQUIVO JSON ESCRITA (W)
            # ABRIR COM O ARGUMENTO DE ESCRITA (w) APAGA O CONTEUDO ATUAL
            # E ESCREVE O CONTEUDO NOVO POR CIMA
            json.dump(dic, data_w)  # ESCREVE O CONTEUDO
            data_w.close()  # FECHA O ARQUIVO JSON
            return True
        except:
            return False

class Delete(Resource):

    def delete(self, chave):
        try:
            # SALVA O CONTEUDO DO ARQUIVO JSON #
            data_r = open("data.json", "r")  # ABRE O ARQUIVO JSON LEITURA (r)
            dic = json.loads(data_r.read())  # LE O CONTEUDO
            data_r.close()  # FECHA O ARQUIVO JSON
            if chave in dic:
                print("ENTROU NO IF")
                for i in dic:
                    print(i)
                del dic[chave]
                # RE-ESCREVE O ARQUIVO JSON #
                data_w = open("data.json", "w")  # ABRIR O ARQUIVO JSON ESCRITA (W)
                # ABRIR COM O ARGUMENTO DE ESCRITA (w) APAGA O CONTEUDO ATUAL
                # E ESCREVE O CONTEUDO NOVO POR CIMA
                json.dump(dic, data_w)  # ESCREVE O CONTEUDO
                data_w.close()  # FECHA O ARQUIVO JSON
                return True
            else:
                return False
        except:
            return False

api.add_resource(Get, "/get")
api.add_resource(Post, "/post/<chave>,<valor>")
api.add_resource(Delete, "/delete/<chave>")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)