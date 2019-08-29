import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Getting Size Of GridWorld:
# m = int(input("Enter Vertical Length Of GW"))
# n = int(input("Enter Horizontal Length Of GW"))
m = 3
n = 4
# Grid World Matrix
GW = np.array(np.zeros(shape=(m, n)))
print(GW)

Blocks = [(0, 1), (1, 2)]
for i in Blocks:
    GW[i] = 1
GW[m - 1, n - 1] = 2
print(GW)
# Reward Matrix
R = np.array(np.ones(shape=(m, n)))
R = (-1) * R
R[m - 1, n - 1] = 500
print(R)

# Extract State Positions:
state_idx = []
for i in range(m):
    for j in range(n):
        if GW[i, j] == 0 or GW[i, j] == 2:
            state_idx.append((i, j))

print(state_idx)

s = pd.Series(data=state_idx, index=range(len(state_idx)))
# print(s)
# print(s[5][0])
# print(type(s[5]))

# current_state_idx = int(np.random.choice(len(state_idx), size=1))
# print(current_state_idx, type(int(current_state_idx)))
# current_state =s[current_state_idx]
# print(current_state)
# print(current_state[1])

t = pd.Series(data=range(len(state_idx)), index=state_idx)
print(t)
print(t[(1, 3)])
q = t[(1, 3)] + 2
print(q)
# Q-Matrix
actions_list = ['up', 'down', 'left', 'right']
print(actions_list)
Q = np.array(np.zeros(shape=(len(state_idx), 4)))
Q_SARSA = np.array(np.zeros(shape=(len(state_idx), 4)))
print(Q)

gamma = 0.9
alpha = 0.5
p = 0.8  # Action Selection Probability


def Sample_Next_Action(state):
    q = np.random.rand(1, 1)

    max_index = np.where(np.max(Q[state_idx.index(state),]) == Q[state_idx.index(state),])[0]
    if max_index.shape[0] > 1:
        max_index = int(np.random.choice(max_index, size=1))
    else:
        max_index = int(max_index)
    if max_index == 0:
        if 0 < q < p:
            next_action = 'up'
        else:
            next_action = np.random.choice(['down', 'left', 'right'], size=1)
    elif max_index == 1:
        if 0 < q < p:
            next_action = 'down'
        else:
            next_action = np.random.choice(['up', 'left', 'right'], size=1)

    elif max_index == 2:
        if 0 < q < p:
            next_action = 'left'
        else:
            next_action = np.random.choice(['up', 'down', 'right'], size=1)
    else:
        if 0 < q < p:
            next_action = 'right'
        else:
            next_action = np.random.choice(['up', 'down', 'left'], size=1)
    return next_action


def Sample_Next_State(current_state, action):
    if action == 'up':
        if current_state[0] == 0:
            next_state = current_state
        elif (current_state[0] - 1, current_state[1]) in Blocks:
            next_state = current_state
        else:
            next_state = (current_state[0] - 1, current_state[1])
    if action == 'down':
        if current_state[0] == m - 1:
            next_state = current_state
        elif (current_state[0] + 1, current_state[1]) in Blocks:
            next_state = current_state
        else:
            next_state = (current_state[0] + 1, current_state[1])
    if action == 'left':
        if current_state[1] == 0:
            next_state = current_state
        elif (current_state[0], current_state[1] - 1) in Blocks:
            next_state = current_state
        else:
            next_state = (current_state[0], current_state[1] - 1)
    if action == 'right':
        if current_state[1] == n - 1:
            next_state = current_state
        elif (current_state[0], current_state[1] + 1) in Blocks:
            next_state = current_state
        else:
            next_state = (current_state[0], current_state[1] + 1)
    return next_state


def Update_q(sample_next_state, current_state, action, gamma, alpha):
    if action == 'up':
        action_num = 0
    elif action == 'down':
        action_num = 1
    elif action == 'left':
        action_num = 2
    else:
        action_num = 3
    max_index_next = np.where(np.max(Q[state_idx.index(sample_next_state),]) == Q[state_idx.index(sample_next_state),])[
        0]
    if max_index_next.shape[0] > 1:
        max_index_next = int(np.random.choice(max_index_next, size=1))
    else:
        max_index_next = int(max_index_next)

    max_value = Q[state_idx.index(sample_next_state), max_index_next]
    Q[state_idx.index(current_state), action_num] = (1 - alpha) * Q[
        state_idx.index(current_state), action_num] + alpha * (
                                                            R[sample_next_state] + gamma * max_value)
    print('max_value', R[sample_next_state] + gamma * max_value)
    if np.max(Q) > 0:
        return np.sum(Q / np.max(Q) * 100)
    else:
        return 0

def Update_SARSA(sample_next_state, current_state, action, next_action, gamma, alpha):
    if action == 'up':
        action_num = 0
    elif action == 'down':
        action_num = 1
    elif action == 'left':
        action_num = 2
    else:
        action_num = 3

    if next_action == 'up':
        action_num1 = 0
    elif next_action == 'down':
        action_num1 = 1
    elif next_action == 'left':
        action_num1 = 2
    else:
        action_num1 = 3
    # max_index_next = np.where(np.max(Q[state_idx.index(sample_next_state),]) == Q[state_idx.index(sample_next_state),])[
    #     0]
    # if max_index_next.shape[0] > 1:
    #     max_index_next = int(np.random.choice(max_index_next, size=1))
    # else:
    #     max_index_next = int(max_index_next)

    # max_value = Q[state_idx.index(sample_next_state), max_index_next]
    Q_SARSA[state_idx.index(current_state), action_num] = (1 - alpha) * Q_SARSA[
        state_idx.index(current_state), action_num] + alpha * (
                                                            R[sample_next_state] + gamma * Q_SARSA[state_idx.index(sample_next_state), action_num1])
    # print('max_value', R[sample_next_state] + gamma * max_value)
    if np.max(Q_SARSA) > 0:
        return np.sum(Q_SARSA / np.max(Q_SARSA) * 100)
    else:
        return 0


# Training
for i in range(700):
    scores1 = []
    current_state_idx1 = int(np.random.choice(len(state_idx), size=1))
    current_state1 = s[current_state_idx1]
    steps1 = [current_state1]
    while current_state1 != (m - 1, n - 1):
        action1 = Sample_Next_Action(state=current_state1)
        Next_state1 = Sample_Next_State(current_state1, action1)
        action2 = Sample_Next_Action(state=Next_state1)
        score1 = Update_SARSA(Next_state1, current_state1, action1,action2, gamma, alpha)
        scores1.append(score1)
        steps1.append(Next_state1)
        current_state1 = Next_state1
    print("Most Efficient Path")
    print(steps1)
print("Trained Q_SARSA Matrix")
print(Q_SARSA / np.max(Q_SARSA) * 100)

k = 0
for i in range(700):
    k = k+1
    scores = []
    current_state_idx = int(np.random.choice(len(state_idx), size=1))
    current_state = s[current_state_idx]
    steps = [current_state]
    while current_state != (m - 1, n - 1):
        action = Sample_Next_Action(state=current_state)
        Next_state = Sample_Next_State(current_state, action)
        score = Update_q(Next_state, current_state, action, gamma, alpha)
        scores.append(score)
        steps.append(Next_state)
        current_state = Next_state
    print("Most Efficient Path")
    print(steps)
    if i>1 and  :


print("Trained Q Matrix")
print(Q / np.max(Q) * 100)

print("Trained Q_SARSA Matrix")
print(Q_SARSA / np.max(Q_SARSA) * 100)
