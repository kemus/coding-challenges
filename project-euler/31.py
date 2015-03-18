def coiner(amount, coins):
    ways = {0:1}
    for coin in coins:
        for j in xrange(coin, amount+1):
            if j in ways:
                ways[j]+=ways[j-coin]
            else:
                ways[j] = ways[j-coin]
    return ways[amount]
print coiner(200, [1,2,5,10,20,50,100,200])
