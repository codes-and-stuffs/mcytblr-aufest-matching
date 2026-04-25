# real basic ass skeleton code, please feel free to change it up as you see fit
from graph_stuff import HKGraph

def get_pitches(filename):
    pass


def get_artists(filename):
    pass


def create_graph(artists=dict, pitches=dict):
    # output: list of graph edges
    edge_list = []

    for artistID in artists:
        print(artists[artistID]["preferences"])
        for pitchID in pitches:
            print(pitches[pitchID]["pitchID"])
            if (pitches[pitchID]["pitchID"] in artists[artistID]["preferences"]) or (pitches[pitchID]["fandom"] in artists[artistID]["wildcards"]):
                if (pitches[pitchID]["adults_only"] == "true") and (artists[artistID]["adult"] == "false"):
                    print("age mismatch")
                elif len(list(set(pitches[pitchID]["mediums"]) & set(artists[artistID]["mediums"]))) == 0:
                    print("medium mismatch")
                elif (pitches[pitchID]["discord"] in artists[artistID]["dnms"]) \
                    or (artists[artistID]["discord"] in pitches[pitchID]["dnms"]):
                    print("dnm mismatch")
                elif (pitches[pitchID]["discord"]) == artists[artistID]["discord"]:
                    print("same participant mismatch")
                else:
                    print("ok")
                    edge_list.append((pitchID, artistID))
    print(edge_list)
    return edge_list


def bipartite_match(artists, pitches, edge_list):
    # output: pairs, unmatched artists, unmatched pitches

    # shuffle list of edges
    print("ORIGINAL LIST:")
    print(hardcoded_edges)
    random.shuffle(hardcoded_edges)
    print("SHUFFLED LIST:")
    print(hardcoded_edges)

    # define graph size and then make it
    number_of_pitches = len(pitches) # authors
    number_of_artists = len(artists) # artists
    graph = HKGraph(number_of_pitches, number_of_artists)

    # add edges one by one, checking they're within the correct range
    for u, v in edges_data:
        print(f"  Adding edge: ({u}, {v})")
        if 1 <= u <= number_of_pitches and 1 <= v <= number_of_artists:
            g.add_edge(u, v)
        else:
            print(f"Warning: Skipping invalid edge ({u}, {v}) - indices out of range [1..{number_of_pitches}] or [1..{number_of_artists}]")

    # run the algorithm (this gives the size, list output printed from inside but i should change that)
    max_matching_size = graph.hopcroft_karp_algorithm()
    
    pass


def main():
    pitches = get_pitches()
    artists = get_artists()
    edge_list = create_graph()
    matched_pairs, unmatched_artists, unmatched_pitches = bipartite_match(artists, pitches, edge_list)
    # then pretty print the outputs
