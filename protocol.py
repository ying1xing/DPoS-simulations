from committee import Committee

class Protocol:
    def __init__(self, committeeSize, validators, deligators, rounds, setup):
        self.committeeSize = committeeSize
        self.validators = validators
        self.deligators = deligators
        self.rounds = rounds
        self.blockchain = []
        self.setup = setup

    def selectCommittee(self):
        self.committee = Committee(self.committeeSize)
        self.committeeSelector(self.committee, self.validators)

    def calculateRewards(self):
        pass

    def run(self):
        for i in self.rounds:
            committee  = self.selectCommittee()
            newBlock = committee.round(self.blockchain)
            if newBlock is not None:
                self.blockchain.append(newBlock)
                self.calculateRewards()



