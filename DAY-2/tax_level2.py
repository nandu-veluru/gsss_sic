'''Level2:
Level 2: Taxable Income Calculation
Objective: Calculate taxable income after standard deductions.
Tasks:
• Deduct a Standard Deduction of ₹50,000 from the annual gross salary.
• Compute the Taxable Income and display all intermediate calculations.
Output: Display gross salary, standard deduction and taxable income.
'''

import tax_level1

temp_variable = tax_level1.annual_gross_salary
print("The gross of the employee is:", temp_variable)

standard_deduction = 50000
taxable_income = temp_variable - standard_deduction
print("Standard deduction: ",standard_deduction)
print("Taxable income of the employee: ",taxable_income)
