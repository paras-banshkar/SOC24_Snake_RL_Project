import numpy as np
state={"sa":0,"sb":1,"sc":2,"sd":3}
A=np.array([[1.0,0.0,0.0,0.0],[0.5,0.0,0.5,0.0],[0.0,0.2,0.0,0.8],[0.0,0.0,0.0,1.0]])
A_n=np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
initial_state=input("etner the initial state : ")
target_state=input("enter the target state : ")
time=int (input("enter the T : "))
for j in range(time):
    A_n=np.matmul(A_n,A)
    print(A_n)
print("probability of reaching state "+target_state+" from state "+initial_state+" in time t= ",end="")
print(time,end="")
print(" is",end=" ")
print(A_n[state[initial_state]][state[target_state]])
