T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    prices = list(map(int,input().split()))

    max_price = 0
    profit=0
    while prices:
        price = prices.pop()

        if max_price< price:
            max_price=price
        else:
            profit+= (max_price-price)
    
    print(f'#{test_case} {profit}')