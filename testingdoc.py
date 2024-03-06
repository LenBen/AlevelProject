scoreValues = ["D","F","E"]
score = 0

for i in range(len(scoreValues)): # calculates percentage score
    score += 1 / scoreValues[i]
score = (score * 100) / len(scoreValues)

print(score)