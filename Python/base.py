# ===================================================
"""Saída e entrada de dados - 10/04/2026"""

# ===================================================
"""
print("olá mundo")

fruta = "banana"
tipo = "Bolão de "
print(tipo + fruta)

print("Repetição" * 6)

nome = "Najones"
print(nome * 3)

print(nome + "ricaço" * 3)

print(f"Olá, {nome} !")  # f-string

print("O tipo é:", type(nome))  # O tipo é: <class 'str'>
print("Listagem de:", dir(nome))  # [analogia] o dir te mostra todos os botões do rádio.
help(
    str
)  # [analogia] O help(str) é o manual que te ensina o que acontece quando você aperta cada botão.

cor = "#8750f7"
print(type(cor))  # <class 'str'>

"""
# ===================================================
""" Operadores matemáticos e lógicos - 10/04/2026"""
# ===================================================

"""
#----------------------------------------------------Operador de indexação
school = "Luther College"
third_position = school[2]
last_position = school[-1]
print("The third position is", third_position) # The third position is t
print("The last position is", last_position) #The last position is e

#----------------------------------------------------Indexação e Slicing
my_namez = 'Henrique Nagy Martins'
print(my_namez[2:]) #nrique Nagy Martins - (pula os dois primeiros)
print(my_namez[:3]) #Hen - (pega do 0 ao 2)
print(my_namez[0:3]) #Hen - (Mesma coisa do de cima)
print(my_namez[::-1]) #snitraM ygaN euqirneH - (Inverter uma lista ou palavra)
print(my_namez[2:-2:2]) #niu ayMri - (Corta os 2 primeiros, tira os 2 últimos e pega de 2 em 2)
"""

# ===================================================
""" Listas e dicionários - 13/04/2026"""
# ===================================================
"""
# Operações profissionais com números
precos = [27.66, 29, 17, 11.23, 9.22, 10, 17, 4, 11, 54, 67, 17]

print(sum(precos))   # Soma tudo: 274.11
print(len(precos))   # Total de itens: 12
print(precos.count(17)) # Quantas vezes tem o 17: 3

# Organização
print(sorted(precos)) # Mostra organizado, mas não altera a lista original
precos.sort()         # Altera a lista precos definitivamente para organizada

# Valores extremos
print(min(precos)) # 4
print(max(precos)) # 67

# Inverter posições manualmente (Ex: trocar o primeiro pelo último)
precos[0], precos[-1] = precos[-1], precos[0]

# Cópia de segurança
lista_a = [1, 2, 3]
lista_b = lista_a        # Se mudar a, muda b (elas estão ligadas)
lista_c = lista_a.copy() # Cópia independente. Se mudar a, c continua igual

# ---------------------------------------Gerenciando itens (Ex: Lista de Apóstolos)
apostolos = ["pedro", "andre", "filipe", "tiago", "judas"]

# Busca e Condição
if "judas" in apostolos:
    print("Encontrado na lista")

# Alterações
apostolos.remove("judas")    # Remove pelo nome exato
apostolos.append("matias")   # Adiciona no fim da fila
apostolos.insert(2, "joão")  # Entra na posição 2 e empurra o resto pra direita

# Limpeza
item_removido = apostolos.pop() # Tira o último da lista e te entrega o valor
apostolos.clear()               # Apaga tudo, deixa a lista vazia []

#---------------------------------------------------- Dicionário/Objeto
customers = {"name":"john","id:":1,"registered":"november"}
getCustomerData = customers["registered"] #Acessar item do objeto/Dicionário
print(getCustomerData) #november
"""
# ===================================================
""" Estrutura condicional (If, Elif, Else) - 14/04/2026 """
# ===================================================
"""
position = "Webdesigner"
correct_password = True

if position == "admin" and correct_password:
    print("Server total access granted")
elif position == "Webdesigner" and correct_password:
    print("Editor mode only granted")  # Editor mode only granted - Vai parar aqui !!!!!
elif not correct_password:
    print("incorrect password, account suspended")
else:
    print("Visitor with no special permissions")

# ---------------------------------------------------- If em uma linha só (Operador ternário)
age = 18
# Variavel = "Valor se True" if (condição) else "Valor se False"
status = "Of legal age" if age >= 18 else "You are not 18"
print(status)  # Of legal age

# ---------------------------------------------------- Verificação direta (Truthy e falsy)
name = ""
shopping_cart = []

# MÉTODO DE PEBA INICIANTE RUINZÃO
if len(shopping_cart) == 0:
    print("Empty cart")

# MÉTODO LENDÁRIO - CHECANDO CARRINHO E NOME
if not shopping_cart:
    print("Empty cart - buy something")

if name:
    print(f"Hello {name}")
else:
    print("Please, input your name: ")

# ---------------------------------------------------- MATCH CASE
command = "delete"
match command:
    case "save":
        print("File saved successfully")
    case "delete":
        print("File sent to the trash")  # Vai parar aqui !!!!!
    case "edit":
        print("Edition mode opened")
    case _:  # Esse underline funciona exatamente como o else
        print("Command not recognized")

# ---------------------------------------------------- OPERADOR IN
cargos_chefia = ["admin", "diretor", "gerente"]
position = "gerente"

if position in cargos_chefia:
    print("Acesso total liberado para diretoria")
else:
    print("Acesso negado!")

# ---------------------------------------------------- PASS
senha = True
if senha:
    pass  # O sistema passa reto por aqui sem dar erro, e depois você escreve a lógica
else:
    print("Senha incorreta")
"""

