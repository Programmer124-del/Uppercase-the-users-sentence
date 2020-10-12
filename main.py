start = True
while True:
    cap_it = input("Please enter a sentence: ")
    print(cap_it.upper())
    start = False
    again = input("""Would you like to go again? 
    To go again, press y.
    To stop, press n.
    > """)

    if again == 'y':
        start = True
    elif again == 'n':
        break
