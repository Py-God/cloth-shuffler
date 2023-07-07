#!python3
import random, sys, pprint, re
from cloth_shuffler_data import picks
from trouser_and_shirt_data_when_i_wore_trouser_on_sunday import trousers_worn, shirts_worn
from trouser_and_shirt_data_when_i_didnt_wear_trouser_on_sunday import trousers_worn, shirts_worn

clothes = {
    'new brown trouser': [
        'purple patterned top', 'clear white top', 'silk plain black top', 'rough plain black top',
        'large blue top', 'orange and white top', 'orange and white longsleeve top', 'blue and red thick shirt',
        ],
    'old brown trouser' : [
        'purple patterned top', 'clear white top', 'silk plain black top', 'rough plain black top',
        'large blue top', 'orange and white top', 'orange and white longsleeve top', 'striped blue shirt', 
        'yellow shirt', 'blue shirt', 'white and blue shirt', 'blue and red thick shirt',
        ],
    'big black striped trouser': [
        'purple patterned top', 'clear white top', 'silk plain black top', 'rough plain black top',
        'large blue top', 'orange and white top', 'orange and white longsleeve top',
        'blue and red thick shirt',
        ],
    'big blue striped trouser': [
        'purple patterned top', 'clear white top', 'silk plain black top', 'rough plain black top',
        'large blue top', 'orange and white top', 'orange and white longsleeve top',
        'blue and red thick shirt',
        ],
    'big plain blue trousers': [
        'clear white top', 'silk plain black top', 'rough plain black top', 'large blue top',
        'orange and white longsleeve top',
        ],
    'chinos' : [
        'purple patterned top', 'clear white top', 'silk plain black top', 'rough plain black top',
        'large blue top', 'orange and white top', 'blue and red thick shirt',
    ],
}

clothes2 = {
    'thick normal blue jeans': [
       'purple patterned top', 'clear white top', 'silk plain black top', 'rough plain black top',
        'large blue top', 'orange and white top', 'blue and red thick shirt', 
    ],
    'thick light blue jeans': [
        'purple patterned top', 'clear white top', 'silk plain black top', 'rough plain black top',
        'large blue top', 'orange and white top', 'blue and red thick shirt'
    ],
    'soft light blue jeans': [
        'purple patterned top', 'clear white top', 'silk plain black top', 'rough plain black top',
        'large blue top', 'orange and white top', 'blue and red thick shirt', 'white and blue shirt',
        'striped blue shirt',
    ],
    'thick dark jeans': [
        'purple patterned top', 'clear white top', 'orange and white top', 'blue and red thick shirt', 
        'white and blue shirt',
    ],
    'slim black trouser': [
        'purple patterned top', 'clear white top', 'silk plain black top', 'rough plain black top',
        'large blue top', 'orange and white top', 'striped blue shirt', 
        'yellow shirt', 'blue shirt', 'blue and red thick shirt',
    ],
    'white juggers': [
        'purple patterned top', 'clear white top', 'silk plain black top', 'rough plain black top',
        'large blue top', 'orange and white top', 'blue and red thick shirt',
    ],
    'black juggers': [
        'striped blue shirt', 'yellow shirt', 'blue shirt', 'purple patterned top', 
        'orange and white top', 'blue and red thick shirt',
    ],
}

# this code makes a temporary list of all the trousers i have in the 1st dictionary
trousers_list = list(clothes.keys())
trousers_list_copy = list(clothes.keys())
# this code makes a temporary list of all the trousers i have in the 1st dictionary
trousers_list2 = list(clothes2.keys())
# get all possible trousers in a list
total_trousers = trousers_list + trousers_list2
# this code makes a temporary list of all the shirts i have in the dictionary
shirts = [
        'purple patterned top', 'clear white top', 'silk plain black top', 'rough plain black top',
        'large blue top', 'orange and white top', 'orange and white longsleeve top', 'striped blue shirt', 
        'yellow shirt', 'blue shirt', 'white and blue shirt', 'blue and red thick shirt',
        ]
