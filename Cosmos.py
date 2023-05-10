import random

class Cosmos:

    def selectCommittee(self, committee, pool):
        sorted_pool = sorted(pool, key=lambda x: x.votingPower, reverse=True)
        for i in range(committee.size):
            committee.validators.append(sorted_pool[i])
            
    def chooseProposer(self, validators):
         return random.choice(validators)