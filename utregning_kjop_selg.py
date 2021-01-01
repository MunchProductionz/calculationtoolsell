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