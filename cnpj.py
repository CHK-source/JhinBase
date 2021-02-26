#JhinBase ©

import requests
from time import sleep
import os
import time

vd='\033[32m'
am='\033[33m'
vm='\033[31m'
az='\033[36m'
ng='\033[1m'
f='\033[m'
lz='\033[34m'   

#JhinBase ©

def cnpj():
    print(f"{C}[{Y}i{C}] Receita Federal: ")
    cpnj1=input(f"{C}[{G}*{C}] Informe o CNPJ (sem pontos e barra): {B}")                           
    url1='https://www.receitaws.com.br/v1/cnpj/{}'.format(cpnj1)
    res=requests.get(url1);req1=res.json()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
    br=f"\n{C}[{G}i{C}] CNPJ encontrado.\nDATA_SITUAÇÃO: {B}{req1['data_situacao']}{C}\nMOTIVO_SITUAÇÃO: {B}{req1['motivo_situacao']}{C}\nCOMPLEMENTO: {B}{req1['complemento']}{C}\nTIPO: {B}{req1['tipo']}{C}\nNOME: {B}{req1['nome']}{C}\nTELEFONE: {B}{req1['telefone']}{C}\nSITUAÇÃO: {B}{req1['situacao']}{C}\nBAIRRO: {B}{req1['bairro']}{C}\nENDEREÇO: {B}{req1['logradouro']}{C}\nNÚMERO: {B}{req1['numero']}{C}\nCEP: {B}{req1['cep']}{C}\nMUNICÍPIO: {B}{req1['municipio']}{C}\nFANTASIA: {B}{req1['fantasia']}{C}\nPORTE: {B}{req1['porte']}{C}\nABERTURA: {B}{req1['abertura']}{C}\nNATUREZA_JUDICIAL: {B}{req1['natureza_juridica']}{C}\nUF: {B}{req1['uf']}{C}\nCNPJ: {B}{req1['cnpj']}{C}\nÚLTIMA_ATUALIZAÇÃO: {B}{req1['ultima_atualizacao']}{C}\nSTATUS: {B}{req1['status']}{C}\nEMAIL: {B}{req1['email']}{C}\nEFR: {B}{req1['efr']}{C}\nSITUAÇÃO_ESPECIAL: {B}{req1['situacao_especial']}{C}\nDATA_SITUAÇÃO_ESPECIAL:{B}{req1['data_situacao_especial']}{C}\nCAPITAL_SOCIAL: {B}{req1['capital_social']}{C}\nATIVIDADE_PRINCIPAL: {B}{req1['atividade_principal']}{C}\nATIVIDADES_SECUNDÁRIAS:{B}{req1['atividades_secundarias']}{C}\nQSA: {B}{req1['qsa']}{C}\nEXTRA: {B}{req1['extra']}{C}\nBILLING: {B}{req1['billing']}{C}"      
    print(br)
def ban():
    print(f"""

  """)

R='\033[1;31m'; B='\033[1;34m'; C='\033[1;37m'; Y='\033[1;33m'; G='\033[1;32m'; RT='\033[;0m'

code_info = C + '[' + Y + 'i' + C + '] '
code_details = C + '[' + G + '*' + C + '] '
code_result = C + '[' + G + '+' + C + '] '
code_error = C + '[' + R + '!' + C + '] '

os.system('cls')

#JhinBase ©

def main():
    os.system('cls');
    print("\n" + code_info + "CNPJ.")
    print(f"""
{C}[{G}i{C}] Formas de operação: 

[{G}1{C}] Consultar CNPJ.
[{G}2{C}] Voltar.
[{G}3{C}] {R}Sair.{C}""")
    tool=str(input(f'\n{C}[{G}+{C}] Selecione a forma de operação:{B} '))
    if tool=='1':   
        os.system('cls');ban();cnpj()
    elif tool=='2':
        os.system("cls")
        import consulta
        consulta.main()
    elif tool=='3':
        os.system('cls');print(f'\n{G}JhinBase.{C}\n');exit()
    else:
        os.system("cls")
        print(f'{C}[{R}-{C}] Seleção inválida.')
        time.sleep(0.2)
        main()                                         

main()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    

#JhinBase ©