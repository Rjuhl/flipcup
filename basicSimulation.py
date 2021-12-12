import numpy as np

num_sims = 10000


def get_exp_sample(beta):
    return np.random.exponential(scale=beta)


def run_simple_exp(i, b1, b2):
    start = 0
    ends = (i - 1) / 2
    assert ends.is_integer() and ends > 0

    s1 = get_exp_sample(b1)
    s2 = get_exp_sample(b2)

    while start != ends and start != ends * -1:
        if s2 > s1:
            start -= 1
            if start != ends * -1:
                s1 += get_exp_sample(b1)
            else:
                break

        elif s1 > s2:
            start += 1
            if start != ends:
                s2 += get_exp_sample(b2)
            else:
                break
        else:
            s1 += get_exp_sample(s1)
            s2 += get_exp_sample(s2)

    player_win = 1 if start < 0 else 2
    time = s1 if player_win == 1 else s2

    return player_win, time


def printOutcome(cp, b1, b2):
    times = []
    p1_wins = 0
    p2_wins = 0
    for i in range(num_sims):
        winner, time = run_simple_exp(cp, b1, b2)
        if winner == 1:
            p1_wins += 1
        else:
            p2_wins += 1
        times.append(time)
    print(sum(times) / len(times))
    print(p1_wins / (p1_wins + p2_wins))


