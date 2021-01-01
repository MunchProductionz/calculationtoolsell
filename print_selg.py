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


