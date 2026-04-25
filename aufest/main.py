# real basic ass skeleton code, please feel free to change it up as you see fit

def get_pitches(filename):
    pass


def get_artists(filename):
    pass


def create_graph(artists=dict, pitches=dict):
    # output: graph
    pass


def bipartite_match(graph):
    # output: pairs, unmatched artists, unmatched pitches
    pass


def main():
    pitches = get_pitches()
    artists = get_artists()
    graph = create_graph()
    matched_pairs, unmatched_artists, unmatched_pitches = bipartite_match(graph)
    # then pretty print the outputs

