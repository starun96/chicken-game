from scipy import stats
import numpy as np

# ---------- Chicken Game ----------

TEAM_NAME = "tarjul"
MEMBERS = ["ts4pe", "jac9vn"]

# 100 repititions to chicken
# avg would work, drawing from bothh parameters
# estimate reaction time, estimate for m and slace, so play it at mean, so fine some point after

outcome = -1
swerve_time = 5

my_moves = []
my_scores = []
opp_moves = []
reaction_times = []  # the last reounds reactiont time
my_previous_move = -1  # my last swerve time
num_rounds_batch = 20
""" 
def regression_info():
    gradient, intercept, r_value, p_value, std_err = stats.linregress(prevSwerve_rounds, prevScore_rounds)
    print "Gradient and intercept:", gradient, intercept
    print "R-squared", r_value**2
    print"P-value", p_value 
"""


""" def calc_sum_last_N_rounds():
    batch_rounds = prevScore_rounds[:-N]
    reaction_mean = np.average(prevReact)
    score_sum = np.sum(batch_rounds)
    if score_sum > 0:
        return swerve_time - reaction_time
    elif:
        score_sum < 0:
        return swerve_time + reaction_mean
    else:
        return swerve_time """


""" # Do for some number of rounds till we get enoguht data to compute information
def chose_next():
    if previous_move == 1:
        return swerve_time

    elif previous_move == -1:
        return swerve_time - 1

    elif previous_move == -10:
        return swerve_time + 1 """


def get_move(state):
    if state['game'] == "chicken":
        """ Chicken game -- avoid colliding or swerving before your opponent, given reaction time distrubtion, previous scores, and opp moves  """

        opp_moves.append(state['previous-move'])
        my_scores.append(state['outcome'])
        reaction_times.append(state['reaction-time'])
        mean_reaction_time = np.average(reaction_times)
        stdev_reaction_time = np.stdev(reaction_times)
        next_move = mean_reaction_time - 3 * stdev_reaction_time
        my_moves.append(next_move)

        return next_move
    else:
        """ Connect More - see if win is solvable (forced), means shorter connect value and thick board, else... """

        pass
