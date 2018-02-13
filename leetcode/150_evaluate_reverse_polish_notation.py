l1=["2", "1", "+", "3", "*"] 
l1=["4", "13", "5", "/", "+"]
tb_1=['+','-']
tb_2=['*','/']

stack=[]

for op in l1:
    if stack != [] and (op in tb_1 or op in tb_2):
        number2=stack.pop()
        number1=stack.pop()
        if op=='+':
            stack.append(number1+number2)
        if op=='-':
            stack.append(number1-number2)
        if op=='*':
            stack.append(number1*number2)
        if op=='/':
            stack.append(number1/number2)
        continue
    op=int(op)
    stack.append(op)
print stack