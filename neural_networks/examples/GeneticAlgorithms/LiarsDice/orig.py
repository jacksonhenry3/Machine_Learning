import numpy as np
import sys
sys.path.insert(0, '../../../network')
from neuralNetwork import network
from scipy.misc import comb
np.random.seed(0)
numberOfPlayers = 5
numberOfDicePerPlayer = 5

class game(object):
    """docstring for game"""
    def __init__(self, numPlayers , dicePerPlayer = 5, onesWild = True):
        super(game, self).__init__()
        self.numPlayers = numPlayers
        self.numDice = numPlayers*dicePerPlayer
        self.dicePerPlayer = dicePerPlayer
        self.onesWild = onesWild



class player(object):
    """docstring for player"""
    def __init__(self, game):
        super(player, self).__init__()
        self.hand = np.random.randint(1,7,(numberOfDicePerPlayer))
        self.game = game

    def probability(self,bet):
        numDice = self.game.numDice - len(self.hand)
        num =bet[0]-len(np.where(self.hand == bet[1])[0])
        if not self.game.onesWild or bet[1] == 1:
            Pis = 1./6.
            PisElse = 5./6.
        else:
            Pis = 2./6.
            PisElse = 4./6.
        p = 0
        for i in range(numDice,num-1,-1):
            p += (Pis**i* PisElse**(numDice-i))*comb(numDice,i)
        return p

    def takeTurn(self,bet):
        p1 = self.probability(bet)
        die = bet[1]
        possibleBets = []
        while die <7:
            num = bet[0]
            if die == bet[1]:
                num = bet[0]+1

            possibleBets.append([num,die])
            die+=1

        possibleBets.sort(key=lambda x: self.probability(x))
        newBet = possibleBets[-1]
        p2 = self.probability(newBet)
        if p1<.5:
            return 'challenge'



newGame = game(2)
charecter = player(newGame)
print charecter.hand
charecter.takeTurn([3,2])
