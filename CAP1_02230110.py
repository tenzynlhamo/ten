################################
# Tenzin Lhamo
# 1ECE
# 02230110
################################
# REFERENCES
#https://readthedocs.org/projects/python-guide/downloads/pdf/latest/
# https://www.algostem.org/?gad_source=1&gclid=CjwKCAjwt-OwBhBnEiwAgwzrUjU8YX0e4nIkS7rPUDZZojOyAzMdGoiWBMsd45j7mdTnc0qg6jhMKRoCKXYQAvD_BwE
#https://www.w3schools.com/python/python_strings.asp
################################
# SOLUTION
# Your Solution Score:49894
# input_0_cap1.txt
################################
def calculate_score(input_file):
    
    scores = {'A': 1, 'B': 2, 'C': 3, 'X': 0, 'Y': 3, 'Z': 6}

    total_score = 0

    with open(input_file, 'r') as f:
        lines = f.readlines()

    for line in lines:
        personA_choice, outcome = line.strip().split()
        # Determining the choice based on the desired outcome
        if outcome == 'X':
            if personA_choice == 'A':
                personB_choice = 'C'  # Scissors defeat Rock
            elif personA_choice == 'B':
                personB_choice = 'A'  # Rock defeats Paper
            else:
                personB_choice = 'B'  # Paper defeats Scissors
        elif outcome == 'Y':
            # If personB need draw then he/she has to choose the same option as personA
            personB_choice = personA_choice
        else:
            # If personB need to win then he/she has to choose the option that loses to the personA's choice
            if personA_choice == 'A':
                personB_choice = 'B'  # Paper defeats Rock
            elif personA_choice == 'B':
                personB_choice = 'C'  # Scissors defeat Paper
            else:
                personB_choice = 'A'  # Rock defeats Scissors
        
        # Calculating the score for the round and adding it to the total score we get,
        round_score = scores[personB_choice] + scores[outcome]
        total_score += round_score

    return total_score


input_file = 'input_0_cap1.txt'
total_score = calculate_score(input_file)
print("Total score:", total_score)