from election.votingutils import *
from . import rule_names

def count_in_plurality(ballots):
    """
    :param ballots: 2D list of lists. Each list contains the preference order of candidates.
    :return: A list of winners
    """
    score_board = init_score_board(ballots[0])
    for preference_order in ballots:
        first_choice_candidate = preference_order[0]
        if first_choice_candidate not in score_board:
            score_board[first_choice_candidate] = 1
        else:
            score_board[first_choice_candidate] += 1
    return get_result_container(rule_names.PLURALITY, score_board)
