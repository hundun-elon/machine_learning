# Machine Learning

## Overview

This repository contains ideas and implementations related to learning machine learning concepts from scratch, really the idea is to get the mathematics behind the deep neural networks.

## Project: Neural Network from Scratch

This is an assignment for my Adaptive computation and Machine Learning course, I am implementing a simple neural network **without using any of Python's machine learning libraries**. The goal is to gain a deeper understanding of the fundamental building blocks of neural networks by coding everything manually, as you can see on `neural_network.py` I am only using `numpy` so that I can get matrix algebra right.

### Neural Network Specifications

- **Architecture:** 3-layer neural network
  - **Input layer:** 5 nodes
  - **Hidden layer:** 10 nodes
  - **Output layer:** 3 nodes
- **Activation Function:**
  - All nodes in the **hidden layer** and **output layer** use the **sigmoid activation function**.
- **Initialization:**
  - All **weights** are initialized to `1`.
  - All **bias values** are initialized to `1`.