# this function literally carries all the code for how i would randomise the selection of the clothes
# but under certain restrictions

# for five days if i wore on sunday

# final code to run
def random_cloth_picker_if_i_wore_a_trouser_on_sunday(trouser, unavailableShirts_list, unavailableTrousers_list):
    # get a list of all the weeks i have generated drip for
    # for generating new weeks
    # for getting cloths i picked the week before like immediately below
    week_list = []
    for week in picks.keys():
        week_list.append(week)

    # remove the trouser i wore on sunday from the list a random trouser should be picked
    trousers_list.remove(trouser)
    # remove the shirt i have unavailable from the entire shirt lists
    # remove it from clothes dict
    if unavailableShirts_list == None:
                pass
    else:
        for key in clothes.keys():
            for shirt in clothes[key]:
                if str(shirt) in unavailableShirts_list:
                    clothes[key].remove(str(shirt))
                else:
                    continue

    # remove it from clothes2 dict
    if unavailableShirts_list == None:
                pass
    else:
        for key in clothes2.keys():
            for shirt in clothes2[key]:
                if str(shirt) in unavailableShirts_list:
                    clothes2[key].remove(str(shirt))
                else:
                    continue

    # remove unavailable trouser from clothes and clothes2 dictionaries
    # dont need to remove it from dict cuz, the randomiser deals with the trouser list
    # so it cannot possibly generate a trouser that isnt in the dict
    if unavailableTrousers_list == None:
        pass
    else:
        for unavailableTrouser in unavailableTrousers_list:
            if unavailableTrouser in trousers_list:
                trousers_list.remove(unavailableTrouser)
            elif unavailableTrouser in trousers_list2:
                trousers_list2.remove(unavailableTrouser)
    
    # remove trouser i wore last week from dict
    if trousers_worn == []:
        pass
    else:
        for trouser_worn_last_week in trousers_worn:
            if trouser_worn_last_week in trousers_list:
                trousers_list.remove(trouser_worn_last_week)
            elif trouser_worn_last_week in trousers_list2:
                trousers_list2.remove(trouser_worn_last_week)

    # condition to remove shirts i wore last week from the list of possible shirts 
    # for trouser on monday if there is enough shirts there
    if shirts_worn == []:
        pass
    elif len(clothes[trouser]) == 1 or len(clothes[trouser]) == 2:
        pass
    elif len(clothes[trouser]) == 3:
        shirts_to_remove = random.sample(shirts_worn, 2)
        check = all(item in clothes[trouser] for item in shirts_to_remove)
        if check == True:
            pass
        else:
            for shirt in shirts_to_remove:
                if shirt in clothes[trouser]:
                    clothes[trouser].remove(shirt)
                else:
                    continue
    elif len(clothes[trouser]) == 4:
        shirts_to_remove = random.sample(shirts_worn, 3)
        check = all(item in clothes[trouser] for item in shirts_to_remove)
        if check == True:
            pass
        else:
            for shirt in shirts_to_remove:
                if shirt in clothes[trouser]:
                    clothes[trouser].remove(shirt)
                else:
                    continue
    elif len(clothes[trouser]) == 5:
        shirts_to_remove = random.sample(shirts_worn, 4)
        check = all(item in clothes[trouser] for item in shirts_to_remove)
        if check == True:
            pass
        else:
            for shirt in shirts_to_remove:
                if shirt in clothes[trouser]:
                    clothes[trouser].remove(shirt)
                else:
                    continue
    elif len(clothes[trouser]) == 6:
        shirts_to_remove = random.sample(shirts_worn, 5)
        check = all(item in clothes[trouser] for item in shirts_to_remove)
        if check == True:
            pass
        else:
            for shirt in shirts_to_remove:
                if shirt in clothes[trouser]:
                    clothes[trouser].remove(shirt)
                else:
                    continue
    elif len(clothes[trouser]) > 6:
        shirts_to_remove = random.sample(shirts_worn, 5)
        for shirt in shirts_to_remove:
                if shirt in clothes[trouser]:
                    clothes[trouser].remove(shirt)
                else:
                    continue


    # first randomly generated trouser
    week_trouser1 = random.choice(trousers_list)
    # second randomly generated trouser
    week_trouser2 = random.choice(trousers_list2)

    # picking 1 random cloth for monday from the possible cloth combination
    week_trouser_possible_tops_for_trouser_picked_on_sunday = random.choice(clothes[trouser])

    # 2 for tuesday and thursday following the same principle
    # remove the shirt you picked on monday from the list of shirts you can pick for trouser 1
    if str(week_trouser_possible_tops_for_trouser_picked_on_sunday) in clothes[week_trouser1]:
        clothes[week_trouser1].remove(str(week_trouser_possible_tops_for_trouser_picked_on_sunday))
    # condition to remove shirts i wore last week from the list of possible shirts 
    # for trouser1 if there is enough shirts there
    if shirts_worn == []:
        pass
    elif len(clothes[week_trouser1]) == 1 or len(clothes[week_trouser1]) == 2  or len(clothes[week_trouser1]) == 3:
        pass
    elif len(clothes[week_trouser1]) == 4:
        shirts_to_remove = random.sample(shirts_worn, 2)
        check = all(item in clothes[week_trouser1] for item in shirts_to_remove)
        if check == True:
            pass
        else:
            for shirt in shirts_to_remove:
                if shirt in clothes[week_trouser1]:
                    clothes[week_trouser1].remove(shirt)
                else:
                    continue
    elif len(clothes[week_trouser1]) == 5:
        shirts_to_remove = random.sample(shirts_worn, 3)
        check = all(item in clothes[week_trouser1] for item in shirts_to_remove)
        if check == True:
            pass
        else:
            for shirt in shirts_to_remove:
                if shirt in clothes[week_trouser1]:
                    clothes[week_trouser1].remove(shirt)
                else:
                    continue
    elif len(clothes[week_trouser1]) == 6:
        shirts_to_remove = random.sample(shirts_worn, 4)
        check = all(item in clothes[week_trouser1] for item in shirts_to_remove)
        if check == True:
            pass
        else:
            for shirt in shirts_to_remove:
                if shirt in clothes[week_trouser1]:
                    clothes[week_trouser1].remove(shirt)
                else:
                    continue
    elif len(clothes[week_trouser1]) > 6:
        shirts_to_remove = random.sample(shirts_worn, 5)
        for shirt in shirts_to_remove:
                if shirt in clothes[week_trouser1]:
                    clothes[week_trouser1].remove(shirt)
                else:
                    continue

    week_trouser_possible_tops1_pick = random.sample(clothes[week_trouser1], 2)


    # 2 for wednesday and friday following the same principle
    # remove shirt picked on monday from the list of shirts you can pick for trouser 2
    if str(week_trouser_possible_tops_for_trouser_picked_on_sunday) in clothes2[week_trouser2]:
        clothes2[week_trouser2].remove(str(week_trouser_possible_tops_for_trouser_picked_on_sunday))
    # remove shirt picked on for trouser one from the list of shirts you can pick for trouser 2
    for week_trouser_possible_tops1_pick_cloth in week_trouser_possible_tops1_pick:
        if str(week_trouser_possible_tops1_pick_cloth) in clothes2[week_trouser2]:
            clothes2[week_trouser2].remove(str(week_trouser_possible_tops1_pick_cloth))

    week_trouser_possible_tops2_pick = random.sample(clothes2[week_trouser2], 2)

    # creates a list of all the trousers i have generated for this week
    # pretty much continuation of the dont_pick_trouser_i_wore_last_week function
    week_trouser_list = []
    week_trouser_list.append(trouser)
    week_trouser_list.append(week_trouser1)
    week_trouser_list.append(week_trouser2)
    # creates a list of all the shirts i have generated for this week
    week_shirt_list = []
    week_shirt_list.append(week_trouser_possible_tops_for_trouser_picked_on_sunday)
    for shirt in week_trouser_possible_tops1_pick:
        week_shirt_list.append(shirt)
    for shirt in week_trouser_possible_tops2_pick:
        week_shirt_list.append(shirt)
    dont_pick_same_set_of_trousers_and_shirts_next_week(week_trouser_list, week_shirt_list)

    # prints all the generated trousers into the terminal
    print('')
    print('---------------------------')
    print('For the week:')
    print(trouser + ': ' + str(week_trouser_possible_tops_for_trouser_picked_on_sunday))
    print('')
    print(week_trouser1 + ': ' + str(week_trouser_possible_tops1_pick))
    print('')
    print(week_trouser2 + ': ' + str(week_trouser_possible_tops2_pick))

    file_path = 'C:\\Users\\USER-PC\\Desktop\\your_generated_drip.txt'
    with open(file_path, 'w') as fileobj:
        fileobj.write((trouser + ': ' + str(week_trouser_possible_tops_for_trouser_picked_on_sunday)) + '\n')
        fileobj.write((week_trouser1 + ': ' + str(week_trouser_possible_tops1_pick)) + '\n')
        fileobj.write((week_trouser2 + ': ' + str(week_trouser_possible_tops2_pick)) + '\n')

    # regex to the week number from the list of weeks i generated above
    week_num_regex = re.compile(r'\d+')
    week_no_list = []
    for week in week_list:
        week_no = week_num_regex.search(week)
        week_no_list.append(int(week_no.group()))
    # sort the week number so i can easily pick the last one and add 1 to create a new week number 
    week_no_list.sort()
    # create a new week
    week = 'week' + str(int(week_no_list[-1])+1)

    # creates a dictionary of all the drip i picked for the week
    picks[week] = {
    trouser: week_trouser_possible_tops_for_trouser_picked_on_sunday,
    week_trouser1: week_trouser_possible_tops1_pick,
    week_trouser2: week_trouser_possible_tops2_pick
    }
    save(picks)
    # exit program after
    sys.exit()

