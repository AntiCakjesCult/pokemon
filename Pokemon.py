import random


def story1():
    storyline1 = int(input(
        '\nWelkom bij de pokemon sword and shield fight simulator!'
        'Je begint bij level 1, kies een van de volgende pokemon waar je mee wilt vechten'
        'en geef het bijbehorende getal?\n'
        'Je hebt keuze uit de volgende pokemons:\n'
        'Scorebunny[1], Sobble[2], Grookey[3], Rookidee[4], Greedent[5], Wooloo[6], Blibbug[7],\n'
        'Je vecht tegen een willekeurige Pokemon dus wees voorzichtig!!\n'))-1
   
    return storyline1

def story2():
    storyline2 = int(input(
        '\nAah je hebt level 1 gehaald!!\n'
        'Kies een van de volgende pokemon voor ronde level 2\n'
        'Je vecht nu tegen een andere pokemon uit level 2!\n'
        'Je hebt keuze uit: Rillaboom[1], Inteleon[2], Cinderace[3], Grimmsnarl[4],'
        ' Corviknight[5], Obstagoon[6], Perrserker[7]\n'
        ))-1
    return storyline2

def story3():
    storyline3 = print(
        'AAAAH goed gedaan je hebt ook level 2 behaald!!!\n'
        'Nu de ben je bij het laatste level gekomen\n'
        'Het schijnt dat hier de moeilijkste en de meest ontvindbare pokemon zich koest houden en jou uitdagen.')

def level1():
    Scorebunny = ['Scorebunny', 18, 2, 5]
    Sobble = ['Sobble',17, 3, 6]
    Grookey = ['Grookey',18, 2, 6]
    Rookidee = ['Rookidee',15, 3, 5]
    Greedent = ['Greedent',14, 3, 5]
    Wooloo = ['Wooloo',15, 4, 6]
    Blibbug = ['Blibbug', 16, 3, 5]
    pokemons = [Scorebunny, Sobble, Grookey, Rookidee,
                Greedent, Wooloo, Blibbug]
    random1 = random.randint(1,7)-1
    return pokemons, random1

        

def level2():
    Rillaboom = ['Rillaboom',180, 30, 50]
    Inteleon = ['Inteleon',190, 25, 60]
    Cinderace = ['Cinderace',195, 20, 70]
    Grimmsnarl = ['Grimmsnarl',200, 45, 70]
    Corviknight = ['Corviknight', 220, 50, 60]
    Obstagoon = ['Obstagoon',190, 30, 80]
    Perrserker = ['Perrserker', 170, 50, 65]
    pokemons = [Rillaboom, Inteleon, Cinderace, Grimmsnarl,
                Corviknight, Obstagoon, Perrserker]
    random2 = random.randint(1,7)-1
    return pokemons, random2

def level3():
    Zacian = ['Zacian', 240, 50, 80]
    Zamazenta = ['Zamazenta', 270, 40, 70]
    Eternatus = ['Eternatus', 255, 60, 85]
    Urshifu_st = ['Urshifu single strike', 230, 65, 80]
    Urshifu_rt = ['Urshifu rapid strike', 255, 60, 85]
    Calyrax = Urshifu_st = ['Calyrax', 260, 55, 75]
    pokemons = [Zacian, Zamazenta, Eternatus, Urshifu_st,
                Urshifu_rt, Calyrax]
    random3 = random.randint(1,6)-1
    return pokemons, random3
    
def fight_display(p_chosen, p_random):
    print('\nJe gekozen pokemon is:  ' + str(p_chosen[0]) + '!' + '\nZijn HP is ' + str(p_chosen[1]) +
          ', zijn aanval is tussen de ' + str(p_chosen[2]) + ' en ' + str(p_chosen[3]) + '!!')
    print('\nJe willekeurige gekozen tegenstander is:  ' + str(p_random[0]) + '!' + '\nZijn HP is ' + str(p_random[1]) +
          ', zijn aanval is tussen de ' + str(p_random[2]) + ' en ' + str(p_random[3]) + '!!\n')

def fight(f_chosen, f_random):
    pkm1 = f_chosen[1]
    pkm2 = f_random[1]
    print('De HP van ' + f_random[0] + ' is ' + str(f_chosen[1]))
    print('De HP van ' + f_chosen[0] + ' is ' + str(f_random[1]) + '\n')
    while pkm1 >= 0 and pkm2 >= 0:
        attack_f_chosen = random.randint(f_chosen[2], f_chosen[3])
        attack_f_random = random.randint(f_random[2], f_random[3])
        pkm1 -= attack_f_random
        pkm2 -= attack_f_chosen
        print('De HP van ' + f_random[0] + ' is nu ' + str(pkm2))
        print('De HP van ' + f_chosen[0] + ' is nu ' + str(pkm1))
    return pkm1, pkm2

def main():
    start = input('Wil je het spel spelen[j/n]')
    while start == 'j':
        user_input = story1()
        list1, randomlvl1 = level1()
        chosen1 = list1[user_input]
        random_chosen1 = list1[randomlvl1]
        fight_display(chosen1, random_chosen1)
        pkm1, pkm2 = fight(chosen1, random_chosen1)
        if pkm1 > pkm2:
            list2, randomlvl2 = level2()
            user_input2 = story2()
            chosen2 = list2[user_input2]
            random_chosen2 = list2[randomlvl2]
            fight_display(chosen2, random_chosen2)
            pkm3, pkm4 = fight(chosen2, random_chosen2)  
        if pkm3 > pkm4:
            list3, randomlvl3 = level3()
            story3()
            input('Druk op enter om door te gaan!!')
            chosen2 = list2[user_input2]
            random_chosen3 = list3[randomlvl3]
            fight_display(chosen2, random_chosen3)
            pkm5, pkm6 = fight(chosen2, random_chosen3)
            if pkm5 > pkm6:
                print('Gefeliciteerd, je hebt gewonnen met'+ str(chosen2[0]))
            else:
                print('Je hebt verloren!!')
        else:
            print('Je hebt verloren')
        start = input('Wil je het spel opnieuw spelen?[j/n]')
    print('Bedankt voor het spelen!!')
main()
