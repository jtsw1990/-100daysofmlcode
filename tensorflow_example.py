import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston

rng = np.random
boston = load_boston()
data = boston["data"]
response = boston["target"]
feature_names = boston["feature_names"]
desc = boston["DESCR"]
learning_rate = 0.01

data.shape
response.shape

# Let's just use RM for this exerise
plt.scatter(data[:, 5], response)

W = tf.Variable(rng.randn(), tf.float32)
b = tf.Variable(rng.randn(), tf.float32)
x = tf.placeholder(tf.float32)

linear_model = tf.add(tf.multiply(x, W), b)
init = tf.global_variables_initializer()

y = tf.placeholder(tf.float32)
cost = tf.reduce_sum(tf.pow(linear_model-y, 2))/(2*response.shape[0])
optimizer = tf.train.GradientDescentOptimizer(learning_rate)
train = optimizer.minimize(cost)
sess = tf.Session()
sess.run(init)
for i in range(100):
    sess.run(train, {x: data[:, 5], y: response})

print(sess.run([W, b]))
