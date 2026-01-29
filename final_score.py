def final_interview_score(confidence, polarity):
    return round((confidence * 0.7) + ((polarity + 1) * 15), 2)
