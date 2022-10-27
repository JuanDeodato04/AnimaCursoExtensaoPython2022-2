# Comando input(): permite que o usuário digite algo...
nome = str(input('Informe o seu nome: '))

# Perguntando a idade ao usuário.
idade = int(input('Quantos anos você tem? '))

# Comando de saída, exibir na tela...
print('Olá, o seu nome é: ' + nome)

# Imprimindo a idade na tela
print(f'Sua idade é: {idade}') 
print('Sua idade é:', idade) # concatenar com (+) não irá funcionar pois idade é um número inteiro, sendo assim usa-se vírgula.

# Mostrar o dobro da idade informada
print('O dobro da sua idade é: {}'.format(idade * 2))
  # Ou
dobroIdade = idade * 2
print(f'O dobro da idade informada é: {dobroIdade}')

# Estrutura condicional - o famoso if(se). Analisar se a pessoal é maior de idade ou não.
if idade >= 18: # Tem como colocar a condicional entre parênteses ou não.
    print('Você é maior de idade!, ótimo! Já pode beber ou dirigir.')
else:
  print('Você é menor de idade. Ainda não pode beber ou dirigir!')

# Perguntar o gênero e analisar se prestou serviço militar ou não.
genero = str(input('Informe o seu gênero (M) para masculino ou (F) para feminino: ')).upper()
if (genero == 'M') and (idade >= 18):
  print('Você já prestou ou irá prestar o serviço militar obrigatório.')
elif (genero == 'M') and (idade < 18):
  print('Ainda não chegou a sua hora de prestar o serviço militar obrigatório, pois você não completou 18 anos.')
else:
  print('No Brasil, o serviço militar não é obrigatório para mulheres.')