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
global

outcome = -1

swerve_time = 5


prevSwerve_rounds = [1, 1, 3, 4, 2, 1]
prevScore_rounds = [-1, -1, 1, 1, 1, -1]


def regression_info(x, y):
    gradient, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    print "Gradient and intercept:", gradient, intercept
    print "R-squared", r_value**2
    print "P-value", p_value


def chose_next():
    if previous_move == 1:
        return swerve_time

    elif previous_move == -1:
        return swerve_time - 1

    elif previous_move == -10:
        return swerve_time + 1


def get_move(state):
    out = state.previous_rounds[len(state.previous_rounds) - 1]
    out = chose_next(out)
    return out

# ---------- Connect More ----------

# see if win is solvable (forced), means shorter connect value and thick board, else...
