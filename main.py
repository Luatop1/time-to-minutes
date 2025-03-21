while True:
    time_input = str(input("Введите время, например 12:07 :"))
    new_time = time_input.split(":")
    if int(new_time[0]) > 24 or int(new_time[0]) < 0 or int(new_time[1]) >= 60 or int(new_time[1]) < 0:
        print("Введите правильно время!")
    else:
        break

def time_to_minutes(user_time, new_time):
    minutes = new_time[0] = int(new_time[0]) * 60 + int(new_time[1])
    return minutes

minutes = time_to_minutes(time_input, new_time)
print(f"Ваше время в минутах: {minutes}")