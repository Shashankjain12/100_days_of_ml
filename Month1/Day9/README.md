[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Shashankjain12/100_days_of_ml/blob/master/Month1/Day9/linear_regression_with_tensorboard.ipynb)


<h1 align="center">Tensorboard</h1>

TensorBoard is a visualization tool, devoted to analyzing Data Flow Graph
and also to better understand the machine learning models.It can view
different types of statistics about the parameters and details of any part of a
computer graph graphically. It often happens that a graph of computation can
be very complex.

A deep neural network can have up to 36,000 nodes. For this reason, TensorBoard collapses nodes in high-level blocks,
highlighting the groups with identical structures. Doing so allows a better analysis of the
graph, focusing only on the core sections of the computation graph. Also, the
visualization process is interactive; user can pan, zoom, and expand the nodes
to display the details.

TensorBoard's algorithms collapse nodes into high-level blocks and highlightgroups with the same structures, 
while also separating out high-degree nodes.

The visualization tool is also interactive: the users can pan, zoom in, expand,
and collapse the nodes.

TensorBoard is equally useful in the development and tuning of a machine
learning model. For this reason, TensorFlow lets you insert so-called
summary operations into the graph. These summary operations monitor
changing values (during the execution of a computation) written in a log file.
Then TensorBoard is configured to watch this log file with summary
information and display how this information changes over time.

The tensorboard graph obtained is:-

![alt image](https://github.com/Shashankjain12/100_days_of_ml/tree/master/Month1/Day9/img.png)
