import random

class RandomSelect:
    def __init__(self):
        self.bonus = 0

    def selectCommittee(self, committee, pool):
        weights = [validator.votingPower for validator in pool]
        validators = set()
        while len(validators) < committee.size:
            chosen_validator = random.choices(pool, weights=weights)[0]
            validators.add(chosen_validator)
        validators = list(validators)
        for i in range(committee.size):
            committee.validators.append(validators[i])
            validators[i].count += 1

    def chooseProposer(self, validators):
        return random.choice(validators)