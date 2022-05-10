last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Create some lists:
subjects = ['physics', 'calculus', 'poetry', 'history']
grades = [98, 97, 85, 88]

gradebook = []
for s, g in zip(subjects, grades):
  gradebook.append([s, g])
print(gradebook)


# Add more subjects:
gradebook.append(['computer science', 100])
gradebook.append(['visual arts', 93])
print(gradebook)


# Modify the gradebook:
gradebook[-1][1] += 5
print(gradebook)

gradebook[2].remove(85)
gradebook[2].append("Pass")
print(gradebook)


# One big gradebook!
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)
