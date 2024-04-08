# Kods ir izveidots pēc minimax.py parauga, izņemot šoreiz ir divi citi mainīgie - alpha un beta

def AlphaBeta(akmentini, punkti, max_speletajs, alpha, beta):
    if akmentini == 0:
        return punkti, 0

    if max_speletajs:
        maxNovert = float('-inf')
        alpha = float('-inf')
        beta = float('inf')
        labakais_gaj = None
        for gajiens in [2,3]:
            if akmentini >= gajiens:
                atlikusie_akmentini = akmentini - gajiens
                punkti_jaunie = punkti + gajiens 

                if atlikusie_akmentini % 2 == 0:
                    punkti_jaunie += 2
                else:
                    punkti_jaunie -= 2

                novertejums = AlphaBeta(atlikusie_akmentini, punkti_jaunie, False, alpha, beta)[0]
                if novertejums > maxNovert:
                    maxNovert = novertejums
                    labakais_gaj = gajiens

                alpha = max(alpha, novertejums)
                if beta <= alpha:
                    break

        return maxNovert, labakais_gaj
    else:
        minNovert = float('inf')
        labakais_gaj = None
        for gajiens in [2,3]:
            if akmentini >= gajiens:
                atlikusie_akmentini = akmentini - gajiens
                punkti_jaunie = punkti + gajiens 

                if atlikusie_akmentini % 2 == 0:
                    punkti_jaunie += 2
                else:
                    punkti_jaunie -= 2

                novertejums = AlphaBeta(atlikusie_akmentini, punkti_jaunie, True, alpha, beta)[0]
                if novertejums < minNovert:
                    minNovert = novertejums
                    labakais_gaj = gajiens

                beta = min(beta, novertejums)
                if beta <= alpha:
                    break

        return minNovert, labakais_gaj
