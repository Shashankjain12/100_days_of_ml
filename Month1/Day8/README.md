[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Shashankjain12/100_days_of_ml/blob/master/Month1/Day7/Tensorflow_examples.ipynb)
<h1 align="center">TensorFlow</h1>
It is the mathematical computation library With the concepts of Data Flow Graphs used to execute our model.
To Understand tensorflow one must understand first about it's key phenomenon Known as Tensors.
<h4>What Are Tensors</h4>
Tensors are the generalisation of vectors and matrices of potentially higher dimenson arrays of data
with different dimensions and ranks that are fed as Input to the neural network.
Tensors are differentiated according to certain ranks this means ranks defines the dimensions of 
particular tensor.

eg. Tensor of rank 0 can be defined as S=[200]
    Tensor of rank 1 is S=[10,2,3] ie dimension is 1-D
    Tensor of rank 2 is m=[1,2,3],[4,5,6]
    Tensor of rank 3 is t=[[[1],[2],[3],[4]]]

Data is stored in the form of tensor and computation is done in a form of a graph.Here computation is done in
a form of graph here computation is done by data flow graph where we store information in form of graphs and
data is stored in form of sessions.
As the graph consists of nodes and edges.

Nodes-> They represents operations that are performed while executing the graph

Edges-> They represents the flow of the graph and the values of a variable in a graph

Whenever, we create a Tensorflow object there is a default graph .
Tensorflow works on two basic concepts:-

1. Building a Computation Graph
2. Executing a Computation Graph

Program Elements in Tensorflow are:-

1. Constants-> Paramenters whose values doesnot changes.To define a constant we use
		` tf.constant() ` command
    

	eg. 
	 ``
	 a= tf.constant(20,tf.float32)
	 b= tf.constant(20,tf.float32) 
	 print(a,b)
	``

2. Variables-> It allows us to add new trainable parameters to the graph.We define it using 
		` tf.Variable()` command

	eg.
	``
	W= tf.Variable([3],dtype=tf.float32)
	b= tf.Variable([-3],dtype=tf.float32)
	model=W*x+b
	``

3. Placeholders-> Allow us to feed data to a Tensorflow model from outside of a model .It permits
		  a value to be assigned later to define that we use:-

		  ` tf.placeholder()` command

	eg.
	``
	a=tf.placeholder(tf.float32)
	b=a*2
	with tf.Session() as sess:
		result=sess.run(b,feed_dict={a:3})
		print(result)
	``

	feed_dict it specifies tensors that provides concrete values to the placeholders

<h5>Session</h5>
A session is run to evaluate the data flow graph

eg.

	``
		a=tf.constant(5)
		b=tf.constant(3)
		c = a * b
		sess=tf.Session()
		print(sess.run(c))
	``


