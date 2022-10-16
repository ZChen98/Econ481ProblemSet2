"""
Justin Chen
Problem Set 2: Basic Operation
"""

# a)
def prisoners_dilemma() -> int:
    """
    Asks two players their strategies and ends when both players choose same strategies

    Returns
    =======
    The number of rounds played
    """
    player_a = str(input('Player A: Would you like to Cooperate or Defect? ')).lower()
    player_b = str(input('Player B: Would you like to Cooperate or Defect? ')).lower()
    round_played = 1

    while player_a != player_b:
        if player_a == 'cooperate' and player_b == 'defect':
            print('A: -20, B: 0')
        elif player_a == 'defect' and player_b == 'cooperate':
            print('A: 0, B: -20')

        player_a = str(input('Player A: Would you like to Cooperate or Defect? ')).lower()
        player_b = str(input('Player B: Would you like to Cooperate or Defect? ')).lower()
        round_played += 1

    if player_a == 'defect':
        print('A: -10, B: -10')
    else:
        print('A: -3, B: -3')

    return round_played

# b)
def factorial(n_arg: int) -> int:
    """Calculates the factorial of any positive integer

    Parameters
    ==========
    n_arg: int; a positive integer for factorial calculation

    Returns
    =======
    Factorial
    """
    factorials = 1

    for i in range(1, n_arg + 1):
        factorials *= i

    return factorials

# c)
def compute_frequency(words: [str]) -> dict:
    """Computes the frequency of each unique string

    Parameters
    ==========
    words: list of strings

    Returns
    =======
    A dictionary of the frequencies of each unique string
    """
    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency
