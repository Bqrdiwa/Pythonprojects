import random
import chemlib

yons = {'Group1': '+1',
        'Group2': '+2',
        'Group13': '+3',
        'Group15': '-3',
        'Group16': '-2',
        'Group17': '-1',
        'Sc': '+3',
        'Al': '+3',
        'Ti': ('+4', '+2'),
        'V': ('+3', '+2'),
        'Cr': ('+3', '+2'),
        'Mn': ('+3', '+2'),
        'Fe': ('+3', '+2'),
        'Co': ('+3', '+2'),
        'Ni': ('+3', '+2'),
        'Cu': ('+1', '+2'),
        'Zn': '+2',
        'Pb': ('+4', '+2'),
        'Sn': ('+4', '+2'),
        'OH': '-1'
        }
Oxid_Nafelex = [
('CO2',''),
('CO',''),
('CO3','2-'),
('SO3','2-'),
('NO3','1-'),
('SO4','2-'),
('PO4','3-'),
]
ban_list = ['H', 'Be']
Felez = []
Na_Felez = []
for i in range(0, 117):
    atm = chemlib.chemistry.pte.loc[i]
    if atm.Metal == True:
        Felez.append(atm)
    elif atm.Nonmetal == True:
        Na_Felez.append(atm)
print(len(Na_Felez))
Nahveye_Anjam_Vakonesh = [
    (['فلز', 'نافلز'], ['نمک فلز و نافلز واکنش دهنده'], ''),
    (['اکسید فلز', 'H2O'], ['هیدروکسید فلز'], ''),
    (['اکسید نافلز', 'H2O'], ['اسید اکسیژن دار'], ''),
    (['آمونیاك', 'اسید'], ['نمک آمونیوم دار'], ''),
    (['کربنات فلز'], ['اکسید فلز', 'CO2'], 'Δ'),
    (['هیدروژن کربنات فلز'], ['کربنات فلز', 'CO2', 'H2O'], ''),
    (['نیترات فلز'], ['نیتریت فلز', 'O2'], ''),
    (['کلرات فلز'], ['کلرید فلز', 'O2'], ''),
    (['فلز قلیایی و قلیایی خاکی', 'H2O'], ['هیدروکسید فلز', 'H2'], ''),
    (['فلز', 'اسید'], ['نمک فلز', 'H2'], ''),
    (['باز', 'اسید'], ['نمک فلز باز', 'H2O'], ''),
]


def get_item_with_bar(element):
    # element should be in yons
    k = yons.keys()
    Syf = element.Symbol
    if Syf not in ban_list:
        if 'Group' + str(element.Group) in k :
            return (Syf, yons['Group' + str(element.Group)])
        elif Syf in k:
            if type(yons[Syf]) != str:
                rng  = random.randint(0,1)
                bar = yons[Syf][rng]
            else:bar = yons[Syf]
            return (Syf, bar)
        else: return None
    return None


