"""
    This script is to study and answer the questions:
        • When the Condorcet winner does not exist, do Borda, plurality, and Copeland select the
        same alternative? How often do they coincide with each other?

        A: They do ocasionally produce the same results, but the probability is low.
            And as the number of voters/candidates increases, it gets even lower.
"""
from election.voting_rules import copeland, borda, plurality
from election.votingutils import *
from election.profiles import non_d_condrcet
from election.io.file_output_buffer import DataPointBuffer


def is_indentical(list_a:list, list_b:list):
    """
    :param list_a:
    :param list_b:
    :return: True if the items in the two lists are identical in order
    """
    size = 0
    if len(list_a) != len(list_b):
        return False
    for i in range(len(list_a)):
        if list_a[i] != list_b[i]:
            return False
    return True


def experiment(candidate_num, voter_num, iteration, buffer: DataPointBuffer):
    indentical_borda_plurality = 0
    indentical_copeland_plurality = 0
    indentical_copeland_borda = 0
    indentical_all = 0
    for i in range(iteration):
        #Get profile that does not have condorcet winner
        ballots = non_d_condrcet(candidate_num, voter_num)
        print("------------------------")
        #     + "Profile(Voter="+str(len(ballots))+"):", str(ballots))

        copeland_winners = get_winners(copeland.count_in_copeland(ballots))
        copeland_winners.sort()

        borda_winners = get_winners(borda.count_in_borda(ballots))
        borda_winners.sort()

        plurality_winners = get_winners(plurality.count_in_plurality(ballots))
        plurality_winners.sort()

        #Count how many times all the rules elect the same candidates
        copeland_plurality_indentical_flag = False
        if is_indentical(copeland_winners, plurality_winners):
            indentical_copeland_plurality += 1
            copeland_plurality_indentical_flag = True
        
        if is_indentical(borda_winners, plurality_winners):
            indentical_borda_plurality += 1
            # Count up if all the rules yield the same result.
            if copeland_plurality_indentical_flag == True:
                indentical_all += 1

        if is_indentical(copeland_winners, borda_winners):
            indentical_copeland_borda += 1

        print("Copeland winners : " + str(copeland_winners) + "\n"
            + "Borda winners    : " + str(borda_winners)+ "\n"
            + "Plurality winners: " + str(plurality_winners))

    buffer.write(str(candidate_num), str(voter_num), str(indentical_copeland_plurality) 
            + "," + str(indentical_borda_plurality) + "," + str(indentical_copeland_borda) + ","
            + str(indentical_all))
    print("\nWith non D_Condorcet profile, the three rules matched their results as following (Candidates="
        + str(candidate_num)+"Voters"+str(voter_num)+"):"+ "\n"
        + "Copeland & Plurality match:" + str(indentical_copeland_plurality) + "/" + str(iteration) + " times"+ "\n"
        + "Borda    & Plurality match:" + str(indentical_borda_plurality) + "/" + str(iteration) + " times"+ "\n"
        + "Copeland & Borda macth    :" + str(indentical_copeland_borda) + "/" + str(iteration) + " times"+ "\n"
        + "All rules macth           :" + str(indentical_all) + "/" + str(iteration) + " times" + "\n")


if __name__ == '__main__':
    candidate_num = 10
    voter_num = 10000
    experiment_iterations = 100

    count = 0
    for i in range(experiment_iterations):
        #Get profile that does not have condorcet winner
        ballots = non_d_condrcet(candidate_num, voter_num)
        print("------------------------")
        print("Profile(Voter="+str(len(ballots))+"):", str(ballots))

        copeland_winners = get_winners(copeland.count_in_copeland(ballots))
        copeland_winners.sort()

        borda_winners = get_winners(borda.count_in_borda(ballots))
        borda_winners.sort()

        plurality_winners = get_winners(plurality.count_in_plurality(ballots))
        plurality_winners.sort()

        #Count how many times all the rules elect the same candidates
        if is_indentical(copeland_winners, borda_winners):
            if is_indentical(copeland_winners, plurality_winners):
                count += 1

        print("Copeland winners : " + str(copeland_winners))
        print("Borda winners    : " + str(borda_winners))
        print("Plurality winners: " + str(plurality_winners))
    print("With non D_Condorcet profile, all three rules matched their results " + str(count) + "/" + str(experiment_iterations) + " times")
