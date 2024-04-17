def start():
    change = []
    denominators = [50, 20, 10, 5, 2, 1, 0.25, 0.10, 0.05, 0.01]
    cost_of_good = float(input("How much does this item cost? "))
    money_given = float(input("How much money are you giving me? "))
    if cost_of_good < money_given:
        left_over = money_given - cost_of_good
        while left_over > 0:
            for denominator in denominators:
                while left_over >= denominator:
                    print(denominator)
                    change.append(denominator)
                    left_over = left_over - denominator

start()