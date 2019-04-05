from scipy import stats
import numpy as np

# ---------- Chicken Game ----------

TEAM_NAME = "tarjul"
MEMBERS = ["ts4pe", "jac9vn"]

# 100 repititions to chicken
# avg would work, drawing from bothh parameters
# estimate reaction time, estimate for m and slace, so play it at mean, so fine some point after

global reaction_time   # the last reounds reactiont time
global previous_move  # last rounds opponents swerve time
#global

global outcome = -1
global swerve_time = 5


global prevSwerve_rounds = []
global prevScore_rounds = []
global prevReact = []


def regression_info():
    gradient, intercept, r_value, p_value, std_err = stats.linregress(prevSwerve_rounds, prevScore_rounds)
    print "Gradient and intercept:", gradient, intercept
    print "R-squared", r_value**2
    print "P-value", p_value


# Do for some number of rounds till we get enoguht data to compute information
def chose_next():
    if previous_move == 1:
        return swerve_time

    elif previous_move == -1:
        return swerve_time - 1

    elif previous_move == -10:
        return swerve_time + 1

def main_play():



def get_move(state):
    out = state.previous_rounds[len(state.previous_rounds) - 1]
    out = chose_next(out)
    return out

# ---------- Connect More ----------

# see if win is solvable (forced), means shorter connect value and thick board, else...
