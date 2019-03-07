# coding: utf-8
import Produtos
import  json

class DataBase():
    '''Função que cria e retorna um objeto do tipo Produto, para os produtos que estão com sua quantidade corrompida,
    dessa forma a própria classe 'Products' define sua quantidade como 0, resolvendo assim o problemas das quantidades'''
    def CreateProduct(self,obj):
        instancia = Produtos.Products(
          id = obj['id'],
          name= obj['name'],
          price = obj['price'],
          category=obj['category'],

         )
        return instancia

    '''Função que cria e retorna um objeto do tipo Produto, utilizando todos os dados recebidos do Arquivos Json'''
    def CreateProductQuantity(self,obj):
        instancia = Produtos.Products(
          id = obj['id'],
          name= obj['name'],
          quantity=obj['quantity'],
          price = obj['price'],
          category=obj['category'],

         )
        return instancia

    '''Função que recebe os dados do arquivo 'broken-database.json' e retorna uma lista de produtos com todos seus dados 
     ja definidos'''
    def GetList(self):
        list = []
        try:
            arquivo_json = open('broken-database.json', 'r', encoding="utf8")
            dados_json = json.load(arquivo_json)
            arquivo_json.close()

            for i in dados_json:
                if "quantity" in i:
                    list.append(DataBase.CreateProductQuantity(DataBase,i))
                else:
                    list.append(DataBase.CreateProduct(DataBase,i))
            return list
        except Exception as erro:
            print("Occoreu um erro ao carregar o arquivo.")
            print("O erro é : {}".format(erro))

    '''Função que recebe uma lista de produtos, e escreve e salva seus dados em um arquivo Json chamado
     'Fixed-DataBase.json' '''
    def SaveDataBase(self,list):
        listSave=[
            dict(id=obj.id, name=obj.name,quantity=obj.quantity,price=obj.price,category=obj.category)
            for obj in list
        ]
        listSave=json.dumps(listSave, indent=4, sort_keys=False,ensure_ascii=False).encode('utf8')
        try:
            data=open("fixed-database.json",'wb')
            data.write(listSave)
            data.close()
        except Exception as erro:
            print("Occoreu um erro ao carregar o arquivo.")
            print("O erro é : {}".format(erro))

    '''Função que recebe os dados do arquivo com todos os porblemas corrigidos 'fixed-database.json' e retorna uma 
    lista de produtos com todos seus dados ja definidos'''
    def GetDatabase(self):
        list = []
        try:
            arquivo_json = open('fixed-database.json', 'r', encoding="utf8")
            dados_json = json.load(arquivo_json)
            arquivo_json.close()
            for i in dados_json:
                list.append(DataBase.CreateProductQuantity(DataBase, i))
            return list
        except Exception as erro:
            print("Occoreu um erro ao carregar o arquivo.")
            print("O erro é : {}".format(erro))