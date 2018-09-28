# PRIMEIRO PROGRAMA BASICO PYTHON, SISTEMA MEDIA DE ALUNO

# PEGAR AS NOTAS DOS ALUNOS
nota1 = float(input("Primeira Nota"))
nota2 = float(input("Segunda Nota"))
# FAZER MA MEDIA DAS 2 NOTAS
media = ((nota1 + nota2)/2)

# PRIMEIRAMENTE, SE A MEDIA FOR MAIOR Q 10, O ALUNO TA USANO HACK
if media > 10:
    print('deus ta vendo essa zoeira eim, como q vc tirou ',media, '???')
# SE A MEDIA FOR IGUAL OU MAIOR Q 7 ELE PASSA TRANQUILAMENTE
elif media >= 7:
    print('parabainx, vc passou com: ', media, ' Pontos')
# CASO ELE TIRE UMA NOTA Q DE PARA RECUPERAR, ELE PDOE OPTAR POR FAZER OU N A REC
elif media >= 2:
    print('vc tirou: ',media)
    recuperation = str(input('c ta na pior, deseja fazer recuperação ? S ou N ')).strip().upper()
# CASO ELE ACEITE, TERÁ UMA NOVA NOTA E ESTA SE SOMARÁ A MEDIA, ASSIM CRIANDO NOVA MEDIA
    if recuperation == 'S' or recuperation == 'SIM':
        novaNota = float(input('Nota da REC'))
        novaMedia = ((novaNota + media)/2)
        if novaMedia > 10:
            print('deus ta vendo essa zoeira eim, como q vc tirou ',novaMedia, '???')
        elif novaMedia >= 7:
            print('Parabainx, vc recuperou-se com: ', novaMedia)
        else:
            print('N foi hj, Mas vc tentou pelo menos')
    else:
        print('vergonhaaa, disgraçaaa, pra toda uma raça')
# SE ELE TIROU UMA NOTA Q N DA PARA RECUPERAR, NEM APARECE A OPÇÃO REC
else:
    print('vc falhou mizeravelmente, nem deus te salva :p')