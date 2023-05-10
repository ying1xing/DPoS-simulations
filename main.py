from protocol import Protocol
from committee import Committee
from deligator import Delegator
from validator import Validator
from cosmos import Cosmos


if __name__ == '__main__':
    validators = []
    delegators = []
    for i in range(100):
        validators.append(Validator(len(validators), 200))
    for i in range(200):
        delegators.append(Delegator(len(delegators), 50))

    committeeSize = 20
    rounds = 1000
    reward = 100

    setup = Cosmos()

    protocol = Protocol(committeeSize, validators, delegators, rounds, setup, reward)
    protocol.run()

