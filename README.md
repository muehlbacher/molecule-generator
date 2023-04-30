# Molecule Generator

Model was build and optimized on colab.research.google.com. To Make it deployable it was packed in subfiles and published on github.

This project was developed as part of a challenge in the master program "Artificial Intelligence" @ Johannes Kepler University (JKU) Linz

**Rank 3 of 100 students**

# Description
The aim of this challenge was to develop a model that can generate realistic molecules. The Molecules are represented as Simplified Molecular Input Line Entry Specification (SMILE) strings. It's a form of line notation for describing the structure of chemical species using ASCII strings. So you can handle the Molecules like text with certain constraints. To this end, a Long Short-Term Memory (LSTM) Network was trained to model the distribution of the molecules (SMILE strings) and generate new data.

A large set of human-designed molecules was provided as training data from which our model learned. The main task was to achieve a low Frechet ChemNet Distance (FCD) while auxiliary metrics "novelty", "validity" and "uniqueness" should be kept high.

Metric: Frechet ChemNet Distance (FCD)
