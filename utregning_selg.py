from formating import f2

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
    for order in entries:
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
    avg_pt_f = formating.f2(avg_pt)
    

    #Utregning

    #Total profit %
    profit_prosent = ((avg_pt / avg_entry_f) - 1) * 100
    profit_prosent_f = formating.f2(profit_prosent)
    profit = (profit_prosent / 100) * ordrestorrelse_f
    profit_f = formating.f2(profit)
    total_profit_prosent = profit_prosent * (ordrestorrelse_prosent_f)
    total_profit_prosent_f = formating.f2(total_profit_prosent)

    #Risiko av total %
    risiko_total_f = liste_utregning_kjop[4]

    #Risk / Reward
    risk_reward = total_profit_prosent / risiko_total_f
    risk_reward_f = formating.f2(risk_reward)

    #EOC
    eoc = float((total_profit_prosent / ordrestorrelse_prosent_f) * 100)
    eoc_f = formating.f2(eoc)


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