def random_cloth_picker_if_i_didnt_wear_a_trouser_on_sunday(trouser, unavailableShirts_list, unavailableTrousers_list):

    week_list = []
    for week in picks.keys():
        week_list.append(week)

    # remove the shirt i have unavailable from the entire shirt lists
    # remove it from clothes dict
    if unavailableShirts_list == None:
                pass
    else:
        for key in clothes.keys():
            for shirt in clothes[key]:
                if str(shirt) in unavailableShirts_list:
                    clothes[key].remove(str(shirt))
                else:
                    continue

    # remove it from clothes2 dict
    if unavailableShirts_list == None:
                pass
    else:
        for key in clothes2.keys():
            for shirt in clothes2[key]:
                if str(shirt) in unavailableShirts_list:
                    clothes2[key].remove(str(shirt))
                else:
                    continue

    # remove unavailable trouser from clothes and clothes2 dictionaries
    if unavailableTrousers_list == None:
        pass
    else:
        for unavailableTrouser in unavailableTrousers_list:
            if unavailableTrouser in trousers_list:
                trousers_list.remove(unavailableTrouser)
            elif unavailableTrouser in trousers_list2:
                trousers_list2.remove(unavailableTrouser)

    # remove trouser i wore last week from dict
    if trousers_worn == []:
        pass
    else:
        for trouser_worn_last_week in trousers_worn:
            if trouser_worn_last_week in trousers_list:
                trousers_list.remove(trouser_worn_last_week)
            elif trouser_worn_last_week in trousers_list2:
                trousers_list2.remove(trouser_worn_last_week)

    # ask what trouser i will wear the next sunday 
    #  if its not a trad, remove that trouser from the list of generatables so that 
    # i wont have to repeat trouser i wore this week on sunday and also next week.
    print('')
    print('''What trouser should you wear next week?
type c if you arent wearing a trouser next week.''')
    print('')
    # print out the list of trousers i have
    for trous in trousers_list:
        print(trous)
    trouser = input()
    # ensure the trouser i pick is actually in the list of trousers i originally can wear on sunday
    if trouser in trousers_list:
        trousers_list.remove(trouser)
    elif trouser in trousers_list_copy:
        pass
    elif trouser == 'c':
        pass
    else:
        print('The trouser you entered is not part of the list, please check, copy and paste the name of the trouser you wore')
        random_cloth_picker_if_i_didnt_wear_a_trouser_on_sunday(trouser, unavailableShirts_list, unavailableTrousers_list)

    # generate 1st trouser: from trousers_list
    week_trouser1 = random.choice(trousers_list)

    # condition to remove shirts i wore last week from the list of possible shirts 
    # for trouser on monday if there is enough shirts there
    if shirts_worn == []:
        pass
    elif len(clothes[week_trouser1]) == 1 or len(clothes[week_trouser1]) == 2 or len(clothes[week_trouser1]) == 3:
        pass
    elif len(clothes[week_trouser1]) == 4:
        shirts_to_remove = random.sample(shirts_worn, 3)
        check = all(item in clothes[week_trouser1] for item in shirts_to_remove)
        if check == True:
            pass
        else:
            for shirt in shirts_to_remove:
                if shirt in clothes[week_trouser1]:
                    clothes[week_trouser1].remove(shirt)
                else:
                    continue
    elif len(clothes[week_trouser1]) == 5:
        shirts_to_remove = random.sample(shirts_worn, 4)
        check = all(item in clothes[week_trouser1] for item in shirts_to_remove)
        if check == True:
            pass
        else:
            for shirt in shirts_to_remove:
                if shirt in clothes[week_trouser1]:
                    clothes[week_trouser1].remove(shirt)
                else:
                    continue
    elif len(clothes[week_trouser1]) == 6:
        shirts_to_remove = random.sample(shirts_worn, 5)
        check = all(item in clothes[week_trouser1] for item in shirts_to_remove)
        if check == True:
            pass
        else:
            for shirt in shirts_to_remove:
                if shirt in clothes[week_trouser1]:
                    clothes[week_trouser1].remove(shirt)
                else:
                    continue
    elif len(clothes[week_trouser1]) > 6:
        shirts_to_remove = random.sample(shirts_worn, 5)
        for shirt in shirts_to_remove:
                if shirt in clothes[week_trouser1]:
                    clothes[week_trouser1].remove(shirt)
                else:
                    continue

    # generate the remaining 2 trousers from trousers_list2
    week_trouser2_and3 = random.sample(trousers_list2, 2)
    week_trouser2 = week_trouser2_and3[0]
    week_trouser3 = week_trouser2_and3[1]
    # generate shirts for week_trouser1
    week_trouser1_shirts_pick = random.sample(clothes[week_trouser1], 2)

    # remove the shirt you generated for trouser1 from trouser2and3 first trouser
    for week_trouser_possible_tops1_pick_cloth in week_trouser1_shirts_pick:
        if str(week_trouser_possible_tops1_pick_cloth) in clothes2[week_trouser2]:
            clothes2[week_trouser2].remove(str(week_trouser_possible_tops1_pick_cloth))
    
    # condition to remove shirts i wore last week from the list of possible shirts
    if shirts_worn == []:
        pass
    elif len(clothes2[week_trouser2]) == 1 or len(clothes2[week_trouser2]) == 2  or len(clothes2[week_trouser2]) == 3 or len(clothes2[week_trouser2]) == 4:
        pass
    elif len(clothes2[week_trouser2]) == 5:
        shirts_to_remove = random.sample(shirts_worn, 3)
        check = all(item in clothes2[week_trouser2] for item in shirts_to_remove)
        if check == True:
            pass
        else:
            for shirt in shirts_to_remove:
                if shirt in clothes2[week_trouser2]:
                    clothes2[week_trouser2].remove(shirt)
                else:
                    continue
    elif len(clothes2[week_trouser2]) == 6:
        shirts_to_remove = random.sample(shirts_worn, 4)
        check = all(item in clothes2[week_trouser2] for item in shirts_to_remove)
        if check == True:
            pass
        else:
            for shirt in shirts_to_remove:
                if shirt in clothes2[week_trouser2]:
                    clothes2[week_trouser2].remove(shirt)
                else:
                    continue
    elif len(clothes2[week_trouser2]) > 6:
        shirts_to_remove = random.sample(shirts_worn, 5)
        for shirt in shirts_to_remove:
                if shirt in clothes2[week_trouser2]:
                    clothes2[week_trouser2].remove(shirt)
                else:
                    continue

    # generate possible shirts for trouser2and3 first trouser
    week_trouser2_shirts_pick = random.sample(clothes2[week_trouser2], 2)

    # remove shirts i picked from first and second trouser from last trouser shirts list
    for shirt in week_trouser1_shirts_pick:
        if shirt in clothes2[week_trouser3]:
            clothes2[week_trouser3].remove(shirt)
    for shirt in week_trouser2_shirts_pick:
        if shirt in clothes2[week_trouser3]:
            clothes2[week_trouser3].remove(shirt)
    
    # generate the shirt for trouser 3
    week_trouser3_shirt_pick = random.choice(clothes2[week_trouser3])

    # creates a list of all the trousers i have generated for this week
    # pretty much continuation of the dont_pick_trouser_i_wore_last_week function
    week_trouser_list = []
    week_trouser_list.append(week_trouser1)
    week_trouser_list.append(week_trouser2)
    week_trouser_list.append(week_trouser3)
    # creates a list of all the shirts i have generated for this week
    week_shirt_list = []
    week_shirt_list.append(week_trouser3_shirt_pick)
    for shirt in week_trouser1_shirts_pick:
        week_shirt_list.append(shirt)
    for shirt in week_trouser2_shirts_pick:
        week_shirt_list.append(shirt)
    dont_pick_same_set_of_trousers_and_shirts_next_week(week_trouser_list, week_shirt_list)

    # print drip for the week
    print('')
    print('---------------------------')
    print('For the week:')
    print(week_trouser1 + ': ' + str(week_trouser1_shirts_pick))
    print('')
    print(week_trouser2 + ': ' + str(week_trouser2_shirts_pick))
    print('')
    print(week_trouser3 + ': ' + str(week_trouser3_shirt_pick))

    file_path = 'C:\\Users\\USER-PC\\Desktop\\your_generated_drip.txt'
    with open(file_path, 'w') as fileobj:
        fileobj.write((week_trouser1 + ': ' + str(week_trouser1_shirts_pick)) + '\n')
        fileobj.write((week_trouser2 + ': ' + str(week_trouser2_shirts_pick)) + '\n')
        fileobj.write((week_trouser3 + ': ' + str(week_trouser3_shirt_pick)) + '\n')

    # regex to the week number from the list of weeks i generated above
    week_num_regex = re.compile(r'\d+')
    week_no_list = []
    for week in week_list:
        week_no = week_num_regex.search(week)
        week_no_list.append(int(week_no.group()))
    # sort the week number so i can easily pick the last one and add 1 to create a new week number 
    week_no_list.sort()
    # create a new week
    week = 'week' + str(int(week_no_list[-1])+1)

    # creates a dictionary of all the drip i picked for the week
    picks[week] = {
    week_trouser1: week_trouser1_shirts_pick,
    week_trouser2: week_trouser2_shirts_pick,
    week_trouser3: week_trouser3_shirt_pick
    }
    save(picks)
    # exit program after
    sys.exit()


