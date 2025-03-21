time_input = str(input("Введите время:"))
def time_to_minutes(user_time):
    new_time = user_time.split(":")
    minutes = new_time[0] = int(new_time[0]) * 60 + int(new_time[1])
    return minutes

a = time_to_minutes(time_input)
print(a)