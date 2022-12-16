# menu interativo
jogador = []

def cadastro():
  
  while True:
    print("Forneça o nome do jogador:")
    dadoNome = {} 
    dadoNome['nome'] = (input("nome:"))

    lista = {i['nome']: i for i in jogador}
    
    jogador.append(dadoNome)

    opcao =input('temos o nome do jogador. vai adicionar mais alguém? s(sim) ou n(não):').strip().lower()
    if (opcao == 'n'):
      menu()
    if (opcao == 's'):
      cadastro()
      break

def mostrarJogador():
  pass 
  
def menu():
  print("f'  1-cadastro, 2-deletar,  3-encerrar programa'")
menu()
while True:
  menu1 = int(input("selecione uma das opções acima:"))
  if menu1==1:
    cadastro()
  elif menu==2:
    mostrarJogador()
  else:
    print('encerrando..')
    print('programa encerrado')
    break
  if menu==2:
    print('mimimi')
  if menu==3:
    print('tututu')
  else:
    print(menu)
  break



#def Menu():
 # if opcao1=
  #opcao2=
  #opcao3=