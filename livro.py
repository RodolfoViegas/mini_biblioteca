# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 22:37:09 2019

@author: Rodolfo Viegas

Classe livro
"""
from arvore_VP2 import NodusVP

class Livro(NodusVP):
    def __init__(self, nome, autor):
        NodusVP.__init__(self,chave=None)
        self.chave = nome
        self.autor = autor
        self.status = "disponível"#3 tipos: disponível, emprestado e reservado

    def getAutor(self):
        return self.autor
    def getStatus(self):
        return self.status
    def setAutor(self, autor):
        self.autor = autor
    def setStatus(self,status):
        self.status = status
    
    def muda_status(self,num):#decidir se essa função fica aqui, como método, ou vai para a biblioteca
        '''função que muda o status do livro(chama o setLivros) para: disponível(default),
        emprestado e reservado'''
        if num == 0:
            self.setStatus("disponível")
        elif num == 1:
            self.setStatus("emprestado")
        elif num == 2:
            self.setStatus("reservado")
        else:
            print("operação errada")
    
        
        
        
        
        
        
    
    