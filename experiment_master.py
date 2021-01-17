from election.io.file_output_buffer import DataPointBuffer
import os
from questions import frequency_condorcet_winners, borda_chooses_condorcet_winner, no_condorcet_winners, plurality_chooses_condorcet_winner
CANDIDATE_NUM_MAX = 100
VOTER_NUM_MAX = 1000
ITERATION_NUM = 10000

def start_experiment(experiment, output_file_name):
    iteration = ITERATION_NUM
    buffer = DataPointBuffer(os.path.join(os.getcwd(), "questions/outputs/" + output_file_name))
    buffer.write("candidates", "voters", "data_count/"+str(iteration))
    for candidate_num in range(3, CANDIDATE_NUM_MAX):
        for voter_num in range(candidate_num, VOTER_NUM_MAX):
            experiment(candidate_num, voter_num, ITERATION_NUM, buffer)
    buffer.dump()

if __name__ == '__main__':
    start_experiment(frequency_condorcet_winners.experiment, "condorcet_winner_frequency.csv")
    start_experiment(borda_chooses_condorcet_winner.experiment, "borda_chooses_condorcet_winner.csv")
    start_experiment(no_condorcet_winners.experiment, "no_condorcet_winners.csv")
    start_experiment(plurality_chooses_condorcet_winner.experiment, "plurality_chooses_condorcet_winner.csv")