# coding: utf-8
import operator
from operator import attrgetter
class Products():



    '''Construtor da classe'''
    def __init__(self,id="",name="",quantity=0,price=0,category=""):
        super(Products,self).__init__()
        self.id=id
        self.name=name
        self.price=price
        self.category=category
        self.quantity=quantity

    def __repr__(self):
        return "\nID={} | NAME={} | QUANTITY={} | PRICE={} | CATEGORY={}".format(self.id,self.name,self.quantity,self.price,self.category)

    '''Função que recebe uma lista de produtos e para cada produto altera os caracteres corrompidos por caracteres normais e 
    retorna uma lista de produtos com nomes corrigidos, resolvendo assim o problema dos nomes corrompidos'''
    def FixName(self, list):
        for i in list:

            i.name = i.name.replace("æ", "a")
            i.name = i.name.replace("¢", "c")
            i.name = i.name.replace("ø", "o")
            i.name = i.name.replace("ß", "b")
        return list

    '''Função que recebe uma lista de produtos , e para cada produto verifica se o preço dele é uma string, caso seja, 
    ela converte ele para um number e ,caso contrario ele apenas mantem o antigo valor,e no fim retorna uma lista com 
    o preço de todos os produtos corrigidos,resolvendo assim o problemas dos preços corrompidos'''
    def FixPrice(self, list):
        for i in list:

            if(isinstance(i.price,str)):
                i.price= float(i.price)
                i.price=round(i.price,2)
        return list

    '''Função que recebe um lista de objetos e ordena eles por ordem alfabetica de categoria, e depois por Id'''
    def Sort(self,list):
        list.sort(key=attrgetter('category','id'))
        return list

    '''Função que recebe uma lista de produtos, cria um dicionario com todas as categorias , calcula o valor total do 
    estoque por categoria e retorna um dicionario com esses dados '''
    def Stock(self,list):
        stock={}
        for i in list:
            if i.category in stock:
                if i.quantity > 0:
                    soma = stock[i.category] + (i.price * i.quantity)
                else:
                    soma = stock[i.category] + i.price
                soma = round(soma, 2)
                stock[i.category] = soma
            else:
                if i.quantity > 0:
                    soma = i.price * i.quantity
                    soma = round(soma, 2)
                    stock[i.category] = soma
                else:
                    stock[i.category] = i.price
        return  stock