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
