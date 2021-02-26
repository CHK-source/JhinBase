#biblioteca
import requests, time
import os

os.system("cls")
R='\033[1;31m'; B='\033[1;34m'; C='\033[1;37m'; Y='\033[1;33m'; G='\033[1;32m'; RT='\033[;0m'

#code
code_info = C + '[' + Y + 'i' + C + '] '
code_details = C + '[' + G + '*' + C + '] '
code_result = C + '[' + G + '+' + C + '] '
code_error = C + '[' + R + '!' + C + '] '

#banner
print("")
print("          ██╗██╗  ██╗██╗███╗   ██╗ ██████╗  █████╗ ███████╗███████╗")
print("          ██║██║  ██║██║████╗  ██║ ██╔══██╗██╔══██╗██╔════╝██╔════╝")
print("          ██║███████║██║██╔██╗ ██║ ██████╔╝███████║███████╗█████╗  ")
print("     ██   ██║██╔══██║██║██║╚██╗██║ ██╔══██╗██╔══██║╚════██║██╔══╝  ")
print("     ╚█████╔╝██║  ██║██║██║ ╚████║ ██████╔╝██║  ██║███████║███████╗")
print("      ╚════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝ v1.0")
print("                           Channel: JhinStroke")
print("                           Github: CHK-source")
print("")

def main():
  print(f'''{G}
\n
               ██████╗  █████╗ ██╗███╗   ██╗███████╗██╗     
               ██╔══██╗██╔══██╗██║████╗  ██║██╔════╝██║     
               ██████╔╝███████║██║██╔██╗ ██║█████╗  ██║     
               ██╔═══╝ ██╔══██║██║██║╚██╗██║██╔══╝  ██║     
               ██║     ██║  ██║██║██║ ╚████║███████╗███████╗
               ╚═╝     ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝╚══════╝
''')

  print(f'''
{C}[{G}JB{C}] Formas de operação: 

[{G}1{C}] IP.
[{G}2{C}] CPF.
[{G}3{C}] CEP.
[{G}4{C}] CNPJ.
[{G}5{C}] Placa.
[{G}6{C}] Telefone.
[{G}7{C}] {R}Sair.{C}
''')
  tool=input(f'{C}[{G}+{C}] Selecione a forma de operação:{B} ')
  if tool == "1":
     os.system('cls')
     import ip
     ip.main()
  elif tool == "2":
     os.system('cls')
     import cpf
     cpf.main()
  elif tool == "3":
     os.system('cls')
     import cep
     cep.main()
  elif tool == "4":
     os.system('cls')
     import cnpj
     cnpj.main()
  elif tool == "5":
     os.system('cls')
     import placa
     placa.main()
  elif tool == "6":
     os.system('cls')
     import telefone
     telefone.main()
  elif tool == "7":
     os.system("cls")
     print(f'\n{G}JhinBase.{C}\n')
     exit()
  else:
     os.system("cls")
     print(f'{C}[{R}-{C}] Seleção inválida.')
     time.sleep(0.2)
     main()
main()

#JhinBase ©