from logic2 import *

# Question 1.1
carrots = Symbol("carrots")
orange = Symbol("orange")
knowledge_for_question1 = And(
    Implication(carrots, orange)
)
print(knowledge_for_question1.formula())  
#---------------------------------------------------
#Question 1.2
person = Symbol("person")
vegetarian = Symbol("vegetarian(x)")
like = Symbol("like")
like_person_carrots = Symbol("like(x, carrots)")
knowledge_for_question2 = And(Implication(vegetarian, like_person_carrots))
print(knowledge_for_question2.formula())  
#---------------------------------------------------

# Question 1.3
pass_exam = Symbol("pass(x)")
study_hard = Symbol("study_hard(x)")
knowledge_for_question3 = Implication(study_hard, pass_exam)
print(knowledge_for_question3.formula())  
#---------------------------------------------------

#Question 1.4
Pass = Symbol("? pass(who)")
knowledge_for_question4 = And(Pass)
print(knowledge_for_question4.formula())  
#---------------------------------------------------

#Question 1.5
teaches = Symbol("? teaches(course, which)")
knowledge_for_question5 = And(teaches)
print(knowledge_for_question5.formula())   
#---------------------------------------------------
# Question 1.6
x = Symbol("x")
y = Symbol("y")
enemies = Symbol(f"enemies({x}, {y})")
hates = Symbol(f"hates({x}, {y})")
fight = Symbol(f"fight({x}, {y})")
knowledge_for_question6 = And(Implication(enemies, And(hates, fight)))
print(knowledge_for_question6.formula()) 