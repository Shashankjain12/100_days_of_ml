<h1 align="center">Supervised Learning</h1>
<h3>Simple Linear Regression</h1>

Thanks to the coursera course by Andrew Ng and Udemy course I am able to grasp the concepts behind simple linear regression

Regression models are both linear and non-linear which can be used for predicting the real values like salary etc.If your independant
variable is time then you are forecasting for future values this concept summarises the value prediction task according to the
concept of simple line ie it leads to construction of line around certain datapoints and there by obtaining the values of y for certain
values of X this leads for prediction of certain values.
This uses a simple mathematical formula for predicting values of y Given As:-

                `y=m*x+c`

here y-->dependant variable that depends on certain values of X
m--> Slope of line ie. the angle of line from x-axis
x-->Independant variable whose values doesnot depends on itself but useful for predicting of dependant variables
c-->Constant 

We also generalises this formula as:-

                `h_theta(x)=theta_zero + theta_one * x`

h(x)-->hypothesis or predicted values
h(x) depends on theta's which are the parameters on whose values the value of y depends

So, We need to minimize the difference between the predicted and orignal values of y 
That means we need to minimize the actual value to the predicted value

		`j(theta)=1/2m*(h_theta(x)^i-y^i)^2`

This j(theta) is also known as cost function which minimizes the sum of square of distance between
predicted and actual values. So to minimize this cost function we need several methods of parameter learning

<h4>1.Gradient Descent Algorithm</h4>

Gradient Descent is the term denotes slope which minimizes the cost function based on certain values of y

Outline:-
1. Start with theta_zero,theta_one
2. Keep Changing the values of theta_zero and theta_one to reduce the cost function 

Given by:-

	`theta(j):= theta(j) - alpha * gradient(j(theta_zero,theta_one))`
	
	alpha:-Learning rate which basically controls how much bigger step do we need to take while calculating
	       local minima ie it updates value of theta after every step simultaneously until it reach local
	       local minimum value.
	       
	So according to this our gradient Descent algo will be -
	
	Repeat Until Convergence{
		theta_zero := theta_zero - alpha* 1/m(h(x) - y)
		theta_one  := theta_one - alpha * 1/m(h(x) - y)*x(i)
		}
		
Thanks for Reading tommorow i will implement this algo.

