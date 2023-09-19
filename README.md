# discrete-dynamical-systems
This repository contains functions that allow easy use of compartmental models and a notebook with some examples. In the current state, it is intended to be used to analyze systems that have:
- discrete time steps, and
- consistent behavior that only depends on the current state.

Created as a part of a mathematical modeling seminar at Carleton College. Based on material in chapter 1 of _A Course in Mathematical Modeling_ by Douglas D. Mooney and Randall Swift.


## To run

We used VSCode to run this code, but it should also work in the regular jupyter environment. 

Try to run the first cell in notebook `example.ipynb` by clicking on the little arrow to the left of the cell. VSCode will likely prompt you to install some extensions to nicely handle Jupyter notebooks. Do that. 

Then VSCode will likely prompt you to choose a kernel. Pick a Python option. (If you don't have python installed, go to python.org and install it). 

Now, things should run. However, you'll get an error if you don't have the right libraries installed. To fix this, open a terminal and run `pip install matplotlib` to install the package `matplotlib` (which powers the charts here). If you don't have pip installed, look up instructions. Good luck.