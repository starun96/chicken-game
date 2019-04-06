from scipy import stats
import numpy as np

# ---------- Chicken Game ----------

TEAM_NAME = "tarjul"
MEMBERS = ["ts4pe", "jac9vn"]

# 100 repititions to chicken
# avg would work, drawing from bothh parameters
# estimate reaction time, estimate for m and slace, so play it at mean, so fine some point after

swerve_time = 5
opp_bias = 0
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


def get_move(state):
    if state['game'] == "chicken":
        """ Chicken game -- avoid colliding or swerving before your opponent, given reaction time distrubtion, previous scores, and opp moves  """

        # gather the inputs; append them to the global state
        opp_moves.append(state['previous-move'])
        outcome = state['outcome']
        my_scores.append(outcome)
        reaction_times.append(state['reaction-time'])

        # we want the next move to be just under the valid range of reaction times, so next_move = mean - 3*stdev
        mean_reaction_time = np.average(reaction_times)
        stdev_reaction_time = np.stdev(reaction_times)

        # adjust the next move depending on whether the opponent is winning or not
        if outcome == -1:
            opp_bias += 1
        if outcome == 1:
            opp_bias -= 1
        next_move = mean_reaction_time + opp_bias - 3 * stdev_reaction_time
        if next_move < 0:
            next_move = 0
        my_moves.append(next_move)

        return next_move
    else:
        """ Connect More - see if win is solvable (forced), means shorter connect value and thick board, else... """

        # gather the inputs
        connect_n = state['connect_n']
        columns = state['columns']
        your_token = state['your-token']
        board = state['board']

        pass
