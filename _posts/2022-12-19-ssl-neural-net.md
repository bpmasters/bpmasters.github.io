---
layout: post
title:  "Biologically Plausible Neural Network for Sound Source Localization"
author: ben
image: assets/images/SSLNetwork.png
featured: false
hidden: true
type: coursework
---

A biologically inspired and plausible neural network architecture for sound source localization on virtualized data.

This project was completed as part of one of my favorite courses I've taken, Simulating Neurobiological Systems. This unique interdisciplinary course covered concepts on topics such as neuroscience, biology, cognitive science, and mathematical modelling. As a graduate student, I was required to complete a final project. My project was to develop a biologically plausible model for sound source localization, using a unique neural network architecture known as a Legendre Memory Unit. The LMU optimally compresses a signal by transformation into the Legendre polynomial basis, which is meant to mimic the encoding of signals that have been filtered by the synaptic cleft.

My architecture utilized a binaural set of LMU's, inspired by the encoding done in tandem by the cochlear nuclei and superior olivary complex for sound source localization in the mammalian brain. After implementing this architecture in TensorFlow, I then converted it into Nengo, and developed an implementation of the model with spiking neurons. My detailed final report can be seen below.


<iframe src="https://drive.google.com/file/d/1xsjc4dvWxk6HYIxXvid_oYpslDUl7YlU/preview" style="width:100%;" height="800px" allow="autoplay"></iframe>
