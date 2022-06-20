
from pulp import*

#1)

Warehouses = ["A" ,"B"]

supply = {"A":2000,
          "B":4500}

Bars = {"1", "2" ,"3" ,"4" }

demand = {"1" :600 ,
          "2" :1000 ,
          "3" :1600 , 
          "4" :150 ,
          "5":800}

costs = {"A" : {"1":3 ,"2":4 ,"3":6 , "4":2} , 
         "B":  {"1":2 , "2":3 , "3":3, "4":1}}

prob = LpProblem("Beer Dsitribution Problem" , LpMinimize)

Routes = [(w ,b) for w in Warehouses for b in Bars]
vars = LpVariable.dicts("Route " ,(Warehouses   , Bars) , 0 , None , LpInteger)

prob +=lpSum([vars[w][b]*costs[w][b] for (w ,b) in Routes]), "Sum_of_Costs"

for w in Warehouses:
    prob += lpSum([vars[w][b] for b in Bars]) <= supply[w], "Sum_of_Prod_%s"%w

for b in Bars :
    prob += lpSum([vars[w][b] for w in Warehouses])>=demand[b] , "Sum_of_Prod_%s"%b
    
    
print(prob.writeLP)
print(value(prob.objective))
print(prob.solve())


for v in prob.variables():
    print(v.name ,"=" , v.varValue)
    

#OUTPUT:-->
"""
<bound method LpProblem.writeLP of Beer_Dsitribution_Problem:
MINIMIZE
3*Route__A_1 + 4*Route__A_2 + 6*Route__A_3 + 2*Route__A_4 + 2*Route__B_1 + 3*Route__B_2 + 3*Route__B_3 + 1*Route__B_4 + 0
SUBJECT TO
Sum_of_Prod_A: Route__A_1 + Route__A_2 + Route__A_3 + Route__A_4 <= 2000

Sum_of_Prod_B: Route__B_1 + Route__B_2 + Route__B_3 + Route__B_4 <= 4500

Sum_of_Prod_4: Route__A_4 + Route__B_4 >= 150

Sum_of_Prod_1: Route__A_1 + Route__B_1 >= 600

Sum_of_Prod_2: Route__A_2 + Route__B_2 >= 1000

Sum_of_Prod_3: Route__A_3 + Route__B_3 >= 1600

VARIABLES
0 <= Route__A_1 Integer
0 <= Route__A_2 Integer
0 <= Route__A_3 Integer
0 <= Route__A_4 Integer
0 <= Route__B_1 Integer
0 <= Route__B_2 Integer
0 <= Route__B_3 Integer
0 <= Route__B_4 Integer
>
None
1
Route__A_1 = 0.0
Route__A_2 = 0.0
Route__A_3 = 0.0
Route__A_4 = 0.0
Route__B_1 = 600.0
Route__B_2 = 1000.0
Route__B_3 = 1600.0
Route__B_4 = 150.0

"""


#2)
JIM = ["M" ,"N" ,"O"]

supply = {"M":700 , 
          "N":300 ,
          "O":500}


plants =  {"A" , "B" ,"C" , "D"}

demand = {"A" : 650 ,
          "B" : 200 , 
          "C" : 450 ,
          "D" : 250}

cost = {"M" : {"A" : 14 , "B" : 22 , "C" : 17 , "D" : 14},
        "N" : {"A" : 17 , "B" : 13 , "C" : 14 , "D" : 19},
        "O" : {"A" : 13 , "B" : 19 , "C" : 28 , "D" : 14}}


prob = LpProblem("Automotive Supplier JIM Company- Problem " , LpMinimize)

Routes = [(j,p) for j in JIM for p in plants]

vars  =  LpVariable.dicts("Route" , (JIM , plants) , 0 ,None , LpInteger)

prob += lpSum([vars[j][p]*cost[j][p] for (j, p) in Routes]), "Sum_of_cost"



for j in JIM :
    prob += lpSum([vars[j][p] for p in plants]) <= supply[j] ,"Sum_of_supply_%s" %j
    
    

for p in plants :
    prob += lpSum([vars[j][p] for j in JIM ]) >= demand[p] , "Sum_of_supply_%s" %p
    
    
print(prob.writeLP)
print(value(prob.objective))
print(prob.solve())




for v in prob.variables():
    print(v.name ,"=" , v.varValue)
    
    
    