def create_vakonesh(script):
    vakonesh_dahande_script = script[0]
    vakonesh_faravarde_script = script[1]
    Pishniaz_vakonesh = script[2]

    vakonesh_dahande = []
    faravarde = []
    for i in vakonesh_dahande_script:
        if i == 'فلز':
            while True:
                rne = random.randint(0, 91)
                Felez_S = Felez[rne]
                if get_item_with_bar(Felez_S) != None:
                    break
            vakonesh_dahande.append((Felez_S, Felez_S.Symbol))
        elif i == 'نافلز':
            two_atomi = ['N', 'O', 'H', 'I', 'Cl', 'F', 'Br']
            while True:
                rne = random.randint(0, 17)
                Na_Felez_S = Na_Felez[rne]
                if get_item_with_bar(Na_Felez_S) != None:
                    break
            SYmpol = Na_Felez_S.Symbol
            for i in two_atomi:
                if SYmpol == i:
                    SYmpol = i + '2'

            vakonesh_dahande.append((Na_Felez_S, SYmpol))
        elif i == 'اکسید فلز':
            while True:
                rne = random.randint(0, 91)
                Felez_S = get_item_with_bar(Felez[rne])
                if Felez_S != None:
                    break
            OxidFelez_S = Build_Yon(((Felez_S[0],Felez_S[1]),('O','-2'),'Metal'))
            vakonesh_dahande.append(OxidFelez_S)
        elif i == 'H2O':
            vakonesh_dahande.append('H2O')
        elif i == 'کربنات فلز':
            while True:
                rne = random.randint(0, 91)
                Felez_S = get_item_with_bar(Felez[rne])
                if Felez_S != None:
                    break
            carbonat = Build_Yon(((Felez_S[0],Felez_S[1]),('CO3','-2'),'Metal'))
            vakonesh_dahande.append(carbonat)

    if vakonesh_faravarde_script == ['نمک فلز و نافلز واکنش دهنده']:
            k = yons.keys()
            if 'Group' + str(vakonesh_dahande[0][0].Group) in k:
                bar_yon_1 = yons['Group' + str(vakonesh_dahande[0][0].Group)]
            elif vakonesh_dahande[0][0].Symbol in k:
                bar_yon_1 = yons[vakonesh_dahande[0][0].Symbol]

            if 'Group' + str(vakonesh_dahande[1][0].Group) in k:
                bar_yon_2 = yons['Group' + str(vakonesh_dahande[1][0].Group)]
            elif vakonesh_dahande[1][0].Symbol in k:
                bar_yon_2 = yons[vakonesh_dahande[1][0].Symbol]
            faravarde.append(Build_Yon(
                ((vakonesh_dahande[0][0].Symbol, bar_yon_1), (vakonesh_dahande[1][0].Symbol, bar_yon_2), 'Metal'))[0])
            reaction = chemlib.Reaction.by_formula(vakonesh_dahande[0][1]+' + '+vakonesh_dahande[1][1]+' --> '+faravarde[0])
            reaction_un_movazene  = reaction.formula.replace('1','').replace('₁','')
            reaction.balance()
            reaction_to_show = str(reaction.formula).replace('1','').replace('₁','')
            movaze_shode = False
            if reaction_un_movazene == reaction_to_show: movaze_shode = True
            return (reaction,reaction_un_movazene,reaction_to_show,movaze_shode)
    elif vakonesh_faravarde_script == ['هیدروکسید فلز']:
            ahan = vakonesh_dahande[0][1][0]
            bar_ahan = vakonesh_dahande[0][1][1]
            faravarde.append(Build_Yon(((ahan,bar_ahan),('OH','-1'),'Metal'))[0])
            vakonesh_dahande[0] = vakonesh_dahande[0][0]
            vakonesh_dahande[1] = vakonesh_dahande[1]
            reaction = chemlib.Reaction.by_formula(vakonesh_dahande[0]+' + '+vakonesh_dahande[1] + ' --> '+ faravarde[0])
            reaction.balance()
            zarib_ha = list(reaction.coefficients.values())
            reaction_un_movazene = str(vakonesh_dahande[0]+' + '+vakonesh_dahande[1] + ' --> '+faravarde[0]).replace('1','').replace('₁','')
            reaction_to_show = str(str(zarib_ha[0])+vakonesh_dahande[0]+' + '+str(zarib_ha[1])+vakonesh_dahande[1] + ' --> '+str(zarib_ha[2])+faravarde[0]).replace('1','').replace('₁','')
            movaze_shode = False
            if reaction_to_show == reaction_un_movazene :movaze_shode = True
            return (reaction,reaction_un_movazene,reaction_to_show,movaze_shode)
    elif vakonesh_faravarde_script == ['اکسید فلز', 'CO2']:
        faravarde.append(Build_Yon(((vakonesh_dahande[0][1]),('O','-2'),'Metal'))[0])
        vakonesh = chemlib.Reaction.by_formula(vakonesh_dahande[0][0]+' --> '+faravarde[0]+' + CO2')
        vakonesh_movazene_nashode   = vakonesh_dahande[0][0]+' --> '+faravarde[0]+' + CO2'
        vakonesh.balance()
        zarib_ha = list(vakonesh.coefficients.values())
        vakonesh_movazene_shode = str(str(zarib_ha[0])+vakonesh_dahande[0][0]+' --> '+str(zarib_ha[1])+faravarde[0]+' + '+str(zarib_ha[2])+'CO2').replace('1','').replace('₁','')
        movazene_shode = False
        if vakonesh_movazene_shode == vakonesh_movazene_nashode :movazene_shode = True
        return (vakonesh,vakonesh_movazene_nashode,vakonesh_movazene_shode,movazene_shode)


