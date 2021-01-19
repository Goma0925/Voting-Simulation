"""
    This script is to study and answer the questions:
        • How often does Borda choose the Condorcet winner?
"""
from election.profiles import d_condorcet
from election.voting_rules import copeland, borda
from election.votingutils import *
from election.io.file_output_buffer import DataPointBuffer
import os

def experiment(candidate_num, voter_num, iteration, buffer: DataPointBuffer):
    count = 0
    for i in range(iteration):
        ballots = d_condorcet(candidate_num, voter_num)
        print("------------------------")
        print("Profile(Voter="+str(len(ballots))+"):", str(ballots))

        #Get the condorcet winner using copeland
        condorcet_winner_list = get_winners(copeland.count_in_copeland(ballots))
        if len(condorcet_winner_list) > 1:
            raise Exception("There should not be more than one condorcet winner")
        condorcet_winner = condorcet_winner_list[0]
        print(" Condorcet winner: " + str(condorcet_winner_list))

        #Check if Borda chooses the condorcet winner
        borda_winners = get_winners(borda.count_in_borda(ballots))
        print(" Borda winners   : " + str(borda_winners))
        if condorcet_winner in borda_winners:
            count += 1
    buffer.write(str(candidate_num), str(voter_num), str(count))
    print("Usng D-Condorcet profile, Borda chose Condorcet winners " + str(count) + "/" + str(iteration) + " times.")



if __name__ == '__main__':
    candidate_num = 4
    voter_num = 200
    experiment_interation = 100

    count = 0
    for i in range(experiment_interation):
        ballots = d_condorcet(candidate_num, voter_num)
        print("------------------------")
        print("Profile(Voter="+str(len(ballots))+"):", str(ballots))

        #Get the condorcet winner using copeland
        condorcet_winner_list = get_winners(copeland.count_in_copeland(ballots))
        if len(condorcet_winner_list) > 1:
            raise Exception("There should not be more than one condorcet winner")
        condorcet_winner = condorcet_winner_list[0]
        print(" Condorcet winner: " + str(condorcet_winner_list))

        #Check if Borda chooses the condorcet winner
        borda_winners = get_winners(borda.count_in_borda(ballots))
        print(" Borda winners   : " + str(borda_winners))
        if condorcet_winner in borda_winners:
            count += 1
    print("Usng D-Condorcet profile, Borda chose Condorcet winners " + str(count) + "/" + str(experiment_interation) + " times.")

