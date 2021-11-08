#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import numpy
import matplotlib.pyplot as mpp #Вызываем библиотеки для работы с мат.функциями и графиками

# Эта программа рисует график функции, заданной выражением ниже

if __name__=='__main__':
    arguments = numpy.arange(0, 200, 0.1)# Условия аргумента функции
    mpp.plot(  #Начинаем работать с библиотекой для построения графика
        arguments,
        [math.sin(a) * math.sin(a/20.0) for a in arguments] #Данные построения графиков
    )
    mpp.show()#Вывод графика
    
