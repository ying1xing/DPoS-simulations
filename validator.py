import random
from block import Block

class Validator:
    def __init__ (self , id , type , stake):
        self.id = id
        self.type = type
        self.stake = stake
        self.proposedBlocks = []
        self.delegators = {}
        self.votingPower = 0
        self.totalReward = 0

    def propose(self, committee):
        r = random.randint(0, 100)
        b = Block(r, self, committee)
        self.proposedBlocks.append(b)
        return b

    def sign(self , block):
        if block.isValid():
            return True
        return False

    def selectVoters(self, votes):
        voters = {}
        for voter in votes:
            if votes[voter]:
                voters[voter] = True
        return voters

    def removeDelegator(self, delegator):
        self.delegators[delegator] = 0
        self.votingPower -= delegator.stake

    def addDelegator(self, delegator):
        self.delegators[delegator] = delegator.stake
        self.votingPower += delegator.stake

    def updateReward(self, pool, reward, totalReward):
        self.totalReward += (self.stake / self.votingPower) * reward
        for delegator in self.delegators:
            if self.delegators[delegator] > 0:
                share = delegator.stake/self.votingPower
                delegator.updateReward(pool, share, totalReward)