def addActivity():
    global activities

    activity_name = input("Aktywność >> ")
    activity_time = float(input("Czas trwania >> "))
    while(activity_time <=0):
        activity_time = input("[!] Podaj dodatni czas >> ")
    
    if activity_name not in activities:
        activities[activity_name] = [activity_time]
    else:
        activities[activity_name].append(activity_time)


def activityTime(activity_name):
    global activities

    if activity_name in activities.keys():
        sum = 0
        for i in activities[activity_name]:
            sum += i
        return sum
    else:
        return 0

def top3Activities():
    global activities
    # lista [nazwa, czas] dla top 3 aktywności
    top3 = [['', 0], ['', 0], ['', 0]]

    if len(activities.keys()) >= 3:
        for key in activities.keys():
            key_time = activityTime(key)

            if key_time > top3[0][1]:
                # przesuwa ranking o 1 miejsce w dół
                top3[1], top3[2] = top3[2], top3[1]
                top3[0], top3[1] = top3[1], top3[0]

                top3[0][1] = key_time
                top3[0][0] = key

            elif key_time > top3[1][1]:
                top3[1], top3[2] = top3[2], top3[1]

                top3[1][1] = key_time
                top3[1][0] = key

            elif key_time > top3[2][1]:
                top3[2][1] = key_time
                top3[2][0] = key

        for i in range(3):
            print("{}. {} [{}]\n".format(i+1, top3[i][0], top3[i][1]))

    else:
        print("[!] Niewystarczająca liczba aktywności.")

    
activities = {}

action = int(input("[1] Dodaj aktywność.\n[2] Łączny czas w aktywności.\n"
                   "[3] Top 3 aktywności.\n\n>> "))

while(action >=1 and action <=3):    
    if action == 1:
        addActivity()

    elif action == 2:
        activity = input("Aktywność >> ")
        print("Łącznie spędzony czas na < {} > to {}."
            .format(activity, activityTime(activity)))

    else:
        top3Activities()

    action = int(input("\n>> "))