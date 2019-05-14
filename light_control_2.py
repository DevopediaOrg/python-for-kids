light_on = None

if 'y' == input("Is it dark? [y/n]: "):
    is_dark = True
else:
    is_dark = False

if 'y' == input("Are you sleepy? [y/n]: "):
    is_sleepy = True
else:
    is_sleepy = False

if is_dark and not is_sleepy:
    light_on = True
    print("Switching on the light!")
else:
    light_on = False
    print("Switching off the light!")
