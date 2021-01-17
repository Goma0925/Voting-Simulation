from election.io.file_output_buffer import DataPointBuffer
from election.io.logger import ErrorLogger
import os
from typing import Callable
from questions import frequency_condorcet_winner_exists, borda_chooses_condorcet_winner, no_condorcet_winners, plurality_chooses_condorcet_winner
CANDIDATE_NUM_MAX = 30
VOTER_NUM_MAX = 100
ITERATION_NUM = 1000

def start_experiment(experiment: Callable, output_file_name):
    """
    :Void: It runs a experiment function with different candidate and voter numbers for a specified number of iterations.
            DataPointBuffer provides a way to record three pieces of data in csv file.
    :param experiment: A function to test an experiment that takes candidate_num, voter_um, and how many iterations the
            experiment should run.
    :param output_file_name: Output file name.
    """
    try:
        iteration = ITERATION_NUM
        buffer = DataPointBuffer(os.path.join(os.getcwd(), "questions/outputs/" + output_file_name))
        buffer.write("candidates", "voters", "data_count/" + str(iteration))
        for candidate_num in range(3, CANDIDATE_NUM_MAX):
            for voter_num in range(candidate_num, VOTER_NUM_MAX):
                experiment(candidate_num, voter_num, ITERATION_NUM, buffer)
        # Output to file.
        buffer.dump()
    except Exception as e:
        ErrorLogger(os.path.join(os.getcwd(), "questions/outputs/error.txt")).write(e)


if __name__ == '__main__':
    start_experiment(frequency_condorcet_winner_exists.experiment, "condorcet_winner_frequency.csv")
    start_experiment(borda_chooses_condorcet_winner.experiment, "borda_chooses_condorcet_winner.csv")
    start_experiment(no_condorcet_winners.experiment, "no_condorcet_winners.csv")
    start_experiment(plurality_chooses_condorcet_winner.experiment, "plurality_chooses_condorcet_winner.csv")