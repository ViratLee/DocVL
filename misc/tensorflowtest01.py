import tensorflow as tf
#from tensorflow import keras
print(tf.__version__)#1.3.0
# creates nodes in a graph
# "construction phase"
x1 = tf.constant(5)
print(type(x1))
print(x1)
x2 = tf.constant(6)
result=tf.multiply(x1,x2)
print(type(result))
print(result)