def Build_Yon(event='auto'):
    if event == 'auto':
        random_at = chemlib.chemistry.pte.loc[random.randint(0, 117)]
        for i in yons.keys():
            if random_at.Symbol == i or 'Group' + str(random_at.Group) == i and random_at.Symbol not in ban_list:
                if random_at.Metal != attom.Metal and random_at.Metalloid == False and random_at.Period <= 6:
                    bar = yons[i]
                    if type(bar) != str:
                        random_picker = random.randint(0, 1)
                        yon_saol = bar[random_picker]
                    else:
                        yon_soal = yons[i]

                    yon_1 = int(yon[-1])
                    yon_soal_1 = int(yon_soal[-1])
                    if yon_soal_1 % yon_1 == 0:
                        yon_soal_1 = int(yon_soal_1 / yon_1)
                        yon_1 = 1
                    elif yon_1 % yon_soal_1 == 0:
                        yon_1 = int(yon_1 / yon_soal_1)
                        yon_soal_1 = 1
                    if Atom_Type == 'Metal':
                        vakonesh = Symbol + str(yon_soal_1) + random_at.Symbol + str(yon_1)
                    else:
                        vakonesh = random_at.Symbol + str(yon_1) + Symbol + str(yyon_soal_1)
                    vakonesh = vakonesh.replace('1', '')
                    return (vakonesh, (random_at.Symbol, yon_soal), (Symbol, yon))
        return None
    else:
        # (sumbol,bar)
        yon_1_bar = int(event[0][1][-1])
        yon_1_Symbol = event[0][0]
        yon_2_bar = int(event[1][1][-1])
        yon_2_Symbol = event[1][0]
        type_avalin = event[2]

        if yon_1_bar % yon_2_bar == 0:
            yon_1_bar = int(yon_1_bar / yon_2_bar)
            yon_2_bar = 1
        elif yon_2_bar % yon_1_bar == 0:
            yon_2_bar = int(yon_2_bar / yon_1_bar)
            yon_soal_1 = 1

        if len(chemlib.Compound(yon_1_Symbol).occurences.keys()) > 1:
            yon_1_Symbol = '(' + yon_1_Symbol + ')'
        if len(chemlib.Compound(yon_2_Symbol).occurences.keys()) > 1:
            yon_2_Symbol = '(' + yon_2_Symbol + ')'
        if type_avalin == 'Metal':
            vakonesh = yon_1_Symbol + str(yon_2_bar) + yon_2_Symbol + str(yon_1_bar)
        else:
            vakonesh = yon_2_Symbol + str(yon_1_bar) + yon_1_Symbol + str(yon_2_bar)
        vakonesh = vakonesh.replace('1', '')
        return (vakonesh, (yon_1_Symbol, event[0][1]), (yon_2_Symbol, event[1][1]))


