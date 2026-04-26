# real basic ass skeleton code, please feel free to change it up as you see fit
from graph_stuff import HKGraph
import csv_to_dict

def get_pitches(filename):
    pitches = csv_to_dict.load_authors(filename)
    return pitches
    # thought - for this and the next function, we CAN just copy over the code - or remove these functions and run these directly in the main code?


def get_artists(filename):
    artists = csv_to_dict.load_artists(filename)
    return artists
    # see above


def create_graph(artists=dict, pitches=dict):
    # output: list of graph edges
    edge_list = []

    # iterates through whether each pitch is present in artist preferences, checks it is OK, then adds an edge connecting artist to that pitch
    # runs in O(mn) where m = number of pitches and n = number of artists - i couldn't think of a more efficient way apologies D:
    for artistID in artists:
        for pitchID in pitches:
            # see NOW after adding everything to the branch i just thought of a way to make this run in O(n)!!
            # if we have a dict matching the pitchID code to our internal pitchID (oh that's confusing why did i name the variables the same thing) 
            # then we can just grab our internal index for the pitch and test everything against that
            # why on earth did i do this instead. what was i thinking. i am so sorry i will fix that at some point probably
            if (pitches[pitchID]["pitchID"].upper() in map(str.upper, artists[artistID]["preferences"].split(";"))) or (set(pitches[pitchID]["fandom"].split(";")) <= set(artists[artistID]["wildcards"].split(";"))):
                # check age
                if (pitches[pitchID]["adults_only"] == "TRUE") and (artists[artistID]["adult"] == "FALSE"):
                    print(f"Age mismatch - dropping edge for pitch {pitchID} and artist {artistID}")
                # check medium - this check IS case sensitive as we assume these are selected with checkboxes
                elif len(list(set(pitches[pitchID]["mediums"].split(";")) & set(artists[artistID]["mediums"].split(";")))) == 0:
                    print(f"Medium mismatch - dropping edge for pitch {pitchID} and artist {artistID}")
                # check for dnms
                elif (pitches[pitchID]["discord"].lower() in map(str.lower, artists[artistID]["dnms"].split(";"))) or (artists[artistID]["discord"].lower() in map(str.lower, pitches[pitchID]["dnms"].split(";"))):
                    print(f"DNM mismatch - dropping edge for pitch {pitchID} and artist {artistID}")
                # check for same artist + author
                elif (pitches[pitchID]["discord"]).lower() == artists[artistID]["discord"].lower():
                    print(f"Artist matching to self - dropping edge for pitch {pitchID} and artist {artistID}")
                else:
                    # all ok :) add edge!
                    print(f"Adding edge for pitch {pitchID} and artist {artistID}")
                    edge_list.append((pitchID, artistID))
    print(f"Edge list: {edge_list}")
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

    # run the algorithm
    max_matching_size, pitches_to_artists, artists_to_pitches = g.hopcroft_karp_algorithm()

    # compile lists of unmatched IDs
    matches = []
    unmatched_pitches = []
    unmatched_artists = []
    for i in range(1,len(pitches_to_artists)):
        if pitches_to_artists[i] == 0:
            unmatched_pitches.append(i)
        else:
            matches.append((i,pitches_to_artists[i]))
    for i in range(1,len(artists_to_pitches)):
        if artists_to_pitches[i] == 0:
            unmatched_artists.append(i)
        # already should be in matches
    
    return matches, unmatched_pitches, unmatched_artists


def main():
    pitches = get_pitches()
    artists = get_artists()
    edge_list = create_graph()
    matched_pairs, unmatched_pitches, unmatched_artists  = bipartite_match(pitches, artists, edge_list)
    # then pretty print the outputs
