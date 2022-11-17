# Criação de funções
preco = 1999.90

# Calcular apenas 5% de imposto, guardar na variável imposto e exibir na tela
imposto = preco * 0.05
print(imposto)

preco2 = 100
imposto2 = preco2 * 0.07
print(imposto2)

# Criar uma função calcularImposto() que calcula um imposto de 5% e retorna a quem pediu...

# Declaração da função
def calcularImposto(precoProduto):
  imposto = precoProduto * 0.10
  return imposto

# Uso da função
preco = 299
imposto = calcularImposto(preco)
print(imposto)

# Exemplo de variável global x local
print(preco)
precoProduto = 100
print(precoProduto)

# Agora calcular imposto a alìquota agora é 7%
valores = [1.99, 24.50, 78.27, 1515.5]
# Calcular o imposto desses quatro valores
for valor in valores:
  print(f'O imposto de {valor} é {calcularImposto(valor)}')

# Declarar um função calcularImpostoAliquota que recebe dois parâmetros: o preço do produto e a alíquota de imposto a ser aplicada e retorna o imposto calculado. Se a aliquota não for informada, utilize 7% como padrão.
def calcularImpostoAliquota(valor, aliquota = 7):
  imposto = valor * (aliquota / 100)
  return imposto

for valor in valores:
  print(f"O imposto de {valor} é {calcularImpostoAliquota(valor)}")

for valor in valores:
  print(f"O imposto de {valor} é {calcularImpostoAliquota(valor, 7)}")

#E se agora o imposto for 10%?
for valor in valores:
  print(f"O imposto de {valor} é {calcularImpostoAliquota(valor, 10)}")