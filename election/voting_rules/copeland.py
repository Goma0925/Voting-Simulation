from election.votingutils import *
from election.voting_rules import rule_names


def count_in_copeland(ballots):
    #Get a list of candidates
    candidates = []
    for preference in ballots[0]:
        candidates.append(preference)

    score_board = init_score_board(candidates)
    #For all the candidate pairs, get the copland score
    for i in range(len(candidates)):
        for j in range(i+1, len(candidates)):
            candidate_a = candidates[i]
            candidate_b = candidates[j]
            a_is_preferred_to_b = 0
            b_is_preferred_to_a = 0
            for ballot in ballots:
                if is_more_preferred(candidate_a, candidate_b, ballot):
                    #If candidate_a is preferred to b, add score to a.
                    a_is_preferred_to_b += 1
                else:
                    #If candidate_b is preferred to a, add score to b.
                    b_is_preferred_to_a += 1

            #Get Copeland score for the candidate pair
            if (a_is_preferred_to_b > b_is_preferred_to_a):
                #If a is more preferred in a pairwise majority sense, add copeland scores to candidate_a
                score_board[candidate_a] += 1
            elif (b_is_preferred_to_a > a_is_preferred_to_b):
                score_board[candidate_b] += 1
            else:
                pass
    return get_result_container(rule_names.COPELAND, score_board)

def is_more_preferred(candidate_a, candidate_b, ballot):
    """
    :param candidate_a:
    :param candidate_b:
    :param ballot: An array containing both candidate_a and candidate_b
    :return: true if candidate_a appears earlier in the list, false if not.
    """
    for candidate in ballot:
        if (candidate == candidate_a):
            return True
        if (candidate == candidate_b):
            return False
    raise Exception("Neither candidate a and b were found in the ballot.")
