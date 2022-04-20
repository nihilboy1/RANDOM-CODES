from math import floor
from time import sleep

print('AUTOREFIN 2020.11.17/ NIHILBOY')

taxacetelem = '1,19', '1,29', '1,39', '1,49', '1,59', '1,69'
taxaitau = '1,35 a 1,41', '1,42 a 1,55', '1,56 a 1,71', '1,72 a 1,79', '1,80', '1,15', '1,35 a 1,55', '1,56 a 1,80'

bancos = 'CETELEM', 'SAFRA'

cerebro_margem = []
cerebro_lib_margem = []
cerebro_cliente_total = []
cerebro_meta = []
cerebro_parcela_juncao = []
cerebro_metadosaldo = []
op = 0
coef = 0.025
while True:
    if op == 0:
        print('\n - SELECIONE A OPERAÇÃO -')
    if op > 0:
        print('\n{}° OPERAÇÃO FOI SALVA '
              '\nQUAL SERÁ A PRÓXIMA?'
              '\n'.format(op))
    tabela = int(input('REFIN S/R CETELEM [1]'
                       '\nREFIN S/R ITAÚ [2]'
                       '\nREFIN S/R SAFRA [3]'
                       '\nREFIN SAFRA [4]'
                       '\nJUNÇÃO SAFRA [5]'
                       '\nOLÉ REFIN [6]'
                       '\nINFORME: '))

    # REFIN SEM REDUÇÃO CETELEM
    if tabela == 1:
        v, x, y = 0
        # PARCELA
        parcela_str = str(input('VALOR DA PARCELA ORIGINAL: '))
        if '.' and ',' in parcela_str:
            parcela_str = parcela_str.replace('.', '')
            parcela_str = parcela_str.replace(',', '.')
            parcela = float(parcela_str)
            v = 1
        if '.' in parcela_str and v != 1:
            parcela = float(parcela_str)
            y = 1
        if ',' in parcela_str and v != 1 and y != 1:
            parcela_replace = parcela_str.replace(',', '.')
            parcela = float(parcela_replace)
            x = 1
        if x != 1 and v != 1 and y != 1:
            parcela = float(parcela_str)
        v = 0
        x = 0
        y = 0
        # TAXA
        while True:
            tax = int(input('TAXAS DE JUROS'
                            # '\n1,19 [0]'
                            # '\n1,29 [1]'
                            # '\n1,39 [2]'
                            '\n1,49 [3]'
                            '\n1,59 [4]'
                            '\n1,69 [5]'
                            '\n'
                            'INFORME: '))
            if tax > 5:
                print('ENTRADA INVÁLIDA!'
                      '(É DE UM À 4, MEU PATRÃO. SE FAÇA DE DOIDO NÃO...)')
            else:
                break
        print('TAXA SELECIONADA: {} DO BANCO CETELEM'.format(taxacetelem[tax]))
        # VALOR LIBERADO
        lib_str = str(input('\n'
                            'VALOR LIBERADO: '))
        if '.' and ',' in lib_str:
            lib_str = lib_str.replace('.', '')
            lib_str = lib_str.replace(',', '.')
            lib = float(lib_str)
            v = 1
        if '.' in lib_str:
            lib = float(lib_str)
            y = 1
        if ',' in lib_str and x != 1:
            lib_replace = lib_str.replace(',', '.')
            lib = float(lib_replace)
            x = 1
        if v != 1 and x != 1 and y != 1:
            lib = float(lib_str)
        v = 0
        x = 0
        y = 0
        # META
        if tax == 0:
            meta = lib * 20 / 100
        if tax == 1:
            meta = lib * 25 / 100
        if tax == 2:
            meta = lib * 35 / 100
        if tax == 3:
            meta = lib * 40 / 100
        if tax == 4:
            meta = lib * 50 / 100
        if tax == 5:
            meta = lib * 60 / 100
        # CEREBRO
        cerebro_meta.append(meta)
        cerebro_cliente_total.append(lib)
        soma_margem = sum(cerebro_margem)
        soma_cliente = sum(cerebro_cliente_total)
        soma_meta100 = sum(cerebro_meta)

        print('\nFOI DIGITADO O REFIN SEM REDUÇÃO DA PARCELA DE {:.2f} DO BANCO CETELEM, NA TAXA DE {}'
              '\nVALOR LIBERADO: {:.2f}'
              '\nMETA: {:.2f}'.format(parcela, taxacetelem[tax], lib, meta).replace('.', ','))

        while True:
            end = int(input('\nREFIN FINALIZADO, DESEJA ENCERRAR A DIGITAÇÃO DESSE CLIENTE? '
                            '\nSIM [1]'
                            '\nNÃO [2]'
                            '\nINFORME: '))
            if end > 2:
                print('\n'
                      'ENTRADA INVÁLIDA')
            if end == 1:
                print('\n'
                      'PROGRAMA FINALIZADO!')
                sleep(1)
                print('\nMARGEM TOTAL ABERTA: {:.0f}'
                      '\nVALOR TOTAL LIBERADO PARA O CLIENTE: {:.2f}'
                      '\nMETA TOTAL PREVISTA: {:.2f}'
                      '\n-------------------------------------------'.format(soma_margem, soma_cliente,
                                                                             soma_meta100).replace('.', ','))
                cerebro_margem.clear()
                cerebro_lib_margem.clear()
                cerebro_cliente_total.clear()
                cerebro_meta.clear()
                op = 0
                break
            if end == 2:
                print('\n'
                      'CONTINUANDO PROGRAMA...')
                op += 1
                sleep(1)
                break

    # REFIN SEM REDUÇÃO ITAÚ
    if tabela == 2:
        v = 0
        x = 0
        y = 0
        # PARCELA
        parcela_str = str(input('VALOR DA PARCELA ORIGINAL: '))
        if '.' and ',' in parcela_str:
            parcela_str = parcela_str.replace('.', '')
            parcela_str = parcela_str.replace(',', '.')
            parcela = float(parcela_str)
            v = 1
        if '.' in parcela_str and v != 1:
            parcela = float(parcela_str)
            y = 1
        if ',' in parcela_str and v != 1 and y != 1:
            parcela_replace = parcela_str.replace(',', '.')
            parcela = float(parcela_replace)
            x = 1
        if x != 1 and v != 1 and y != 1:
            parcela = float(parcela_str)
        v = 0
        x = 0
        y = 0
        # -------------------------
        tax = int(input("TABELAS SEM CARÊNCIA"
                        "\n1,35 a 1,41 [0]"
                        "\n1,42 a 1,55 [1]"
                        "\n1,56 a 1,71 [2]"
                        "\n1,72 a 1,79 [3]"
                        "\n1,80 [4]"
                        "\nTABELAS COM CARÊNCIA"
                        "\n1,15 [5]"
                        "\n1,35 a 1,55 [6]"
                        "\n1,56 a 1,80 [7]"
                        "\nINFORME: "))

        print('TAXA SELECIONADA: {} DO BANCO ITAÚ'.format(taxaitau[tax]))
        # -------------------------

        lib_str = str(input('\n'
                            'VALOR LIBERADO: '))
        if '.' and ',' in lib_str:
            lib_str = lib_str.replace('.', '')
            lib_str = lib_str.replace(',', '.')
            lib = float(lib_str)
            v = 1
        if '.' in lib_str:
            lib = float(lib_str)
            y = 1
        if ',' in lib_str and x != 1:
            lib_replace = lib_str.replace(',', '.')
            lib = float(lib_replace)
            x = 1
        if v != 1 and x != 1 and y != 1:
            lib = float(lib_str)
        v = 0
        x = 0
        y = 0
        # -------------------------
        if tax == 0:
            meta = lib * 15 / 100
        if tax == 1:
            meta = lib * 20 / 100
        if tax == 2:
            meta = lib * 25 / 100
        if tax == 3:
            meta = lib * 35 / 100
        if tax == 4:
            meta = lib * 40 / 100
        if tax == 5:
            meta = lib * 20 / 100
        if tax == 6:
            meta = lib * 35 / 100
        if tax == 7:
            meta = lib * 50 / 100
        # -------------------------
        cerebro_meta.append(meta)
        cerebro_cliente_total.append(lib)
        soma_margem = sum(cerebro_margem)
        soma_cliente = sum(cerebro_cliente_total)
        soma_meta100 = sum(cerebro_meta)

        print('\nFOI DIGITADO O REFIN SEM REDUÇÃO DA PARCELA DE {:.2f} NA TAXA DE {} DO BANCO ITAÚ'
              '\nVALOR LIBERADO: {:.2f}'
              '\nMETA: {:.2f}'.format(parcela, taxaitau[tax], lib, meta).replace('.', ','))

        while True:
            end = int(input('\nREFIN FINALIZADO, DESEJA ENCERRAR A DIGITAÇÃO DESSE CLIENTE? '
                            '\nSIM [1]'
                            '\nNÃO [2]'
                            '\nINFORME: '))
            if end > 2:
                print('\n'
                      'ENTRADA INVÁLIDA')
            if end == 1:
                print('\n'
                      'PROGRAMA FINALIZADO!')
                sleep(1)
                print('\nMARGEM TOTAL ABERTA: {:.0f}'
                      '\nVALOR TOTAL LIBERADO PARA O CLIENTE: {:.2f}'
                      '\nMETA TOTAL PREVISTA: {:.2f}'
                      '\n-------------------------------------------'.format(soma_margem, soma_cliente,
                                                                             soma_meta100).replace('.', ','))
                cerebro_margem.clear()
                cerebro_lib_margem.clear()
                cerebro_cliente_total.clear()
                cerebro_meta.clear()
                op = 0
                break
            if end == 2:
                print('\n'
                      'CONTINUANDO PROGRAMA...')
                op += 1
                sleep(1)
                break
    # REFIN SEM REDUÇÃO SAFRA
    if tabela == 3:
        v = 0
        x = 0
        y = 0
        # PARCELA
        parcela_str = str(input('VALOR DA PARCELA ORIGINAL: '))
        if '.' and ',' in parcela_str:
            parcela_str = parcela_str.replace('.', '')
            parcela_str = parcela_str.replace(',', '.')
            parcela = float(parcela_str)
            v = 1
        if '.' in parcela_str and v != 1:
            parcela = float(parcela_str)
            y = 1
        if ',' in parcela_str and v != 1 and y != 1:
            parcela_replace = parcela_str.replace(',', '.')
            parcela = float(parcela_replace)
            x = 1
        if x != 1 and v != 1 and y != 1:
            parcela = float(parcela_str)
        v = 0
        x = 0
        y = 0
        # TAXA
        tax = str(input('INFORME A TAXA DE JUROS: '))
        # VALOR LIBERADO
        lib_str = str(input('\n'
                            'VALOR LIBERADO: '))
        if '.' and ',' in lib_str:
            lib_str = lib_str.replace('.', '')
            lib_str = lib_str.replace(',', '.')
            lib = float(lib_str)
            v = 1
        if '.' in lib_str:
            lib = float(lib_str)
            y = 1
        if ',' in lib_str and x != 1:
            lib_replace = lib_str.replace(',', '.')
            lib = float(lib_replace)
            x = 1
        if v != 1 and x != 1 and y != 1:
            lib = float(lib_str)
        v = 0
        x = 0
        y = 0
        # META
        meta = lib * 25 / 100
        # CEREBRO
        cerebro_meta.append(meta)
        cerebro_cliente_total.append(lib)
        cerebro_metadosaldo.append(metadosaldo)
        soma_margem = sum(cerebro_margem)
        soma_cliente = sum(cerebro_cliente_total)
        soma_meta100 = sum(cerebro_meta)

        print('\nFOI DIGITADO O REFIN SEM REDUÇÃO DA PARCELA DE {:.2f} NA TAXA DE {} DO BANCO SAFRA'
              '\nVALOR LIBERADO: {:.2f}'
              '\nMETA: {:.2f}'.format(parcela, tax, lib, meta).replace('.', ','))

        while True:
            end = int(input('\nREFIN FINALIZADO, DESEJA ENCERRAR A DIGITAÇÃO DESSE CLIENTE? '
                            '\nSIM [1]'
                            '\nNÃO [2]'
                            '\nINFORME: '))
            if end > 2:
                print('\n'
                      'ENTRADA INVÁLIDA')
            if end == 1:
                print('\n'
                      'PROGRAMA FINALIZADO!')
                sleep(1)
                print('\nMARGEM TOTAL ABERTA: {:.0f}'
                      '\nVALOR TOTAL LIBERADO PARA O CLIENTE: {:.2f}'
                      '\nMETA TOTAL PREVISTA: {:.2f}'
                      '\n-------------------------------------------'.format(soma_margem, soma_cliente,
                                                                             soma_meta100).replace('.', ','))
                cerebro_margem.clear()
                cerebro_lib_margem.clear()
                cerebro_cliente_total.clear()
                cerebro_meta.clear()
                op = 0
                break
            if end == 2:
                print('\n'
                      'CONTINUANDO PROGRAMA...')
                op += 1
                sleep(1)
                break

    # REFIN SAFRA NORMAL
    if tabela == 4:
        v = 0
        x = 0
        y = 0
        troco = 100
        # PARCELA
        parcela_str = str(input('VALOR DA PARCELA ORIGINAL: '))
        if '.' and ',' in parcela_str:
            parcela_str = parcela_str.replace('.', '')
            parcela_str = parcela_str.replace(',', '.')
            parcela = float(parcela_str)
            v = 1
        if '.' in parcela_str and v != 1:
            parcela = float(parcela_str)
            y = 1
        if ',' in parcela_str and v != 1 and y != 1:
            parcela_replace = parcela_str.replace(',', '.')
            parcela = float(parcela_replace)
            x = 1
        if x != 1 and v != 1 and y != 1:
            parcela = float(parcela_str)
        v = 0
        x = 0
        y = 0
        # PARCELA 2
        parcela2_str = str(input('VALOR DA PARCELA REDUZIDA: '))
        if '.' and ',' in parcela2_str:
            parcela2_str = parcela2_str.replace('.', '')
            parcela2_str = parcela2_str.replace(',', '.')
            parcela2 = float(parcela2_str)
            v = 1
        if '.' in parcela2_str and v != 1:
            parcela2 = float(parcela2_str)
            y = 1
        if ',' in parcela2_str and v != 1 and y != 1:
            parcela2_replace = parcela2_str.replace(',', '.')
            parcela2 = float(parcela2_replace)
            x = 1
        if x != 1 and v != 1 and y != 1:
            parcela2 = float(parcela2_str)
        v = 0
        x = 0
        y = 0
        while True:
            cot = int(input('É COTAÇÃO?'
                            '\nSIM [1]'
                            '\nNÃO [2]'
                            '\nINFORME: '))
            if cot > 2:
                print('ENTRADA INVÁLIDA')
            if cot == 1:
                txcot = str(input('INFORME A TAXA: '))
                troco_str = str(input('INFORME O TROCO: '))
                if '.' and ',' in troco_str:
                    troco_str = troco_str.replace('.', '')
                    troco_str = troco_str.replace(',', '.')
                    troco = float(troco_str)
                    v = 1
                if '.' in troco_str and v != 1:
                    troco = float(parcela2_str)
                    y = 1
                if ',' in troco_str and v != 1 and y != 1:
                    troco_replace = troco_str.replace(',', '.')
                    troco = float(troco_replace)
                    x = 1
                if x != 1 and v != 1 and y != 1:
                    troco = float(troco_str)
                v = 0
                x = 0
                y = 0
            break
            if cot == 2:
                print('NÃO É COTAÇÃO')
                break
        # while True:
        # coef_test = int(input('\nCALCULAR A MARGEM COM CARÊNCIA?'
        # '\nSIM [1]'
        # '\nNÃO [2]'
        # '\nINFORME: '))
        # if coef_test == 1:
        # coef = 0.025
        # break
        # if coef_test == 2:
        # coef = 0.0244
        # break
        # if coef_test > 2:
        # print('ENTRADA INVÁLIDA')

        # MARGEM
        margem = parcela - parcela2
        margem_true = floor(margem)
        cerebro_margem.append(margem_true)
        # VALOR LIBERADO COM A MARGEM
        lib_margem = margem_true / coef
        cerebro_lib_margem.append(lib_margem)
        # VALOR LIBERADO TOTAL
        cliente_total = lib_margem + troco
        cerebro_cliente_total.append(cliente_total)
        # META
        meta = lib_margem + troco
        cerebro_meta.append(meta)
        meta50 = lib_margem / 2 + troco
        # PRINT DO REFIN SAFRA NORMAL
        print('\nFOI DIGITADO O REFIN DA PARCELA DE {:.2f} DO SAFRA, ABRINDO {:.0f} DE MARGEM'
              '\nPARCELA REDUZIDA: {:.2f}'
              '\nVALOR DA MARGEM: {:.2f}'
              '\nVALOR DO TROCO: {:.2f}'.format(parcela, margem_true, parcela2, lib_margem, troco).replace('.', ','))
        if cot == 1:
            print('TAXA UTILIZADA NA COTAÇÃO: {}'.format(txcot))

        soma_margem = sum(cerebro_margem)
        soma_cliente = sum(cerebro_cliente_total)
        soma_meta100 = sum(cerebro_meta)

        while True:
            end = int(input('\nREFIN FINALIZADO, DESEJA ENCERRAR A DIGITAÇÃO DESSE CLIENTE? '
                            '\nSIM [1]'
                            '\nNÃO [2]'
                            '\nINFORME: '))
            if end > 2:
                print('\n'
                      'ENTRADA INVÁLIDA')
            if end == 1:
                print('\n'
                      'PROGRAMA FINALIZADO!')
                sleep(1)
                print('\nMARGEM TOTAL ABERTA: {:.0f}'
                      '\nVALOR TOTAL LIBERADO PARA O CLIENTE: {:.2f}'
                      '\nMETA TOTAL PREVISTA: {:.2f}'
                      '\n-------------------------------------------'.format(soma_margem, soma_cliente,
                                                                             soma_meta100).replace('.', ','))
                cerebro_margem.clear()
                cerebro_lib_margem.clear()
                cerebro_cliente_total.clear()
                cerebro_meta.clear()
                op = 0
                break
            if end == 2:
                print('\n'
                      'CONTINUANDO PROGRAMA...')
                op += 1
                sleep(1)
                break

    # REFIN SAFRA JUNÇÃO
    if tabela == 5:
        v = 0
        x = 0
        y = 0
        troco = 100
        n = 1
        print('DIGITE (FIM) QUANDO NÃO HOUVER MAIS PARCELAS PARA ADICIONAR'
              '\n')
        # -------------------
        while True:
            parcela_str = str(input('VALOR DA {}° PARCELA: '.format(n)))
            if 'FIM' in parcela_str:
                parcela = sum(cerebro_parcela_juncao)
                print('PARCELAS SOMADAS: {:.2f}'.format(parcela).replace('.', ','))
                break
            if '.' and ',' in parcela_str:
                parcela_str = parcela_str.replace('.', '')
                parcela_str = parcela_str.replace(',', '.')
                parcela = float(parcela_str)
                v = 1
            if '.' in parcela_str and v != 1:
                parcela = float(parcela_str)
                y = 1
            if ',' in parcela_str and v != 1 and y != 1:
                parcela_replace = parcela_str.replace(',', '.')
                parcela = float(parcela_replace)
                x = 1
            if x != 1 and v != 1 and y != 1:
                parcela = float(parcela_str)
            v = 0
            x = 0
            y = 0
            cerebro_parcela_juncao.append(parcela)
            n = n + 1

        # -------------------
        parcela2_str = str(input('VALOR DA PARCELA REDUZIDA: '))
        if '.' and ',' in parcela2_str:
            parcela2_str = parcela2_str.replace('.', '')
            parcela2_str = parcela2_str.replace(',', '.')
            parcela2 = float(parcela2_str)
            v = 1
        if '.' in parcela2_str and v != 1:
            parcela2 = float(parcela2_str)
            y = 1
        if ',' in parcela2_str and v != 1 and y != 1:
            parcela2_replace = parcela2_str.replace(',', '.')
            parcela2 = float(parcela2_replace)
            x = 1
        if x != 1 and v != 1 and y != 1:
            parcela2 = float(parcela2_str)
        v = 0
        x = 0
        y = 0

        # while True:
        # coef_test = int(input('\nCALCULAR A MARGEM COM CARÊNCIA?'
        # '\nSIM [1]'
        # '\nNÃO [2]'
        # '\nINFORME:'))
        # f coef_test == 1:
        # coef = 0.025
        # break
        # if coef_test == 2:
        # coef = 0.0244
        # break
        # if coef_test > 2:
        # print('ENTRADA INVÁLIDA')

        # MARGEM
        margem = parcela - parcela2
        margem_true = floor(margem)
        cerebro_margem.append(margem_true)
        # VALOR LIBERADO COM A MARGEM
        lib_margem = margem_true / coef
        cerebro_lib_margem.append(lib_margem)
        # VALOR LIBERADO TOTAL
        cliente_total = lib_margem + troco
        cerebro_cliente_total.append(cliente_total)
        # META
        meta = lib_margem + troco
        cerebro_meta.append(meta)
        meta50 = lib_margem / 2 + troco
        # PRINT DO REFIN SAFRA NORMAL
        print('\nFOI DIGITADA A JUNÇÃO DAS SEGUINTES PARCELAS NO BANCO SAFRA: {} | PARCELAS SOMADAS {:.2f} | MARGEM '
              'ABERTA: {:.0f} '
              '\nPARCELA REDUZIDA: {:.2f}'
              '\nVALOR DA MARGEM: {:.2f}'
              '\nVALOR DO TROCO: {:.2f}'.format(cerebro_parcela_juncao, parcela, margem_true, parcela2, lib_margem,
                                                troco).replace('.', ','))
        soma_margem = sum(cerebro_margem)
        soma_cliente = sum(cerebro_cliente_total)
        soma_meta100 = sum(cerebro_meta)
        while True:
            end = int(input('\nREFIN FINALIZADO, DESEJA ENCERRAR A DIGITAÇÃO DESSE CLIENTE? '
                            '\nSIM [1]'
                            '\nNÃO [2]'
                            '\nINFORME: '))
            if end > 2:
                print('\n'
                      'ENTRADA INVÁLIDA')
            if end == 1:
                print('\n'
                      'PROGRAMA FINALIZADO!')
                sleep(1)
                print('\nMARGEM TOTAL ABERTA: {:.0f}'
                      '\nVALOR TOTAL LIBERADO PARA O CLIENTE: {:.2f}'
                      '\nMETA TOTAL PREVISTA: {:.2f}'
                      '\n-------------------------------------------'.format(soma_margem, soma_cliente,
                                                                             soma_meta100).replace('.', ','))
                cerebro_margem.clear()
                cerebro_lib_margem.clear()
                cerebro_cliente_total.clear()
                cerebro_meta.clear()
                cerebro_parcela_juncao.clear()
                op = 0
                break
            if end == 2:
                print('\n'
                      'CONTINUANDO PROGRAMA...')
                op += 1
                sleep(1)
                break

    # REFIN NORMAL OLÉ
    if tabela == 6:
        v = 0
        x = 0
        y = 0
        # PARCELA DO REFIN OLÉ
        parcela_str = str(input('VALOR DA PARCELA ORIGINAL: '))
        if '.' and ',' in parcela_str:
            parcela_str = parcela_str.replace('.', '')
            parcela_str = parcela_str.replace(',', '.')
            parcela = float(parcela_str)
            v = 1
        if '.' in parcela_str and v != 1:
            parcela = float(parcela_str)
            y = 1
        if ',' in parcela_str and v != 1 and y != 1:
            parcela_replace = parcela_str.replace(',', '.')
            parcela = float(parcela_replace)
            x = 1
        if x != 1 and v != 1 and y != 1:
            parcela = float(parcela_str)
        v = 0
        x = 0
        y = 0
        # SALDO DO REFIN OLÉ
        saldo_str = str(input('VALOR DO SALDO DEVEDOR: '))
        if '.' and ',' in saldo_str:
            saldo_str = saldo_str.replace('.', '')
            saldo_str = saldo_str.replace(',', '.')
            saldo = float(saldo_str)
            ole_sld = saldo * 1.043
            troco = ole_sld - saldo
            v = 1
        if ',' in saldo_str:
            saldo_replace = saldo_str.replace(',', '.')
            saldo = float(saldo_replace)
            ole_sld = saldo * 1.043
            troco = ole_sld - saldo
            x = 1
        if '.' in saldo_str:
            saldo = float(saldo_str)
            ole_sld = saldo * 1.043
            troco = ole_sld - saldo
            y = 1
        if x != 1 and v != 1 and y != 1:
            saldo = float(saldo_str)
            ole_sld = saldo * 1.043
            troco = ole_sld - saldo
        v = 0
        x = 0
        y = 0
        print('SALDO CALCULADO: {:.2f}\nTROCO: {:.2f}'.format(ole_sld, troco).replace('.', ','))
        # REDUÇÃO DO REFIN OLÉ
        parcela2_str = str(input('VALOR DA PARCELA REDUZIDA: '))
        if '.' and ',' in parcela2_str:
            parcela2_str = parcela2_str.replace('.', '')
            parcela2_str = parcela2_str.replace(',', '.')
            parcela2 = float(parcela2_str)
            v = 1
        if '.' in parcela2_str and v != 1:
            parcela2 = float(parcela2_str)
            y = 1
        if ',' in parcela2_str and v != 1 and y != 1:
            parcela2_replace = parcela2_str.replace(',', '.')
            parcela2 = float(parcela2_replace)
            x = 1
        if x != 1 and v != 1 and y != 1:
            parcela2 = float(parcela2_str)
        v = 0
        x = 0
        y = 0

        # MARGEM
        margem = parcela - parcela2
        margem_true = floor(margem)
        cerebro_margem.append(margem_true)
        # VALOR LIBERADO COM A MARGEM
        lib_margem = margem_true / coef
        cerebro_lib_margem.append(lib_margem)
        # VALOR LIBERADO TOTAL
        cliente_total = lib_margem + troco
        cerebro_cliente_total.append(cliente_total)
        # META
        meta = lib_margem + troco
        cerebro_meta.append(meta)
        meta50 = lib_margem / 2 + troco
        # PRINT DO REFIN OLÉ NORMAL
        print('\nFOI DIGITADO O REFIN DA PARCELA DE {:.2f} DO OLÉ, ABRINDO {:.0f} DE MARGEM'
              '\nPARCELA REDUZIDA: {:.2f}'
              '\nVALOR DA MARGEM: {:.2f}'
              '\nVALOR DO TROCO: {:.2f}'.format(parcela, margem_true, parcela2, lib_margem, troco).replace('.', ','))
        while True:
            end = int(input('\nREFIN FINALIZADO, DESEJA ENCERRAR A DIGITAÇÃO DESSE CLIENTE? '
                            '\nSIM [1]'
                            '\nNÃO [2]'
                            '\nINFORME: '))
            if end > 2:
                print('\n'
                      'ENTRADA INVÁLIDA')
            if end == 1:
                print('\n'
                      'PROGRAMA FINALIZADO!')
                sleep(1)
                print('\nMARGEM TOTAL ABERTA: {:.0f}'
                      '\nVALOR TOTAL LIBERADO PARA O CLIENTE: {:.2f}'
                      '\nMETA TOTAL PREVISTA: {:.2f}'
                      '\n-------------------------------------------'.format(soma_margem, soma_cliente,
                                                                             soma_meta100).replace('.', ','))
                cerebro_margem.clear()
                cerebro_lib_margem.clear()
                cerebro_cliente_total.clear()
                cerebro_meta.clear()
                cerebro_parcela_juncao.clear()
                op = 0
                break
            if end == 2:
                print('\n'
                      'CONTINUANDO PROGRAMA...')
                op += 1
                sleep(1)
                break






    # PORTABILIDADE
    if tabela == 7:
        v = 0
        x = 0
        y = 0
        vendedor = str(input('BANCO DE ORIGEM: '))
        comprador = int(input('BANCO DE DESTINO:'
                              '\nCETELEM [0]'
                              '\nSAFRA [1]'
                              '\nBRADESCO [2]'
                              '\nINFORME: '))
        while True:
            comissão = int(input('A PARCELA A SER PORTADA TEM MAIS DE 12 PAGAS?'
                                '\nSIM [0]'
                                '\nNÃO [1]'
                                '\nINFORME: '))
            if comissão == 0 or 1:
                break
        banco_nome = bancos[comprador]
        # PARCELA
        parcela_str = str(input('INFORME O VALOR DA PARCELA: '))
        if '.' and ',' in parcela_str:
            parcela_str = parcela_str.replace('.', '')
            parcela_str = parcela_str.replace(',', '.')
            parcela = float(parcela_str)
            v = 1
        if '.' in parcela_str and v != 1:
            parcela = float(parcela_str)
            y = 1
        if ',' in parcela_str and v != 1 and y != 1:
            parcela_replace = parcela_str.replace(',', '.')
            parcela = float(parcela_replace)
            x = 1
        if x != 1 and v != 1 and y != 1:
            parcela = float(parcela_str)
        v = 0
        x = 0
        y = 0
        if comprador == 0:
            while True:
                produto = int(input('\nTIPO DE REFINANCIAMENTO'
                                    '\nSEM REDUÇÃO: [0]'
                                    '\nCOM REDUÇÃO: [1]'
                                    '\nINFORME: '))
                if produto <= 1:
                    break
                else:
                    print('ENTRADA INVÁLIDA')

        if produto == 1:
            tipo_refin = 'REFIN COM REDUÇÃO'
            # SALDO DO REFIN DA PORT
            saldo_str = str(input('INFORME O SALDO DEVEDOR: '))
            troco = 0
            if '.' and ',' in saldo_str:
                saldo_str = saldo_str.replace('.', '')
                saldo_str = saldo_str.replace(',', '.')
                saldo = float(saldo_str)
                portab_sld = saldo * 1.05 + 1
                troco = portab_sld - saldo
                v = 1
            if ',' in saldo_str:
                saldo_replace = saldo_str.replace(',', '.')
                saldo = float(saldo_replace)
                portab_sld = saldo * 1.05 + 1
                troco = portab_sld - saldo
                x = 1
            if '.' in saldo_str:
                saldo = float(saldo_str)
                portab_sld = saldo * 1.05 + 1
                troco = portab_sld - saldo
                y = 1
            if x != 1 and v != 1 and y != 1:
                saldo = float(saldo_str)
                portab_sld = saldo * 1.05 + 1
                troco = portab_sld - saldo
            v = 0
            x = 0
            y = 0
            print('SALDO CALCULADO: {:.2f}\nTROCO: {:.2f}'.format(portab_sld, troco).replace('.', ','))
            metadosaldo = saldo * 25 / 100
            # REDUÇÃO DO REFIN DA PORT
            parcela2_str = str(input('VALOR DA PARCELA REDUZIDA: '))
            if '.' and ',' in parcela2_str:
                parcela2_str = parcela2_str.replace('.', '')
                parcela2_str = parcela2_str.replace(',', '.')
                parcela2 = float(parcela2_str)
                v = 1
            if '.' in parcela2_str and v != 1:
                parcela2 = float(parcela2_str)
                y = 1
            if ',' in parcela2_str and v != 1 and y != 1:
                parcela2_replace = parcela2_str.replace(',', '.')
                parcela2 = float(parcela2_replace)
                x = 1
            if x != 1 and v != 1 and y != 1:
                parcela2 = float(parcela2_str)
            v = 0
            x = 0
            y = 0
            margem = parcela - parcela2
            margem_true = floor(margem)
            cerebro_margem.append(margem_true)
            # VALOR LIBERADO COM A MARGEM
            lib_margem = margem_true / coef
            cerebro_lib_margem.append(lib_margem)
            # VALOR LIBERADO TOTAL
            cliente_total = lib_margem + troco
            cerebro_cliente_total.append(cliente_total)
            # META
            meta = lib_margem + troco
            cerebro_meta.append(meta)
            meta50 = lib_margem / 2 + troco
            soma_margem = sum(cerebro_margem)
            soma_cliente = sum(cerebro_cliente_total)
            metamargem = sum(cerebro_meta)
            metasaldo = sum(cerebro_metadosaldo)
            soma_meta100 = metamargem + metasaldo


        print('\nFOI DIGITADA A PORTABILIDADE DA PARCELA DE {:.2f} DO BANCO {} PARA O BANCO {}'
              '\n{}'
              '\nTROCO: {}'
              '\nVALOR LIBERADO: {:.2f}'
              '\nMETA DA MARGEM: {:.2f}'
              '\nMETA DO SALDO: {}'.format(parcela, vendedor, banco_nome, tipo_refin, troco, lib_margem, meta, metadosaldo).replace('.', ','))

        while True:
            end = int(input('\nPORTABILIDADE FINALIZADA, DESEJA ENCERRAR A DIGITAÇÃO DESSE CLIENTE? '
                            '\nSIM [1]'
                            '\nNÃO [2]'
                            '\nINFORME: '))
            if end > 2:
                print('\n'
                      'ENTRADA INVÁLIDA')
            if end == 1:
                print('\n'
                      'PROGRAMA FINALIZADO!')
                sleep(1)
                print('\nMARGEM TOTAL ABERTA: {:.0f}'
                      '\nVALOR TOTAL LIBERADO PARA O CLIENTE: {:.2f}'
                      '\nMETA TOTAL PREVISTA: {:.2f}'
                      '\n-------------------------------------------'.format(soma_margem, soma_cliente,
                                                                             soma_meta100).replace('.', ','))
                cerebro_margem.clear()
                cerebro_lib_margem.clear()
                cerebro_cliente_total.clear()
                cerebro_meta.clear()
                cerebro_metadosaldo.clear()
                op = 0
                break
            if end == 2:
                print('\n'
                      'CONTINUANDO PROGRAMA...')
                op += 1
                sleep(1)
                break

        if produto == 0:
            tipo_refin = 'REFIN SEM REDUÇÃO'
            # TAXA
            while True:
                tax = int(input('\nTAXAS DE JUROS'
                                '\n1,19 [0]'
                                '\n1,29 [1]'
                                '\n1,39 [2]'
                                '\n1,49 [3]'
                                '\n1,59 [4]'
                                '\n'
                                'INFORME: '))
                if tax > 4:
                    print('ENTRADA INVÁLIDA!')
                else:
                    break
                print('TAXA SELECIONADA: {} DO BANCO CETELEM'.format(taxacetelem[tax]))
            # VALOR LIBERADO
            lib_str = str(input('INFORME O VALOR LIBERADO: '))
            if '.' and ',' in lib_str:
                lib_str = lib_str.replace('.', '')
                lib_str = lib_str.replace(',', '.')
                lib = float(lib_str)
                v = 1
            if '.' in lib_str:
                lib = float(lib_str)
                y = 1
            if ',' in lib_str and x != 1:
                lib_replace = lib_str.replace(',', '.')
                lib = float(lib_replace)
                x = 1
            if v != 1 and x != 1 and y != 1:
                lib = float(lib_str)
            v = 0
            x = 0
            y = 0
            # -------------------------
            if tax == 0:
                meta = lib * 20 / 100
            if tax == 1:
                meta = lib * 25 / 100
            if tax == 2:
                meta = lib * 35 / 100
            if tax == 3:
                meta = lib * 50 / 100
            if tax == 4:
                meta = lib * 60 / 100
            # -------------------------
            cerebro_meta.append(meta)
            cerebro_cliente_total.append(lib)
            soma_margem = sum(cerebro_margem)
            soma_cliente = sum(cerebro_cliente_total)
            soma_meta100 = sum(cerebro_meta)

            print('\nFOI DIGITADA A PORTABILIDADE DA PARCELA DE {:.2f} DO BANCO {} PARA O BANCO {}'
                  '\n{}'
                  '\nVALOR LIBERADO: {:.2f}'
                  '\nMETA: {:.2f}'.format(parcela, vendedor, banco_nome, tipo_refin, lib, meta).replace('.', ','))

            while True:
                end = int(input('\nPORTABILIDADE FINALIZADA, DESEJA ENCERRAR A DIGITAÇÃO DESSE CLIENTE? '
                                '\nSIM [1]'
                                '\nNÃO [2]'
                                '\nINFORME: '))
                if end > 2:
                    print('\n'
                          'ENTRADA INVÁLIDA')
                if end == 1:
                    print('\n'
                          'PROGRAMA FINALIZADO!')
                    sleep(1)
                    print('\nMARGEM TOTAL ABERTA: {:.0f}'
                          '\nVALOR TOTAL LIBERADO PARA O CLIENTE: {:.2f}'
                          '\nMETA TOTAL PREVISTA: {:.2f}'
                          '\n-------------------------------------------'.format(soma_margem, soma_cliente,
                                                                                 soma_meta100).replace('.', ','))
                    cerebro_margem.clear()
                    cerebro_lib_margem.clear()
                    cerebro_cliente_total.clear()
                    cerebro_meta.clear()
                    op = 0
                    break
                if end == 2:
                    print('\n'
                          'CONTINUANDO PROGRAMA...')
                    op += 1
                    sleep(1)
                    break