import codecademylib3_seaborn
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from svm_visualization import draw_boundary
from players import aaron_judge, jose_altuve, david_ortiz


#CREATE THE LABELS
#print(aaron_judge.columns)
#print(aaron_judge.description.unique())
#print(aaron_judge['type'].unique()) #looking at the 'type' column

aaron_judge['type'] = aaron_judge['type'].map({'S': 1, 'B': 0})
#print(aaron_judge['type'])



#PLOTTING THE PITCHES
print(aaron_judge['plate_x']) #if plate_x = 0, the pitch was directly in the middle of the home plate; neg. is to the left of home plate, pos. is right of the home plate.
aaron_judge = aaron_judge.dropna(subset = ['plate_x', 'plate_z', 'type'])
#plate_z measures how high off the ground the pitch was. If plate_z = 0, the pitch was at ground level when it got to to the home plate.

plt.scatter(x = aaron_judge['plate_x'], y = aaron_judge['plate_z'], c = aaron_judge['type'], cmap = plt.cm.coolwarm, alpha = 0.25)
plt.show()


#BUILDING THE SVM
training_set, validation_set = train_test_split(aaron_judge, random_state = 1)

classifier = SVC(kernel = 'rbf', gamma = 2, C = 2)
classifier.fit(training_set[['plate_x', 'plate_z']], training_set['type'])

plt.clf()
fig, ax = plt.subplots()
plt.scatter(x = aaron_judge['plate_x'], y = aaron_judge['plate_z'], c = aaron_judge['type'], cmap = plt.cm.coolwarm, alpha = 0.25)
draw_boundary(ax, classifier)
plt.show()



#OPTIMIZING THE SVM
print(classifier.score(validation_set[['plate_x', 'plate_z']], validation_set['type']))




#EXPLORE OTHER PLAYERS
jose_altuve['type'] = jose_altuve['type'].map({'S': 1, 'B': 0})
#print(jose_altuve['type'])

jose_altuve = jose_altuve.dropna(subset = ['plate_x', 'plate_z', 'type'])

plt.clf()
plt.scatter(x = jose_altuve['plate_x'], y = jose_altuve['plate_z'], c = jose_altuve['type'], cmap = plt.cm.coolwarm, alpha = 0.25)
plt.show()

training_set, validation_set = train_test_split(jose_altuve, random_state = 1)
classifier = SVC(kernel = 'rbf', gamma = 2, C = 2)
classifier.fit(training_set[['plate_x', 'plate_z']], training_set['type'])

plt.clf()
fig, ax = plt.subplots()
plt.scatter(x = jose_altuve['plate_x'], y = jose_altuve['plate_z'], c = jose_altuve['type'], cmap = plt.cm.coolwarm, alpha = 0.25)
draw_boundary(ax, classifier)
ax.set_ylim(-2, 6)
ax.set_xlim(-3, 3)
plt.show()



david_ortiz['type'] = david_ortiz['type'].map({'S': 1, 'B': 0})
#print(jose_altuve['type'])

david_ortiz = david_ortiz.dropna(subset = ['plate_x', 'plate_z', 'type'])

plt.clf()
plt.scatter(x = david_ortiz['plate_x'], y = david_ortiz['plate_z'], c = david_ortiz['type'], cmap = plt.cm.coolwarm, alpha = 0.25)
plt.show()

training_set, validation_set = train_test_split(david_ortiz, random_state = 1)
classifier = SVC(kernel = 'rbf', gamma = 2, C = 2)
classifier.fit(training_set[['plate_x', 'plate_z']], training_set['type'])

plt.clf()
fig, ax = plt.subplots()
plt.scatter(x = david_ortiz['plate_x'], y = david_ortiz['plate_z'], c = david_ortiz['type'], cmap = plt.cm.coolwarm, alpha = 0.25)
draw_boundary(ax, classifier)
plt.show()
