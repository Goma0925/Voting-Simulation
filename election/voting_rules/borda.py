from election.votingutils import *
from election.voting_rules import rule_names


def count_in_borda(ballots: list):
    score_board = init_score_board(ballots[0])
    for ballot in ballots:
        for i in range(len(ballot)):
            score_board[ballot[i]] += get_asym_borda_score(i, len(ballot))
    return get_result_container(rule_names.BORDA, score_board)


def get_asym_borda_score(index: int, candidate_num: int):
    """
    :param index: Index of the candidate that you want to get the score of. 0 represents the most preferred.
    :param candidate_num: How many other candidates there are.
    :return: Asymmetric Borda score of the candidate. Eg) Last => 0, Top among 4 candidates => 3
    """
    return candidate_num - 1 - index

