names = ["Judith", "Abel", "Tyson", "Martha", "Beverley", "David", "Anabel"]
estimated_insurance_costs = [1000.0, 2000.0, 3000.0, 4000.0, 5000.0, 6000.0, 7000.0]
actual_insurance_costs = [1100.0, 2200.0, 3300.0, 4400.0, 5500.0, 6600.0, 7700.0]

# Add your code here
total_cost = 0

# while total_cost < len(actual_insurance_costs):
#   print(actual_insurance_costs[total_cost])
#   total_cost += 1


for insurance in actual_insurance_costs:
  total_cost += insurance
  print(total_cost)

average_cost = total_cost / len(actual_insurance_costs)
print("Average Insurance Cost: " + str(average_cost) + " dollars.")

print("")
#Range
for i in range(0, len(names)):
  name = names[i]
  insurance_cost = actual_insurance_costs[i]
  print("The insurance cost for " + name + " is " + str(insurance_cost) + " dollars.")
  
  insurance_calcu_one = insurance_cost - average_cost
  insurance_calcu_two = average_cost - insurance_cost
  #Conditions
  if insurance_cost > average_cost:
    print("The insurance cost for " + name + " is " + str(insurance_calcu_one) + " dollars above average.")
    print("")
  elif insurance_cost < average_cost:
    print("The insurance cost for " + name + " is " + str(insurance_calcu_two) + " dollars below average.")
    print("")  
  else:
    print("The insurance cost for " + name + " is equal to the average.")
    print("")  


#List Comprehension
updated_estimated_costs = [cost * (11/10) for cost in estimated_insurance_costs]
print(updated_estimated_costs)
