# ===================================================
''' Saída e entrada de dados - 10/04/2026'''
# ===================================================
'''
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

'''

# ===================================================
''' Operadores matemáticos e lógicos - 10/04/2026'''
# ===================================================

#----------------------------------------------------Operador de indexação
'''
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
'''

# ===================================================
''' Listas e dicionários - 13/04/2026'''
# ===================================================

#---------------------------------------------------- LISTAS
'''
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
'''

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




'''
#Dicionário/Objeto
customers = {"name":"john","id:":1,"registered":"november"}
getCustomerData = customers["registered"] #Acessar item do objeto/Dicionário
print(getCustomerData) #november
'''