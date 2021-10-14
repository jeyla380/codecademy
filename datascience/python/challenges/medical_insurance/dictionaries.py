# Add your code here
medical_costs = {}

medical_costs.update({"Marina": 6607.0, "Vinay": 3225.0})
#print(medical_costs)
medical_costs.update({"Connie": 8886.0, "Isaac": 16444.0, "Valentina": 6420.0})
#print(medical_costs)

medical_costs.update({"Vinay": 3325.0})
#print(medical_costs)

total_cost = 0
for cost in medical_costs.values():
  total_cost += cost
#print(total_cost)
average_cost = total_cost / len(medical_costs)
print("Average Insurance Cost: " + str(average_cost))
print("")
print("------------------------------------")

#--------------------------------------#
names = ["Marina", "Vinay", "Connie", "Isaac", "Valentina"]
ages = [27, 24, 43, 35, 52]
#print(names)
#print(ages)
zipped_ages = zip(names, ages)
names_to_ages = {key:value for key, value in zipped_ages}
#print(names_to_ages)
marina_age = names_to_ages.get("Marina", "None")
print("Marina's age is " + str(marina_age))
print("")
print("------------------------------------")

#--------------------------------------#
medical_records = {}
medical_records["Marina"] = {"Age": 27, "Sex": "Female", "BMI": 31.1, "Children": 2, "Smoker": "Non-smoker", "Insurance Cost": 6607.0}
#print(medical_records)
medical_records.update({"Vinay": {"Age": 24, "Sex": "Male", "BMI": 26.9, "Children": 0, "Smoker": "Non-smoker", "Insurance Cost": 3225.0}, "Connie": {"Age": 43, "Sex": "Female", "BMI": 25.3, "Children": 3, "Smoker": "Non-smoker", "Insurance Cost": 8886.0}, "Isaac": {"Age": 35, "Sex": "Male", "BMI": 20.6, "Children": 4, "Smoker": "Smoker", "Insurance Cost": 16444.0}, "Valentina": {"Age": 52, "Sex": "Female", "BMI": 18.7, "Children": 1, "Smoker": "Non-smoker", "Insurance Cost": 6420.0}})
#print(medical_records)
#print("Connie's insurance cost is " + str(medical_records["Connie"]["Insurance Cost"]) + " dollars.")

medical_records.pop("Vinay")
#print(medical_records)

for name, dictionary in medical_records.items():
  #print(name + " " + str(dictionary))
  print(name + " is a " + str(dictionary["Age"]) + " year old " + dictionary["Sex"] + " " + dictionary["Smoker"] + " with a BMI of " + str(dictionary["BMI"]) + " and insurance cost of " + str(dictionary["Insurance Cost"]))
  print("")
print("------------------------------------")


