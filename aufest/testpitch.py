class TestPitch:
    def __init__(self, fandom=str, pairing=str, minors_allowed=bool):
        self._fandom = fandom
        self._pairing = pairing
        self._minors_allowed = minors_allowed

    def get_fandom(self):
        return self._fandom

    def get_pairing(self):
        return self._pairing

    def minors_allowed(self):
        return self._minors_allowed