hunger_settings = ['hungry', 'full']
feeding_time = (9, 15, 18, 21)
current_time = 19
total_hours = 24
last_fed = 0

for i in feeding_time:
    print('List of feeding times')
    print(i)
    if current_time - i < 6:
        print('Moving to next iteration')
    else:
        last_fed = i
        print('last fed time is {lf}'.format(lf=last_fed))
        break
