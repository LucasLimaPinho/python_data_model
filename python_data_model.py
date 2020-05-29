import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# "Fluent Python de Luciano Ramanho (O'Reilly). Copyrigh 2015 Luciano Ramanho, 
# 978-1-491-94600-8
# Desempacotadores de tuplas e descritores são específicos de Python.
# Esses são alguns exemplos de especificidade da linguagem para se obter 
# fluência.
# O interpretador Python chama métodos especiais para realizar operações 
# básicas em objetosm geralmente acionados por uma sintaze especial. 
# Os nomes dos m[étodos especiais são sempre escritos com underscores diplos no
# início e no fim (ou seja, __getitem__)

# dunder methods _> under_under methods -> magic methods -> métodos especiais

# Alguns métotodos especiais (dunder methods): __getitem__ e __len__
import collections
Card = collections.namedtuple('Card', ['rank','suit'])

# namedtuple pode ser utilizada para criar classes de objetos que sejam
# apenas grupos de atributos
# sem métodos próprios, como um registro de banco de dados. 
class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank,suit) for suit in self.suits
                      for rank in self.ranks]
    def __len__(self):
        return len(self._cards)
    def __getitem__(self,position):
        return self._cards[position]

beer_card = Card('7','diamonds')
beer_card
deck = FrenchDeck()
len(deck) # método especial (dunder method) -> __len__
deck[0] # método especial (dunder method) -> __getitem__
deck[-1] # devolve última posição

from random import choice 
choice (deck)

deck[:3]
deck[12::13] #escolher somente os ases iniciando no índice 12 e avançando 13 cartas de cada vez

for card in deck:
    print(card)

for card in reversed(deck):
    print(card)
    
# Collections in Python are containers that are used to store
# collections of data, for example, list, dict, set, tuple etc.
# Cada item de um dicionário em python possui um KVP - Key Value Pair.
    
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high):
    print(card)

# Os métodos especiais foram criados para serem chamados pelo interpretador
# Python e não por você    
    
# Normalmente, seu código não deverá ter muitas chamadas diretas a 
# métodos especiais (dunder methods), a menos que você esteja usando bastante
# metaprogramação

# O único méotdo especial chamado frequentemente de forma direta pelo usuário
# de forma direta pelo usuário é __init__ para provocar o iniciarlizador
# da superclasse quando você implementa seu próprio __init__
    
# A utilização de funções embutidas que invocam o método especial correspondente
# costumam ser bem mais rápidas do que a utilização de métodos. 
# evite criar atributos arbitrários personalizados com a sintaxe _foo_,
# pois esses nomes poderão adquirir significados especiais no futuro,
# mesmo se não estiverem  em uso atualmente.

# Calculano o valor absoluto de um número complexo e sua soma "Normal"
from math import hypot

class Vector:
    def __init__(self, x=0,y=0):
        self.x = x
        self.y = y
    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)
    def __abs__(self):
        return hypot(self.x, self.y)
    def __bool__(self):
        return bool(abs(self))
    def __add__(self,other):
        x= self.x + other.x
        y= self.y + other.y
        return Vector(x,y)
    def __mul__(self,scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
v1 = Vector(2,3)
v2 = Vector(1,1)
v3 = v1 + v2
v4 = abs(v1+v2)
v1
v2
v3
v4

# O método especial __repr__ é chamado pela função embutida repr para obtermos
# representação em string do objeto para inspeção.
# Se __repr__ não for implementado, as instâncias dos verores serão exibidas
# no console como <Vector object at 0x10e100070>
