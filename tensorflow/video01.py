#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: /Users/maion/OneDrive/Documentos/Documentos Felipe/programs/ruby/Python/PyCharmProjects/testes/tensorflow/video01.py
# Project: /Users/maion/OneDrive/Documentos/Documentos Felipe/programs/ruby/Python/PyCharmProjects/testes/tensorflow
# Created Date: Tuesday, September 24th 2019, 4:48:50 pm
# Author: Felipe Maion
# -----
# Last Modified: Tue Sep 24 2019
# Modified By: Felipe Maion
# -----
# Copyright (c) 2019 MaioneSys
# 
# 
# 
# -----
# HISTORY:
# Date      	By	Comments
# ----------	---	----------------------------------------------------------
###
# https://codelabs.developers.google.com/codelabs/tensorflow-lab1-helloworld/#3

import tensorflow as tf
import numpy as np
from tensorflow import keras

model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])

model.compile(optimizer='sgd', loss='mean_squared_error')

xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
ys = np.array([-2.0, 1.0, 4.0, 7.0, 10.0, 13.0], dtype=float)

model.fit(xs, ys, epochs=500)

print(model.predict([10.0]))