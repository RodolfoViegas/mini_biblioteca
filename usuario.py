# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 17:24:38 2019

@author: Rodolfo Viegas 
Classe Usuário. Nodo de uma árvore vermelho-preto específica
"""
from arvore_VP2 import NodusVP

class Usuario(NodusVP):
    def __init__(self,cpf,nome,reserva="não",num_empréstimos=0,multa=0,livros=[]):
        NodusVP.__init__(self, chave=None)
        self.chave = cpf#número de cpf como chave para identificar o usuário.
        self.nome = nome
        self.num_emp = num_empréstimos#máximo de dois por empréstimo.
        self.multa = multa
        self.livros = livros#lista com o nome dos livros.
        self.reserva = reserva#sim ou não, podendo somente reservar um livro.
        
    def getCPF(self):
        return self.chave
    def getNome(self):
        return self.nome 
    def getNumEmp(self):
        return self.num_emp 
    def getMulta(self):
        return self.multa
    def getLivros(self):
        return self.livros
    def getReserva(self):
        return self.reserva
    
    def setCPF(self,cpf):
        self.chave = cpf
    def setNome(self,nome):
        self.nome = nome 
    def setNumEmp(self,num_emp):
        self.num_emp = num_emp
    def setMulta(self, multa):
        self.multa = multa
    def setLivros(self,livro):
        self.livros = livro
    def setReserva(self,reserva):
        self.reserva = reserva
    
    def add_livro(self,livro):
        if len(self.livros) == 3:
            return "máximo de livros emprestados"
        else:
            self.livros.append(livro)
        
    def remove_livro(self,num):
        '''se add um livro a lista livros, mudar na árvore livros o status do livro para
        para disponível. Uma função no arqui biblioteca
        que irá operacionalizar chamando esse método(com o nome do objeto usuario) e chamando
        um outro método que muda o status com o nome do livro'''
        if len(self.getLivros()) == 3:
                if num == 1:
                    del self.livros[0]
                elif num == 2:
                    del self.livros[1]
                elif num == 3:
                    del self.livros[2]
                else:
                    print("número errado")
                
        elif len(self.getLivros()) == 2:
                if num == 1:
                    del self.livros[0]
                elif num == 2:
                    del self.livros[1]
                else:
                    print("número errado")
        elif len(self.getLivros()) == 1: 
                if num == 1:
                    del self.livros[0]
                else:
                    print("número errado")
        elif len(self.getLivros()) == 0: 
                print("sem livros em posse")
        
        else:
            print("número errado")
        
            