# function to store all the trousers i wear for the next 3 weeks (9 trousers)
# it ensures the trouser i wear the next week isnt what ill wear up to 3 weeks forward
def dont_pick_same_set_of_trousers_and_shirts_next_week(week_trouser_list, week_shirt_list):
    trousers_limit = 9
    shirts_limit = 10

    trousers_worn.extend(week_trouser_list)
    if len(trousers_worn) >= trousers_limit:
        trousers_worn.clear()

    shirts_worn.extend(week_shirt_list)
    if len(shirts_worn) >= shirts_limit:
        shirts_worn.clear()

    file_paths = {
        'path_when_i_didnt_wear': 'C:\\Users\\USER-PC\\Desktop\\PYTHON\\my projects\\problemsolving\\trouser_and_shirt_data_when_i_didnt_wear_trouser_on_sunday.py',
        'path_when_i_wore': 'C:\\Users\\USER-PC\\Desktop\\PYTHON\\my projects\\problemsolving\\trouser_and_shirt_data_when_i_wore_trouser_on_sunday.py'
    }
    
    if week_trouser_list[-1] in trousers_list2 and week_trouser_list[-2] in trousers_list2:
        file_path = file_paths['path_when_i_didnt_wear']
    else:
        file_path = file_paths['path_when_i_wore']

    with open(file_path, 'w') as fileobj:
        fileobj.write('trousers_worn = ' + pprint.pformat(trousers_worn) + '\n')
        fileobj.write('shirts_worn = ' + pprint.pformat(shirts_worn) + '\n')


