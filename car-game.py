# Practising while loop in Python


command = ""

help_message = '''
Type:
Start - to start the car
Stop - to stop the car
quit - to quit game
   '''

is_car_started = False
is_car_stopped = False


while True:
    command = input("tosh> ").upper()
    if command == "START":
        if is_car_started:
            print("You have already started this car!")
        else:
            is_car_started = True
            print("Car started, moving...")
    elif command == "STOP":
        if is_car_stopped:
            print("Until you spoil this car?")
        else:
            is_car_stopped = True
            print("Car is stopped")
    elif command == "HELP":
        print(help_message)
    elif command == "QUIT":
        print("Okay, bye.")
        break
    else:
        print("Wrong input!")

