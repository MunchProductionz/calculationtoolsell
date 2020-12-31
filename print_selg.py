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


