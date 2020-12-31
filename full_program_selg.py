
#Formating
def f0 (tall):
    return format(tall, '.0f')
def f1 (tall):
    return format(tall, '.1f')
def f2 (tall):
    return format(tall, '.2f')


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
    ordrestorrelse_f = liste_utregning_kjop[0]
    ordrestorrelse_prosent_f = liste_utregning_kjop[1]
    avg_entry_f = liste_utregning_kjop[5]
    stoploss_f = liste_utregning_kjop[6]
    antall_kjop = liste_utregning_kjop[7]

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
    avg_pt = sum_pts / antall_selg
    avg_pt_f = f2(avg_pt)
    

    #Utregning

    #Total profit %
    profit_prosent = ((avg_pt / avg_entry_f) - 1) * 100
    profit_prosent_f = f2(profit_prosent)
    profit = (profit_prosent / 100) * ordrestorrelse_f
    profit_f = f0(profit)
    total_profit_prosent = profit_prosent * (ordrestorrelse_prosent_f)
    total_profit_prosent_f = f2(total_profit_prosent)

    #Risiko av total %
    risiko_total_f = liste_utregning_kjop[4]

    #Risk / Reward
    risk_reward = total_profit_prosent / risiko_total_f
    risk_reward_f = f2(risk_reward)

    #EOC
    eoc = float((total_profit_prosent / ordrestorrelse_prosent_f) * 100)
    eoc_f = f2(eoc)


    #Outputs
    oversikt.append(total_profit_prosent_f)
    oversikt.append(risiko_total_f)
    oversikt.append(risk_reward_f)
    oversikt.append(eoc_f)
    oversikt.append(avg_pt_f)
    oversikt.append(avg_entry_f)
    oversikt.append(antall_kjop)
    oversikt.append(antall_selg)
    oversikt.append(profit_f)
    oversikt.append(profit_prosent_f)

    return oversikt


#Print_selg
def print_selg (liste):

    #Inputs
    total_profit_prosent_f = liste[0]
    risiko_total_f = liste[1]
    risk_reward_f = liste[2]
    eoc_f = liste[3]
    avg_pt_f = liste[4]
    avg_entry_f = liste[5]
    antall_kjop = liste[6]
    antall_selg = liste[7]
    profit_f = liste[8]
    profit_prosent_f = liste[9]

    #Outputs
    print(f'Total profit %: {total_profit_prosent_f}')
    print(f'Risiko av total %: {risiko_total_f}%')
    print(f'Risk / Reward: {risk_reward_f}')
    print(f'EOC: {eoc_f}%')
    print()
    print(f'PT: {avg_pt_f}')
    print(f'Entry: {avg_entry_f}')
    print(f'Antall kjøpt: {antall_kjop}')
    print(f'Antall solgt: {antall_selg}')
    print(f'Profit: {profit_f}')
    print(f'Profit %: {profit_prosent_f}%')
    
    
#Main_selg
def main ():
    print_selg(utregning_selg(utregning_kjop))
    

main()