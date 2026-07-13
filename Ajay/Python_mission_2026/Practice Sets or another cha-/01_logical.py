# IF Applicant has high income and good credit
# Eligible for loan

has_high_income = True
has_good_credit = False

if has_high_income or has_good_credit:
    print("Eligible for Loan")

""" In This operator (or) One condition should be true, if one 
Codition is True and second is False, Then it will print Eligible for Loan.
If Both are False, Then it will not print Eligible for Loan. """


has_good_income = True
has_good_credit = False

if has_good_income and has_good_credit:
    print("Eligible for Loan")

""" In This operator (and) Both condition should be true, if one is False,
Then it will not print Eligible For Loan. if Both are True,
Then it will print Eligible for Loan. """


has_good_credit = True
has_criminal_record = False

if has_good_credit and not has_criminal_record:
    print("Eligible for Loan")

""" In this operator (not) If the applicant has a good credit and does not
have a criminal record, then they are eligible for a loan.
The not operator negates the condition of having a criminal record,
meaning that if the applicant does not have a criminal record,
the condition will be true. 
"""