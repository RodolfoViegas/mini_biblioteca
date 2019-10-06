# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 14:32:12 2019

@author: Rodolfo Viegas
"""

        

class NodusVP:
    '''classe que define o objeto nodo paras árvores vermelho-preto'''
    def __init__(self,chave=None,cor=None,pai=None,esquerda=None,direita=None):#retirando a mudança do prof.: de nihil para None
        self.cor = cor
        self.chave = chave
        self.pai = pai
        self.esquerda = esquerda
        self.direita = direita
    def __str__(self):
        if self.chave == int:
            return "%d" %(self.chave)
        elif self.chave == float:
            return "%f" %(self.chave)
        else:
            return "%s" %(self.chave)
        
    def getCor(self):
        return self.cor
    
    def getChave(self):
        return self.chave
    
    def getDireita(self):
        return self.direita
    
    def getPai(self):
        return self.pai
    
    def getEsquerda(self):
        return self.esquerda

    def setPai(self, pai):
        self.pai = pai
        
    def setEsquerda(self, esq):
        self.esquerda = esq
        
    def setDireita(self, direita):
        self.direita = direita
        
    def setChave(self,chave):
        self.chave = chave
    def setCor(self,cor):
        self.cor = cor
        
        
#-------------#-------------#----------------#----------------#-------
class ArvoreVP():
    '''Classe que cria o objeto árvore vermelho-preto'''
    def __init__(self):#retirei o parâmetro nihil
        self.nihil = NodusVP("preto",self,self,self)
        self.raiz = self.nihil
        
        
        
    def rb_inorder_tree_walk(self,x):#retirei o argumento raiz e joguei dentro o método atribuindo a x
        '''O argumento x é o atributo raiz da árvore. Este método retorna todas
        as chaves em ordem'''
        if x != self.nihil:
            self.rb_inorder_tree_walk(x.getEsquerda()) 
            print(x.chave)
            self.rb_inorder_tree_walk(x.getDireita())
            
            
            
    def rb_iterative_tree_search(self, chave):
        '''Método que realisa busca de um nódo através de sua chave(valor interno)
        como argumento.'''
        x = self.raiz
        while x != self.nihil and chave != x.getChave():
            if chave < x.getChave():
                x = x.getEsquerda()
            else:
                x = x.getDireita()
        return x
    
    def rb_minimum(self,x):
        '''Método que retorna o nódo com a menor chave da árvore, usando
        o atributo raiz como parâmetro.'''
        while x.getEsquerda() != self.nihil:
            x = x.getEsquerda()
        return x
    
    def rb_maximum(self,x):
        '''Método que retorna o nódo com a maior chave da árvore, usando
        o atributo raiz como parâmetro.'''
        if x == self.nihil:
            return self.nihil
        while x.getDireita() != self.nihil:
            x = x.getDireita()
        return x
    
    def rb_sucessor(self,x): 
        if x.getDireita() != self.nihil:
            return self.rb_minimum(x.getDireita()) # tirei tbm o x.direita do argumento e usei o get
        y = x.getPai()
        while y != self.nihil and x == y.getDireita():
            x = y
            y = y.getPai()
        return y
            
    def rb_predecessor(self,x): #lembrar de testar
        if x.getEsquerda() != self.nihil:
            return self.rb_maximum(x.getEsquerda())
        y = x.getPai()
        while y != self.nihil and x == y.getEsquerda():
            x = y
            y = y.getPai()
        return y
    
    def left_rotate(self,x):#prestar a atenção com as mundaças para getters e setters
        y = x.getDireita()
        x.setDireita(y.getEsquerda())#x.direita = y.esquerda
        if y.getEsquerda() != self.nihil:
            y.getEsquerda().setPai(x)#y.esquerda.pai = x
        y.setPai(x.getPai())#y.pai = x.pai
        if x.getPai() == self.nihil:
            self.raiz = y
        elif x == x.getPai().getEsquerda():
            x.getPai().setEsquerda(y)#x.pai.esquerda = y
        else:
            x.getPai().setDireita(y)#x.pai.direita = y
        y.setEsquerda(x)#y.esquerda = x
        x.setPai(y)#x.pai = y
        
    def right_rotate(self,x):
        y = x.getEsquerda()
        x.setEsquerda(y.getDireita())#x.esquerda = y.direita
        if y.getDireita() != self.nihil:
            y.getDireita().setPai(x)#y.direita.pai = x
        y.setPai(x.getPai())#y.pai = x.pai
        if x.getPai() == self.nihil:
            self.raiz = y
        elif x == x.getPai().getDireita():
            x.getPai().setDireita(y)#x.pai.direita = y
        else:
            x.getPai().setEsquerda(y)#x.pai.esquerda = y
        y.setDireita(x)#y.direita = x
        x.setPai(y)#x.pai = y
       
    def rb_insert_fixup(self, nodo):#alerta para as linhas 155 e 157, nodo recebe ou a chave do nodo? Por esquanto testado nodo
        while nodo.getPai().getCor() == "vermelho":
            if nodo.getPai() == nodo.getPai().getPai().getEsquerda():
                y = nodo.getPai().getPai().getDireita()
                if y.getCor() == "vermelho":
                    nodo.getPai().setCor("preto")#nodo.pai.cor = "preto"
                    y.setCor("preto")#y.cor = "preto"
                    nodo.getPai().getPai().setCor("vermelho")#nodo.pai.pai.cor = "vermelho"
                    nodo = nodo.getPai().getPai()
                elif nodo == nodo.getPai().getDireita():
                    nodo = nodo.getPai()
                    self.left_rotate(nodo)
                    nodo.getPai().setCor("preto") #nodo.pai.cor = "preto"
                    nodo.getPai().getPai().setCor("vermelho") #nodo.pai.pai.cor = "vermelho"
                    self.right_rotate(nodo.getPai().getPai())
            else:
                y = nodo.getPai().getPai().getEsquerda()
                if y.getCor() == "vermelho":
                    nodo.getPai().setCor("pretor")#nodo.pai.cor = "preto"
                    y.setCor("preto")#y.cor = "preto"
                    nodo.getPai().getPai().setCor("vermelho")#nodo.pai.pai.cor = "vermelho"
                    nodo = nodo.getPai().getPai()
                elif nodo == nodo.getPai().getEsquerda():
                    nodo = nodo.getPai()
                    self.right_rotate(nodo)
                    nodo.getPai().setCor("preto")#nodo.pai.cor = "preto"
                    nodo.getPai().getPai().setCor("vermelho")#nodo.pai.pai.cor = "vermelho"
                    self.left_rotate(nodo.getPai().getPai())
                    
        self.raiz.setCor("preto")#self.raiz.cor = "preto"
                    
        
    def rb_insert(self, nodo):
        y = self.nihil
        x = self.raiz
        while x != self.nihil:
            y = x
            if nodo.getChave() < x.getChave():
                x = x.getEsquerda()
            else:
                x = x.getDireita()
        nodo.setPai(y)#nodo.pai = y
        if y == self.nihil:
            self.raiz = nodo
        elif nodo.getChave() < y.getChave():
            y.setEsquerda(nodo)#y.esquerda = nodo
        else:
            y.setDireita(nodo)#y.direita =  nodo
        nodo.setEsquerda(self.nihil)#nodo.esquerda = self.nihil
        nodo.setDireita(self.nihil)#nodo.direita = self.nihil
        nodo.setCor("vermelho")#nodo.cor = "vermelho"
        self.rb_insert_fixup(nodo)
        
        
        
    def rb_transplant(self, u, v):
        if u.getPai() == self.nihil:
            self.raiz = v
        elif u == u.getPai().getEsquerda():
            u.getPai().setEsquerda(v)#u.pai.esquerda = v
        else:
            u.getPai().setDireita(v)#u.pai.direita = v
        v.setPai(u.getPai())#v.pai = u.pai
    

    def rb_delete_fixup(self,x):
        while x != self.raiz and x.getCor() == "preto":
            if x == x.getPai().getEsquerda():
                w = x.getPai().getDireita()
                if w.getCor() == "vermelho":
                    w.setCor("preto")#w.cor = "preto"
                    x.pai.cor = "vermelho"
                    self.left_rotate(x.getPai())
                    w = x.getPai().getDireita()
                if w.getEsquerda().getCor() == "preto" and w.getDireita().getCor() == "preto":
                    w.getCor("vermelho")#w.cor = "vermelho"
                    x = x.getPai()
                elif w.getDireta().getCor() == "preto":
                    w.getEsquerda().setCor("preto")#w.esquerda.cor = "preto"
                    w.setCor("vermelho")#w.cor = "vermelho"
                    self.right_rotate(w)
                    w = x.getPai().getDireta()
                    x.setCor(x.getPai.setCor())#w.cor = x.pai.cor
                    x.getPai().setCor("preto")#x.pai.cor = "preto"
                    w.getDireita().setCor("preto")#w.direita.cor = "preto"
                    self.left_rotate(x.getPai())
                    x = self.raiz
            else:
                w = x.getPai().getEsquerda()
                if w.getCor() == "vermelho":
                    w.setCor("preto")#w.cor = "preto"
                    x.getPai().setCor("vermelho")#x.pai.cor = "vermelho"
                    self.right_rotate(x.getPai())
                    w = x.getPai().getEsquerda()
                if w.getDireita().getCor() == "preto" and w.getEsquerda().getCor() == "preto":
                    w.setCor("vermelho")#w.cor = "vermelho"
                    x = x.getPai()
                elif w.getEsquerda().getCor() == "preto":
                    w.getDireita().setCor("preto")#w.direita.cor = "preto"
                    w.setCor("vermelho")#w.cor = "vermelho"
                    self.left_rotate(w)
                    w = x.getPai().getEsquerda()
                    w.setCor(x.getPai().getCor())#w.cor = x.pai.cor
                    x.getPai().setCor("preto")#x.pai.cor = "preto"
                    w.getEsquerda().setCor("pretor")#w.esquerda.cor = "preto"
                    self.right_rotate(x.getPai())
                    x = self.raiz 
        x.setCor("preto")#x.cor = "preto"
                    
                    
                    
    def rb_delete(self,nodo):
        y = nodo
        y_cor_original = y.getCor()
        if nodo.getEsquerda() == self.nihil:
            x = nodo.getDireita()
            self.rb_transplant(nodo,nodo.getDireita())
        elif nodo.getDireita() == self.nihil:
            x = nodo.getEsquerda()
            self.rb_transplant(nodo, nodo.getEsquerda())
        else:
            y = self.tree_minimum(nodo.getDireita())
            y_cor_original = y.getCor()
            x = y.getDireita()
            if y.getPai() == nodo:
                x.setPai(y)#x.pai = y
            else:
                self.rb_transplant(y,y.getDireita())
                y.setDireita(nodo.getDireita())#y.direita = nodo.direita
                y.getDireita().setPai(y)#y.direita.pai = y
            self.rb_transplant(nodo,y)
            y.setEsquerda(nodo.getEsquerda())#y.esquerda = nodo.esquerda
            y.getEsquerda().setPai(y)#y.esquerda.pai = y
            y.setCor(nodo.getCor())#y.cor = nodo.cor
        if y_cor_original == "preto":
            self.rb_delete_fixup(x)
            
            
            
            