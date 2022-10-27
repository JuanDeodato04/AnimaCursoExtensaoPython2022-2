# Pede o nome do aluno e sua nota (de 0 a 10) e, se ele tirou nota 10, elogie.
nomeAluno = str(input('Informe o nome do aluno: ')).title()
nota = float(input('Digite a nota do(a) ' + nomeAluno + '? '))
if (nota == 10):
  print(f'{nomeAluno}, parabéns pela nota máxima!')
elif (6 <= nota < 10):
  print(f'Muito bom {nomeAluno}, mas precisa estudar mais.')
else:
  print('Mandou mal, ainda precisa estudar muito...')