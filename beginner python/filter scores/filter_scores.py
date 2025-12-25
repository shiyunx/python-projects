# List of scores
scores = [78, 23, 53, 37, 66, 12, 98, 40, 47, 80]
# Use lambda and filter
scores_pass = list(filter(lambda score: score >= 50, scores))
print(scores_pass)


