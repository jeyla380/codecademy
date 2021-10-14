# create the initial variables below
age = 28
sex = 0
bmi = 26.2
num_of_children = 3
smoker = 0

# Add insurance estimate formula below
insurance_cost = (250 * age) - (128 * sex) + (370 * bmi) + (425 * num_of_children) + (24000 * smoker) - 12500

print("This person's insurance cost is " + str(insurance_cost) + " dollars.\n")

# Age Factor
age += 4
new_insurance_cost = (250 * age) - (128 * sex) + (370 * bmi) + (425 * num_of_children) + (24000 * smoker) - 12500

print("This person's new insurance cost is " + str(new_insurance_cost) + " dollars.\n\n")


change_in_insurance_cost = new_insurance_cost - insurance_cost
print("*************************************")
print("The change in cost of insurance after increasing the age by 4 years is " + str(change_in_insurance_cost) + " dollars.\n\n")

# BMI Factor
age = 28
bmi += 3.1

new_insurance_cost = (250 * age) - (128 * sex) + (370 * bmi) + (425 * num_of_children) + (24000 * smoker) - 12500
change_in_insurance_cost = new_insurance_cost - insurance_cost

print("*************************************")
print("The change in estimated insurance cost after increasing BMI by 3.1 is " + str(change_in_insurance_cost) + " dollars.\n\n")

# Male vs. Female Factor
bmi = 26.2
sex = 1

new_insurance_cost = (250 * age) - (128 * sex) + (370 * bmi) + (425 * num_of_children) + (24000 * smoker) - 12500
change_in_insurance_cost = new_insurance_cost - insurance_cost

print("*************************************")
print("The change in estimated cost for being male instead of female is " + str(change_in_insurance_cost) + " dollars.\n\n")
#result means that men tend to have lower medical costs on average than women, which is why the answer is negative.

# Extra Practice
  #smoker
sex = 0
smoker = 1

new_insurance_cost = (250 * age) - (128 * sex) + (370 * bmi) + (425 * num_of_children) + (24000 * smoker) - 12500
change_in_insurance_cost = new_insurance_cost - insurance_cost

print("*************************************")
print("The change in estimated insurance cost for being a smoker instead of non-smoker is " + str(change_in_insurance_cost) + " dollars.\n\n")

#num_of_children
num_of_children = 4
new_insurance_cost = (250 * age) - (128 * sex) + (370 * bmi) + (425 * num_of_children) + (24000 * smoker) - 12500
change_in_insurance_cost = new_insurance_cost - insurance_cost

print("The change in estimated cost for having 4 children instead of 3 children is " + str(change_in_insurance_cost) + " dollars.")
