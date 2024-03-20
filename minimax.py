
#tiek definēta funkcija 
#akemntini --> norāda akmentiņu skaitu uz galda
#punkti --> pašreizējais punktu skaits
#max_speletajs --> pašreizējais spēlētājs ir maksimizējošais spēlētājs

def MiniMax(akmentini,punkti,max_speletajs):

    #parbaude vai uz galda nav akmentiņu
    #ja nav, tad funkcija beidzas un atgriež pašreizējo punktu skaitu
    if akmentini == 0:
        return punkti,0
    
    #ja tagadējais spēlētājs ir max, tiek inicializēts mainīgais maxNovert ar negatīvu bezgalību, lai nākamā novērtējuma vērtība būtu lielāka
    if max_speletajs:
        maxNovert= float('-inf')
        #tiek ņemts vērā labākais gajiens
        labakais_gaj = None
        #cikls iet cauri iespējamajiem gājieniem - paņemt 2 vai 3 akmeņus
        for gajiens in [2,3]:
            if akmentini >= gajiens: #pārbauda, vai ir pietiekami daudz akmeņu, lai izpilditu gājienu
                atlikusie_akmentini = akmentini - gajiens #aprēķina atlikušo akmentiņu skaitu pēc gājiena
                punkti_jaunie = punkti + gajiens # Tiek pievienoti paņemtie akmentiņi pie punktiem
            
            #Ja atlikušais akmentiņu skaits ir pāra skaitlis, tad pievieno 2 punktus, ja nepāra - noņem 2 punktus
                if atlikusie_akmentini % 2 == 0:
                    punkti_jaunie += 2
                else:
                    punkti_jaunie -= 2
                
                #izsauc minimax funkciju ar jauno akmeņu skaitu un punktu skaitu, pārejot uz minimizējojšo spēlētāju
                novertejums = MiniMax(atlikusie_akmentini,punkti_jaunie,False)[0]
                #pārbauda, vai novērtējuma vērtība ir lielāka par maksimālo novērtējumu
                if novertejums > maxNovert:
                    maxNovert = novertejums
                    labakais_gaj = gajiens
        #atgriež maksimālo novērtējumu un labāko gājienu, kas veicams, lai sasniegtu šo novērtējumu
        return maxNovert, labakais_gaj
    else: #gājienu veic minimizējošais spēlētājs ar līdzīgu algoritmu, mēģinot minimizēt punktu skaitu
        maxNovert = float('inf')
        labakais_gaj = None
        for gajiens in [2,3]:
            if akmentini >= gajiens:
                atlikusie_akmentini = akmentini - gajiens
                punkti_jaunie = punkti + gajiens 
            
                if atlikusie_akmentini % 2 == 0:
                    punkti_jaunie += 2
                else:
                    punkti_jaunie -= 2
                
                novertejums = MiniMax(atlikusie_akmentini,punkti_jaunie,True)[0]
                if novertejums < minNovert:
                    minNovert = novertejums
                    labakais_gaj = gajiens

        return minNovert, labakais_gaj
    

