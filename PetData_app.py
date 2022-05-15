from math import inf
import random

lista_nome_cachorros = []
lista_nome_gatos = []
lista_numeros_cachorros = []
lista_numeros_gatos = []


class cachorro:

  def __init__(self,nome_cachorro):
    if nome_cachorro not in lista_nome_cachorros:
      self.nome_cachorro = nome_cachorro
      lista_nome_cachorros.append(self.nome_cachorro)
    else:
      print("Já existe um cachorro com esse nome")
    while True:
      numero_dog = random.randint(1,100)
      if numero_dog not in lista_numeros_cachorros:
        self.numero_dog = numero_dog
        lista_numeros_cachorros.append(self.numero_dog)
        break
      else:
        continue
    
  def latir(self):
    latir = ("O {} está latindo, au au au!".format(self.nome_cachorro))
    return latir
    
    
  def __str__(self):
    return "o nome do seu cachorro é {} e o numero de registro dele é {}".format(self.nome_cachorro,self.numero_dog)
 
class gato:

  def __init__(self,nome_gato):
    if nome_gato not in lista_nome_gatos:
      self.nome_gato = nome_gato
      lista_nome_gatos.append(self.nome_gato)
    else:
      print("Já existe um gato com esse nome")
    while True:
      numero_cat = random.randint(1,100)
      if numero_cat not in lista_numeros_gatos:
        self.numero_cat = numero_cat
        lista_numeros_gatos.append(self.numero_cat)
        break
      else:
        continue

  def miar(self):
    miar = ("O gato {} está miando, miau miau miau!".format(self.nome_gato))
    return miar

  def __str__(self):
      return "o nome do seu gato é {} e o numero de registro dele(a) é {}".format(self.nome_gato,self.numero_cat)


print("Bem vindo ao PetData \n\n")

while True:
  prox_açao = input("Você deseja adicionar um animal :")
  if prox_açao.lower() == "sim":
    while True:
      tipo_animal = input("Qual tipo do seu animal, gato ou cachorro?  ")
      if tipo_animal.lower() in "cachorro" or "gato":
        break
      else:
        continue
    if tipo_animal.lower() in  "cachorro":
      nome_cachorro = input("Qual o nome do seu cachorro? ")
      cachorro_1 = cachorro(nome_cachorro)
      print(cachorro_1)
      print(cachorro_1.latir())

    elif tipo_animal.lower() in "gato":
      nome_gato = input("Qual o nome do seu gato? ")
      gato_1 = gato(nome_gato)
      print(gato_1)
      print(gato_1.miar())
    continue

  else:
    break

print("Lista de Cachorros")
for i,e in zip(lista_nome_cachorros,lista_numeros_cachorros):
  print("Nome: {} Número: {}".format(i.capitalize(),e))

print("Lista de Gatos")
for i,e in zip(lista_nome_gatos,lista_numeros_gatos):
  print("Nome: {} Número: {}".format(i.capitalize(),e))
