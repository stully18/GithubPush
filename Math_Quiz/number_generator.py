import random

operator_list = ['+','-','*']

def random_equation():
   operator = str(random.choice(operator_list))
   num1 = random.randint(1,20)
   num2= random.randint(21,75)
   equation = f'{num1}{operator}{num2}'
   equation_ans = eval(equation)
   return equation,equation_ans
