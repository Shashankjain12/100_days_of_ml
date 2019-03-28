<h1 align="center">Builing a Model</h1>

5 methods of building a model :-

1. All in

2. Backward Elimination

3. Forward Elimination

4. Bidirectional Elimination

5. Score Comparison

<h3>All-In</h3>
It means throw in all your variables that means all of independant variables are thrown into model at once
without being inspecting whether it is effective or not.

<h3> Backward Elimination</h3>

1. Select the significance level to stay in the model eg. SL=0.05 

2. Fit the full model with all possible predictors

3. Consider the predictor with the highest P-value. If P > SL goto step 4 else go to Finish.

4. Remove the predictor

5. Fit the model without this variable.

Do this until your P<SL 

<h3> Forward Elimination </h3>

1. Select SL to enter the model eg. SL=0.05

2. Fit all simple linear regression models y-xn Select the one with the lowest P-value

3. Keep the variables and fit the possible models with one extra predictor added to one you
   already have

4. Consider the predictor with lowest p value if P<SL go to step 3 else goto Finish

