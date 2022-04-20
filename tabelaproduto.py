while True:
    prod = int(input('Qual o produto?'
                     '\n PORT [1]'
                     '\n REFIN [2]'
                     '\n NOVO [3]'
                     '\n INFORME: '))
    if prod == 1:
        txp = str(input('\n Taxa da port: '))
        txr = str(input('\n Taxa do refin da port: '))
        sald = str(input('\n Saldo usado na port: '))
        mrg = str(input('\n Margem aberta: '))
        parc1 = str(input('\n Parcela original: '))
        parc2 = str(input('\n Parcela reduzida: '))
        troco = str(input('\n Troco: '))

        print('\n'
              '\n'
              'PROPOSTA DIGITADA, SEGUEM OS DADOS: TAXA DA PORT: {} // '
              'TAXA DO REFIN: {} // '
              'SALDO UTILIZADO: {} // '
              'MARGEM ABERTA: {} // '
              'TROCO: {} // '
              'PAR ORIGINAL: {} // '
              'PAR REDUZIDA: {} // '
              '\n'
              '\n'.format(txp, txr, sald, mrg,troco, parc1, parc2,))
    if prod == 2:
        txr = str(input('\n Taxa do refin: '))
        parc1 = str(input('\n Parcela original: '))
        parc2 = 'SEM REDUÇÃO'
        mrg = str(input('\n Margem aberta: '))
        if mrg != '0':
            parc2 = str(input('\n Parcela reduzida: '))
        troco = str(input('\n Troco: '))

        print('\n'
              '\n'
              'PROPOSTA DIGITADA, SEGUEM OS DADOS:'
              'TAXA DO REFIN: {} // '
              'MARGEM ABERTA: {} // '
              'TROCO: {} // '
              'PAR ORIGINAL: {} // '
              'PAR REDUZIDA: {} // '
              '\n'
              '\n'.format(txr,mrg,troco, parc1, parc2,))
    if prod == 3:
        parc1 = str(input('\n Parcela: '))
        txr = str(input('\n Taxa: '))
        prz = str(input('\n Prazo: '))
        car = str(input('\n Carência: '))
        lib = str(input('\n Valor liberado: '))

        print('\n'
              '\n'
              'PROPOSTA DIGITADA, SEGUEM OS DADOS:'
              'TAXA DA MARGEM {} // '
              'PARCELA: {} // '
              'PRAZO: {} // '
              'CARÊNCIA: {} // '
              'VALOR LIBERADO: {} // '
              '\n'
              '\n'.format(txr,parc1,prz,car, lib))
     

        
