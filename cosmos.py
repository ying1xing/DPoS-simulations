import random

class Cosmos:

    def __init__(self):
        self.bonus = 0.05

    def selectCommittee(self, committee, pool):
        sorted_pool = sorted(pool, key=lambda x: x.votingPower, reverse=True)
        for i in range(committee.size):
            committee.validators.append(sorted_pool[i])
            sorted_pool[i].count += 1
            
    def chooseProposer(self, validators):
         return random.choice(validators)
