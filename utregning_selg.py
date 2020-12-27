from formating import f2

def utregning_selg (liste_utregning_kjøp):
    oversikt = []

    #Inputs
    print('Vennligst skriv inn ønsket ordre.')
    pt = float(input('Pris per aksje: '))
    antall_selg = int(input('Antall aksjer: '))
    ordrestørrelse_prosent = liste_utregning_kjøp[1]
    entry = liste_utregning_kjøp[5]
    antall_kjøp = liste_utregning_kjøp[6]
    

    #Utregning

    #Total profit %
    profit = antall_selg * (pt - entry)
    profit_f = formating.f2(profit)
    profit_prosent = profit_f / (entry * antall_kjøp)
    profit_prosent_f = formating.f2(profit_prosent)
    total_profit_prosent = profit_prosent * (ordrestørrelse_prosent)
    total_profit_prosent_f = formating.f2(total_profit_prosent)

    #Risiko av total %
    risiko_total_f = liste_utregning_kjøp[4]

    #Risk / Reward
    risk_reward = total_profit_prosent_f / risiko_total_f
    risk_reward_f = formating.f2(risk_reward)

    #EOC
    eoc = float((total_profit_prosent / ordrestørrelse_prosent) * 100)
    eoc_f = formating.f2(eoc)


    #Outputs
    oversikt.append(total_profit_prosent_f)
    oversikt.append(risiko_total_f)
    oversikt.append(risk_reward_f)
    oversikt.append(eoc_f)
    oversikt.append(pt)
    oversikt.append(entry)
    oversikt.append(antall_selg)
    oversikt.append(profit_f)
    oversikt.append(profit_prosent_f)

    return oversikt


