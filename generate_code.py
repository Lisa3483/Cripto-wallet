from string import ascii_lowercase
from random import randint, sample, choice
from pprint import pprint


class SATGenerator:
    def __init__(self, variables=ascii_lowercase, min_length=20, min_count=50, max_count=100):
        self.variables = variables
        self.min_length = min_length
        self.min_count, self.max_count = min_count, max_count
        self.solve = {var: choice([False, True]) for var in variables}
        self.task = ""

    def generate(self, filename):
        pprint(self.solve)
        self.generate_conjuncts()
        self.save(filename)

    def generate_conjuncts(self):
        count = randint(self.min_count, self.max_count)
        i = 0
        while i < count:
            is_True, conjunct = self.generate_disjuncts()
            if is_True:
                self.task += f"{conjunct}\n"
                print(f"Genereate {i + 1}/{count} conjuncts SUCCESS")
                i += 1

    def generate_disjuncts(self):
        count = randint(self.min_length, len(self.variables))
        indices = sample(range(len(self.variables)), count)
        random_subset = ''.join([self.variables[i] for i in indices])

        is_True = False
        normal_vars, reversed_vars = "", ""
        for ch in random_subset:
            isReverse = choice([False, True])
            if isReverse:
                reversed_vars += ch
                is_True = is_True or not self.solve[ch]
            else:
                normal_vars += ch
                is_True = is_True or self.solve[ch]
        return is_True, f"{normal_vars}_{reversed_vars}",

    def save(self, filename):
        with open(filename, "w") as f:
            f.write(self.task)
