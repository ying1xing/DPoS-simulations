import random

class Cosmos:

    def selectCommittee(self, committee, pool):
        pool.sort(key=lambda x: x.votingPower, reverse=True)
        for i in range(committee.size):
            committee.validators.append(pool[i])
            
    def chooseProposer(self, validators):
         return random.choice(validators)