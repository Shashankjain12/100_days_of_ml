<h1 align="center">Multiple Regression using Tensorflow</h1>

This involves studying the dataset and on the basis of those observation predicting the quality
of the product using multiple regression So I had used tensorflow due to it's Fascinating libraries and other
amazing features

So, This involves using of certain simple machine learning steps:-

Step 1. Dataset preprocessing
        --> Here I had normalised the dataset for gathering our data into one single scale
        --> Dividing/Separating the dataset into X and y splits so as to separate
            Indpendant and dependant variables in the dataset

Step 2. Splitting of datasets into one training and test sets so as to evaluate and train our model
        for it's specific performance checking

Step 3. creation of certain feature column with the previous numerical values

        ` tf.feature_column.numeric_column("Name of the column") `

Step 4. Verifying the estimators on certain input functions divided by X_train and y_train
        we can also provide them with certain batches and number of epochs with value of shuffle=True

Step 5. Creation of the model using linear Regression to obtain certain estimators on the training data

        ` tf.estimator.linearClassifier(feature_cols= feat_cols) `

Step 6. Training of our model based on that certain input function

        ` model.train(input_fn= input_function) `

Step 7. It involves predicting and evaluating the results that are to be found as the output

        Thanks for reading, Happy Coding :)
        Code for the following is in jupyter notebook

