

class PERT:

    def __init__(self):
        self.lol = []
        self.r = 0
        self.p = 0
        self.o = 0
        self.total_r = 0
        self.total_p = 0
        self.total_o = 0
        self.total_mean = 0
        self.total_std_dev = 0
        self.weeks = []


    def brain(self):
        x = input("Press [enter] to make a calculation, 'y' to push calculation, or 'n' to exit ")
        if x == 'n':
            print(self.lol)
            return "Exiting program..."
        elif x == '':
            ans = input("Enter durations [O R P]... ")
            try:
                fix = [int(i) for i in ans.split(' ')]
            except ValueError:
                fix = [float(i) for i in ans.split(' ')]
            self.lol.append(fix)
            self.brain()
        elif x == 'y':
            self.hours_to_weeks()
            self.calculation()
            return
        else:
            print("Invalid input, press [enter] or 'n'")
            self.brain()

    def calculation(self):
        for i in self.lol:
            self.o = i[0]
            self.r = i[1]
            self.p = i[2]
            mean = (self.o + 4 * self.r + self.p) / 6
            std_dev = (self.p - self.o) / 6
            i.append(round(mean, 2))
            i.append(round(std_dev, 4))
        for i in self.lol:
            self.total_mean += i[3]
            self.total_std_dev += i[4]
            self.total_o += i[0]
            self.total_r += i[1]
            self.total_p += i[2]
        print("List of data:")
        for i in self.lol:
            print("\t", i)
        print("\n============================\n")
        print(f"Total PERT estimate: {round(self.total_mean, 2)}")
        print(f"Total deviation: {self.total_std_dev}")
        print(f"Total optimistic: {self.total_o}")
        print(f"Total realistic: {self.total_r}")
        print(f"Total pessimistic: {self.total_p}")
        print("\n============================\n")
        print("we are done here...bye")

    def hours_to_weeks(self):
        week_o = 0
        week_p = 0
        week_r = 0
        week_mean = 0
        self.weeks = [[x / 8 for x in i] for i in self.lol]
        print(".\n...\n.....\n.......")
        print("Weeks data:")
        for i in self.weeks:
            print("\t", i)
            week_o += i[0]
            week_r += i[1]
            week_p += i[2]
            # week_mean += i[3]
        # print(f"Mean week estimate: {week_mean}")
        print(".....................")
        print(f"Optimistic week estimate: \n\t{week_o}")
        print(f"Realistic week estimate: \n\t{week_r}")
        print(f"Pessimistic week estimate: \n\t{week_p}")
        print(".......\n.....\n...\n.")


def main():
    calc = PERT()
    calc.brain()


if __name__ == '__main__':
    main()
