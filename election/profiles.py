"""
    This module creates a certain profile of votes
"""
from election.voting_rules import copeland
from election.votingutils import *
import itertools, random


def impartial_culture(candidate_num, voter_num):
    """
    * Generates an impartial culture of ballots 
    :param candidate_num: Number of candidates
    :param voter_num: Number of voters
    :return: 2D list of lists. Each list contains the random preference order of candidates.
    """
    if (candidate_num < 2):
        raise Exception("candidate_num has to be more than 1.")

    candidates = []
    for i in range(candidate_num):
        candidates.append(i+1)

    candidate_permutations = []
    [candidate_permutations.append(preference) for preference in itertools.permutations(candidates)]

    all_ballots = []
    for i in range(voter_num):
        # Choose one of the possible preference order at the equal chance.
        ballot = candidate_permutations[random.randint(0, len(candidate_permutations)-1)]
        all_ballots.append(ballot)
    return all_ballots


def d_condorcet(candidate_num, voter_num):
    """
    :param candidate_num:
    :param voter_num:
    :return: A 2D list of preference order votes that only include condorcet winners. It uses copeland rule.
    """
    while True:
        ballots = impartial_culture(candidate_num, voter_num)
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
        ballots = impartial_culture(candidate_num, voter_num)
        is_condorcet_profile = is_condorcet_winner(copeland.count_in_copeland(ballots))
        if not is_condorcet_profile:
            return ballots

