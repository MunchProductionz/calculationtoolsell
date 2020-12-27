def print_selg (liste):

    #Inputs
    ordrestørrelse = liste[0]
    ordrestørrelse_prosent_f = liste[1]
    risiko = liste[2]
    risiko_prosent_f = liste[3]
    risiko_total_f = liste[4]

    #Outputs
    print(f'Kjøpsum: {ordrestørrelse}')
    print(f'Kjøpsum av kapital: {ordrestørrelse_prosent_f}%')
    print(f'Risiko ved handel: {risiko} kr')
    print(f'Risiko ved handel: {risiko_prosent_f}%')
    print(f'Risiko av total: {risiko_total_f}%')

