# imports
import csv # see https://docs.python.org/3/library/csv.html

# files to use - TODO
name_of_author_csv = ""
name_of_artist_csv = ""

# test dictionaries used here
author_dict = {
    1: {"pitchID": "D01", "discord": "tubbo_", "fandom": "dream smp", "adults_only": "false", "mediums": ["art", "podfic"], "dnms": []},
    2: {"pitchID": "E01", "discord": "falsetwo", "fandom": "empires smp", "adults_only": "true", "mediums": ["webweave"], "dnms": []},
    3: {"pitchID": "D02", "discord": "someone_else", "fandom": "dream smp", "adults_only": "false", "mediums": ["art","webweave", "podfic", "other"], "dnms": ["tubbo_"]}
}

artist_dict = {
    1: {"discord": "aaaaaaa", "preferences": ["D01","D03"], "wildcards": ["dream smp"], "adult": "false", "mediums": ["art"], "dnms": []},
    2: {"discord": "skdfsdjkftghnfghh", "preferences": ["E01"], "wildcards": [], "adult": "true", "mediums": ["art", "webweave"], "dnms": []},
    3: {"discord": "awawsawawawawa", "preferences": ["D01"], "wildcards": ["vampires smp"], "adult": "true", "mediums": ["webweave", "podfic"], "dnms": []}
}
# should be the following in practice:
# author_dict = {}
# artist_dict = {}

# load author dict - UNTESTED
# with open(name_of_author_csv, newline='') as signup_csv:
#     signup_reader = csv.DictReader(signup_csv, fieldnames=["pitchID","discord","fandom","adults_only","mediums","dnms"])
#     next_id = 1
#     for row in signup_reader:
#         author_dict.update({next_id: row })
#         next_id += 1

# load artist dict - UNTESTED
# with open(name_of_artist_csv, newline='') as signup_csv:
#     signup_reader = csv.DictReader(signup_csv, fieldnames=["discord","preferences","wildcards","adult", "mediums", "dnms"])
#     next_id = 1
#     for row in signup_reader:
#         artist_dict.update({next_id: row })
#         next_id += 1

print("Author dictionary:")
print(author_dict)
print("Artist dictionary:")
print(artist_dict)
