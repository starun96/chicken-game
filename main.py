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
    gradient, intercept, r_value, p_value, std_err = stats.linregress(
        prevSwerve_rounds, prevScore_rounds)
    print "Gradient and intercept:", gradient, intercept
    print "R-squared", r_value**2
    print"P-value", p_value
"""


def col_value(board, connect_n, col_index, symbol):
    height_cell = len(board[col_index]) - 1
    max_matching_cells = 0
    # check how many matching cells are below it
    num_matching_cells = 0
    for current_cell_index in range(0, height_cell, -1):
        if board[col_index][current_cell_index] != symbol:
            break
        else:
            num_matching_cells += 1
    if num_matching_cells > max_matching_cells:
        max_matching_cells = num_matching_cells
    num_matching_cells = 0

    # check how many matching cells are horizontally adjacent to it

    # first check all cols to the left of the cell
    for current_cell_index in range(0, col_index, -1):
        try:
            if board[current_cell_index][height_cell] != symbol:
                break
            else:
                num_matching_cells += 1
        except IndexError:
            break

    # then check all cols to the right of the cell
    for current_cell_index in range(col_index + 1, len(board)):
        try:
            if board[current_cell_index][height_cell] != symbol:
                break
            else:
                num_matching_cells += 1
        except IndexError:
            break

    if num_matching_cells > max_matching_cells:
        max_matching_cells = num_matching_cells
    num_matching_cells = 0

    # check how many matching cells are diagonal (downwards) to it

    # first check all cells diagonal from the top left
    for current_cell_index in range(0, len(board)):
        try:
            if board[col_index - current_cell_index][height_cell + current_cell_index] != symbol:
                break
            else:
                num_matching_cells += 1
        except IndexError:
            break

    # check how many matching cells are diagonal (upwards) to it
    for current_cell_index in range(0, len(board)):
        try:
            if board[col_index + current_cell_index][height_cell - 1:
            else:
                num_matching_cells += 1
        except IndexError:
            break

def get_move(state):
    if state['game'] == "chicken":
        """ Chicken game -- avoid colliding or swerving before your opponent, given reaction time distrubtion, previous scores, and opp moves  """

        # gather the inputs; append them to the global state
        opp_moves.append(state['previous-move'])
        outcome= state['outcome']
        my_scores.append(outcome)
        reaction_times.append(state['reaction-time'])

        # we want the next move to be just under the valid range of reaction times, so next_move = mean - 3*stdev
        mean_reaction_time= np.average(reaction_times)
        stdev_reaction_time= np.stdev(reaction_times)

        # adjust the next move depending on whether the opponent is winning or not
        if outcome == -1:
            opp_bias += 1
        if outcome == 1:
            opp_bias -= 1
        next_move= mean_reaction_time + opp_bias - 3 * stdev_reaction_time
        if next_move < 0:
            next_move= 0
        my_moves.append(next_move)

        return next_move
    else:
        """ Connect More - see if win is solvable (forced), means shorter connect value and thick board, else... """

        # gather the inputs
        connect_n= state['connect_n']
        columns= state['columns']
        your_token= state['your-token']
        board= state['board']

        my_next_states= []
        opp_next_states= []
        for col_index, col in enumerate(board):
            # create a board with my next move at the current column
            my_next_state= board.copy()
            my_next_state[col_index].append("Y")
            my_next_states.append(my_next_state)

            # create a board with my opponent's next move at the current column
            opp_next_state= board.copy()
            opp_next_state[col_index].append("R")
            opp_next_states.append(opp_next_state)

        return next_move
