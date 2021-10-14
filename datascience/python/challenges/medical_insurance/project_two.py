# Create calculate_insurance_cost() function below: 
def calculate_insurance_cost(age, sex, bmi, num_of_children, smoker, name):
  estimated_cost = (250 * age) - (128 * sex) + (370 * bmi) + (425 * num_of_children) + (24000 * smoker) - 12500
  print(name + ":")
  print("Estimated cost of insurance = $" + str(estimated_cost))
  print("")
  #print("The estimated insurance cost for " + name +  " is " + str(estimated_cost) + " dollars.")
  return estimated_cost

def difference_in_cost(individual_one, individual_two):
  difference = omar_insurance_cost - maria_insurance_cost
  print("The difference in insurance between " + individual_one + " and " + individual_two + " is $" + str(difference))


# Initial variables for Maria 

# Estimate Maria's insurance cost
maria_insurance_cost = calculate_insurance_cost(28, 0, 26.2, 3, 0, name = "Maria")



# Initial variables for Omar

# Estimate Omar's insurance cost 
omar_insurance_cost = calculate_insurance_cost(35, 1, 22.2, 0, 1, name = "Omar")

#difference in insurance cost
difference_in_cost("Maria", "Omar")
print("---------------------------------------------------------------\n")



#My insurance cost
my_insurance_cost = calculate_insurance_cost(24, 0, 20.8, 0, 0, name = "J")