# ===================================================
""" Laços de repetição (loops) - 15/04/2026 """
# ===================================================
"""
# ---------------------------------------------------- FOR IN
for i in range(5):
    print(i)  # 0 1 2 3 4 (sendo um em cada linha)

# Conta de 2 em 2, parando antes do 10
for numero in range(0, 10, 2):
    print(numero)  # 0, 2, 4, 6, 8

cores = ["black", "red", "green", "toranja"]
for cor in cores:
    print(cor)  # black red green toranja (sendo um em cada linha)

users = ["Rebecca", "Daniele", "Estelas", "Esther"]
for eachUser in users:
    print(f"Welcome e-mail to {eachUser}")  # Welcome e-mail to Rebecca and so on....


# ---------------------------------------------------- ENUMERATE
pages = ["home", "about us", "contact", "blog"]
# o start=1 faz o nº começar no 1 em vez do 0
for position, pageName in enumerate(pages, start=1):
    print(
        f"Menu {position}: {pageName}"
    )  # Menu 1: home  Menu 2: about us Menu 3: contact Menu 4: blog

# ---------------------------------------------------- BREAK CONTINUE
# Usando o break para economizar processamento
passwordz = ["231", "admin", "20haha26"]
for item in passwordz:
    if item == "admin":
        print(
            f"{item} = Pass found, stop searching"
        )  # admin = Pass found, stop searching
        break

# Usando continue para limpar dados ruins
prices = [10.90, 0, 25, 29.90, 0, 15]
for item in prices:
    if item == 0:
        continue  # Ignora o zero e vai para o próximo
    print(
        f"Proceed to pay USD $ {item}"
    )  # Proceed to pay USD $ 10.9 Proceed to pay USD $ 25 Proceed to pay USD $ 29.9 Proceed to pay USD $ 15

# ---------------------------------------------------- Compreensão de listas
valores = [10, 20, 30]
# Cria uma lista nova somando 5 em cada valor
valores_com_taxa = [valor + 5 for valor in valores]
print(valores_com_taxa)  # [15, 25, 35]
"""

# ===================================================
""" Módulos - 16/04/2026 """
# ===================================================
"""
import math

print(math.sqrt(9))  # Raiz quadrada do 9 = 3.0
print(math.floor(3.9))  # Arredonda para baixo = 3

from random import choice, randint

sorteio = ["joão", "maria", "felipe"]
print(choice(sorteio))  # Escolhe um item aleatório da sua lista
print(randint(1, 10))  # Sorteia um nº de 1 a 10

import datetime as dt

hoje = dt.date.today()
print(f"A data de hoje é {hoje}")  # A data de hoje é 2026-04-16

# Meu teste de como pegar a hora usa a library
hour1 = dt.datetime.now()
hour2 = dt.datetime.today()
print(hour1, hour2)
"""

