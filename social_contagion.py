import networkx as nx
import matplotlib.pyplot as plt
import random

file = None  # open('out', 'w')
a = 1
b = 100000


def create_bitcoin_graph(g):
    with open('bitcoin.csv') as f:
        for row in f:
            s = row.split(',')
            g.add_edge(s[0], s[1], weight=int(s[2]))


def from_bools_to_colors(contagion_list):
    for k, v in contagion_list.items():
        if v:
            contagion_list[k] = 'red'
        else:
            contagion_list[k] = 'blue'
    return contagion_list


# Saves graphs into data folder
def draw_graph(g, day, layout):
    colors = from_bools_to_colors(nx.get_node_attributes(g, 'contagion'))
    nx.draw(g, node_color=list(colors.values()), pos=layout, node_size=50, font_size=6, font_color='w', arrowsize=3)
    plt.draw()
    plt.savefig('data/' + str(day) + '.png', dpi=500)
    plt.close()


# First Iteration of contagion
def initialize_graph(g, percentage):
    n = len(g) * percentage
    for i in range(int(n)):
        v = random.choice(list(g.node.keys()))
        g.node[v]['contagion'] = True


def main():
    g = nx.DiGraph()
    create_bitcoin_graph(g)
    # g = nx.scale_free_graph(2000)
    # g = nx.fast_gnp_random_graph(500,0.075)
    g = g.to_undirected()
    layout = nx.spring_layout(g)
    nx.set_node_attributes(g, False, 'contagion')  # Setta a tutti i parametri contagion il valore false
    draw_graph(g, 0, layout)

    initialize_graph(g, 0.1)
    draw_graph(g, 1, layout)

    days = 5
    for day in range(days):
        print('Day: ', day, file=file)
        for n in g.nodes():
            nn_number = len(list(set(g.edges(n))))
            if nn_number == 0:
                continue

            blues = 0
            for frm, to in list(set(g.edges(n))):
                if not g.node[to]['contagion']:
                    blues += 1
            p = blues / nn_number
            not_contagion_percentage = p * nn_number * a
            contagion_percentage = (1 - p) * nn_number * b
            if contagion_percentage > not_contagion_percentage:
                g.node[n]['contagion'] = True
        draw_graph(g, day + 2, layout)

    plt.close()

    infected = []
    not_infected = []
    for n in g.nodes:
        if g.node[n]['contagion']:
            infected.append(n)
        else:
            not_infected.append(n)
    print('Infected nodes: \n\t', infected, file=file)
    print('Not-Infected nodes: \n\t', not_infected, file=file)


if __name__ == '__main__':
    main()
