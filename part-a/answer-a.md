## Part a

### Describe what the code in `z3-test.py` is doing in a paragraph or two.

The code first defines two booleans (a, b) and two ints (x, y). The code then gives a logical expression with these variables and asks if it is satisfiable. The program returns that it is - specifically when x = 99, y = 100, b = TRUE, a = FALSE. The code then adds the condition y < 1 to the logical expression and again asks if it satisfiable. The expression now contains both x > 0 and x < y < 1. Since there is no integer between 0 and 1, the expression is no longer satisfiable so the program now returns unsat.

For each case, the program first prints the expression being tested, then the result (sat/unsat) and finally a model that satisfies the expression (if the expression is satisfiable).
