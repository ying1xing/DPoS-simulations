from validator import Validator
class Committee:
    def __init__(self, size, setup):
        self.size = size
        self.validators = []
        self.votes = {}
        self.proposer = None
        self.selectedVoters = []
        self.setup = setup

    def chooseProposer(self):
        self.proposer = self.setup.chooseProposer(self.validators)

    def totalVotersVotingPower(self):
        total = sum(v.votingPower for v in self.selectedVoters)
        return total

    def calculateRewards(self, reward):
        total = self.totalVotersVotingPower()
        for validator in self.selectedVoters:
            share = (validator.votingPower / total) * reward
            validator.updateReward(self.validators, share, reward)

    def round(self):
        self.chooseProposer()
        newBlock = self.proposer.propose(self)
        for v in self.validators:
            self.votes[v] = v.sign(newBlock)
        self.selectedVoters = self.proposer.selectVoters(self.votes)
        if newBlock.isConfirmed(self.validators, self.selectedVoters):
            return newBlock
        else:
            print ("Invalid")
            return None
