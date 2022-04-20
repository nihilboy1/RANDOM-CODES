#12454722402
from math import floor
from time import sleep
while True:
    cpflist = []
    results1 = []
    """
    Aqui dentro o usuário informa o cpf
    e eu só passo pra próxima parte quando ele estiver limpo
    """
    
    cpfusu = str(input('Informe um CPF para ser analisado: ')).strip().replace('.', '').replace('-', '')
    c = len(cpfusu)
    cpflimpo = cpfusu if cpfusu.isnumeric()and c == 11 else print('Entrada inválida!')
    if cpflimpo:
        print ('Iniciando análise do CPF...')
    else:
        print('Informe apenas 11 digitos, e todos sendo numeros')
    cpf1 = cpflimpo[0:9]

    """
    Agora começa o loop, onde eu vou multiplicar os numeros, guardar eles nas listas
    e depois somalos
    """
    multi = 10
    for num in cpf1:
        cpflist.append(num)
        numint = int(num)
        result = numint * multi
        results1.append(result)
        multi = multi - 1
    soma1 = sum(results1)
    divi = soma1 / 11
    resto = soma1 - (11 * floor(divi))
    if resto < 2:
        digito1 = 0
        print('primeiro if: {} '.format(digito1))
    elif resto > 1:
        digito1 = 11 - resto
        print('segundo if: {} '.format(digito1))
        print(digito1)
    

        

    
         
         
    
