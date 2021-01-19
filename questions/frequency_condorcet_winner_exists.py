"""
    This script is to study and answer the questions:
        • How often does a Condorcet winner exist?
    Since Copeland rule always returns the condorcet winners when it exists, it uses copeland rule to detect Condorcet winners.
"""
from election.votingutils import *
from election.voting_rules.copeland import count_in_copeland
from election.io.file_output_buffer import DataPointBuffer
from election.profiles import impartial_culture
import os

def get_condorcet_winner_count(candidate_num, voter_num, iteration):
    condorce_winner_count = 0
    for i in range(iteration):
        ballots = impartial_culture(candidate_num, voter_num)
        # print("Ballots:"+str(ballots))
        # print("-----------------------------------------------")
        # print("Result (Copeland) :", str(count_in_copeland(ballots)))
        found_condorcet_winner = is_condorcet_winner(count_in_copeland(ballots))
        # print("Condorcet winner? :", found_condorcet_winner)
        if found_condorcet_winner:
            condorce_winner_count += 1
        # print("-----------------------------------------------")
    return condorce_winner_count

def experiment(candidate_num, voter_num, iteration, buffer: DataPointBuffer):
    print(str(candidate_num) + " candidates /" + str(voter_num) + " voters/ " + str(iteration) + " iterations")
    condorce_winner_count = get_condorcet_winner_count(candidate_num, voter_num, iteration)
    print("Frequency of Condorcet winner existence: " + str(condorce_winner_count) + "/" + str(iteration) + " times.")
    buffer.write(str(candidate_num), str(voter_num), str(condorce_winner_count))

if __name__ == '__main__':
    iteration = 10000
    buffer = DataPointBuffer(os.path.join(os.getcwd(), "questions/outputs/condorcet_winner_frequency.csv"))
    buffer.write("candidates", "voters", "condorcet_winners/"+str(iteration))
    for candidate_num in range(2, 30):
        for voter_num in range(candidate_num, 100):
            print(str(candidate_num) + " candidates /" + str(voter_num) + " voters/ " + str(iteration) + " iterations")
            condorce_winner_count = get_condorcet_winner_count(candidate_num, voter_num, iteration)
            print("Frequency of Condorcet winner existence: " + str(condorce_winner_count) + "/" + str(iteration) + " times.")
    buffer.dump()

