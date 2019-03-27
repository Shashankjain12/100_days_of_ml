<h1 align="center">Multiple Linear Regression</h1>

This can be considered as the extended version of the Simple Linear Regression Where we can have more than one dependant variables
and more than one indpendant variables and on the basis of these independant variables we can combine our inference to find the dependant variables

Formula that can be used to calculate the dependant variable values can be given as:-
	` y=b_zero+ b_one*x_one + b_two*x_two + .... + b_n * x_n `

Assumptions for Linear regression are:-

1. Linearity that the data is always linear with only two variable X and y

2. Homoscedasticity- In statistics, a sequence or a vector of random variables is homoscedastic if all random variables in the sequence 
   or vector have the same finite variance. This is also known as homogeneity of variance. 

3. Multi Variate Normality- The multivariate normal distribution is often used to describe, at least approximately, any set of (possibly)
   correlated real-valued random variables each of which clusters around a mean value.

4. Independence Of Errors- It assumes that this dataset will be available with the minimu set of errors deviating from the orignal values

5. Lack of multicollinearity

So, In this section we will look for multiple linear regression with deviating the following assumptions

## Dummy Variables

For the categorical set of data we need to create certain dummy variables ensuring the particular columns in the dataset.
Dummy variables includes certain categories that are separated after resolving the categorical issues.

 	` y=b_zero+ b_one*x_one + b_two*x_two + .... + b_n * x_n `

For example here all variables that are encoded are considered to be as dummy variables
So as we know categorical variables separating the data can create as many columns as that of number of different
categories So number of categories is equal to number of columns generated 

### Dummy Variable Trap

So we need to ensure to avoid dependancy between independant variables so we introduced dummy variables
To remove Dummy variable trap as we know 
	
	` D2= 1 - D1 `
 
So Dummy Variables can be removed to avoid this trap

Next time Let's Code .. :)
