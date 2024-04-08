#izveido virsotnes objektu
class Virs:
    #pieskir virsotnei atributus
    def __init__(self, id ,akmenuSk, p1, a1, p2, a2, lvl):
        self.id = id
        self.akmenuSk = akmenuSk
        self.p1 = p1
        self.a1 = a1
        self.p2 = p2
        self.a2 = a2
        self.lvl = lvl
        

#izveido koka strukturu
class Koks:
    #pieskir kokam atributus, kuros glabat virsotnes un lokus
    def __init__(self):
        self.virsotnes = []
        self.loki = dict()

    #funkcija lai pievienotu virsotni virsotnu kopai
    def piev_virs(self, Virs):
        self.virsotnes.append(Virs)

    
    #funkcija lai pievienotu loku loku kopai
    def piev_loku(self, sVirs, bVirs):
        self.loki[sVirs] = self.loki.get(sVirs,[]) + [bVirs]


#funkcija kas apraksta speles gajienu. ka vertibas panem gajiena veidu (2akmeni vai 3), virsotnu kopu, virsotni, kura sobrid atrodas un speletaju, kurs sak gajienu
def gajiens(gTips, genVirs, pasrV):

#pasrV --> Pašreizējā virsotne
#genVirs --> uzģenerēto virsotņu kopa
#gTips --> gājiena tips (2 vai 3 akmeni nonemti)

    #ja akmeņi nav 0, tad izveido jaunas virsotnes id un aprekina tas akmenu skaitu
    if pasrV[1] - int(gTips) >= 0:
        global z
        jauns_ID = 'V' + str(z)
        jauni_akmeni = pasrV[1] - int(gTips)
        #virsotnes numurs
        z += 1

       


        #atjauno punktu skaitu balstoties uz speles noteikumiem atskiriba no gajiena
        #parbauda vai gajiena tips ir 2 vai 3
        if gTips == '2' or gTips == '3':
            #parbaude kas parbauda vai virsotnes atrodas viena limeni --> vai gajienu veica viens vai otrs speletajs
            if pasrV[6] % 2 != 0:
                #parbauda vai jaunas virsotnes akmenu skaits ir para vai nepara
                if (jauni_akmeni % 2) == 0 :
                    p1_jPunkti = pasrV[2] + 2
                    p2_jPunkti = pasrV[4] 
                    a1_jAkmeni = pasrV[3] + int(gTips)
                    a2_jAkmeni = pasrV[5]
                else:
                    p1_jPunkti = pasrV[2] - 2
                    p2_jPunkti = pasrV[4] 
                    a1_jAkmeni = pasrV[3] + int(gTips)
                    a2_jAkmeni = pasrV[5]
            else:
                if (pasrV[1] % 2 == 0):
                    p1_jPunkti = pasrV[2]
                    p2_jPunkti = pasrV[4] + 2
                    a1_jAkmeni = pasrV[3] 
                    a2_jAkmeni = pasrV[5] + int(gTips)
                elif (pasrV[1] % 2 != 0):
                    p1_jPunkti = pasrV[2]
                    p2_jPunkti = pasrV[4] - 2
                    a1_jAkmeni = pasrV[3] 
                    a2_jAkmeni = pasrV[5] + int(gTips)
        #ja gajiena tips nav 2 vai 3, tad jaunajam virsotnem pieskir pasreizejas virsotnes vertibas
        else:  
            p1_jPunkti = pasrV[2]
            p2_jPunkti = pasrV[4]
            a1_jAkmeni = pasrV[3] 
            a2_jAkmeni = pasrV[5]
                        
            

        #nosaka jaunas virsotnes limeni
        jauns_LVL = pasrV[6] + 1
        #pieskir jaunajai virsotnei atributu vertibas
        jauna_Virs = Virs(jauns_ID, jauni_akmeni, p1_jPunkti, a1_jAkmeni, p2_jPunkti, a2_jAkmeni, jauns_LVL)

        test = False
        #mainigais kas norada virsotnes kartas skaitli kopa
        k = 0

        #parbauda vai jauna virsotne jau pastav koka
        while (not test) and (k < len(spele.virsotnes) - 1):
            if(spele.virsotnes[k].akmenuSk == jauna_Virs.akmenuSk) and (spele.virsotnes[k].p1 == jauna_Virs.p1) and (spele.virsotnes[k].a1 == jauna_Virs.a1) and (spele.virsotnes[k].p2 == jauna_Virs.p2) and (spele.virsotnes[k].a2 == jauna_Virs.a2) and (spele.virsotnes[k].lvl == jauna_Virs.lvl):
                test = True
            else:
                k += 1
        #ja nepastav pievieno kokam gan virsotni gan loku
        if not test:
            spele.piev_virs(jauna_Virs)
            genVirs.append([jauns_ID, jauni_akmeni, p1_jPunkti, a1_jAkmeni, p2_jPunkti, a2_jAkmeni, jauns_LVL])
            spele.piev_loku(pasrV[0], jauns_ID)
     
        
        #ja pastav tad pievieno tikai papildus loku kas aizved uz so virsotni
        else: 
            z -= 1
            spele.piev_loku(pasrV[0], spele.virsotnes[k].id)
      