# ===================================================
""" Funções - 24/04/2026 """
# ===================================================
"""
# 1. Modelo básico
def create_slug(title):
    "Remove the page name to turn into a valid link"
    slug = title.lower().replace(" ", "-")
    return slug


Newlink = create_slug("This is the new name")
print(Newlink)  # this-is-the-new-name


# 2. Saudação nome
def helloFunc(name):
    return "Hello " + name


msg = helloFunc("najones, how are u?")
print(msg)  # Hello najones, how are u?


# Media calc
def mediaCalc(n1, n2):
    result = (n1 + n2) / 2
    return result


print(mediaCalc(10, 4))  # 7.0


# def com for ir
def showNegative(numberz):
    for num in numberz:
        if 0 < num < 7:  # num > 0 and num < 7: também dá certo
            print(num)


aleatorys = [0, 3, 2, 12, 22, 5432, 2, 12, 0.4, 0.55]
showNegative(aleatorys)


# def com for ir metodo 2
def find_webp(archives_files):
    for archi in archives_files:
        if archi.endswith(".webp"):
            print(archi)


image = ["logo.png", "fundo.png", "bannerhome.png", "mobcapa.webp"]
find_webp(image)  # mobcapa.webp


# 5. Calcular a altura de uma imagem
def calc_height(widthz):
    #Descobre a altura exata mantendo a proporção 16:9
    return (widthz * 9) / 16


help(calc_height)  # Lê o texto das aspas triplas no terminal
print(calc_height(1920))  # 1080.0


# 6. Valor padrão
def rename_archive(name, format=("webp")):
    return f"{name}-otimizado.{format}"


print(rename_archive("banner"))  # banner-otimizado.webp
print(rename_archive("logo", "svg"))  # logo-otimizado.svg
"""

# ===================================================
""" Gerenciamento de memória | Memória: Mutáveis vs Imutáveis - 04/05/2026 """
# ===================================================
"""
# ---------------------------------------------------- Imutáveis (int, float, bool, str, tuplas). Se você muda o valor, o Python cria um novo objeto.
a = 10
b = a
a = 20
print(b)  # 10 (b continua apontando para o valor antigo)

# ---------------------------------------------------- Mutáveis (listas [], dicionários {}, set). A caixa na memória é a mesma, o que muda é o conteúdo.
lista_a = [1, 2, 3]
lista_b = lista_a
lista_a.append(4)
print(lista_b)  # [1, 2, 3, 4] (b muda junto, pois é a mesma lista na memória)

# OBS: Listas [] aceitam mudanças. Tuplas () são bloqueadas. O Python trava se tentar mudar o item da tupla.
"""

# ===================================================
""" Programação orientada a objetos (POO) - 04/05/2026 """
# ===================================================
""" 

class Usuario:
    def __init__(self, nome, cargo):
        self.nome = nome
        self.cargo = cargo

    def apresentar(self):
        return f"olá, sou {self.nome} e atuo como {self.cargo}"


user1 = Usuario("Henrique", "Webdesigner")
print(user1.apresentar())  # olá, sou Henrique e atuo como Webdesigner


# ---------------------------------------------------- Herança
class Programador(Usuario):
    def codar(self):
        print(f"{self.nome} está escrevendo em python")


dev = Programador("Nagys", "Dev")
dev.codar()  # Ação exclusiva dele | Nagys está escrevendo em python
print(dev.apresentar())  # Herdou da classe pai  | olá, sou Nagys e atuo como Dev


# ---------------------------------------------------- Sobrecarga 1
class Carrinho:
    def __init__(self, valor):
        # Cria o objeto e guarda o valor inicial na memória.
        self.valor = valor

    # O __add__ só acorda quando o sinal de + é usado entre dois objetos desta classe.
    def __add__(self, outro_carrinho):
        # Soma o valor deste objeto (self) com o objeto visitante (outro_carrinho).
        # O return cria e devolve um carrinho novo com o total.
        return Carrinho(self.valor + outro_carrinho.valor)


compra1 = Carrinho(50)  # Cria o primeiro objeto.
compra2 = Carrinho(120)  # Cria o segundo objeto, independente do primeiro.

# O sinal de + engatilha o __add__. O compra1 vira o 'self' e o compra2 vira o 'outro_carrinho'.
total = compra1 + compra2
print(total.valor)  # 170


# ---------------------------------------------------- Sobrecarga mais completo
# Exemplo real de sobrecarga fundindo dados de dispositivos diferentes
class Carrinho:
    def __init__(self, itens, valor_total):
        self.itens = itens
        self.valor_total = valor_total

    # Ensina o Python a fundir dois objetos complexos em um só
    def __add__(self, outro_carrinho):
        # Junta a lista de itens dos dois carrinhos
        nova_lista = self.itens + outro_carrinho.itens

        # Soma o preço dos dois carrinhos
        novo_valor = self.valor_total + outro_carrinho.valor_total

        # Devolve um terceiro carrinho novinho com tudo somado e fundido
        return Carrinho(nova_lista, novo_valor)


# Carrinho 1 criado isoladamente no celular
carrinho_celular = Carrinho(["Camiseta"], 50)

# Carrinho 2 criado isoladamente no PC
carrinho_pc = Carrinho(["Tenis", "Meia"], 120)

# O sinal de + dispara o __add__ e faz a fusão dos dois objetos
carrinho_final = carrinho_celular + carrinho_pc

print(carrinho_final.itens)  # ['Camiseta', 'Tenis', 'Meia']
print(carrinho_final.valor_total)  # 170
"""

