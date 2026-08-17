import random
import time

operators = ["+","-","*"]
total = 5

def generate_problem():
    left = random.randint(3,12)
    right = random.randint(3,12)
    operator = random.choice(operators)

    expr = str(left)+ " "+operator + " "+str(right)
    answer = eval(expr)
    return expr,answer

wrong = 0
input("Press enter to start: ")
print("-----------------------")

start = time.time()

for i in range(total):
    expr,answer = generate_problem()
    while True:
        guess = input("Problem #" + str(i + 1) + ": "+ expr + " " + "=")
        if guess == str(answer):
            break
        wrong  += 1

end = time.time()

total_time = end - start
print("-----------------------")
print(f"Good Job!,You finished in {total_time:.2f}sec")
print("-----------------------")