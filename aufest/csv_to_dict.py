import csv # perfect library for our uses! see https://docs.python.org/3/library/csv.html

# these functions load from csv files into new dictionaries
def load_authors(name_of_author_csv):
    author_dict = {}
    with open(name_of_author_csv, newline='') as signup_csv:
        signup_reader = csv.DictReader(signup_csv)
        next_id = 1
        for row in signup_reader:
            author_dict.update({next_id: row })
            next_id += 1
    return author_dict

def load_artists(name_of_artist_csv):
    artist_dict = {}
    with open(name_of_artist_csv, newline='') as signup_csv:
        signup_reader = csv.DictReader(signup_csv)
        next_id = 1
        for row in signup_reader:
            artist_dict.update({next_id: row })
            next_id += 1
    return artist_dict

# put final lists into output csv file
def output_to_csv(matched_pairs, unmatched_pitches, unmatched_artists, name_of_output_csv):
    with open(name_of_output_csv, 'w', newline='') as output_csv:
        writing_object = csv.writer(output_csv)
        # i'm sure there's a nicer way to format this
        writing_object.writerow(["Matched pairs"])
        writing_object.writerow(["Pitch ID", "Author Discord", "Artist Discord"])
        writing_object.writerows(matched_pairs)
        writing_object.writerow([])
        writing_object.writerow(["Unmatched authors"])
        writing_object.writerow(["Pitch ID", "Author Discord"])
        writing_object.writerows(unmatched_pitches)
        writing_object.writerow([])
        writing_object.writerow(["Unmatched artists"])
        writing_object.writerow(["Artist Discord"])
        writing_object.writerows(unmatched_artists)
    return

# put lists in output csv alongside each other - essentially a "pretty print" version
def better_output_to_csv(matched_pairs, unmatched_pitches, unmatched_artists, name_of_output_csv):
    # set up three 'columns'
    to_write = []
    to_write.append(["Matched pairs","","","Unmatched authors","","Unmatched artists"])
    to_write.append(["Pitch ID","Author Discord","Artist Discord","Pitch ID","Author Discord","Artist Discord"])
    # loop through lists to build a 2D list that directly reflects what we want in the CSV
    for i in range(max(len(matched_pairs),len(unmatched_pitches),len(unmatched_artists))):
        this_row = []
        for list_to_load in [matched_pairs, unmatched_pitches, unmatched_artists]:
            if i < len(list_to_load):
                # column exists here - print values
                for item in list_to_load[i]:
                    this_row.append(item)
            else:
                # add necessary whitespace if no column here
                if list_to_load == matched_pairs:
                    this_row.extend(["","",""])
                if list_to_load == unmatched_pitches:
                    this_row.extend(["",""])
        to_write.append(this_row)
    # drop that directly into the CSV
    with open(name_of_output_csv, 'w', newline='') as output_csv:
        writing_object = csv.writer(output_csv)
        writing_object.writerows(to_write)
    return

# does NOT RUN in normal execution - use this for debugging
if __name__ == "__main__":
    # files to use
    name_of_author_csv = "pitches.csv"
    name_of_artist_csv = "artists.csv"

    # unload data from csvs
    author_dict = load_authors(name_of_author_csv)
    artist_dict = load_artists(name_of_artist_csv)
    
    # old test dictionaries - uncomment if you want to skip the file loading stage
    # author_dict = {
    #     1: {"pitchID": "D01", "discord": "tubbo_", "fandom": "dream smp", "adults_only": "false", "mediums": ["art", "podfic"], "dnms": []},
    #     2: {"pitchID": "E01", "discord": "falsetwo", "fandom": "empires smp", "adults_only": "true", "mediums": ["webweave"], "dnms": []},
    #     3: {"pitchID": "D02", "discord": "someone_else", "fandom": "dream smp", "adults_only": "false", "mediums": ["art","webweave", "podfic", "other"], "dnms": ["tubbo_"]}
    # }
    
    # artist_dict = {
    #     1: {"discord": "aaaaaaa", "preferences": ["D01","D03"], "wildcards": ["dream smp"], "adult": "false", "mediums": ["art"], "dnms": []},
    #     2: {"discord": "skdfsdjkftghnfghh", "preferences": ["E01"], "wildcards": [], "adult": "true", "mediums": ["art", "webweave"], "dnms": []},
    #     3: {"discord": "awawsawawawawa", "preferences": ["D01"], "wildcards": ["vampires smp"], "adult": "true", "mediums": ["webweave", "podfic"], "dnms": []}
    # }

    # print loaded data
    print("Author dictionary:")
    print(author_dict)
    print("Artist dictionary:")
    print(artist_dict)
