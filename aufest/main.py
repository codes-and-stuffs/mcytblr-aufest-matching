# real basic ass skeleton code, please feel free to change it up as you see fit

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


def bipartite_match(edge_list):
    # output: pairs, unmatched artists, unmatched pitches
    
    # i think here it'd be easiest to just import the graph stuff script and run it all there 
    # it just needs an input of the edge list and the number of artists + authors!
    
    pass


def main():
    pitches = get_pitches()
    artists = get_artists()
    edge_list = create_graph()
    matched_pairs, unmatched_artists, unmatched_pitches = bipartite_match(edge_list)
    # then pretty print the outputs
