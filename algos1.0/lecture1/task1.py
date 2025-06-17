current_temp, target = map(int, input("Enter current temp in the room and target temp(e.g. 10 20): ").split()) # split() -> ["10", "20"]; map -> int 10, int 20
mode = input("Modes available: freeze, heat, auto, fan: ").lower()

if mode == "freeze":
    if target <= current_temp:
        print(target)
    elif target >= current_temp:
        print(current_temp)
    else:
        print("Error")
elif mode == "heat":
    if target >= current_temp:
        print(target)
    elif target <= current_temp:
        print(current_temp)
    else:
        print("Error")
elif mode == "fan":
    print(current_temp)
elif mode == "auto":
    print(target)