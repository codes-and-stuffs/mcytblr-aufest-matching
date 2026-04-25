class TestFandom:
    def __init__(self, name, size):
        self._name = name       # name of smp
        self._size = size       # size is out of 1 rather than hard coding participant numbers
        self._pairings = []     # assuming most participants will match largely based on preferred pairings

    def get_name(self):
        return self._name

    def get_size(self):
        return self._size

    def get_pairings(self):
        return self._pairings

    def add_pairing(self, pairing):
        self._pairings += pairing


def create_fandoms():
    hermitcraft = TestFandom("Hermitcraft SMP", 0.5)
    dsmp = TestFandom("Dream SMP", 0.45)
    vampires = TestFandom("Vampires SMP", 0.3)
    traffic = TestFandom("Life SMP Series", 0.35)
    empires = TestFandom("Empires SMP", 0.1)
    sfawtde = TestFandom("SFAWTDE", 0.1)
    qsmp = TestFandom("Quackity SMP", 0.05)
    rpf = TestFandom("Video Blogging RPF", 0.05)

    all_fandoms = [hermitcraft, dsmp, vampires, traffic, empires, sfawtde, qsmp]

    for i in range(10):
        teeny_tiny_fandom_name = f"teeny tiny SMP {i+1}"
        teeny_tiny_fandom = TestFandom(teeny_tiny_fandom_name, 0.01)
        all_fandoms.append(teeny_tiny_fandom)

    return all_fandoms