#mainigais kas aicina lietotaju ievadit sakotnejo akmenu skaitu
akmeni = int(input("ievadi sākotnējo akmentiņu skaitu\n"))

#parbaude vai lietotaja ievaditais skaitlis atbilst speles nosacijumiem
while akmeni > 70 or akmeni < 50:
    akmeni = int(input("Ievadi akmeņu skaitu no 50 līdz 70!\n"))


#izveido tuksu speles koku un pieskir to mainigajam spele
spele = Koks()

#izveido tuksu genereto virsotnu kopu (saja gadijuma sarakstu)
genVirs = []

#pievieno speles kokam sakotnejo virsotni
spele.piev_virs(Virs('V1', akmeni, 0, 0, 0, 0, 1))

#pievieno genereto virsotnu kopai sakotnejo virsotni
genVirs.append(['V1', akmeni, 0, 0, 0, 0, 1])

#2 jo V1 jau ir pievienots un ir nepieciesams nakamas virsotnes numurs V2, V3 utt. 
z = 2

#cikls kas iet cauri katrai generetajai virsotnei genereto virsotnu kopa
while len(genVirs) > 0:
    
    #pirma genereta virsotne saraksta klust par pasreiz apskatamo virsotni
    siVirs=genVirs[0]
    #gajiens kura speletajs nonem 2 akmentinus
    gajiens('2',genVirs,siVirs)
    #gajiens, kura speletajs nonem 3 akmentinus
    gajiens('3',genVirs,siVirs)
    #ja visi gajieni no virsotnes ir apskatiti tad dzes virsotni no genereto virsotnu kopas
    genVirs.pop(0)

#cikls kas izvada virsotnes un to atributu vertibas
for x in spele.virsotnes:
    print(x.id,x.akmenuSk,x.p1,x.a1,x.p2,x.a2,x.lvl)
#cikls kas izvada lokus
for x, y in spele.loki.items():
    print(x, y)   





################################
    # funkcija tiek definēta:
    #virsotne - pašreizējais speles stāvoklis
    #max_speletajs - norada, vai ir maksimizejosais speletajs
    #dzilums - gājienu dziļums
