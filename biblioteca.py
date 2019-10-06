# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 16:48:08 2019

@author: Rodolfo Viegas de Albuquerque
Disciplina: Algoritmos e Estrutura de Dados
Projeto: Biblioteca: verificando livros
"""
from arvore_VP2 import ArvoreVP
from usuario import Usuario
from livro import Livro

arvore_usuarios = ArvoreVP()
arvore_livros = ArvoreVP()


def cadastra_livro(livro):
    if arvore_livros.rb_iterative_tree_search(livro) == livro:
            print("livro encontrado")
    else:
        nome=input("Nome do livro: ")
        autor = input("Nome do autor: ")
        livro = Livro(nome, autor)
        arvore_livros.rb_insert(livro)
        

def cadastra_usuario(cpf):
    if arvore_usuarios.rb_iterative_tree_search(cpf) == cpf:
        print("usuario já cadastrado")
    else:
        cpf=input("Nome do livro: ")
        nome = input("Nome do autor: ")
        usuario = Usuario(cpf,nome)
        arvore_livros.rb_insert(usuario)
        
        
def busca_usuario(cpf):
    if arvore_usuarios.rb_iterative_tree_search(cpf) == cpf:
        print("usuario encontrado")
    x = input("Deseja realizar o cadastro? Digite sim para cadastrar ou não para encerrar")
    if x == "sim":
        cadastra_usuario(cpf)
    else:
        print("fim de busca")
        
        

def busca_livro(livro,usuario):#mexer tbm no objeto usuário
        if arvore_livros.rb_iterative_tree_search(livro) == livro:
            print("livro encontrado")
            if livro.getStatus() == "disponível":
                x = int(input("digite 1 para empréstimo ou outro número para cancelar: "))
                if len(usuario.getLivros) == 3:
                    print("Usuário com total de livros emprestados")
                    e = input("Vai devolver algum livros? Digite sim para devolver ou não para encerrar: ")
                    if e == "sim":
                        for i,j in enumerate(usuario.getLivros):
                            print("Número%d\tlivro: %s"%(i+1,j))
                        dev=int(input("Digite o número que corresponde ao livro: "))
                        usuario.remove_livro(dev)#parei em remover, mudar o status do livro
                if x == 1:
                    livro.setStatus(1)
                    #coisas para mexer no usuário
                else:
                    print("consulta encerrada")
            elif livro.getStatus() == "emprestado":
                x = int(input("digite 2 para reservar ou 0 para devolver ou outro número para cancelar: "))
                if x == 2:
                    livro.setStatus(2)
                    #coisas para mexer no usuário
                elif x == 0:
                    livro.setStatus(0)
                    #coisas para mexer no usuário
                else:
                    print("consulta encerrada")
            else:
                print("livro reservado")
                
              
            
        
        

print("Bem-vindo à Biblioteca AED")
x = int(input("Operações para usuários digite 1.Para funcionários digite 2"))
if (x != 1) or (x != 2):
    while (x != 1) or (x!= 2):
        x = int(input("Operações para usuários digite 1.Para funcionários digite 2. Para sair 0 "))
        


print("nada")
    

 
