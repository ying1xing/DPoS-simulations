from protocol import Protocol
from committee import Committee
from deligator import Delegator
from validator import Validator
from byzantine import Byzantine
from cosmos import Cosmos
from randomselect import RandomSelect
import matplotlib.pyplot as plt

if __name__ == '__main__':
    validators = []
    delegators = []
    for i in range(70):
        validators.append(Validator(len(validators), 200))
    for i in range(30):
        validators.append(Byzantine(len(validators), 200, [validators[0]], True))
    for i in range(1000):
        delegators.append(Delegator(len(delegators), 50))

    committeeSize = 20
    rounds = 50000
    reward = 1000

    #setup = Cosmos()
    setup = RandomSelect()

    protocol = Protocol(committeeSize, validators, delegators, rounds, setup, reward)
    protocol.run()

    rewards = [v.totalReward for v in validators]

    dcounts = [v.dcount/rounds for v in validators]

    print(dcounts)
    print(rewards)

    # Generate x-axis values (0 to 99 in this case)
    x = range(len(rewards))

    # Create the bar plot
    plt.bar(x, rewards)

    # Add labels and title
    plt.xlabel('Item')
    plt.ylabel('Reward')
    plt.title('Comparison of Rewards')

    # Display the plot
    plt.show()

    plt.bar(x, dcounts)

    # Add labels and title
    plt.xlabel('Validators')
    plt.ylabel('Average number of delegators per round')
    plt.title('Comparison')

    # Display the plot
    plt.show()

