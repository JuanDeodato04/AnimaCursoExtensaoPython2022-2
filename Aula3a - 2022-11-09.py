# Próxima aula dia 09-11-2022...
print('Inicio da aula 3 (09/11/22)')

contador = 1
while (contador <= 10):
  print(contador)
  contador += 1

# Laço for (pytho for = for each)
fruta = 'Morango'
print(fruta)

fruta1 = 'Morango'
fruta2 = 'Laranja'
fruta3 = 'Pêra'

# Lista
frutas = ['morango', 'laranja', 'Pêra']

# Mostra todas as frutas
print(frutas)

# Exibir apenas um elemento
print(frutas[2])

# Exibir a quantidade de frutas que tem na lista
print(len(frutas))

# Adicionar uma nova fruta
frutas.append('Manga')
print(len(frutas)) # Tamanho
print(frutas)

# Exemplo com while
i = 0 # i de index
while (i < len(frutas)):
  print(frutas[i])
  i += 1 # Mesma coisa que i = i + 1

# Exemplo com o FOR
for fruta in frutas:
  print(fruta)