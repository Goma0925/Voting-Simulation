"""
    This script is to study and answer the questions:
        • How often does Plurality choose the Condorcet winner?
         A: Plurality rule does NOT always choose a condorcet winner, but it does most of the times.
            As the number of voters increases, the likelihood of choosing the condorcet winner decreases.
"""
from election.profiles import d_condorcet
from election.voting_rules import copeland, plurality
from election.votingutils import *
from election.io.file_output_buffer import DataPointBuffer


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
        print(" Condorcet winner : " + str(condorcet_winner_list))

        #Check if Plurality chooses the condorcet winner
        plurality_winners = get_winners(plurality.count_in_plurality(ballots))
        print(" Plurality winners: " + str(plurality_winners))
        if condorcet_winner in plurality_winners:
            count += 1
    buffer.write(str(candidate_num), str(voter_num), str(count))
    print("Usng D-Condorcet profile, Plurality chose Condorcet winners " + str(count) + "/" + str(iteration) + " times.")


if __name__ == '__main__':
    candidate_num = 4
    voter_num = 5
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
        print(" Condorcet winner : " + str(condorcet_winner_list))

        #Check if Plurality chooses the condorcet winner
        plurality_winners = get_winners(plurality.count_in_plurality(ballots))
        print(" Plurality winners: " + str(plurality_winners))
        if condorcet_winner in plurality_winners:
            count += 1
    print("Usng D-Condorcet profile, Plurality chose Condorcet winners " + str(count) + "/" + str(experiment_interation) + " times.")