# 3rd code to run (condition)
def verify_unavailable_shirt(trouser, unavailableShirt_amount, unavailableTrousers_list):
    print('')
    # create a list of the unavailable shirts i have for that week
    unavailableShirts_list = []

    # code to handle the prompts based on the number of unavailable shirts
    for number in range(1, unavailableShirt_amount + 1):
        print('Pick the ' + 'no' + str(number) + ' shirt you have unavailable')
        unavailableShirts_pick = input()
        
        # ensure the trouser I type in is actually part of the shirts list
        if unavailableShirts_pick in shirts:
            if unavailableShirts_pick in unavailableShirts_list:
                print('You have already picked this trouser, pick another.')
                continue
            # if it is, add it to the list
            unavailableShirts_list.append(unavailableShirts_pick)
        else:
            print('Not part of the list, restarting...')
            verify_unavailable_shirt(trouser, unavailableShirt_amount, unavailableTrousers_list)
    
    # after thouroughly appending the list, send the list as an argument to the week cloth picker
    random_cloth_picker_if_i_didnt_wear_a_trouser_on_sunday(trouser, unavailableShirts_list, unavailableTrousers_list)

def ask_how_many_unavailable_shirts_i_have(trouser, unavailableTrousers_list):
    print('')
    print('How many unavailable shirts do you have? (Enter a number)')
    # get an integer of the amount of unavailable shirts i have
    unavailableShirt_amount = input()
    confirm_number = re.compile(r'\d+')
    amount_match = confirm_number.search(unavailableShirt_amount)

    if amount_match:
        amount = int(amount_match.group())
        # ensure its actually an integer and it doesnt exceed the original amount of shirts i have
        if amount in range(1, 13):
            verify_unavailable_shirt(trouser, amount, unavailableTrousers_list)
        else:
            print('That is not an acceptable answer.')
            ask_how_many_unavailable_shirts_i_have(trouser, unavailableTrousers_list)
    else:
        print('that is not a valid number.')
        ask_how_many_unavailable_shirts_i_have(trouser, unavailableTrousers_list)

