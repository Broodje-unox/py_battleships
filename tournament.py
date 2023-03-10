from engine import Game
import matplotlib.pyplot as plt  

n_games = 5000
n_shots = []
n_wins1 = 0
n_wins2 = 0 

for i in range(n_games):
    game = Game(human1 = False, human2 = False)
    while not game.over:
        if game.player1_turn:
            game.basic_ai()
        else: 
            game.basic_ai()
    n_shots.append(game.n_shots)
    if game.result == 1:
        n_wins1 += 1
    elif game.result == 2:
        n_wins2 += 1

print(n_wins1)
print(n_wins2)

values = []
for i in range(17, 200):
    values.append(n_shots.count(i))

plt.bar(range(17, 200), values)
plt.show()
