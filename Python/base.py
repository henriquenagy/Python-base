# ===================================================
"""Saída e entrada de dados - 10/04/2026"""
# ===================================================
"""
print("olá mundo")

fruta= "banana"
tipo = "Bolão de "
print(tipo+fruta)

print("Repetição"*6)

nome = "Najones"
print(nome*3)

print(nome + "ricaço"*3)

print(f"Olá, {nome} !") #f-string

print("O tipo é:", type(nome)) #O tipo é: <class 'str'>
print("Listagem de:", dir(nome)) # [analogia] o dir te mostra todos os botões do rádio.
help(str) #[analogia] O help(str) é o manual que te ensina o que acontece quando você aperta cada botão.

cor = "#8750f7"
print(type(cor)) # <class 'str'>
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
#---------------------------------------------------- LISTAS
colors = ["blue", "red", "green", "orange"] #Lista com texto
prices = [27.66,29,17,11.23,9.22,10,17,4,11,54,67,17] #Lista com números, usa-se o ponto como separação e não virgula
pickColorOne = colors[0] #Seleciona a 1a posição
print(pickColorOne) #blue

print("Soma todos os números de uma vez:",sum(prices)) #274.11
print("Quantos itens existem na lista:",len(prices)) #12
print("Quantas vezes um nº específico aparece:", prices.count(17)) #3
print("Organizada na mesma linha:", sorted(prices)) #[4, 9.22, 10, 11...] Ñ altera original, só cria uma cópia já organizada para mostrar na tela.
print("Checa pra vc confirmar que já voltou ao normal",prices) # [27.66, 29, 17, 11.23, 9.22, 10, 17, 4, 11, 54, 67, 17]
prices.sort() #SORT - Cuidado com o de cima!!!
print("Lista organizada:", prices) #[4, 9.22, 10, 11, 11.23, 17, 17, 17, 27.66, 29, 54, 67] ALTERA DE VEZ!!!
print("Menor nº da lista",min(prices)) #4
print("Maior nº da lista",max(prices)) #67
prices[0],prices[-1] = prices[-1], prices[0] #Inverter posições
print(prices)#INVERTIDO - [67, 9.22, 10, 11, 11.23, 17, 17, 17, 27.66, 29, 54, 4]

# Cuidado com cópias de listas
lista_a = [1, 2, 3]
lista_b = lista_a # Não é uma cópia. Se mudar a, muda b.
lista_c = lista_a.copy() # Jeito certo de criar uma cópia independente
"""

"""
#----------------------------------------------------  Métodos para manipular os itens
Apostolos = ["simão pedro", "andre", "filipe", "bartolomeu", "tomé", "simão", "tadeu", "lucas", "tiago", "mateus", "joão", "judas"]

print("judas" in Apostolos) # Retorna True se existir na lista

if "judas" in Apostolos: 
    print("Judas vacilão") # Executa se a condição acima for True

Apostolos.remove("judas") # Remove o item pelo valor exato
print("Judas removido", Apostolos) # Mostra sem o Judas

Apostolos.append("matias") # Adiciona ao final da lista
print("Matias, chega mais:", Apostolos) # Mostra com Matias no fim

Apostolos.insert(6, "Henriques") # Empurra para a direita e entra no índice 6
print("Seja bem vindo nagys:", Apostolos) # Mostra com Henriques no meio

print("Só vai sobrar:", Apostolos.pop()) # Remove todos e imprime o último item (Matias)

Apostolos.clear() # Esvazia a lista inteira
print("Cadê a turma?: ", Apostolos) # Retorna [] (lista vazia)
"""

"""
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
