from committee import Committee
from validator import Validator

class Cosmos:

    def selectMostStaked(committee, pool):
        pool.sort(key=lambda x: x.votingPower, reverse=True)
        for i in range(committee.size):
            committee.validators.append(pool[i])