# ===================================================
""" Recursão - 04/05/2026 """
# ===================================================
""" 

def contagem_regressiva(n):
    if n <= 0:  # Caso base: ponto de parada
        print("Fim")
        return
    print(n)
    contagem_regressiva(n - 1)  # Chama ela mesma se aproximando do caso base


contagem_regressiva(10)
"""
# ===================================================
""" Estruturas de dados (Pilhas, filas e árvores) - 04/05/2026 """
# ===================================================
""" 
# Exemplo: botão voltar do navegador.
pilha = []
pilha.append("Pagina 1")  # Insere no topo
pilha.append("Pagina 2")
print(pilha)  # ['Pagina 1', 'Pagina 2']
ultima_pagina = pilha.pop(-1)  # Remove do topo
print(pilha)  # ['Pagina 1']

# Exemplo: fila de tarefas do processador.
from collections import deque

fila = deque(["Cliente 1", "cliente 2"])
print(fila)  # deque(['Cliente 1', 'cliente 2'])
fila.append("Cliente 3")  # Entra no fim da fila
print(fila)  # deque(['Cliente 1', 'cliente 2', 'Cliente 3'])
atendido = fila.popleft()  # O primeiro item sai do começo da fila
print(fila)  # deque(['cliente 2', 'Cliente 3'])

"""
# ===================================================
""" Algoritmos de busca e ordenação 05/05/2026 """
# ===================================================
# ---------------------------------------------------- LISTA ORDENADA
"""
# Na vida real, não escrevemos Bubble sort ou Quick sort na mão. O Python já tem o Quick/Merge sort embutido e super rápido.
lista_nomes = ["Zecas", "Carol", "Mayco", "Cíntia", "Ana paula", "Elon"]
lista_ordenada = sorted(lista_nomes)
print(lista_ordenada)  # ['Ana paula', 'Carol', 'Cíntia', 'Elon', 'Mayco', 'Zecas']

# ---------------------------------------------------- PESQUISA SEQUENCIAL (O jeito lento)
# Olha um por um. Péssimo para listas grandes.
for nome in lista_ordenada:
    if nome == "Carol":
        print(f"{nome} foi achado em sequencial!")  # Carol foi achado em sequencial!
        break


# ---------------------------------------------------- PESQUISA SEQUENCIAL (O jeito profissional)
# Só funciona em listas já ordenadas. Corta a lista pela metade a cada passo.
def busca_binaria(lista, alvo):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2  # Acha o índice do meio exato
        chute = lista[meio]

        if chute == alvo:
            return f"Achou binária: {chute}"
        if chute > alvo:
            fim = meio - 1  # Descarta a metade da direita
        else:
            inicio = meio + 1  # Descarta a metade da esquerda
    return "Não achou"


print(busca_binaria(lista_ordenada, "carlos"))  # Não achou


# ----------------------------------------------------Transformação de chave ou Hashing (O mais rápido de todos)
# É o que o dicionário do Python usa. Você vai direto no endereço da memória.
clientes = {"Carol": "ativo", "Ana": "inativo"}
print(clientes["Carol"])  # Retorna 'ativo' instantaneamente
"""
# ===================================================
""" Resolução de exercícios univesp - 28/04/2026 """
# ===================================================
"""
# A soma dos 5 primeiros inteiros positivos:
numeros = [1, 2, 3, 4, 5]
print(sum(numeros))  # 15

# 2. A idade média de Sara (idade 23), Mark (idade 19) e Fátima (idade 31)
osNumbers = [23, 19, 31]
media = sum(osNumbers)
print(media / 3)  # 24.333333333333332

# 3. O número de vezes que 73 cabe em 403.
print(403 // 73)  # 5

# 4. O resto de quando 403 é dividido por 73.
print(403 % 73)  # 38

# 5. 2 à 10ª potência.
print(2**10)  # 1024

# 6. O valor absoluto da distância entre a altura de Sara (54 polegadas) e a altura de Mark (57 polegadas).
print(abs(54 - 57))  # 3

# 7. O menor preço entre os seguintes preços: R$ 34,99, R$ 29,95 e R$ 31,50.
prices = [34.99, 29.95, 31.50]
print(min(prices))  # 29.95
"""
# -------------------------Traduza os comandos a seguir para expressões Booleanas em Python e avalie-as:

