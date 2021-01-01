
#Formating
def f0 (tall):
    return format(tall, '.0f')
def f1 (tall):
    return format(tall, '.1f')
def f2 (tall):
    return format(tall, '.2f')

#Entries_kjop
def kjop ():
    print('Vennligst skriv inn ønsket ordre.')
    print('Skriv inn ordre på formen "<pris> <antall>".')

    orders = []
    order = input('Order 1: ').split()
    orders.append(order)
    counter = 1
    
    while True:
        counter += 1
        order = input(f'Order {counter}: ').split()
        if not order:
            break
        orders.append(order)
        
    return orders


#Utregning_kjop
def utregning_kjop ():
    oversikt = []
    minste_kurtasje = 29
    prosent_kurtasje = 0.00005
    prosent_justering = 100

    #Inputs

    #Entries
    entries = kjop()
    sum_entries = 0
    sum_antall = 0
    for order in entries:
        ordersum = float(order[0])*int(order[1])
        kurtasje = 0
        
        if ordersum < 50000:
            kurtasje = minste_kurtasje
        else:
            kurtasje = ordersum * prosent_kurtasje
        
        sum_entries += ordersum + kurtasje          #Problem
        sum_antall += int(order[1])
    
    antall = sum_antall
    avg_entry = sum_entries / antall
    avg_entry_f = f2(avg_entry)

    print()
    
    #Stoploss
    stoploss = float(input('Stoploss-pris per aksje: '))
    stoploss_f = f2(stoploss)
    
    #Kapital
    kapital = float(input('Tilgjengelig kapital: '))
    
    print()
    print()



    #Utregning
    
    #Ordrestorrelse
    ordrestorrelse = avg_entry * antall
    ordrestorrelse_f = f0(ordrestorrelse)
    ordrestorrelse_prosent = (ordrestorrelse / kapital) * prosent_justering
    ordrestorrelse_prosent_f = f2(ordrestorrelse_prosent)

    #Risiko %
    risiko_prosent = (1 - (stoploss / avg_entry)) * prosent_justering         #risiko_prosent = (1 - (stoploss /avg_entry))
    risiko_prosent_f = f2(risiko_prosent)
    risiko = (risiko_prosent / prosent_justering) * ordrestorrelse            #risiko = risiko_prosent * ordrestorrelse
    risiko_f = f0(risiko)         

    #Risiko av total %
    risiko_total_prosent = (risiko_prosent * ordrestorrelse_prosent) / prosent_justering
    risiko_total_prosent_f = f2(risiko_total_prosent)


    #Outputs
    oversikt.append(ordrestorrelse_f)
    oversikt.append(ordrestorrelse_prosent_f)
    oversikt.append(risiko_f)
    oversikt.append(risiko_prosent_f)
    oversikt.append(risiko_total_prosent_f)
    oversikt.append(avg_entry_f)
    oversikt.append(stoploss_f)
    oversikt.append(antall)

    return oversikt


#PT_selg
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


#Utregning_selg
def utregning_selg (liste_utregning_kjop):
    oversikt = []
    minste_kurtasje = 29
    prosent_kurtasje = 0.00005    

    #Inputs
    ordrestorrelse_f = int(liste_utregning_kjop[0])
    ordrestorrelse_prosent_f = float(liste_utregning_kjop[1])
    avg_entry_f = float(liste_utregning_kjop[5])
    stoploss_f = float(liste_utregning_kjop[6])
    antall_kjop = int(liste_utregning_kjop[7])

    pts = selg()
    sum_pts = 0
    sum_antall = 0
    for order in pts:
        ordersum = float(order[0])*int(order[1])
        kurtasje = 0
        
        if ordersum < 50000:
            kurtasje = minste_kurtasje
        else:
            kurtasje = ordersum*prosent_kurtasje
        
        sum_pts += ordersum - kurtasje          #Problem
        sum_antall += int(order[1])

    antall_selg = sum_antall
    avg_pt = float(sum_pts / antall_selg)
    avg_pt_f = f2(avg_pt)
    

    #Utregning

    #Total profit %
    profit_prosent = float(((avg_pt / avg_entry_f) - 1) * 100)
    profit_prosent_f = f2(profit_prosent)
    profit = (profit_prosent / 100) * ordrestorrelse_f
    profit_f = f0(profit)
    total_profit_prosent = (profit_prosent * (ordrestorrelse_prosent_f)) / 100
    total_profit_prosent_f = f2(total_profit_prosent)

    #Risiko av total %
    risiko_total_f = float(liste_utregning_kjop[4])

    #Risk / Reward
    risk_reward = total_profit_prosent / risiko_total_f
    risk_reward_f = f2(risk_reward)

    #EOC
    eoc = float((total_profit_prosent / ordrestorrelse_prosent_f) * 100)
    eoc_f = f2(eoc)


    #Outputs
    oversikt.append(profit_f)
    oversikt.append(profit_prosent_f)
    oversikt.append(total_profit_prosent_f)
    oversikt.append(risiko_total_f)
    oversikt.append(risk_reward_f)
    oversikt.append(eoc_f)
    oversikt.append(avg_pt_f)
    oversikt.append(avg_entry_f)
    oversikt.append(stoploss_f)
    oversikt.append(antall_kjop)
    oversikt.append(antall_selg)


    return oversikt


#Print_selg
def print_selg (liste):

    #Inputs
    profit_f = liste[0]
    profit_prosent_f = liste[1]
    total_profit_prosent_f = liste[2]
    risiko_total_f = liste[3]
    risk_reward_f = liste[4]
    eoc_f = liste[5]
    avg_pt_f = liste[6]
    avg_entry_f = liste[7]
    stoploss_f = liste[8]
    antall_kjop = liste[9]
    antall_selg = liste[10]


    print()


    #Outputs
    print(f'Profit: {profit_f} kr')
    print(f'Profit ved handel %: {profit_prosent_f}%')
    print(f'Profit av total %: {total_profit_prosent_f}%')
    print(f'Risiko av total %: {risiko_total_f}%')
    print()
    print(f'Risk / Reward: {risk_reward_f}')
    print(f'EOC: {eoc_f}')
    print()
    print(f'PT: {avg_pt_f} kr')
    print(f'Entry: {avg_entry_f} kr')
    print(f'Stoploss: {stoploss_f} kr')
    print(f'Antall kjøpt: {antall_kjop}')
    print(f'Antall solgt: {antall_selg}')

      
#Main_selg
def main ():
    print_selg(utregning_selg(utregning_kjop()))
    

main()