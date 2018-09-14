# Graph-Social-Contagion-with-NetworkX-in-Python
Implemented a Social Contagion on a Realistic Graph in Python. The library used is NetworkX and the graph is the Bitcoin Alpha.

## Getting Started

To download my repo:

```
git clone https://github.com/riki95/Graph-Social-Contagion-with-NetworkX
```

The program was written in Python and compiled with Python 3.6 so you need it to run.
The program needs a graph in input which is a csv file and I used the Bitcoin Alpha Dataset.

### Bitcoin Alpha Dataset

The [Bitcoin Alpha Dataset](https://snap.stanford.edu/data/soc-sign-bitcoin-alpha.html) is a csv file that consists on 4 columns:
```
SOURCE, TARGET, RATING, TIME
```

I've decided to only study Source, Target and Rating because Time was not so important to care about.
You can just download my repo and you will find the dataset with the first row removed (it was the one with the Column's names) or you can download it from the official website.

## Reproduce experiments

Reproducing experiments is very easy, running this command on terminal is enough:

```
python social_contagion.py
```
You will see the analysys on the terminal that is increasing the number of days and in the folder of the Python script will appear a **Data** folder. Inside of it you will file some png files that represent the social contagion spread.

You can modify the Graph in input and the analysis is quite the same. Obviously you have to adapt some methods. 

## Contagion Plots

Thanks to this script you will be able to reproduce a Social Contagion on your Graph. First of all, the Graph will be printed:

![Graph Image 1](https://i.imgur.com/72EXAqG.png)

You can modify colors, nodes, scales and so on. You can also draw histograms:

![Diameter Historgram](https://i.imgur.com/aplPStE.png)

This has been done with Matplotlib and it is very useful if you need to plot degrees or something like that.

## Authors

* **Riccardo Basso** - *Università degli studi di Genova*