# second code to run
# ask if i have a shirt unavailable
def unavailable_shirt(trouser, unavailableTrousers_list):
    print('')
    print('Do you have any of your shirts unavailable? (y = yes, n = no)')
    allowed_inputs = ['y', 'yes', 'n', 'no']
    ans = input().lower()

    if ans in allowed_inputs:
        # verify if my input is part of allowed inputs
        if ans in ['y', 'yes']:
            # show list of all shirts
            print('---------------------------')
            for shirt in shirts:
                print(shirt)   
            print('---------------------------')
            ask_how_many_unavailable_shirts_i_have(trouser, unavailableTrousers_list)
        else:
            random_cloth_picker_if_i_didnt_wear_a_trouser_on_sunday(trouser, None, unavailableTrousers_list)
    else:
        print('That is not an option.')
        unavailable_shirt(trouser, unavailableTrousers_list)


def verify_unavailable_trouser(trouser, unavailableTrouser_amount):
    print('')
    # create a list of the unavailable trousers for that week
    unavailableTrousers_list = []
    
    # code to handle the prompts based on the number of unavailable trousers
    for number in range(1, unavailableTrouser_amount + 1):
        print('Pick the ' + 'no' + str(number) + ' trouser you have unavailable')
        unavailableTrousers_pick = input()
        
        # ensure the trouser I type in is actually part of the trousers list
        if unavailableTrousers_pick in total_trousers:
            if unavailableTrousers_pick in unavailableTrousers_list:
                print('You have already picked this trouser, pick another.')
                continue
            # if it is, add it to the list
            unavailableTrousers_list.append(unavailableTrousers_pick)
        else:
            print('Not part of the list, restarting...')
            verify_unavailable_trouser(trouser, unavailableTrouser_amount)
    
    # after appending the list, send it as an argument to the unavailable_shirt function
    unavailable_shirt(trouser, unavailableTrousers_list)


