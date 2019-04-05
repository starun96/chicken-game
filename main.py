

# ---------- Chicken Game ----------

TEAM_NAME = "tarjul"
MEMBERS = ["ts4pe", "jac9vn"]

# 100 repititions to chicken
# avg would work, drawing from bothh parameters
# estimate reaction time, estimate for m and slace, so play it at mean, so fine some point after mean

global reacton_time   # the last reounds reactiont time
global previous_move  # last rounds opponents swerve time
global

outcome = -1

swerve_time = 5

previous_rounds = []

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
