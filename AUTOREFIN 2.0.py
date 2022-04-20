from math import floor
from time import sleep
print('--- AUTOREFIN 2.0 \n--- NIHILBOY ')
taxacetelem = '1,19', '1,29', '1,39', '1,49', '1,59'
taxaitau = '1,38', '1,42', '1,56', '1,72', '1,80'
cerebro_margem = []
cerebro_lib_margem = []
cerebro_cliente_total = []
cerebro_meta = []
while True:
    tabela = int(input('QUAL SERÁ A PRÓXIMA OPERAÇÃO?'
                       '\n'
                       '\nREFIN RECUP -> 1'
                       '\nREFIN TROCO LIVRE -> 2'
                       '\nREFIN PORTAB -> 3'
                       '\nREFIN S/R CETELEM -> 4'
                       '\nREFIN S/R ITAÚ -> 5'
                       '\nSAFRA REFIN -> 6'
                       '\nSAFRA REFIN COTAÇÃO -> 7'
                       '\nOLÉ REFIN -> 8'
                       '\n'
                       '\nINFORME: '))

    # REFIN CETELEM RECUP
    if tabela == 1:
        v = 0
        x = 0
        troco = 200
        # PARCELA DA RECUP
        parcela_str = str(input('Valor da parcela ATUAL: '))
        if '.' in parcela_str:
            parcela = float(parcela_str)
            v = 1
            x = 1
        if ',' in parcela_str and x != 1:
            parcela_replace = parcela_str.replace(',', '.')
            parcela = float(parcela_replace)
            v = 1
        if v != 1:
            parcela = float(parcela_str)
        v = 0
        x = 0
        # SALDO DA RECUP
        saldo_str = str(input('Valor do saldo devedor: '))
        if ',' in saldo_str:
            saldo_replace = saldo_str.replace(',', '.')
            saldo = float(saldo_replace)
            recup = saldo + troco
            x = 1
            v = 1
        if '.' in saldo_str:
            saldo = float(saldo_str)
            v = 1
            recup = saldo + troco
        if v != 1:
            saldo = float(saldo_str)
            recup = saldo + troco
        v = 0
        x = 0
        print('Saldo devedor para a RECUP: {:.2f}\nTroco: {:.2f}'.format(recup, troco).replace('.', ','))
        # REDUÇÃO DA RECUP
        parcela2_str = str(input('Valor da parcela REDUZIDA: '))
        if ',' in parcela2_str:
            parcela2_replace = parcela2_str.replace(',', '.')
            parcela2 = float(parcela2_replace)
            v = 1
        if '.' in parcela2_str:
            parcela2 = float(parcela2_str)
            x = 1
            v = 1
        if v != 1:
            parcela2 = float(parcela2_str)

        # MARGEM
        margem = parcela - parcela2
        margem_true = floor(margem)
        cerebro_margem.append(margem_true)
        # VALOR LIBERADO COM A MARGEM
        lib_margem = margem_true / 0.0244
        cerebro_lib_margem.append(lib_margem)
        # VALOR LIBERADO TOTAL
        cliente_total = lib_margem + troco
        cerebro_cliente_total.append(cliente_total)
        # META
        meta = lib_margem + troco
        cerebro_meta.append(meta)
        meta50 = lib_margem / 2 + troco
        # PRINT DA RECUP
        print('\nFOI DIGITADO O REFIN DA PARCELA DE {:.2f} DO CETELEM, ABRINDO {:.0f} DE MARGEM'
                '\nPARCELA REDUZIDA: {:.2f}'
                '\nVALOR DA MARGEM: {:.2f}'
                '\nVALOR DO TROCO: {:.2f}'.format(parcela, margem_true, parcela2, lib_margem, troco).replace('.', ','))
            
        end = int(input('\nREFIN FINALIZADO, DESEJA ENCERRAR A DIGITAÇÃO? '
                            '\nSIM > 1'
                            '\nNÃO > 2'
                            '\nINFORME: '))
            
        soma_margem = sum(cerebro_margem)
        soma_cliente = sum(cerebro_cliente_total)
        soma_meta100 = sum(cerebro_meta)
            
        if end == 1:
            print('\nMARGEM TOTAL ABERTA: {:.0f}'
                    '\nVALOR TOTAL LIBERADO PARA O CLIENTE: {:.2f}'
                    '\nMETA TOTAL PREVISTA: {:.2f}'.format(soma_margem, soma_cliente, soma_meta100).replace('.', ','))

            print('\n'
                    'FINALIZANDO PROGRAMA...')
            sleep(5)
            print('FINALIZADO!')
            print('\n')

            cerebro_margem.clear()
            cerebro_lib_margem.clear()
            cerebro_cliente_total.clear()
            cerebro_meta.clear()

    # REFIN CETELEM TROCO LIVRE
    if tabela == 2:
        v = 0
        x = 0
        parcela_str = str(input('Valor da parcela ATUAL: '))
        if '.' in parcela_str:
            parcela = float(parcela_str)
            v = 1
            x = 1
        if ',' in parcela_str and x != 1:
            parcela_replace = parcela_str.replace(',', '.')
            parcela = float(parcela_replace)
            v = 1
        if v != 1:
            parcela = float(parcela_str)
        v = 0
        x = 0
        saldo_str = str(input('Valor do saldo devedor: '))
        troco_str = str(input('Qual será o valor do troco?'))
        if ',' in troco_str:
            troco_replace = troco_str.replace(',', '.')
            troco = float(troco_replace)
            v = 1
        if '.' in troco_str:
            troco = float(troco_str)
            v = 1
        if v != 1:
            troco = float(troco_str)
            v = 1
        v = 0
        if ',' in saldo_str:
            saldo_replace = saldo_str.replace(',', '.')
            saldo = float(saldo_replace)
            recup = saldo + troco
            v = 1
        if '.' in saldo_str:
            saldo = float(saldo_str)
            v = 1
            recup = saldo + troco
        if v != 1:
            saldo = float(saldo_str)
            recup = saldo + troco
        v = 0
        print('Saldo devedor para a PORTAB: {:.2f}\nTroco: {:.2f}'.format(recup, troco).replace('.', ','))
        parcela2_str = str(input('Valor da parcela REDUZIDA: '))
        if ',' in parcela2_str:
            parcela2_replace = parcela2_str.replace(',', '.')
            parcela2 = float(parcela2_replace)
            v = 1
        if '.' in parcela2_str:
            parcela2 = float(parcela2_str)
            x = 1
            v = 1
        if v != 1:
            parcela2 = float(parcela2_str)

        # MARGEM
        margem = parcela - parcela2
        margem_true = floor(margem)
        cerebro_margem.append(margem_true)
        # VALOR LIBERADO COM A MARGEM
        lib_margem = margem_true / 0.0244
        cerebro_lib_margem.append(lib_margem)
        # VALOR LIBERADO TOTAL
        cliente_total = lib_margem + troco
        cerebro_cliente_total.append(cliente_total)
        # META
        meta100 = lib_margem + troco
        cerebro_meta.append(meta100)
        meta50 = lib_margem / 2 + troco
        # PRINT DA TROCO LIVRE
        print('\nFOI DIGITADO O REFIN DA PARCELA DE {:.2f} DO CETELEM, ABRINDO {:.0f} DE MARGEM'
              '\nPARCELA REDUZIDA: {:.2f}'
              '\nVALOR DA MARGEM: {:.2f}'
              '\nVALOR DO TROCO: {:.2f}'.format(parcela, margem_true, parcela2, lib_margem, troco).replace('.', ','))

        end = int(input('\nREFIN FINALIZADO, DESEJA ENCERRAR A DIGITAÇÃO? '
                        '\nSIM > 1'
                        '\nNÃO > 2'
                        '\nINFORME: '))

        soma_margem = sum(cerebro_margem)
        soma_cliente = sum(cerebro_cliente_total)
        soma_meta100 = sum(cerebro_meta)
            
        if end == 1:
            print('\nMARGEM TOTAL ABERTA: {:.0f}'
                    '\nVALOR TOTAL LIBERADO PARA O CLIENTE: {:.2f}'
                    '\nMETA TOTAL PREVISTA: {:.2f}'.format(soma_margem, soma_cliente, soma_meta100).replace('.', ','))

            print('\n'
                    'FINALIZANDO PROGRAMA...')
            sleep(5)
            print('FINALIZADO!')
            print('\n')

            cerebro_margem.clear()
            cerebro_lib_margem.clear()
            cerebro_cliente_total.clear()
            cerebro_meta.clear()

    # REFIN CETELEM PORTAB
    if tabela == 3:
        v = 0
        x = 0
        # PARCELA DA PORTAB
        parcela_str = str(input('Valor da parcela ORIGINAL: '))
        if '.' in parcela_str:
            parcela = float(parcela_str)
            v = 1
            x = 1
        if ',' in parcela_str and x != 1:
            parcela_replace = parcela_str.replace(',', '.')
            parcela = float(parcela_replace)
            v = 1
        if v != 1:
            parcela = float(parcela_str)
        v = 0
        x = 0
        # SALDO DA PORTAB
        saldo_str = str(input('Valor do SALDO DEVEDOR: '))
        if ',' in saldo_str:
            saldo_replace = saldo_str.replace(',', '.')
            saldo = float(saldo_replace)
            x = 1
            v = 1
        if '.' in saldo_str:
            saldo = float(saldo_str)
            v = 1
        if v != 1:
            saldo = float(saldo_str)
        portab = saldo * 1.05 + 10
        troco = portab - saldo
        v = 0
        x = 0
        print('Saldo calculado: {:.2f}\nTroco: {:.2f}'.format(portab, troco).replace('.', ','))
        # REDUÇÃO DA PORTAB
        parcela2_str = str(input('Valor da parcela REDUZIDA: '))
        if ',' in parcela2_str:
            parcela2_replace = parcela2_str.replace(',', '.')
            parcela2 = float(parcela2_replace)
            v = 1
        if '.' in parcela2_str:
            parcela2 = float(parcela2_str)
            x = 1
            v = 1
        if v != 1:
            parcela2 = float(parcela2_str)

        # MARGEM
        margem = parcela - parcela2
        margem_true = floor(margem)
        cerebro_margem.append(margem_true)
        # VALOR LIBERADO COM A MARGEM
        lib_margem = margem_true / 0.0244
        cerebro_lib_margem.append(lib_margem)
        # VALOR LIBERADO TOTAL
        cliente_total = lib_margem + troco
        cerebro_cliente_total.append(cliente_total)
        # META
        meta100 = lib_margem + troco
        cerebro_meta.append(meta100)
        meta50 = lib_margem / 2 + troco
        # PRINT DA PORTAB
        print('\nFOI DIGITADO O REFIN DA PARCELA DE {:.2f} DO CETELEM, ABRINDO {:.0f} DE MARGEM'
                '\nPARCELA REDUZIDA: {:.2f}'
                '\nVALOR DA MARGEM: {:.2f}'
                '\nVALOR DO TROCO: {:.2f}'.format(parcela, margem_true, parcela2, lib_margem, troco).replace('.', ','))

        end = int(input('\nOPERAÇÃO CONCLUÍDA, DESEJA ENCERRAR A DIGITAÇÃO? '
                        '\nSIM > 1'
                        '\nNÃO > 2'
                        '\nINFORME: '))

        soma_margem = sum(cerebro_margem)
        soma_cliente = sum(cerebro_cliente_total)
        soma_meta100 = sum(cerebro_meta)

        if end == 1:
            print('\nMARGEM TOTAL ABERTA: {:.0f}'
                    '\nVALOR TOTAL LIBERADO PARA O CLIENTE: {:.2f}'
                    '\nMETA TOTAL PREVISTA: {:.2f}'.format(soma_margem, soma_cliente, soma_meta100).replace('.', ','))

            print('\n'
                    'FINALIZANDO PROGRAMA...')
            sleep(5)
            print('FINALIZADO!')
            print('\n')

            cerebro_margem.clear()
            cerebro_lib_margem.clear()
            cerebro_cliente_total.clear()
            cerebro_meta.clear()

    # REFIN SEM REDUÇÃO CETELEM
    if tabela == 4:
        v = 0
        x = 0
        #-------------------------
        parcela_str = str(input('Valor da parcela: '))
        if '.' in parcela_str:
            parcela = float(parcela_str)
            v = 1
            x = 1
        if ',' in parcela_str and x != 1:
            parcela_replace = parcela_str.replace(',', '.')
            parcela = float(parcela_replace)
            v = 1
        if v != 1:
            parcela = float(parcela_str)
        v = 0
        x = 0
        # ------------------------
        while True:
            tax = int(input('\nQUAL TAXA SERÁ UTILIZADA?'
                            '\n1,19 -> 0'
                            '\n1,29 -> 1'
                            '\n1,39 -> 2'
                            '\n1,49 -> 3'
                            '\n1,59 -> 4'
                            '\nINFORME: '))
            if tax > 4:
                print('TAXA SELECIONADA INVÁLIDA')
            else:
                break

        print('Você selecionou a taxa {} do banco CETELEM'.format(taxacetelem[tax]))
        # -------------------------
        lib_str = str(input('\nInforme o valor liberado: '))
        if '.' in lib_str:
            lib = float(lib_str)
            v = 1
            x = 1
        if ',' in lib_str and x != 1:
            lib_replace = lib_str.replace(',', '.')
            lib = float(lib_replace)
            v = 1
        if v != 1:
            lib = float(lib_str)
        v = 0
        x = 0
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

        print('\nFOI DIGITADO O REFIN SEM REDUÇÃO DA PARCELA DE {:.2f} NA TAXA DE {} DO BANCO CETELEM'
              '\nVALOR LIBERADO: {:.2f}'
              '\nMETA PREVISTA: {:.2f}'.format(parcela, taxacetelem[tax], lib, meta).replace('.', ','))

        end = int(input('\nREFIN FINALIZADO, DESEJA ENCERRAR A DIGITAÇÃO? '
                        '\nSIM > 1'
                        '\nNÃO > 2'
                        '\nINFORME: '))
        if end == 1:
            print('\nMARGEM TOTAL ABERTA: {:.0f}'
                  '\nVALOR TOTAL LIBERADO PARA O CLIENTE: {:.2f}'
                  '\nMETA TOTAL PREVISTA: {:.2f}'.format(soma_margem, soma_cliente, soma_meta100).replace('.', ','))

            print('\n'
                  'FINALIZANDO PROGRAMA...')
            sleep(5)
            print('FINALIZADO!')
            print('\n')

            cerebro_margem.clear()
            cerebro_lib_margem.clear()
            cerebro_cliente_total.clear()
            cerebro_meta.clear()

    # REFIN SEM REDUÇÃO ITAÚ
    if tabela == 5:
        v = 0
        x = 0
        #-------------------------
        parcela_str = str(input('Valor da parcela: '))
        if '.' in parcela_str:
            parcela = float(parcela_str)
            v = 1
            x = 1
        if ',' in parcela_str and x != 1:
            parcela_replace = parcela_str.replace(',', '.')
            parcela = float(parcela_replace)
            v = 1
        if v != 1:
            parcela = float(parcela_str)
        v = 0
        x = 0
        # -------------------------
        tax = int(input('\nQUAL TAXA SERÁ UTILIZADA?'
                        '\n1,38 > 0'
                        '\n1,42 > 1'
                        '\n1,56 > 2'
                        '\n1,72 > 3'
                        '\n1,80 > 4'
                        '\nINFORME: '))
        print('Você selecionou a taxa {} do banco ITAÚ'.format(taxacetelem[tax]))
        # -------------------------
        lib_str = str(input('\nInforme o valor liberado: '))
        if '.' in lib_str:
            lib = float(lib_str)
            v = 1
            x = 1
        if ',' in lib_str and x != 1:
            lib_replace = lib_str.replace(',', '.')
            lib = float(lib_replace)
            v = 1
        if v != 1:
            lib = float(lib_str)
        v = 0
        x = 0
        # -------------------------
        if tax == 0:
            meta = lib * 20 / 100
        if tax == 1:
            meta = lib * 25 / 100
        if tax == 2:
            meta = lib * 35 / 100
        if tax == 3:
            meta = lib * 45 / 100
        if tax == 4:
            meta = lib * 55 / 100
        # -------------------------
        cerebro_meta.append(meta)
        cerebro_cliente_total.append(lib)
        soma_margem = sum(cerebro_margem)
        soma_cliente = sum(cerebro_cliente_total)
        soma_meta100 = sum(cerebro_meta)

        print('\nFOI DIGITADO O REFIN SEM REDUÇÃO DA PARCELA DE {:.2f} NA TAXA DE {} DO BANCO ITAÚ'
              '\nVALOR LIBERADO: {:.2f}'
              '\nMETA PREVISTA: {:.2f}'.format(parcela, taxacetelem[tax], lib, meta).replace('.', ','))

        end = int(input('\nREFIN FINALIZADO, DESEJA ENCERRAR A DIGITAÇÃO? '
                        '\nSIM > 1'
                        '\nNÃO > 2'
                        '\nINFORME: '))
        if end == 1:
            print('\nMARGEM TOTAL ABERTA: {:.0f}'
                  '\nVALOR TOTAL LIBERADO PARA O CLIENTE: {:.2f}'
                  '\nMETA TOTAL PREVISTA: {:.2f}'.format(soma_margem, soma_cliente, soma_meta100).replace('.', ','))

            print('\n'
                  'FINALIZANDO PROGRAMA...')
            sleep(5)
            print('FINALIZADO!')
            print('\n')

            cerebro_margem.clear()
            cerebro_lib_margem.clear()
            cerebro_cliente_total.clear()
            cerebro_meta.clear()

    # REFIN SAFRA NORMAL
    if tabela == 6:
        v = 0
        x = 0
        troco = 100
        #-------------------
        parcela_str = str(input('Valor da parcela ATUAL: '))
        if '.' in parcela_str:
            parcela = float(parcela_str)
            v = 1
            x = 1
        if ',' in parcela_str and x != 1:
            parcela_replace = parcela_str.replace(',', '.')
            parcela = float(parcela_replace)
            v = 1
        if v != 1:
            parcela = float(parcela_str)
        v = 0
        x = 0
        #-------------------
        parcela2_str = str(input('Valor da parcela REDUZIDA: '))
        if ',' in parcela2_str:
            parcela2_replace = parcela2_str.replace(',', '.')
            parcela2 = float(parcela2_replace)
            v = 1
        if '.' in parcela2_str:
            parcela2 = float(parcela2_str)
            x = 1
            v = 1
        if v != 1:
            parcela2 = float(parcela2_str)

        # MARGEM
        margem = parcela - parcela2
        margem_true = floor(margem)
        cerebro_margem.append(margem_true)
        # VALOR LIBERADO COM A MARGEM
        lib_margem = margem_true / 0.0244
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
                '\nVALOR DO TROCO: {:.2f}'
                '\nTOTAL LIBERADO: {:.2f}'
                '\nMETA PREVISTA: {:.2f}'.format(parcela, margem_true, parcela2, lib_margem, troco, cliente_total, meta).replace('.', ','))
        end = int(input('\nREFIN FINALIZADO, DESEJA ENCERRAR A DIGITAÇÃO? '
                        '\nSIM > 1'
                        '\nNÃO > 2'
                        '\nINFORME: '))
        soma_margem = sum(cerebro_margem)
        soma_cliente = sum(cerebro_cliente_total)
        soma_meta100 = sum(cerebro_meta)
        if end == 1:
            print('\nMARGEM TOTAL ABERTA: {:.0f}'
                    '\nVALOR TOTAL LIBERADO PARA O CLIENTE: {:.2f}'
                    '\nMETA TOTAL PREVISTA: {:.2f}'.format(soma_margem, soma_cliente, soma_meta100).replace('.', ','))

            print('\n'
                    'FINALIZANDO PROGRAMA...')
            sleep(5)
            print('FINALIZADO!')
            print('\n')

            cerebro_margem.clear()
            cerebro_lib_margem.clear()
            cerebro_cliente_total.clear()
            cerebro_meta.clear()

    # REFIN SAFRA COTAÇÃO
    if tabela == 7:
        v = 0
        x = 0
        troco = 250
        # PARCELA REFIN SAFRA
        parcela_str = str(input('Valor da parcela ATUAL: '))
        if '.' in parcela_str:
            parcela = float(parcela_str)
            v = 1
            x = 1
        if ',' in parcela_str and x != 1:
            parcela_replace = parcela_str.replace(',', '.')
            parcela = float(parcela_replace)
            v = 1
        if v != 1:
            parcela = float(parcela_str)
        v = 0
        x = 0
        # REDUÇÃO DA RECUP
        parcela2_str = str(input('Valor da parcela REDUZIDA: '))
        if ',' in parcela2_str:
            parcela2_replace = parcela2_str.replace(',', '.')
            parcela2 = float(parcela2_replace)
            v = 1
        if '.' in parcela2_str:
            parcela2 = float(parcela2_str)
            x = 1
            v = 1
        if v != 1:
            parcela2 = float(parcela2_str)

        # MARGEM
        margem = parcela - parcela2
        margem_true = floor(margem)
        cerebro_margem.append(margem_true)
        # VALOR LIBERADO COM A MARGEM
        lib_margem = margem_true / 0.0244
        cerebro_lib_margem.append(lib_margem)
        # VALOR LIBERADO TOTAL
        cliente_total = lib_margem + troco
        cerebro_cliente_total.append(cliente_total)
        # META
        meta = lib_margem + troco
        cerebro_meta.append(meta)
        meta50 = lib_margem / 2 + troco
        # PRINT DO REFIN SAFRA NORMAL
        print('\nFOI DIGITADO O REFIN/COTAÇÃO DA PARCELA DE {:.2f} DO SAFRA, ABRINDO {:.0f} DE MARGEM, NA TAXA DE: '
                '\nPARCELA REDUZIDA: {:.2f}'
                '\nVALOR DA MARGEM: {:.2f}'
                '\nVALOR DO TROCO: {:.2f}'.format(parcela, margem_true, parcela2, lib_margem, troco).replace('.', ','))

        end = int(input('\nREFIN FINALIZADO, DESEJA ENCERRAR A DIGITAÇÃO? '
                        '\nSIM > 1'
                        '\nNÃO > 2'
                        '\nINFORME: '))

        soma_margem = sum(cerebro_margem)
        soma_cliente = sum(cerebro_cliente_total)
        soma_meta100 = sum(cerebro_meta)
        if end == 1:
            print('\nMARGEM TOTAL ABERTA: {:.0f}'
                    '\nVALOR TOTAL LIBERADO PARA O CLIENTE: {:.2f}'
                    '\nMETA TOTAL PREVISTA: {:.2f}'.format(soma_margem, soma_cliente, soma_meta100).replace('.', ','))

            print('\n'
                    'FINALIZANDO PROGRAMA...')
            sleep(5)
            print('FINALIZADO!')
            print('\n')

            cerebro_margem.clear()
            cerebro_lib_margem.clear()
            cerebro_cliente_total.clear()
            cerebro_meta.clear()

    # REFIN NORMAL OLÉ
    if tabela == 8:
        v = 0
        x = 0
        # PARCELA DO REFIN OLÉ
        parcela_str = str(input('Valor da parcela ATUAL: '))
        if '.' in parcela_str:
            parcela = float(parcela_str)
            v = 1
            x = 1
        if ',' in parcela_str and x != 1:
            parcela_replace = parcela_str.replace(',', '.')
            parcela = float(parcela_replace)
            v = 1
        if v != 1:
            parcela = float(parcela_str)
        v = 0
        x = 0
        # SALDO DO REFIN OLÉ
        saldo_str = str(input('Valor do saldo devedor: '))
        if ',' in saldo_str:
            saldo_replace = saldo_str.replace(',', '.')
            saldo = float(saldo_replace)
            ole_sld = saldo * 1.043
            troco = ole_sld - saldo
            x = 1
            v = 1
        if '.' in saldo_str:
            saldo = float(saldo_str)
            v = 1
            ole_sld = saldo * 1.043
            troco = ole_sld - saldo
        if v != 1:
            saldo = float(saldo_str)
            ole_sld = saldo * 1.043
            troco = ole_sld - saldo
        v = 0
        x = 0
        print('Saldo devedor pro refin olé: {:.2f}\nTroco: {:.2f}'.format(ole_sld, troco).replace('.', ','))
        # REDUÇÃO DO REFIN OLÉ
        parcela2_str = str(input('Valor da parcela REDUZIDA: '))
        if ',' in parcela2_str:
            parcela2_replace = parcela2_str.replace(',', '.')
            parcela2 = float(parcela2_replace)
            v = 1
        if '.' in parcela2_str:
            parcela2 = float(parcela2_str)
            x = 1
            v = 1
        if v != 1:
            parcela2 = float(parcela2_str)

        # MARGEM
        margem = parcela - parcela2
        margem_true = floor(margem)
        cerebro_margem.append(margem_true)
        # VALOR LIBERADO COM A MARGEM
        lib_margem = margem_true / 0.0244
        cerebro_lib_margem.append(lib_margem)
        # VALOR LIBERADO TOTAL
        cliente_total = lib_margem + troco
        cerebro_cliente_total.append(cliente_total)
        # META
        meta = lib_margem + troco
        cerebro_meta.append(meta)
        meta50 = lib_margem / 2 + troco
        # PRINT DO REFIN SAFRA NORMAL
        print('\nFOI DIGITADO O REFIN DA PARCELA DE {:.2f} DO OLÉ, ABRINDO {:.0f} DE MARGEM'
                '\nPARCELA REDUZIDA: {:.2f}'
                '\nVALOR DA MARGEM: {:.2f}'
                '\nVALOR DO TROCO: {:.2f}'.format(parcela, margem_true, parcela2, lib_margem, troco).replace('.', ','))
        end = int(input('\nREFIN FINALIZADO, DESEJA ENCERRAR A DIGITAÇÃO? '
                        '\nSIM > 1'
                        '\nNÃO > 2'
                        '\nINFORME: '))

        soma_margem = sum(cerebro_margem)
        soma_cliente = sum(cerebro_cliente_total)
        soma_meta100 = sum(cerebro_meta)

        if end == 1:
            print('\nMARGEM TOTAL ABERTA: {:.0f}'
                    '\nVALOR TOTAL LIBERADO PARA O CLIENTE: {:.2f}'
                    '\nMETA TOTAL PREVISTA: {:.2f}'.format(soma_margem, soma_cliente, soma_meta100).replace('.', ','))

            print('\n'
                    'FINALIZANDO PROGRAMA...')
            sleep(5)
            print('FINALIZADO!')
            print('\n')

            cerebro_margem.clear()
            cerebro_lib_margem.clear()
            cerebro_cliente_total.clear()
            cerebro_meta.clear()
