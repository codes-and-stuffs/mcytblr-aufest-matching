class TestArtist:
    def __init__(self, fandoms=list, pairings=list, wildcards=list, is18plus=bool):
        self._fandoms = fandoms
        self._pairings = pairings
        self._wildcards = wildcards
        self._is18plus = is18plus

    def get_fandoms(self):
        return self._fandoms

    def get_pairings(self):
        return self._pairings

    def get_wildcards(self):
        return self._wildcards

    def is_18plus(self):
        return self._is18plus
