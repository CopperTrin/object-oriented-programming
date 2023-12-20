def calc_average_score(subject_score):
    average_scores = {}

    for student, scores in subject_score.items():
        average_score = "{:.2f}".format(sum(scores.values()) / len(scores))
        average_scores[student] = average_score
    
    return average_scores


def add_score(subject_score, student, subject, score):
    if student in subject_score:
        subject_score[student][subject] = score
    else:
        subject_score[student] = {subject: score}
    return subject_score

subject = add_score(subject_score={},student = '66010473',subject='OOP',score='50')
subject = add_score(subject_score=subject,student = '66010473',subject='OOD',score='50')

print(subject)