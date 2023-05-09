from validator import Validator
class Committee:
    def __init__(self, size, setup):
        self.size = size
        self.validators = []
        self.votes = {}
        self.proposer = None
        self.selectedVotes = []
        self.setup = setup

    def chooseProposer(self):
        self.proposer = self.setup.chooseProposer(self.validators)

    def round(self):
        self.chooseProposer()
        newBlock = self.proposer.propose(self)
        for v in self.validators:
            self.votes[v] = v.sign(newBlock)
        self.selectedVoters = self.proposer.selectVotes(self.votes)
        if newBlock.isConfirmed(self.validators, self.selectedVoters):
            return newBlock
        else:
            print ("Invalid")
            return None