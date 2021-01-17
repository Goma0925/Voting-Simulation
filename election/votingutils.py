from election.voting_rules import rule_names


def init_score_board(candidates: list):
    """
    :param candidates: List of strings/int representing candidates
    :return: A dictionary of all the candidates paired with int 0: {"A": 0, "B":0, ...}
    """
    score_board = {}
    for candidate in candidates:
        score_board[candidate] = 0
    return score_board


def get_result_container(rule_name:str, score_board: dict):
    """
    * A supporter function to unify the output format of voting_rules' functions.
    :param rule_name: Name of the rule used
    :param score_board: A dict of vote score counts: eg) {"CANDIDATE-A": 10, "CANDIDATES-B":3, ...}
    :return: Creates a election result container with the rule name.
    """
    return {"RULE": rule_name, "score_board": score_board}


def get_winners(result_container):
    """
    :param score_board: A election result container generated using get_result_container
    :return: List of winners.
    """
    max_vote_count = 0
    winners = []
    score_board = result_container["score_board"]
    for candidate in score_board:
        if (score_board[candidate] > max_vote_count):
            # Replace the top candidate if you find a bigger vote count
            winners.clear()
            winners.append(candidate)
            max_vote_count = score_board[candidate]
        elif (score_board[candidate] == max_vote_count):
            #If you find a tie, add it to winners.
            # If you find a tie, add it to winners.
            winners.append(candidate)
    return winners


def is_condorcet_winner(copeland_result_container):
    """
    :param copeland_result_container: result_container of count_in_copeland's result.
    :return: True if the result outputs the condorcet winner. False otherwise
    """
    score_board = copeland_result_container["score_board"]
    candidate_num = len(score_board)
    if copeland_result_container["RULE"] != rule_names.COPELAND:
        raise Exception("is_condorcet_winner() takes a copeland rule's result")

    winners = get_winners(copeland_result_container)
    if len(winners) == 1:
        # Check if the winner has score = (candidate_num - 1),
        # in which case the candidate is preferred to any other candidates.
        if score_board[winners[0]] == (candidate_num - 1):
            return True
        else:
            return False
    else:
        #If there are multiple winners, there's no condorcet winner.
        return False

