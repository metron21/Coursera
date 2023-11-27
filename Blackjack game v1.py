import random
    ##Implicit values / structure = cards  and players and choices
x = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
z = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    # use the random.choice to pic randomly from the list in a static manner.
player = random.choice(x)
dealer = random.choice(z)
    ### Player rule: I get to draw an unlimited amount of times until i meet condition <22
    # using the increment function += I add random numbers from the list
    # += inside the loop grabs a different iteration of cards as long <22 condition remains true
while player < 22:
    
    inc = random.choice(x)

    print("Dealer has: " + str(dealer))
    print("Player has: " + str(player))
    
    i = input("Hit or stand: ")
    # The += was logic choice because i want to add increments only after i hit
    if i == "hit":
        player += inc
        if player > 21:
            print("Player busts")
            break
    elif i == "stand":
        # i want the dealer to draw until <17 condiotion is met
        while dealer < 17:
            dealer += random.choice(x)
        # result is outside of the loop because i want result number not all iterations
        print ("dealer has:" +str(dealer))
           
        # I easliy use blackjack rules to determine who wins usings if statements
        if dealer == player:
            print("Push")
        elif dealer == 21:
            print ("Dealer BJ")
        elif dealer > 21:
            print("Dealer busts. Player wins!")
        elif dealer > player:
            print("Dealer wins!")
        elif dealer < player:
            print("Player wins!")
        break