class Patient:
  def __init__(self, name, age, sex, bmi, num_of_children, smoker):
    self.name = name
    self.age = age
    # add more parameters here
    self.sex = sex
    self.bmi = bmi
    self.num_of_children = num_of_children
    self.smoker = smoker

  def estimated_insurance_cost(self):
    estimated_cost = (250 * self.age) - (128 * self.sex) + (370 * self.bmi) + (425 * self.num_of_children) + (24000 * self.smoker) - 12500
    print(self.name + "'s estimated insurance costs is " + str(estimated_cost) + " dollars.")

  def update_age(self, new_age):
    self.age = new_age
    print(self.name + " is now " + str(self.age) + " years old.")

  def update_num_children(self, new_num_children):
    self.num_of_children = new_num_children
    if self.num_of_children == 1:
      print(self.name + " has " + str(self.num_of_children) + " child.")
    else:
      print(self.name + " has " + str(self.num_of_children) + " children.")
  
  def patient_profile(self):
    patient_information = {}

    patient_information["Name"] = self.name
    patient_information["Age"] = self.age
    patient_information["Sex"] = self.sex
    patient_information["BMI"] = self.bmi
    patient_information["Number of Children"] = self.num_of_children
    patient_information["Smoker"] = self.smoker
    return patient_information

patient1 = Patient("John Doe", 25, 1, 22.2, 0, 0)
#print(patient1.name) >> "John Doe"
#print(patient1.age) >> 25
#print(patient1.sex) >> 1
#print(patient1.bmi) >> 22.2
#print(patient1.num_of_children) >> 0
#print(patient1.smoker) >> 0

patient1.estimated_insurance_cost() #>> doesn't need to put anything because of 'self'
patient1.update_age(26) #>> needs to put in 'new_age', but nothing in 'self'
patient1.estimated_insurance_cost()

patient1.update_num_children(1)

print(patient1.patient_profile())