#OUTPUT:-->
"""

<bound method LpProblem.writeLP of Automotive_Supplier_JIM_Company-_Problem_:
MINIMIZE
14*Route_M_A + 22*Route_M_B + 17*Route_M_C + 14*Route_M_D + 17*Route_N_A + 13*Route_N_B + 14*Route_N_C + 19*Route_N_D + 13*Route_O_A + 19*Route_O_B + 28*Route_O_C + 14*Route_O_D + 0
SUBJECT TO
Sum_of_supply_M: Route_M_A + Route_M_B + Route_M_C + Route_M_D <= 700

Sum_of_supply_N: Route_N_A + Route_N_B + Route_N_C + Route_N_D <= 300

Sum_of_supply_O: Route_O_A + Route_O_B + Route_O_C + Route_O_D <= 500

Sum_of_supply_D: Route_M_D + Route_N_D + Route_O_D >= 250

Sum_of_supply_B: Route_M_B + Route_N_B + Route_O_B >= 200

Sum_of_supply_A: Route_M_A + Route_N_A + Route_O_A >= 650

Sum_of_supply_C: Route_M_C + Route_N_C + Route_O_C >= 450

VARIABLES
0 <= Route_M_A Integer
0 <= Route_M_B Integer
0 <= Route_M_C Integer
0 <= Route_M_D Integer
0 <= Route_N_A Integer
0 <= Route_N_B Integer
0 <= Route_N_C Integer
0 <= Route_N_D Integer
0 <= Route_O_A Integer
0 <= Route_O_B Integer
0 <= Route_O_C Integer
0 <= Route_O_D Integer
>
None
-1
Route_M_A = 150.0
Route_M_B = 0.0
Route_M_C = 350.0
Route_M_D = 250.0
Route_N_A = 0.0
Route_N_B = 200.0
Route_N_C = 100.0
Route_N_D = 0.0
Route_O_A = 500.0
Route_O_B = 0.0
Route_O_C = 0.0
Route_O_D = 0.0


"""

#3)

company = ["A" , "B" , "C"]

supply = {"A" : 60 ,
          "B" : 85 ,
          "C" : 35}


shops = {"R1" , "R2" , "R3" , "R4"}

demand = {"R1" : 30 , 
          "R2" : 25 ,
          "R3" : 55 , 
          "R4" : 65}


costs = {"A" : {"R1" : 6 , "R2" : 5 , "R3" : 1 , "R4" : 6},
         "B" : {"R1" : 2 , "R2" : 5 , "R3" : 8 , "R4" : 2},
         "C" : {"R1" : 8 , "R2" : 7 , "R3"  : 9 ,"R4"  : 2}}



prob = LpProblem("Transportation Problem" , LpMinimize)

Routes = [(c ,s) for c in company for s in shops]

vars = LpVariable.dicts("Route" , (company , shops) , 0 , None , LpInteger)

prob += lpSum([vars[c][s]*costs[c][s] for (c, s) in Routes]) , "Sum_of_Costs"

for c in company:
    prob += lpSum([vars[c][s] for s in shops ]) <= supply[c] , "Sum_of_Prod_%s" %c


for s in shops :
    prob += lpSum([vars[c][s] for c in company]) >= demand[s] , "Sum_of_Prod_%s" %s



for v  in prob.variables():
    print(v.name , "=" , v.varValue)
    
    
print(prob.writeLP)
print(prob.solve())
print(value(prob.objective))

#OutPUT :--->

"""


<bound method LpProblem.writeLP of Transportation_Problem:
MINIMIZE
6*Route_A_R1 + 5*Route_A_R2 + 1*Route_A_R3 + 6*Route_A_R4 + 2*Route_B_R1 + 5*Route_B_R2 + 8*Route_B_R3 + 2*Route_B_R4 + 8*Route_C_R1 + 7*Route_C_R2 + 9*Route_C_R3 + 2*Route_C_R4 + 0
SUBJECT TO
Sum_of_Prod_A: Route_A_R1 + Route_A_R2 + Route_A_R3 + Route_A_R4 <= 60

Sum_of_Prod_B: Route_B_R1 + Route_B_R2 + Route_B_R3 + Route_B_R4 <= 85

Sum_of_Prod_C: Route_C_R1 + Route_C_R2 + Route_C_R3 + Route_C_R4 <= 35

Sum_of_Prod_R2: Route_A_R2 + Route_B_R2 + Route_C_R2 >= 25

Sum_of_Prod_R4: Route_A_R4 + Route_B_R4 + Route_C_R4 >= 65

Sum_of_Prod_R1: Route_A_R1 + Route_B_R1 + Route_C_R1 >= 30

Sum_of_Prod_R3: Route_A_R3 + Route_B_R3 + Route_C_R3 >= 55

VARIABLES
0 <= Route_A_R1 Integer
0 <= Route_A_R2 Integer
0 <= Route_A_R3 Integer
0 <= Route_A_R4 Integer
0 <= Route_B_R1 Integer
0 <= Route_B_R2 Integer
0 <= Route_B_R3 Integer
0 <= Route_B_R4 Integer
0 <= Route_C_R1 Integer
0 <= Route_C_R2 Integer
0 <= Route_C_R3 Integer
0 <= Route_C_R4 Integer
>
1
370.0

"""





