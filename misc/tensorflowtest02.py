from __future__ import print_function
import tensorflow as tf
import os

# The default path for saving event files is the same folder of this python file.
tf.app.flags.DEFINE_string('log_dir', os.path.dirname(os.path.abspath(__file__)) + '/logs',
'Directory where event logs are written to.')

# Store all elements in FLAG structure!
FLAGS = tf.app.flags.FLAGS

# Defining some constant values
a = tf.constant(5.0, name="a")
b = tf.constant(10.0, name="b")

# Some basic operations
x = tf.add(a, b, name="add")
y = tf.div(a, b, name="divide")

# Run the session
with tf.Session() as sess:
    writer = tf.summary.FileWriter(os.path.expanduser(FLAGS.log_dir), sess.graph)
    print("output: ", sess.run([a,b,x,y]))

# Closing the writer.
writer.close()
sess.close()