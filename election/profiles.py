"""
    This module creates a certain profile of votes
"""
from election.voting_rules import copeland
from election.votingutils import *

def get_impartial_culture(candidate_num, voter_num):
    """
    :param candidate_num: Number of candidates
    :param voter_num: Number of voters
    :return: Generate an impartial culture in 2D list of lists. Each list contains the preference order of candidates.
    """
    if (candidate_num < 2):
        raise Exception("candidate_num has to be more than 1.")

    # Get all the combinations of possible preference order
    candidates = [i for i in range(1, candidate_num + 1)]
    possible_preference_order = []
    for i in range(len(candidates)):
        for j in range(i + 1, len(candidates)):
            pass


def d_condorcet(candidate_num, voter_num):
    """
    :param candidate_num:
    :param voter_num:
    :return: A 2D list of preference order votes that only include condorcet winners. It uses copeland rule.
    """
    while True:
        ballots = get_ballots(candidate_num, voter_num)
        found_condorcet_profile = is_condorcet_winner(copeland.count_in_copeland(ballots))
        if found_condorcet_profile:
            return ballots

def non_d_condrcet(candidate_num, voter_num):
    """
    :param candidate_num:
    :param voter_num:
    :return: A 2D list of preference order votes that does NOT include condorcet winners. It uses copeland rule.
    """
    while True:
        ballots = get_ballots(candidate_num, voter_num)
        is_condorcet_profile = is_condorcet_winner(copeland.count_in_copeland(ballots))
        if not is_condorcet_profile:
            return ballots

