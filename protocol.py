from committee import Committee

class Protocol:
    def __init__(self, committeeSize, validators, deligators, committeeSelector, rounds):
        self.committeeSize = committeeSize
        self.validators = validators
        self.deligators = deligators
        self.committeeSelector = committeeSelector
        self.rounds = rounds
        self.blockchain = []

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



