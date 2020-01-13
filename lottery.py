from random import randint

def lottery():
    main_numbers = [randint(1, 35) for i in range(7)]
        powerball_number = [randint(1, 20)]
            #draw_number = main_numbers + powerball_number
                print(main_numbers, powerball_number)
for i in range(10):
    lottery()