def MiniMax(virsotne,dzilums,max_speletajs):

    #parbaude vai uz galda nav akmentiņu vai ir sasniegts dziluma ierobezojums
    if virsotne.akmenuSk == 0 or dzilums == 0:

        return virsotne.p1 - virsotne.p2, None
    #ja tagadējais spēlētājs ir max, tiek inicializēts mainīgais maxNovert ar negatīvu bezgalību, lai nākamā novērtējuma vērtība būtu lielāka
    if max_speletajs:
        maxNovert= float('-inf')
        #tiek ņemts vērā labākais gajiens
        labakais_gajiens = None
        #cikls iet cauri iespējamajiem gājieniem - paņemt 2 vai 3 akmeņus
        for gajiens in [2,3]:
            if virsotne.akmenuSk >= gajiens: #pārbauda, vai ir pietiekami daudz akmeņu, lai izpilditu gājienu

                #izveidots jauns spēles stāvoklis pēc gājiena
                jauna_virsotne = Virs(0,virsotne.akmenuSk ,virsotne.p1,virsotne.a1,virsotne.p2,virsotne.a2,virsotne.lvl+1)
                #rekursivi izsauc funkciju ar jauno spēles stāvokli, parsledzoties uz min speletaju un samazinot dziļuma ierobežojumu
                vertiba = MiniMax(jauna_virsotne, dzilums - 1,False)[0]
                #atjaunina maksimalo novertējumu un labako gajienu, ja ir atrasta labāka vērtība
                if vertiba > maxNovert:
                    maxNovert = vertiba
                    labakais_gajiens = gajiens
        # atgriež maksimālo novērtējumu un labāko gajienu maksimizējošam speletajam
        return maxNovert, labakais_gajiens

    else: #gājienu veic minimizējošais spēlētājs ar līdzīgu algoritmu, mēģinot minimizēt punktu skaitu
        minNovert = float('inf')#sākotnējā vērtība ir +bezgalība
        #līdzigs cikls kā maksimizējošam spēlētājam
        for gajiens in [2,3]:
            if virsotne.akmenuSk >= gajiens:
                jauna_virsotne = Virs(0,virsotne.akmenuSk,virsotne.p1,virsotne.a1,virsotne.p2,virsotne.a2,virsotne.lvl+1)
               
                vertiba = MiniMax(jauna_virsotne,dzilums-1,True)[0]
                #atjaunina minimālo novērtējumu,ja ir atrasta mazākā vērtība
                if vertiba < minNovert:
                    minNovert = vertiba
                    labakais_gajiens= gajiens
        #atgriež minimālo novērtējumu, tiek atgriezta 0, jo nav nepieciešama labākā gājiena atgriešana
        return minNovert, 0
        
#########################################
# def AlphaBetaDriver inicializē alpha un beta vērtības, lai tās netiktu atkārtotas ik reizi, kad tiek izsaukta AlphaBeta() funkcija

def AlphaBetaDriver(virsotne, dzilums, max_speletajs): 
    alpha = float('-inf')
    beta = float('inf')
    return AlphaBeta(virsotne, dzilums, alpha, beta, max_speletajs)

def AlphaBeta(virsotne, dzilums, alpha, beta, max_speletajs):
    if virsotne.akmenuSk == 0 or dzilums == 0:
        return virsotne.p1 - virsotne.p2, None

    if max_speletajs:
        maxNovert = float('-inf')
        labakais_gajiens = None
        for gajiens in [2,3]:
            if virsotne.akmenuSk >= gajiens:
                jauna_virsotne = Virs(0,virsotne.akmenuSk ,virsotne.p1,virsotne.a1,virsotne.p2,virsotne.a2,virsotne.lvl+1)
                vertiba = AlphaBeta(jauna_virsotne, dzilums - 1, alpha, beta, False)[0]
                if vertiba > maxNovert:
                    maxNovert = vertiba
                    labakais_gajiens = gajiens
                alpha = max(alpha, vertiba) # Jaunā Alpha tiek izvēlēta starp pašreizējo alpha vērtību, vai izvēlēto alpha vērtību
                if beta <= alpha: # Alpha nekad nevar būt mazāks par beta
                    break
        return maxNovert, labakais_gajiens
    else:
        minNovert = float('inf')
        for gajiens in [2,3]:
            if virsotne.akmenuSk >= gajiens:
                jauna_virsotne = Virs(0,virsotne.akmenuSk,virsotne.p1,virsotne.a1,virsotne.p2,virsotne.a2,virsotne.lvl+1)
                vertiba = AlphaBeta(jauna_virsotne, dzilums - 1, alpha, beta, True)[0]
                if vertiba < minNovert:
                    minNovert = vertiba
                beta = min(beta, vertiba) # Jaunā Beta tiek izvēlēta starp pašreizējo beta vērtību, vai izvēlēto beta vērtību
                if beta <= alpha: # Alpha nekad nevar būt mazāks par beta
                    break
        return minNovert, 0

