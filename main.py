from protocol import Protocol
from committee import Committee
from deligator import Delegator
from validator import Validator
from byzantine import Byzantine
from cosmos import Cosmos
from randomselect import RandomSelect
import matplotlib.pyplot as plt
import time

if __name__ == '__main__':
    validators = []
    delegators = []
    for i in range(70):
        validators.append(Validator(len(validators), 200))
    for i in range(30):
        validators.append(Byzantine(len(validators), 200, [validators[0]], False))
    for i in range(1000):
        delegators.append(Delegator(len(delegators), 50, 1, 0))

    committeeSize = 20
    rounds = 600
    reward = 1000
    offline_rate = 0.1  # 手动设置掉线率

    # setup = Cosmos()
    setup = RandomSelect()

    protocol = Protocol(committeeSize, validators, delegators, rounds, setup, reward, offline_rate)
    protocol.run()

    rewards = [v.totalReward for v in validators]
    dcounts = [v.dcount/rounds for v in validators]
    overallrewards = [v.overallRewars for v in validators]
    block_proposal_counts = [v.block_proposal_count for v in validators]  # 获取出块次数

    print(dcounts)
    print(rewards)
    print(overallrewards)
    print(block_proposal_counts)  # 打印出块次数

    # Generate x-axis values (0 to 99 in this case)
    x = range(len(rewards))

    # Create the bar plot for rewards
    plt.bar(x, rewards)
    plt.xlabel('Item')
    plt.ylabel('Reward')
    plt.title('Comparison of Rewards')
    plt.savefig('rewards_plot.png')
    plt.clf()

    # Create the bar plot for delegators
    plt.bar(x, dcounts)
    plt.xlabel('Validators')
    plt.ylabel('Average number of delegators per round')
    plt.title('Comparison')
    plt.savefig('delegators_plot.png')
    plt.clf()

    # Create the bar plot for block proposal counts
    plt.bar(x, block_proposal_counts)
    plt.xlabel('Validators')
    plt.ylabel('Block Proposal Count')
    plt.title('Block Proposal Counts of Validators')
    plt.savefig('block_proposal_counts_plot.png')
