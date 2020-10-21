for _ in range(int(input())):
    answer = 0
    budget = []
    items,purchases = map(int, input().split())
    
    for i in range(items): # Build list of categories
        category,PST,GST,HST = input().split()
        budget += [[category,int(PST[:-1]),int(GST[:-1]),int(HST[:-1])]]

    for j in range(purchases): # Cross-reference categories to calculate difference in tax
        category,price = input().split()
        price = float(price[1:])
        answer += budget[budget[0].index(category)][3] - (budget[budget[0].index(category)][1] + budget[budget[0].index(category)][2])
    print(answer)
