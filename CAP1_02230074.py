#################################################
# Sangay Dhaden
# 1EE
# 02230074
#################################################
# REFERENCES
# https://www.blackbox.ai/chat/expert-pytho
# https://chat.openai.com/c/91fc83d4-deaa-4b85-8d15-3837efa46920
# https://www.youtube.com/watch?v=Qcefu1jVPds
#################################################
# SOLUTION
# Your solution score: 49524
# 4
#################################################

# Reading the input.txt file
def read_input(Enter_your_input_file): # defining function "read_input"
        a = [] # empty list for storing opponent and outcome pairs
        with open(Enter_your_input_file, 'r') as files: # opening input file
                for b in files:
                        opponent, outcome = b.split() # spliting opponent and outcome column
                        a.append((opponent, outcome)) # adding oponent and outcome pair in the empty list above                
        return a
# Game rules 
# Rock defeats Scissors
# Scissors defeats Paper
# Paper defeats Rock.
# Same shape means draw 

# Score system
# 1 for Rock 
# 2 for Paper
# 3 for Scissors  
      #AND
# 0 if you lost 
# 3 if the round was a draw
# 6 if you won 

# Calculation of score for each round
def calc_score(round_played):
        score = 0
        for opponent, outcome in round_played: 
                if outcome == 'X': # we have to lose
                        if opponent == 'A': # A for rock
                                score += 3 # we lose(0) if 'X' is scissor(3)
                        elif opponent == 'B': # B for paper
                                score += 1# we lose(0) if 'X' is rock(1)
                        elif opponent == 'C': # C for scissor
                                score += 2 # we lose(0) if 'X' is paper(2)
                elif outcome == 'Y': # Y means draw, which means we've to end in draw
                        if opponent == 'A': # A for rock
                                score += 4 # we end in draw(3) if 'Y' is rock(1)
                        elif opponent == 'B': # B for paper
                                score += 5 # we end in draw(3) if 'Y' is paper(2)
                        elif opponent == 'C': # C for scissor
                                score += 6 # we end in draw(3) if 'Y' is scissor(3)
                elif outcome == 'Z': # we have to win
                        if opponent == 'A': # A for rock
                                score += 8 # we win(6) if 'Z' is paper(2)
                        elif opponent == 'B': # B for paper
                                score += 9 # we win(6) if 'Z' is scissor(3)
                        elif opponent == 'C': # C for scissor
                                score += 7 # we win(6) if 'Z' is rock(1)                        
        print(f"Total score is: {score}") # calculating total sum of score respective of our own input file 
# Now to run a programe
Enter_your_input_file = "CSF101-CAP/input_4_cap1 (2).txt"  # To enter the input file, we have our own assigned input file with accordance to last no. of our std id
calc_score(read_input(Enter_your_input_file)) # Calculate the score using the data obtained from reading the input file