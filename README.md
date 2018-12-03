# Graph-Social-Contagion-with-NetworkX
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

You can modify colors, nodes, scales and so on. The png images will be numbered from 1 (the first) to the last one and they represent the days of the contagion. For eample the second one look like this:

![Graph Image 2](https://i.imgur.com/iEAn7r7.jpg)

Where red nodes represent the infected ones. At the end, if the contagion parameters are good enough, you will get this:

![Graph Image 2](https://i.imgur.com/xf5u7Hv.png)

Every node is red, this means that you infected the whole graph. Sometimes the graph is so big that you cannot visualize all the nodes and maybe there are blue nodes hidden behind the reds. So you can check on terminal because at the end the list of remaining nodes to infect will be printed and if it is empty, it means that you did a good work.

## Authors

* **Riccardo Basso** - *Università degli studi di Genova*