print(f"A soma de 2 e 2 é menor que 4 >>>>>", 2 + 2 < 4)  # False
print(f"O valor de 7 // 3 é igual a 1 + 1 >>>>>", 7 // 3 == 1 + 1)  # True
print(
    f"A soma de 3 ao quadrado e 4 ao quadrado é igual a 25 >>>>>", 3**2 + 4**2 == 25
)  # True
print(f"A soma de 2, 4 e 6 é maior que 12 >>>>>", 2 + 4 + 6 > 12)  # False
print(f"1387 é divisível por 19 >>>>>", 1387 % 19 == 0)
print(f"31 é par >>>>>", 31 % 2 == 0)
print(
    f"O preço mais baixo dentre R$ 34,99, R$ 29,95 e R$ 31,50 é menor que R$ 30,00 >>>>>",
    min(34.99, 29.95, 31.5) < 30.0,
)  # True

# -------------------------Escreva instruções Python que correspondem às ações a seguir e execute-as:
# Atribua o valor inteiro 3 à variável a.
a = 3
# Atribua 4 à variável b.
b = 4
# Atribua à variável c o valor da expressão a * a + b * b.
c = a * a + b * b
print(c)  # 25

# ------------------------- Escreva expressões Python usando s1, s2 e s3 e os operadores + e * a fim de avaliar para:
s1 = "ant"
s2 = "bat"
s3 = "cod"

ex1 = s1 + " " + s2 + " " + s3  # ant bat cod
ex2 = (s1 + " ") * 10
ex3 = s1 + " " + (s2 + " ") * 2 + (s3 + " ") * 3
ex4 = (s1 + " " + s2 + " ") * 7
ex5 = (s2 * 2 + s3 + " ") * 5
print(ex1, ex2, ex3, ex4, ex5, sep="\n")

s1 = "ant"
s2 = "bat"
s3 = "cod"

# -------------------------Escreva expressões usando a string s e o operador de indexação que é avaliado como:
s = "0123456789"
ind1 = s[0]
ind2 = s[1]
ind3 = s[6]
ind4 = s[-2]
ind5 = s[-1]
print(ind1, ind2, ind3, ind4, ind5, sep="\n")  # 0 1 6 8 9

# -------------------------Escreva 2 expressões que são avaliadas, respectivamente, como a primeiro e a última palavras em palavras, na ordem do dicionário.
palavras = ["taco", "bola", "celeiro", "cesta", "peteca"]
palavras_ordenada = sorted(palavras)
pfirst_plast = palavras_ordenada[0] + " " + palavras_ordenada[-1]
print(pfirst_plast)  # bola taco

# -------------------------lista de notas de trabalho de casa dos alunos
notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]
# Uma expressão que avalia quantas vezes tem numero 7
sete_many = notas.count(7)  # 2
# Uma instrução que muda a última nota para 4.
notas[-1] = 4  # [9, 7, 7, 10, 3, 9, 6, 6, 4]
# Uma expressão que avalia para a nota mais alta.
maior_nota = max(notas)  # 10
# Uma instrução que classifica as notas da lista.
organizada_notas = sorted(notas)  # [3, 4, 6, 6, 7, 7, 9, 9, 10]
# Uma expressão que avalia para a média das notas.
media_notas = sum(notas) / len(notas)  # 6.777777777777778
print(sete_many, maior_nota, organizada_notas, media_notas, sep="\n")

# -------------------------Solicite ao user a temperatura atual em graus Fahrenheit
farenheit = int(input("Digite um valor de temperatura farenheit inteiro:"))
celsius = 5 / 9 * (farenheit - 32)
print(f"O valor da temperatura farenheit em celsius é: {celsius}")
