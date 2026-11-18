import random
import time

operators = ["+", "-", "*", "/"]
min_operand = 3
max_operand = 12
total_problem = 30


def generate_problem():
    left = random.randint(min_operand, max_operand)
    right = random.randint(min_operand, max_operand)
    operator = random.choice(operators)

    expr = str(left) + " " + str(operator) + " " + str(right)
    answer = eval(expr)
    return expr, answer


wrong = 0
input("Press enter to start")
print("--------------------")

startime = time.time()

for i in range(total_problem):
    expr, answer = generate_problem()
    while True:
        guess = input("Problem #" + str(i + 1) + " : " + expr + " = ")
        if guess == str(answer):
            break
    wrong += 1

endtime = time.time()
totaltime = round(endtime - startime, 2)

print("--------------------")
print("Nice Work!! You finishes in ", totaltime, "seconds!")
