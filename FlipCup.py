import ExpectedTime
import ProbWinning
import basicSimulation


# c = Num of Checkpoints, r1 = lambda_1, and r2 = lambda_2
def wc(c, r1, r2):
    return ProbWinning.findWinningChances(c, r1, r2)


# ranges = (range graphed of var1, range graphed of var2)
# const_dim = the dim to hold const 0 = c, 1 = r1, 2 = r2
# c = val if const dim
# r1 = val if const dim
# r2 = val if const dim
def g3D(ranges, const_dim, c=None, r1=None, r2=None):
    return ProbWinning.graph3D(ranges, const_dim, c=c, r1=r1, r2=r2)


# r1 =  Const rate of player 1, r2 = Const rate of player 2, and ran = range checkpoints to graph
def g2D(r1, r2, ran):
    return ProbWinning.graph2D(r1, r2, ran)


# c = Num of Checkpoints, r1 = lambda_1, and r2 = lambda_2
def et(c, r1, r2):
    return ExpectedTime.findExpTime(c, r1, r2)


# c = Num of Checkpoints, r1 = lambda_1, r2 = lambda_2, and times = the number of sims to average across
def sim(c, r1, r2, times=1):
    p1_wins = 0
    p2_wins = 0
    b1 = 1/r1
    b2 = 1/r2
    t = []
    for i in range(times):
        winner, time = basicSimulation.run_simple_exp(c, b1, b2)
        if winner == 1:
            p1_wins += 1
        else:
            p2_wins += 1
        t.append(time)
    return sum(t) / len(t), p1_wins / (p1_wins + p2_wins)