###################################

#funkcija ļauj spēlētājam izvēlēties, cik akmentiņus ņemt    
def speletajs():
    #izvēles ievade, kur spēlētājs izvēlās paņemt 2 vai 3 akmentiņus. tas tiek saglabats mainīgajā 'izv'
    izv = input("Izvēlies paņemt 2 vai 3 akmentiņus: ")
    #cikls pārbauda, vai ievadītā vērtība atbilst 2 vai 3. ja neatbilst,tad izvada kļūdu paziņojumu un liek atkal ievadīt vērtību
    while izv not in ['2', '3']:
        print("error")
        izv = input("Izvēlies paņemt 2 vai 3 akmentiņus: ")
        #atgriež spēlētāja izvēli kā vesela skaitla vertibu
    return int(izv)

# funkcija lauj izveleties,kurs sāks speli - speletajs vai dators
def saks_speli():
    #izveles ievade, kur tiek jautats, vai spēli saks speletajs vai dators. ievade saglabāta mainīgajā 'izvele'
    izvele = input("Vai spēli sāks spēlētājs (1) vai dators (2): ")
    #cikls pārbauda,vai vērtība 1 un 2 ir derīga. ja ievade nav derīga, tiek izvadits kļūdas paziņojums un liek ievadīt vēlreiz
    while izvele not in ['1','2']:
        print("error")
        izvele = input("Vai spēli sāks spēlētājs (1) vai dators (2): ")
        #atgriež galīgo izvēli
    return izvele

#funkcija ļauj izvēlēties, kāds algoritms tiks izmantots spēles gaitā - Minimax vai Alfa-beta
def algo_izvele():
#izvada uz ekrāna, ka ir jāizvēlas algortims
    print("Izvēlieties algoritmu:")
    #jāievada izvēle starp algoritmiem, ievade saglabāta mainīgajā 'izvele'
    izvele = input("Ievadiet M (Minimax) vai A (Alfa-beta): ")
    #cikls parbauda, vai ievadītā vērtība atbilst opcijām ('M' vai 'A'). Ja nav atbilstoša, tad izvada kļūdu un liek ievadīt vēlreiz
    while izvele not in ['M', 'A']:
        print("error")
        izvele= input("Ievadiet M vai A: ")
        #atgriež galīgo algoritma izvēli
    return izvele

