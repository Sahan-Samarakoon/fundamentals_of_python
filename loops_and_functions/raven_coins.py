found_coins = 20
magic_coins = 70
stolen_coins = 3
coins = found_coins
for i in range(1,53):
    coins = coins + magic_coins - stolen_coins
    print("%s week:%s" % (i,coins) )
