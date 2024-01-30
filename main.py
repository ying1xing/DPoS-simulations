from protocol import Protocol
from committee import Committee
from deligator import Delegator
from validator import Validator
from cosmos import Cosmos
import matplotlib.pyplot as plt

if __name__ == '__main__':
    validators = []
    delegators = []
    for i in range(100):
        validators.append(Validator(len(validators), 200))
    for i in range(1000):
        delegators.append(Delegator(len(delegators), 50))

    committeeSize = 20
    rounds = 1000
    reward = 1000

    setup = Cosmos()

    protocol = Protocol(committeeSize, validators, delegators, rounds, setup, reward)
    protocol.run()

    rewards = [item.totalReward for item in validators]

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

