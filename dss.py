'''


'''
prob_dict = {'a':'1','b':'2','c':'3','d':'4','e':'5','f':'6'}
print("city = S")
while True:
    problem = list(map(str,input("enter problems").split()))
    if set(problem)&set(prob_dict.keys()):
        break
    else:
        print("oops,give alphabets as input")
solution = ['7']#common solution 
for i in problem:
    solution += prob_dict[i]
    
    print("generate solution #"+str(prob_dict[i])+" for problem "+i)
    #you can add a solution here.and solution to each problem gets solved.
solution_int = []
solution_int += [int(x) for x in solution]
print(sorted(solution_int))
print("generate solutions",end = ' ')
for i in sorted(solution_int):
    if sorted(solution_int).index(i)==len(sorted(solution_int))-1:
        print(' and '+str(i))
    elif sorted(solution_int).index(i)==len(sorted(solution_int))-2:
        print(i,end='')
    else:
        print(i,end=',')
        

