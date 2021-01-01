from formating import f2

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


