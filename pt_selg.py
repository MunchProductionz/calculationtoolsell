#order = [price, amount]
#orders = [[price_1, amount_1], [price_2, amount_2], ...]

def selg ():
    print('Vennligst skriv inn ønsket PT.')
    print('Skriv inn PT på formen "<pris> <antall>".')

    orders = []
    order = input('PT 1: ').split()
    orders.append(order)
    counter = 1
    
    while True:
        counter += 1
        order = input(f'PT {counter}: ').split()
        if not order:
            break
        orders.append(order)
        
    return orders