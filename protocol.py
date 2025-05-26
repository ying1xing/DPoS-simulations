# -*- coding: utf-8 -*-
from committee import Committee
import time
import random

class Protocol:
    def __init__(self, committeeSize, validators, delegators, rounds, setup, reward, offline_rate):
        self.committeeSize = committeeSize
        self.validators = validators
        self.delegators = delegators
        self.rounds = rounds
        self.blockchain = []
        self.setup = setup
        self.reward = reward
        self.offline_rate = offline_rate  # 新增参数，用于存储掉线率

    def selectCommittee(self):
        committee = Committee(self.committeeSize, self.setup)
        self.setup.selectCommittee(committee, self.validators)
        return committee

    def calculateRewards(self, committee):
        committee.calculateRewards(self.reward)

    def calculateValidatorsScores(self):
        total_rewards = sum(validator.totalReward for validator in self.validators)
        total_stake = sum(validator.votingPower for validator in self.validators)
        for validator in self.validators:
            if validator.count == 0:
                validator.score = 10000000
            else:
                validator.score = ((validator.totalReward / total_rewards) / (validator.votingPower * validator.count)) * 10000000

    def updateDelegations(self):
        for delegator in self.delegators:
            delegator.changeValidator(self.validators)

    def run(self):
        block_gap = 3  # 设置出块间隙为 3 秒
        block_times = []  # 用于存储每两个相邻块之间的生成时间差
        last_time = time.time()  # 记录上一个块的生成时间
        start_time = time.time()  # 记录模拟开始时间
        block_count = 0  # 记录成功生成的块的数量

        for i in range(self.rounds):
            print(i)
            self.updateDelegations()
            committee = self.selectCommittee()

            # 根据设置的掉线率模拟出块节点掉线
            if random.random() < self.offline_rate:
                print(f"Round {i}: 出块节点掉线")
                time.sleep(block_gap)
                continue

            start_round_time = time.time()
            newBlock = committee.round()
            end_round_time = time.time()

            if end_round_time - start_round_time > block_gap:
                print(f"Round {i}: 出块时间超过 {block_gap} 秒，进入下一轮")
                continue

            if newBlock is not None:
                current_time = time.time()  # 记录当前块的生成时间
                block_times.append(current_time - last_time)  # 计算时间差并存储
                last_time = current_time  # 更新上一个块的生成时间

                self.blockchain.append(newBlock)
                self.calculateRewards(committee)
                self.calculateValidatorsScores()

                block_count += newBlock.transaction_count  # 增加块的数量
                time.sleep(block_gap)  # 引入 3 秒的出块间隙

        end_time = time.time()  # 记录模拟结束时间
        total_time = end_time - start_time  # 计算总时间

        # 计算平均出块时间
        if block_times:
            average_block_time = sum(block_times) / len(block_times)
            print("Average block time: {:.2f} seconds".format(average_block_time))
        else:
            print("No blocks were generated.")

        # 计算 TPS
        if total_time > 0:
            tps = block_count / total_time
            print("TPS: {:.2f} transactions per second".format(tps))
        else:
            print("TPS cannot be calculated as total time is 0.")
