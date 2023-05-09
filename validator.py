import random
from block import Block

class Validator:
    def __init__ (self , id , type , stake):
        self.id = id
        self.type = type
        self.stake = stake
        self.proposedBlocks = []
        self.deligators = {}
        self.votingPower = 0

    def propose(self, committee):
        r = random.randint(0, 100)
        b = Block(r, self, committee)
        self.proposedBlocks.append(b)
        return b

    def sign(self , block):
        if block.isValid():
            return True
        return False

    def selectVotes(self, votes):
        voters = []
        for voter in votes:
            if votes[voter]:
                voters.append[voter]
        return voters