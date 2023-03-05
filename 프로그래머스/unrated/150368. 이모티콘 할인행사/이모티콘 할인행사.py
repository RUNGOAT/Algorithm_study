def solution(users, emoticons):
    global max_join, max_sale
    N, M = len(users), len(emoticons)
    discount_list = [0] * M
    max_join = max_sale = 0
    
    def check():
        join = sale = 0
        for rate, cost in users:
            purchase = 0
            for m in range(M):
                discount = discount_list[m]
                if rate <= discount:
                    purchase += (emoticons[m] * (100 - discount)) // 100
            if cost <= purchase:
                join += 1
            else:
                sale += purchase
        return join, sale
                
    
    def dfs(idx):
        global max_join, max_sale
        if idx == M:
            join, sale = check()
            if (max_join, max_sale) < (join, sale):
                max_join, max_sale = join, sale
            return
        for discount in [10, 20, 30, 40]:
            discount_list[idx] = discount
            dfs(idx + 1)
            
    dfs(0)
    return [max_join, max_sale]