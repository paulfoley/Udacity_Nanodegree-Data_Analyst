## Program to convert scores to a rating

def convert_to_numeric(score):
    """ Convert a score to a float. """
    return float(score)

def sum_of_middle_three(score1, score2, score3, score4, score5):
    """ Find the sum of the middle three numbers"""
    maximum = max(score1, score2, score3, score4, score5)
    minimum = min(score1, score2, score3, score4, score5)
    total = score1 + score2 + score3 + score4 + score5 - maximum - minimum
    return total


def score_to_rating_string(score):
    """ Convert the average score, which should be between 0 and 5, into a rating. """
    if score < 1:
        return "Terrible"
    elif score < 2:
        return "Bad"
    elif score < 3:
        return "OK"
    elif score < 4:
        return "Good"
    else:
        return "Excellent"

def scores_to_rating(score1,score2,score3,score4,score5):
    """
    Turns five scores into a rating by averaging the
    middle three of the five scores and assigning this average
    to a written rating.
    """
    #STEP 1 convert scores to numbers
    score1 = convert_to_numeric(score1)
    score2 = convert_to_numeric(score2)
    score3 = convert_to_numeric(score3)
    score4 = convert_to_numeric(score4)
    score5 = convert_to_numeric(score5)

    #STEP 2 and STEP 3 find the average of the middle three scores
    score = sum_of_middle_three(score1,score2,score3,score4,score5)/3

    #STEP 4 turn average score into a rating
    rating = score_to_rating_string(score)

    return rating

# Test Cases
print(scores_to_rating(1,2,3,4,5))