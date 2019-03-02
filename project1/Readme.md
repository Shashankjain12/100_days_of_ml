<h1 align="center">Project 1:MNIST dataset Prediction using Tensorflow</h1>
This project involves linear regression of mnist dataset using LinearRegression machine learning

This project involves:-

1. MNIST Dataset- An 28*28 dataset with input vector as simple digits from 0-9 and we need to predict whether the digit is same as the input vector
2. Linear Regression Model
3. Tensorflow - For effective calculation for this project i will be using tensorflow as it got some enriched libraries containing MNIST dataset

Some common formulas of mathematical algo required are:-

For simple linear regression-
	> Setting up of weights as the Variables as tensorflow variables
	> Setting up of X as the placeholder value for inputs
	> Setting up of y as the placeholder value for outputs
	> Setting up of set of biases as the variables for set of zeroes as the vector
		
		w-->tf.Variable(initial_value=None,dtype=None,Trainable=True,shape=None)
		
		X-->tf.placeholder(dtype=tf.float32,shape=[batch_size,784],name="Image")
		
		y-->tf.placeholder(dtype=tf.float32,shaoe=[batch_size,10],name="Label")
		
		b-->tf.Variable(initial_value=None,dtype=None,trainable=True,name=None)
		
		logits-->X*w+b

		y_predicted-->softmax(logits)

		loss-->cross_entropy(Y,y_predicted)
		
		optimizer-->tf.train.GradienDescentOptimizer(learning_rate=0.001).minimize(loss)

Result:68% accuracy for linear regression model
