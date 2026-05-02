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
