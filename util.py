class Vect(object):
    def __init__(self, *coords):
        super(Vect, self).__setattr__("pos", [*coords])

    def __eq__(self, other):
        return all([s_x == o_x for s_x, o_x in zip(self.pos, other.pos)])

    def __sub__(self, other):
        return Vect(*[s_x - o_x for s_x, o_x in zip(self.pos, other.pos)])

    def __add__(self, other):
        return Vect(*[s_x + o_x for s_x, o_x in zip(self.pos, other.pos)])

    def __getattr__(self, name):
        if name == "x":
            return self.pos[0]
        elif name == "y":
            return self.pos[1]
        elif name == "z":
            return self.pos[2]
        else:
            super(Vect, self).__getattr__(name)  # pyright: ignore

    def __setattr__(self, name, val):
        if name == "x":
            self.pos[0] = val
        elif name == "y":
            self.pos[1] = val
        elif name == "z":
            self.pos[2] = val
        else:
            super(Vect, self).__setattr__(name, val)

    @staticmethod
    def __get_primes(n):
        low_primes = [2, 3, 5, 7, 11, 13]
        if n <= 6:
            return low_primes[:n]
        else:
            primes = low_primes
            i = 17
            while len(primes) < n:
                if all([i % j != 0 for j in range(2, int(i / 2) + 2)]):
                    primes.append(i)
                i += 1
            return primes

    def __hash__(self):
        hash = 1
        primes = Vect.__get_primes(2 * len(self.pos))
        prime_pairs = [(i, j) for i, j in zip(primes[::2], primes[1::2])]
        for (i, j), coord in zip(prime_pairs, self.pos):
            hash *= i ** abs(coord) * j ** int(coord / abs(coord) + 1)
        return hash

    def __repr__(self):
        out = ", ".join([str(x) for x in self.pos])
        return f"({out})"

    def move(self, *args):
        self.pos = [x + arg for x, arg in zip(self.pos, args)]
