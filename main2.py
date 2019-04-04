TEAM_NAME = "tarjul2"
MEMBERS = ["ts4pe", "jac9vn"]


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
