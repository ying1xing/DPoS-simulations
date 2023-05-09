from validator import Validator
class Committee:
    def __init__(self, size):
        self.size = size
        self.validators = []
        self.votes = {}
        self.proposer = None

    def chooseProposer(self):
        pass

    def round(self, blockchain):
        self.chooseProposer()
        newBlock = self.proposer.propose(self.blocks)
        for v in self.validators:
            self.votes[v] = v.sign(newBlock)
        self.proposer.selectVotes(self.votes)
        if newBlock.isConfirmed(self.validators, self.votes):
            blockchain.append(newBlock)
            return True
        else:
            print ("Invalid")
            return False