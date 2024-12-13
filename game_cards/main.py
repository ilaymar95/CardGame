from card_game import CardGame

print("Card game will begin shorty!")
cards_to_deal=int(input("How many cards do you want? 10-26: "))
name1 = input("What is your name player 1?: ")
name2 = input("What is your name player 2?: ")
card_game = CardGame(name1,name2,cards_to_deal)
print(card_game.player1)
print(card_game.player2)
count_player1=0
count_player2=0
#Testing new_game()
# card_game.new_game()
for i in range (10):
    print(f"Round {i+1} started\n")
    player1_card = card_game.player1.get_card()
    player2_card = card_game.player2.get_card()
    print(f'{card_game.player1.name} took out {player1_card}\n{card_game.player2.name} took out {player2_card}')
    if player1_card > player2_card:
        print(f'{card_game.player1.name} won the round!')
        count_player1+=1
        card_game.player1.add_card(player1_card)
        card_game.player1.add_card(player2_card)
    else:
        print(f'{card_game.player2.name} won the round!')
        count_player2+=1
        card_game.player2.add_card(player1_card)
        card_game.player2.add_card(player2_card)
    print(f"Round {i+1} finished\n")

if card_game.get_winner() is None:
    print('The game ended in a tie!')
    print(card_game.player1)
    print(card_game.player2)
else:
    winner = card_game.get_winner()
    if winner.name == card_game.player1.name:
        print(f'{winner.name} won the game with {count_player1}/10 wins!')
    else:
        print(f'{winner.name} won the game with {count_player2}/10 wins!')
    print(winner)



