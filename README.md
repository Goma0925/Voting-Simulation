# Voting Theory Project 1

Created: Jan 18, 2021 4:15 PM

## Study Objective

This repository is created as part of Voting Theory study and consists of a Python module to study the properties of voting rules including the Copeland, Borda, and Plurality rule. The modules include the functions to model the election result of three rules, profile generator functions, and some helper functions and classes. The questions to answer include:

- How often does a Condorcet winner exist?
- How often does Borda choose the Condorcet winner?
- How often does Plurality choose the Condorcet winner?
- When the Condorcet winner does not exist, do Borda, plurality, and Copeland select the

    same alternative? How often do they coincide with each other?

## General Method of Study

To study the trend of the election result with different numbers of candidates(x) and voters(y), a thousand elections were conducted using an impartial culture to generate the preference profile. The range of data included the combinations of 3 to 9 candidates and 3 to 100 voters. Due to the computational limitations, some data lack part of the data in the range. All the computations were done on cloud using ![AWS EC2](https://aws.amazon.com/jp/ec2/).

## Results

### **Q. How often does a Condorcet winner exist?**

- **Method:**

    Using the Copeland, the number of times in which the Condorcet winner was found in the profile (z), which is plotted in Plot 1 and 2 below.

- **Findings:**

    There are several clear trends in the frequency of Condorcet winners. The first one is the general decline trend of the frequency as the number of candidates (x) increases (Plot 1).

    ![media/condorcet_winner_frequency.png](media/condorcet_winner_frequency.png)

    Plot 1: A general negative trend toward a larger number of candidates.

    Furthermore, there are distinct trends between when the number of voters is even and odd. When the number is even, the frequency of Condorcet winners was relatively lower while the odd number of voters yielded more Condorcet winners.

    ![media/condorcet_winner_freq2.png](media/condorcet_winner_freq2.png)

    Plot 2: Sideway view of Plot 1. Clear distinct trends between even (lower cluster) and odd (higher cluster) numbers of voters.

### **Q2.  How often does Borda choose the Condorcet winner?**

- **Method**:

    Given only the profiles that contain Condorcet winner, the number of times Borda rule chose the Condorcet winner was counted out of a thousand profiles (z).

- **Findings:**

    Borda rule constantly elected the Condorcet winner approximately 85-95% of the time. A slight negative trend was observed as both the number of candidates and voters increased (Plot 3).

    ![media/borda_chooses_condorcet.png](media/borda_chooses_condorcet.png)

    Plot 3: A generally constant nomination of the Condorcet winner by Borda.

### Q3. How often does Plurality choose the Condorcet winner?

- **Method:**

    Given only the profiles that contain Condorcet winner, the number of times Plurality rule chose the Condorcet winner was counted out of a thousand profiles (z).

- **Findings:**
It can be said that more than half of the time, the Plurality rule chooses the Condorcet winner, usually between 60 to 90%. The rate decreases as the numbers of candidates and voters increase (Plot 4).

    ![media/plurality_chooses_condorcet.png](media/plurality_chooses_condorcet.png)

    Plot 4: A negative trend in choosing the Condorcet winner as the numbers of candidates and voters increase

### Q4. When the Condorcet winner does not exist, do Borda, plurality, and Copeland select the same alternative? How often do they coincide with each other?

- **Method:**

    For a thousand profiles, Copeland, Borda, and Plurality rule chose the winner(s). For each profile, the number of times was counted when 1) Copeland and Plurality, 2) Borda and Plurality, 3) Copeland and Borda, 4) all rules matched their result.

- **Findings:**

    **1) Copeland and Plurality match:**

    Generally, the number of their match is low between 100 to 300. Within the dataset, the matching rate is relatively high when both the numbers of candidates and voters are low. An interesting finding was that when there are three candidates and a prime number of voters, then these two rules never match their result.

    ![media/Copeland_Plurality_match.png](media/Copeland_Plurality_match.png)

    **2) Borda and Plurality match:**

    The number of their match seems to stay relatively constant when there is the same number of candidates regardless of the number of voters. There is also a negative trend as the number of candidates increases (Plot 6).

    ![media/Borda_Plurality_match.png](media/Borda_Plurality_match.png)

    Plot 6: A negative trend as the number of candidate increases.

    **3) Copeland and Plurality match:**

    The number of their matches increases as the number of candidates increases and decreases as the number of voters decreases (Plot 7).

    ![media/Copeland_Plurality_match.png](media/Copeland_Plurality_match.png)

    Plot 7: Relatively A positive trend as the number of candidate increases and a negative trend as the number of voters decreases.

    **4) All rules match:**

    The number of their matches is constantly low between 0 to 150. The results of the three rules agreed the most when there are both low numbers of candidates and voters (Plot 8).

    ![media/All_rules_match.png](media/All_rules_match.png)

    Plot 8: A relatively constant trend except for when there are both fewer candidates and voters.
