

import re
import random

class Eliza:
    def __init__(self, name="Eliza", patterns=[], default="I'm not sure I understand you fully."):
        self.name = name
        self.patterns = patterns
        self.default = default

    def second_person(self, statement):
        statement = statement.replace("my", "your");
        statement = statement.replace("I ", "you ");
        statement = statement.replace("am ", "are ");
        statement = statement.replace("I was ", "you were ");
        return statement

    def respond(self, statement):
        for pattern, responses in self.patterns:
            match = re.search(pattern, statement.strip(" .!?"), re.IGNORECASE)
            if match:
                response = random.choice(responses).format(*(self.second_person(g) for g in match.groups()))
                return response
        return self.default

    def add_pattern(self, pattern, responses):
        self.patterns.insert(0, (pattern, responses))
