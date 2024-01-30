from validator import Validator

class Byzantine (Validator):
    def __init__(self, id , stake, victims):
        super().__init__(id , stake)
        self.victims = victims
        pass

    def selectVoters(self, votes):
        voters = []
        for voter in votes:
            if voter not in self.victims:
                if votes[voter]:
                    voters.append(voter)
        return voters