#spēles galvenā funkcija
def play():
    #izsauc funkciju, kas noskaidro, kurš sāks spēli - spēlētājs vai dators
    uzsacejs = saks_speli()
    #tiek inicializēts sākotnējais spēles stāvoklis, izmantojot klasi Virs
    tagad_stavoklis = Virs('V1', akmeni, 0, 0, 0, 0, 1)
    #inicializē mainīgos ar 0, tie tiks izmantoti, lai sekotu līdzi abu spēlētāju punktiem
    speletaja_punkti = 0
    datora_punkti = 0 
    #izsauc funkciju, lai noskaidrotu, kādu algoritmu izmantos dators
    algoritms=algo_izvele()
    #uzsāk ciklu, kas turpināsies, kamēr spēlē ir atlikuši akmentiņi
    while tagad_stavoklis.akmenuSk > 0:
        # pārbauda, vai spēli sāks spēlētājs
        if uzsacejs == '1' or uzsacejs == '2' and tagad_stavoklis.akmenuSk <=0:
            #izvada atlikušo akmentiņu skaitu
            print(f"Atlikušie akmentiņi: {tagad_stavoklis.akmenuSk}")
            #izsauc funkciju, lai spēlētājs izvēlētos, cik akmentiņus paņemt
            spel_izvele = speletajs()
            #samazina kopējo akmeņu skaitu atkarībā no spēlētāja paņemtā akmeņu daudzuma
            tagad_stavoklis.akmenuSk -= spel_izvele
            #palielina spēlētāja punktu skaitu atkarībā, cik akmeņus spēlētājs paņēmis 
            speletaja_punkti += spel_izvele

            # pēc katras spēlētāja kartas tiek piešķirti vai atņemti punkti spēlētājam...
            #...atkarībā, vai uz galda palikuši akmentiņi pāra skaitā(tiek pieskaitīti klāt) vai nepāra skaitā(tiek noņemti)
            if tagad_stavoklis.akmenuSk % 2 == 0:
                speletaja_punkti += 2
            else:
                speletaja_punkti -= 2

            #tiek izvadīti pašreizējie rezultāti
            print(f"Tu paņēmi {spel_izvele} akmentiņus. Atlikušie akmeņi: {tagad_stavoklis.akmenuSk}")
            print(f"Spēlētāja punkti: {speletaja_punkti}, Datora punkti: {datora_punkti}")
            # pāriet uz datora kārtu
            uzsacejs = '2'
            
            #pārbauda, vai dators uzsāk spēli un ir izvēlēts Minimax algoritms
        if tagad_stavoklis.akmenuSk > 0 and uzsacejs == '2' and algoritms == 'M':
            dators_izvele = MiniMax(tagad_stavoklis, 10, True)[1]
            #tiek atjaunoti punkti un izvadīti pašreizējie rezultāti
            print (f"Dators paņem {dators_izvele} akmentiņus.")
            print(f"Spēlētāja punkti: {speletaja_punkti}, Datora punkti: {datora_punkti}")


        # elif tagad_stavoklis.akmenuSk > 0 and uzsacejs == '2' and algoritms == 'A':
          #  dators_izvele = Alfabeta()
           # print (f"Dators paņem {dators_izvele} akmentiņus.")
           # print(f"Spēlētāja punkti: {speletaja_punkti}, Datora punkti: {datora_punkti}")

        #nosaka, ja dators ir veicis pieļaujamo izvēli pirms spēles stāvokļa atjaunināšanas
        if dators_izvele is not None:   
            #samazinās akmeņu skaits pēc datora izvēlētā akmentiņu skaita
            tagad_stavoklis.akmenuSk -= dators_izvele
            #palielina punktu skaitu datoram, cik dators ir paņēmis
            datora_punkti += dators_izvele

            # pēc katras spēlētāja kartas tiek piešķirti vai atņemti punkti spēlētājam...
            #...atkarībā, vai uz galda palikuši akmentiņi pāra skaitā(tiek pieskaitīti klāt) vai nepāra skaitā(tiek noņemti)
            if tagad_stavoklis.akmenuSk % 2 == 0:
                datora_punkti += 2
            else:
                datora_punkti -=2
                #tiek izvadīti pašreizējie rezultāti
            print(f"Spēlētāja punkti: {speletaja_punkti}, Datora punkti: {datora_punkti}")
            #pāriet uz spēlētāja kārtu
            uzsacejs = '1'

        # ja akmentiņu vaiŗak nav uz galda, tiek izvadīti galējie spēlētāja un datora punkti
        if tagad_stavoklis.akmenuSk <=0:
            print("\nGala punkti:")
            print(f"Spēlētāja punkti: {speletaja_punkti}, Datora punkti: {datora_punkti}")
            #ja punktu skaits ir vienāds, tad ir neizšķirts
            if speletaja_punkti == datora_punkti:
                print("Neizšķirts!")
                #ja speletaja punkti ir vairāk par datora punktiem, tad ir uzvara, pretēji - dators uzvar
            elif speletaja_punkti > datora_punkti:
                print("Uzvara!")
            else:
                print("Dators uzvar!")
            break
        
##funkcija nodrošina, ka sāks spēles procesu
play()


    



