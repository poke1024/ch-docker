#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tensorflow as tf
from tensorflow import keras

from pathlib import Path

import sys
import os

print("*" * 80)

def check_version(library, actual, expected):
	if actual != expected:
		print(f"your version of {library} what is {actual}, but should be {expected}.")
		sys.exit(1)
	else:
		print(f"detected {library} {actual}.")

check_version("tensorflow", tf.__version__, "2.3.1")
check_version("keras", keras.__version__, "2.4.0")

def check_tensorflow():
	# see https://www.tensorflow.org/tutorials/quickstart/beginner

	print("*" * 80)
	print("running a minimal keras test case")
	print("*" * 80)

	mnist = tf.keras.datasets.mnist

	(x_train, y_train), (x_test, y_test) = mnist.load_data()
	x_train, x_test = x_train / 255.0, x_test / 255.0

	model = tf.keras.models.Sequential([
		tf.keras.layers.Flatten(input_shape=(28, 28)),
		tf.keras.layers.Dense(128, activation='relu'),
		tf.keras.layers.Dropout(0.2),
		tf.keras.layers.Dense(10)
	])

	loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

	model.compile(optimizer='adam',
		loss=loss_fn,
		metrics=['accuracy'])

	model.fit(x_train, y_train, epochs=5)

	model.evaluate(x_test,  y_test, verbose=2)

	print("*" * 80)
	print("ok.")


def check_tesserocr():
	from tesserocr import PyTessBaseAPI

	script_dir = Path(os.path.dirname(os.path.realpath(__file__)))

	with PyTessBaseAPI() as api:
	    api.SetImageFile(str(script_dir / "börsenzeitung.jpg"))
	    text = api.GetUTF8Text()


check_tensorflow()
check_tesserocr()
