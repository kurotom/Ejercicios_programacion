"""
Your task is to write methods that return the highest score from the list, the last added score and the three
highest scores.
"""


def latest(scores):
    """ Ultima puntuacion """
#    return scores[len(scores) - 1]
    return scores[-1]


def personal_best(scores):
    """ Mejor puntuacion """
#    return sorted(scores, reverse=True)[0]
    return max(scores)


def personal_top_three(scores):
    """ Mejor puntuacion ordenada de mayor a menor """
    return sorted(scores, reverse=True)[:3]


print(latest([100, 30, 20, 50, 0]))                # 0
print(personal_best([30, 80, 10, 50, 20]))         # 80
print(personal_top_three([30, 10, 80, 0, 30]))     # [80, 30, 30]
