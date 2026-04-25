import unittest
import random

from testfandom import *
from testpitch import *
from testartist import *

all_fandoms = create_fandoms()


def create_participants(pitch_count=int):

    pitches = []
    for fandom in all_fandoms:
        fandom_st_dev = int(fandom.get_size() * 100)
        fandom_pitch_count = int(((fandom.get_size() * 200)
                                 + random.randint(fandom_st_dev*-1, fandom_st_dev))
                                 /2)
        print(f"{fandom.get_name()} pitches: {fandom_pitch_count}")
        for i in range(fandom_pitch_count):
            pitch_count += 1
            ships = ["popular ship 1", "popular ship 2", "less popular ship 1", "less popular ship 2", "obscure asf ship 1", "obscure asf ship 2"]
            weights = [30, 30, 20, 10, 5, 5]
            roll_dice_for_ship = random.choices(ships, weights=weights, k=1)
            ith_pitch = TestPitch(fandom.get_name(), roll_dice_for_ship, bool(i%2))
            print(f"{ith_pitch.get_fandom()} pitch {i}: {roll_dice_for_ship}, minors allowed? {bool(i%2)}")
            pitches.append(ith_pitch)

    pitches_dict = {}
    for i in range(len(pitches)):
        pitches_dict[i] = [f"test pitch: {pitches[i].get_fandom()}, {pitches[i].get_pairing()}", pitches[i].minors_allowed()]

    artists_dict = {}

    return pitches_dict, artists_dict


class TestMatching(unittest.TestCase):

    def test_artist_dict(self):
        # test whether the artists are being gotten from the csv correctly
        self.assertTrue(0)

    def test_pitch_dict(self):
        # test whether the pitches are being gotten from the csv correctly
        self.assertTrue(0)

    def test_30(self):
        test_pitches = create_participants(30)[1]
        test_artists = create_participants(30)[2]
        # run matching with these dictionaries as input
        # print pairs and unmatchables
        # is everyone matched?
        self.assertTrue(0)

    def test_100(self):
        # same as above
        self.assertTrue(0)

    def test_200(self):
        self.assertTrue(0)

    def test_30_extra_pitches(self):
        self.assertTrue(0)

    def test_100_extra_pitches(self):
        self.assertTrue(0)

    def test_200_extra_pitches(self):
        self.assertTrue(0)

    def test_30_extra_artists(self):
        self.assertTrue(0)

    def test_100_extra_artists(self):
        self.assertTrue(0)

    def test_200_extra_artists(self):
        self.assertTrue(0)


if __name__ == '__main__':
    unittest.main()