def Jdvl_Test_C():
    global soal_list
    global yons
    global attom, Symbol
    global ban_list

    def random_yon():
        tow_atom = []
        while len(tow_atom) != 3:
            atm_1 = chemlib.chemistry.pte.loc[random.randint(0, 117)]
            atm_2 = chemlib.chemistry.pte.loc[random.randint(0, 117)]
            if atm_2.Symbol != atm_1.Symbol and atm_2.Metal == True and atm_1.Nonmetal == True and atm_1.Symbol not in ban_list and atm_2.Symbol not in ban_list:
                for i in yons.keys():
                    if atm_1.Symbol == i or 'Group' + str(atm_1.Group) == i:
                        for y in yons.keys():
                            if atm_2.Symbol == y or 'Group' + str(atm_2.Group) == y:
                                if type(yons[i]) != str:
                                    random_121 = random.randint(0, 1)
                                    atom_1_bar = yons[i][random_121]
                                else:
                                    atom_1_bar = yons[i]
                                if type(yons[y]) != str:
                                    random_121 = random.randint(0, 1)
                                    atom_2_bar = yons[y][random_121]
                                else:
                                    atom_2_bar = yons[y]
                                tow_atom.append((atm_1.Symbol, atom_1_bar))
                                tow_atom.append((atm_2.Symbol, atom_2_bar))
                                tow_atom.append(atm_1.Metal)
        return Build_Yon(((tow_atom[0][0], tow_atom[0][1]), (tow_atom[1][0], tow_atom[1][1]), tow_atom[2]))

    def create_vakonesh(event='random'):
        if event != 'random':
            vakonesh_dahandeye_1 = event


        else:
            pass

    addad_atomi = random.randint(0, 118)
    if random.randint(1, 3) == 1: addad_atomi = random.randint(3, 68)
    attom = chemlib.chemistry.pte.loc[12]
    Symbol = attom.Symbol
    Name = attom.Element
    Addad_atomi = attom.AtomicNumber
    group = attom.Group
    row = attom.Period
    Phase = attom.Phase
    Arayesh = attom.Config
    Shoa_Atomi = attom.AtomicRadius
    Atom_Type = attom.Type
    list_m = [(attom.Metal, 'فلز'), (attom.Nonmetal, 'نافلز'), (attom.Metalloid, 'شبه فلز')]
    for i in list_m:
        if i[0]:
            Type = i[1]
    Electron_zarfiat = attom.Valence
    if Phase == 'solid':
        Phase = 'جامد'
    elif Phase == 'liq':
        Phase = 'مایع'
    elif Phase == 'gas':
        Phase = 'گاز'
    print(attom)
    P = attom.Protons
    N = attom.Neutrons
    E = attom.Electrons

    Khatm = Arayesh[-3:]
    ham_grouhi_ha = []
    for i in range(0, 118):
        atom = chemlib.chemistry.pte.loc[i]
        if atom.Group == group and atom.Symbol != Symbol:
            ham_grouhi_ha.append((atom.Element, atom.Symbol))
    List_test = 1

    yon = None
    if Atom_Type != 'Metalliod':
        for i in yons.keys():
            if Symbol == i or 'Group' + str(group) == i and Symbol not in ban_list:
                bar = yons[i]
                if type(bar) != str:
                    random_picker = random.randint(0, 1)
                    yon = bar[random_picker]
                else:
                    yon = yons[i]

    soal_list = []
    if List_test == 1:
        if yon != None:
            attomaye_mored_nazar = []
            soal_count = 2
            while len(attomaye_mored_nazar) < soal_count:
                Popo = Build_Yon()
                if Popo != None and Popo[0] not in attomaye_mored_nazar:
                    attomaye_mored_nazar.append(Popo)

            soal_type = ['ekhtelaf', 'arayesh_yon', 'fdkiometry', 'balavand']
            soal_accepted = []
            random12 = random.randint(0, 3)
            soal_accepted.append(soal_type[random12])
            soal_type.pop(random12)
            random12 = random.randint(0, 2)
            soal_accepted.append(soal_type[random12])
            soal_accepted.append('estekiometry')
            for i in soal_accepted:
                if i == 'balavand':
                    random_soal_tarh = random.randint(0, 1)
                    atomi_k_soalbarshe = attomaye_mored_nazar[random_soal_tarh]
                    majmoe_zirvandaye_asli = int(atomi_k_soalbarshe[1][1][-1]) + int(atomi_k_soalbarshe[2][1][-1])
                    rando_yo = random_yon()
                    bar_avali = rando_yo[1][1][-1]
                    bar_dovomi = rando_yo[2][1][-1]
                    mazmoe_zirvandaye_fake = int(bar_dovomi) + int(bar_avali)
                    javab_1 = 'False'
                    if majmoe_zirvandaye_asli == mazmoe_zirvandaye_fake: javab_1 = 'True'
                    soal_list.append((('TrueORFalse', javab_1),
                                      'ایا در ترکیب اولی (%s) مجموع بار کاتیون و انیون با مجموع بار کاتیون و انیون در %s برابر است؟' % (
                                      atomi_k_soalbarshe[0], rando_yo[0])))
                if i == 'estekiometry':
                    random_soal_tarh = random.randint(0, 1)
                    atomi_k_soalbarshe = attomaye_mored_nazar[random_soal_tarh]
                    yon_mored = atomi_k_soalbarshe[0]


print(create_vakonesh(Nahveye_Anjam_Vakonesh[4]))
test_types = ['TrueORFalse', '4 Gozinei']
