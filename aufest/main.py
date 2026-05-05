# real basic ass skeleton code, please feel free to change it up as you see fit
from graph_stuff import HKGraph
import csv_to_dict
import random

def get_pitches(filename):
    pitches = csv_to_dict.load_authors(filename)
    return pitches
    

def get_artists(filename):
    artists = csv_to_dict.load_artists(filename)
    return artists


def create_graph(artists, pitches):
    # outputs list of graph edges

    # initialise list
    edge_list = []
    # iterates through whether each pitch is present in artist preferences, checks it is OK, then adds an edge connecting artist to that pitch
    # i attempted to make this more efficient but it's so much more convoluted and only goes from O(mn) to O(n) so i don't think it's worth it
    for artistID in artists:
        for pitchID in pitches:
            # TODO: make this fully case insensitive, just in case
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
    # print for debugging and return
    print(f"Edge list: {edge_list}")
    return edge_list


def bipartite_match(artists, pitches, edge_list):
    # outputs lists of matched pairs, unmatched artists, unmatched pitches

    # shuffle list of edges
    print("ORIGINAL LIST:")
    print(edge_list)
    random.shuffle(edge_list) # comment this line to remove randomisation
    print("SHUFFLED LIST:")
    print(edge_list)
    
    # define graph size and then make it
    number_of_pitches = len(pitches)
    number_of_artists = len(artists)
    graph = HKGraph(number_of_pitches, number_of_artists)

    # add edges one by one, checking they're within the correct range
    for u, v in edge_list:
        print(f"Adding edge: ({u}, {v})")
        if 1 <= u <= number_of_pitches and 1 <= v <= number_of_artists:
            graph.add_edge(u, v)
        else:
            print(f"Warning: Skipping invalid edge ({u}, {v}) - indices out of range [1..{number_of_pitches}] or [1..{number_of_artists}]")

    # run the algorithm
    max_matching_size, pitches_to_artists, artists_to_pitches = graph.hopcroft_karp_algorithm()

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
        # already should be in matches so continue
    # all done, return
    return matches, unmatched_pitches, unmatched_artists


def main():
    # load inputs
    pitches = get_pitches("pitches.csv")
    artists = get_artists("artists.csv")
    # make graph of possible matches
    edge_list = create_graph(artists, pitches)
    # find best matchine
    matched_pairs, unmatched_pitches, unmatched_artists = bipartite_match(pitches, artists, edge_list)
    # then pretty print the outputs
    matches_to_export = []
    pitches_to_export = []
    artists_to_export = []
    for pitch, artist in matched_pairs:
        matches_to_export.append([pitches[pitch]["pitchID"], pitches[pitch]["discord"], artists[artist]["discord"]])
    for pitch in unmatched_pitches:
        pitches_to_export.append([pitches[pitch]["pitchID"], pitches[pitch]["discord"]])
    for artist in unmatched_artists:
        artists_to_export.append([artists[artist]["discord"]])
    csv_to_dict.output_to_csv(matches_to_export, pitches_to_export, artists_to_export, "output.csv")
    print("All done! The finished lists can be found in output.csv.")