def ask_how_many_unavailable_trousers_i_have(trouser):
    print('How many unavailable trousers do you have? (Enter a number)')
    # get an integer of the amount of unavailable trouser i have
    unavailableTrouser_amount = input()
    confirm_number = re.compile(r'\d+')
    amount_match = confirm_number.search(unavailableTrouser_amount)

    if amount_match:
        amount = int(amount_match.group())
        # ensure its actually an integer and it doesnt exceed the original amount of shirts i have
        if amount in range(1, 14):
            verify_unavailable_trouser(trouser, amount)
        else:
            print('That is not an acceptable answer.')
            ask_how_many_unavailable_trousers_i_have(trouser)
    else:
        print('That is not valid a number.')
        ask_how_many_unavailable_trousers_i_have(trouser)

def unavailable_trouser(trouser):
    print('Do you have any of your trousers unavailable? (y = yes, n = no)')
    allowed_inputs = ['y', 'yes', 'n', 'no']
    ans = input().lower()

    if ans in allowed_inputs:
        # verify if my input is part of allowed inputs
        if ans in ['y', 'yes']:
            # show list of all trouser
            print('---------------------------')
            for trous in total_trousers:
                if trous != trouser:
                    print(trous)  
            print('---------------------------') 
            ask_how_many_unavailable_trousers_i_have(trouser)
        else:
            unavailable_shirt(trouser, None)
    else:
        print('That is not an option.')
        unavailable_trouser(trouser)

