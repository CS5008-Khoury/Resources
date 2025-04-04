""" 
Grabs a random leet code problem. 
"""
import random


# phase 2, add more details to the problems, ability to search by tags, difficulty. Returns url, not just number

problems = [27, 53, 70, 94, 98, 104, 111, 121, 206, 217, 234, 268, 700,  897, 1732]


def get_random_problem() -> int:
    return random.choice(problems)


question = random.randint(1, 10)

print(f"Problem {get_random_problem()}, Question {question}")