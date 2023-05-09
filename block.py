class Block:
    def __init__(self, id, content, proposer, committee):
        self.id = id
        self.content = content
        self.signers = []
        self.proposer = proposer
        self.committee = committee

    def isValid(self):
        return True

    def isConfirmed(self , size):
        if len(self.signatures) > (2*(size / 3)):
            return True
        return False