# first code to run
# ask to pick what trouser you wore on sunday
def ask_to_pick_what_trouser_you_wore_on_sunday():
    print('')
    print('what trouser did you wear on sunday?')
    print('Available trousers:')
    print('---------------------------')
    # print out the list of trousers i have
    for trous in trousers_list:
        print(trous)
    print('---------------------------')
    trouser = input('Enter the trouser you wore: ')

    # ensure the trouser i pick is actually in the list of trousers i originally can wear on sunday
    if trouser in trousers_list:
        unavailable_trouser(trouser)
    else:
        print('The trouser you entered is not part of the list, please check, copy and paste the name of the trouser you wore.')
        ask_to_pick_what_trouser_you_wore_on_sunday()

def did_you_wear_a_trouser_on_sunday():
    allowed_inputs = ['y', 'yes', 'n', 'no']
    print('Did you wear a trouser on Sunday? (y = yes, n = no)')
    ans = input().lower()

    if ans in allowed_inputs:
        # verify if my input is part of allowed inputs
        if ans in ['n', 'no']:
            unavailable_trouser(None)
        else:
            ask_to_pick_what_trouser_you_wore_on_sunday()
    else:
        print('That is not an option.')
        did_you_wear_a_trouser_on_sunday()

# save the dictionary of all the cloth combination i had that week into its file
def save(picks):
    file_path = 'C:\\Users\\USER-PC\\Desktop\\PYTHON\\my projects\\problemsolving\\cloth_shuffler_data.py'
    with open(file_path, 'w') as fileobj:
        fileobj.write('picks = ' + pprint.pformat(picks) + '\n')
    
did_you_wear_a_trouser_on_sunday()
