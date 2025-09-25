def mysterious_present(n , w, h):
    cards = list()
    for nth in range(1, n+1):
        card = input().strip().split(" ")
        w_n, h_n = map(int, card)
        if w_n > w and h_n > h:
            cards.append([nth , w_n, h_n])
    
    for i in range(len(cards)):
        _, width_i, heigth_i = cards[i]
        for j in range(i, len(cards)):
            _, width_j, heigth_j = cards[j]
            if width_i > width_j and heigth_i > heigth_j:
                cards[i], cards[j] = cards[j], cards[i]
            elif width_i == width_j and heigth_i > heigth_j:
                cards[i], cards[j] = cards[j], cards[i]
            elif width_i == width_j and heigth_i == heigth_j:
                cards[j][0] = cards[i][0]
    
    result = []
    for i in range(len(cards)):
        n_0, x_0, y_0 = cards[0]
        pivot = [n_0, x_0, y_0]
        
        for card in cards:
            if pivot == card:
                continue
            if pivot[1] > card[1] and pivot[2] > card[2]:
                pivot = card
            elif pivot[1] == card[1] and pivot[2] > card[2]:
                pivot = card

        cards.remove(pivot)
        if pivot not in result and result == []:
            result.append(pivot)
        else:
            valid = True
            for card in result:
                if card[2] == pivot[2] or card[1] == pivot[1]:
                    valid = False
                    break
            if valid:
                result.append(pivot)

            
    print(len(result))
    output = [str(nth) for nth, _, _ in result if True]
    print(" ".join(output))
    

first_input = input().strip().split(" ")
n, w, h = map(int, first_input)
if 1 <= n <= 5000 and 1 <= w and h <= 10**6:
    mysterious_present(n, w, h)
