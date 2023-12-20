def calc_average_score(subject_score):
    avg_score = "{:.2f}".format(sum(subject_score.values())/len(subject_score))
    return avg_score


def add_score(subject_score, subject, score):
    subject_score[subject] = score
    return subject_score



