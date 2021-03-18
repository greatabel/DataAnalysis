1.

Consider the decision version of the Subset Sum problem: Given a set of nn items with integer weights w_iw 
i
​	
 , an integer bound WW and an integer target ww, given in the input by their binary representation, decide if there exists a subset SS of the items such that \sum_{i\in S}^{ }w_i\le W∑ 
i∈S
​	
 w 
i
​	
 ≤W and \sum_{i\in S}^{ }w_i\ge w∑ 
i∈S
​	
 w 
i
​	
 ≥w.  

 

Explain how the decision version of the problem reduces to the optimisation version and vice-versa.

The Subset Sum problem is known to be NP-complete, which means that it can be reduced to the 33-SAT problem. The Subset Sum problem is also known to admit an FPTAS. Can you use the reduction from Subset Sum to 33-SAT to obtain an FPTAS for the optimisation version of 33-SAT, which is called MAX-33-SAT, where the goal is to maximise the number of satisfied clauses? Justify your answer.