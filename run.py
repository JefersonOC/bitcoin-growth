# Ano em que a rede foi iniciada por Satoshi Nakamoto
START_YEAR = 2009
# Intervalo de anos com blocos de 10 minutos
YEAR_INTERVAL = 4
# A recompensa inical de 50 bitcoins em satoshis
START_BLOCK_REWARD = 50 * 10**8
# Intervalo de blocos entre o halving da recompensa
REWARD_INTERVAL = 210 * 10**3


def show_mine_progress():
    curr_year = START_YEAR
    curr_reward = START_BLOCK_REWARD
    total_coins = 0
    while curr_reward > 0:
        print("Ano: %d, Recompensa atual: %d, Moedas em circulação: %d satoshis" %
              (curr_year, curr_reward, total_coins))
        # O número de moedas é somado com todas as recompensas de 210000 blocos
        # gerados em 4 anos
        total_coins += curr_reward * REWARD_INTERVAL
        curr_year += YEAR_INTERVAL
        # empurra os bits para a direita uma vez, efetivamente dividindo
        # a recompensa pela metade.
        # Ex.: 4 em binário (100) com os bits empurrados para a
        # direita será 2 (010)
        curr_reward >>= 1
    print("\nTotal de moedas em circulação: %d satoshis" % total_coins)


show_mine_progress()
