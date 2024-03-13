
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


