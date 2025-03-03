treasures = [0, 1, 0, 1, -1, 1, 1, -1, 1, 1]
chance = 1

while chance < 6:
    print("This is your chance", chance)
    slots = input("Enter your 4 slot choices (comma-separated, e.g., 1,2,3,4): ")
    print("You entered:", slots)
    
    try:
        s1, s2, s3, s4 = map(int, slots.split(","))
        
        if not all(0 <= s < len(treasures) for s in [s1, s2, s3, s4]):
            print("Invalid input. Please enter numbers between 0 and 9.")
            continue

        t1, t2, t3, t4 = treasures[s1], treasures[s2], treasures[s3], treasures[s4]
        
        if t1 == -1 or t2 == -1 or t3 == -1 or t4 == -1:
            print("Game over\n --**-- You hit a BOMB --**--")
            break
        elif t1 + t2 + t3 + t4 == 4:
            print("You won the match!")
            break
        else:
            print("You lost this round.")
            chance += 1
    except ValueError:
        print("Invalid input format. Please enter four numbers separated by commas.")

if chance >= 6:
    print("Game over. Better luck next time!")
