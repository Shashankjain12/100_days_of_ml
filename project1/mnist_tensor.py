import tensorflow as tf
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"]="2"
from tensorflow.examples.tutorials.mnist import input_data
from keras.utils import np_utils 

(x_train,y_train),(x_test,y_test)=tf.keras.datasets.mnist.load_data()

x_train = x_train.reshape(60000, 784)
x_test = x_test.reshape(10000, 784)
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255

y_train = np_utils.to_categorical(y_train, 10)
y_test = np_utils.to_categorical(y_test, 10)

X=tf.placeholder(tf.float32,shape=[None,784],name="Image")
y=tf.placeholder(tf.float32,shape=[None,10],name="label")

W=tf.Variable(initial_value=tf.zeros([784,10]),trainable=True,name=None,dtype=None)
b=tf.Variable(initial_value=tf.zeros([10]),trainable=True,name=None,dtype=None)

logits=tf.matmul(X,W)+b

entropy=tf.nn.softmax_cross_entropy_with_logits(logits=logits,labels=y)
loss=tf.reduce_mean(entropy)

optimizer=tf.train.GradientDescentOptimizer(learning_rate=0.001).minimize(loss)

writer=tf.summary.FileWriter("./graphs",tf.get_default_graph())

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    sess.run(optimizer,feed_dict={X:x_train,y:y_train})
    correct_pred=tf.equal(tf.argmax(logits,1),tf.argmax(y,1))
    acc=tf.reduce_mean(tf.cast(correct_pred,tf.float32))
    print(sess.run(acc,feed_dict={X:x_test,y:y_test}))
    




