light_on = None
is_dark = input("Is it dark? [y/n]: ")
is_sleepy = input("Are you sleepy? [y/n]: ")

if is_dark == 'y' and is_sleepy != 'y':
    light_on = True
    print("Switching on the light!")
else:
    light_on = False
    print("Switching off the light!")
