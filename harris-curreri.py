# This program calculates total energy requirement in burn patients
# It uses the two widely applied formulas; Curreri and Harris-Benedict

def main():

    class Patient:

        def __init__(self):
            self.sex = 0
            self.age = 0
            self.wt = 0
            self.ht = 0
            self.tsba = 0
            self.kcal= 0

        def curreri(self):
            if self.age < 16:
                self.kcal = 60 * self.wt + 35 * self.tsba
                return self.kcal
            elif self.age > 16:
                self.kcal = 25 * self.wt + 40 * self.tsba
                return self.kcal
            else:
                pass

        def harris(self):
            if self.sex == "m":
                self.kcal = 66.5 + 13.8 * self.wt + 5 * self.ht - 6.76 * self.age
                return self.kcal
            elif self.sex == "f":
                self.kcal = 655 + 9.6 * self.wt + 1.85 * self.ht - 4.68 * self.age
                return self.kcal
            else:
                pass

        def average(self):
            return (self.curreri() + self.harris()) / 2

# A simple interface
    print("\n")
    print("=====================================================")
    print("||                                                 ||")
    print("||          Energy Requirement Calculator          ||")
    print("||                                                 ||")
    print("=====================================================")

# Ask the user to input the patient parameters    
    new_ptn = Patient()
    new_ptn.sex = str(input("Patient gender(m/f): "))
    new_ptn.age = int(input("Age(years): "))
    new_ptn.wt = int(input("Weight(kg): "))
    new_ptn.ht = int(input("Height(cm): "))
    new_ptn.tsba = int(input("TSBA(%): "))

# This outputs the Curreri formula
    print("\nCurreri Energy Requirement")
    print(str(new_ptn.curreri()) + " kcal")

# This here outputs the Harris-Benedict formula
    print("\nHarris-Benedict Basal Energy Expenditure")
    print(str(new_ptn.harris()) + " kcal")

# And this outputs the average of the two systems
    print("\nTotal Daily Energy Requirement (Avg.)")
    print(str(new_ptn.average()) + " kcal")
    print("\n")

if __name__ == "__main__":
    main()
