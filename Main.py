# coding: utf-8
import Data
import Produtos


'''Lista que vai receber produtos que viram da função GetList da classe DataBase'''
products=Data.DataBase.GetList(Data)

'''Lista de produtos chama a função fix name de Products,passando ela propria por parametro,recebendo como retorno uma 
lista com todos os nomes dos produtos corrigidos'''
products=Produtos.Products.FixName(Produtos,products)

'''Lista de produtos chama a função fix price de Products,passando ela propria por parametro,recebendo como retorno uma 
lista com todos os preços dos produtos corrigidos'''
products=Produtos.Products.FixPrice(Produtos,products)

'''Fazendo a chamada da função SaveDataBase da classe database,e passando por parametro a lista de produtos já com todos os problemas
corrigidos'''
Data.DataBase.SaveDataBase(Data,products)

'''Lista database chama a função GetDataBase da classe DataBase para receber os objetos da lista corrigida '''
database=Data.DataBase.GetDatabase(Data)

'''Fazendo a chamada da função Sort da classe products que recebe uma lista de produtos e retorna uma lista ordenada de 
 acordo com as especificações'''
Produtos.Products.Sort(Produtos,database)

'''Dicionario Stored faz chamada da função Stock da classe products,que recebe uma lista de produtos e retorna um dicionario
 com o valor total do estoque divido por categoria'''
Stored=Produtos.Products.Stock(Produtos,database)

'''Saida das validações'''
print("\nValidação 1: Prdoutos ordenados por ordem alfabetica de categoria, e depois por Id")
print(database)
print("\nValidação 2: Valor total do estoque por categoria")
print(Stored)
input()