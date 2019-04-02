# This program calculates total energy requirement in burn patients
# It uses the two widely used formula; Curreri and Harris-Benedict


def main():

    class Patient:

        def __init__(self):
            self.sex = ["m", "f"]
            self.age = 0
            self.wt = 0
            self.ht = 0
            self.tsba = 0
            self.kcal= 0

        def curreri(self):
            if self.age < 16:
                self.kcal = 60 * self.wt + 35 * self.tsba
                return self.kcal
            else:
                self.kcal = 25 * self.wt + 40 * self.tsba
                return self.kcal

        def harris(self):
            if self.sex == "m":
                self.kcal = 66.5 + 13.8 * self.wt + 5 * self.ht - 6.76 * self.age
                return self.kcal
            elif self.sex == "f":
                self.kcal = 655 + 9.6 * self.wt + 1.85 * self.ht - 4.68 * self.age
                return self.kcal
            else:
                pass
    
    new_ptn = Patient()
    new_ptn.sex = str(input("Patient gender (m/f): "))
    new_ptn.age = int(input("Age(years): "))
    new_ptn.wt = int(input("Weight(kg): "))
    new_ptn.ht = int(input("Height(cm): "))
    new_ptn.tsba = int(input("TSBA(%): "))

    print(new_ptn.curreri())
    print(new_ptn.harris())

if __name__ == "__main__":
    main()

