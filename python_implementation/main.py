

from eliza import Eliza
from eliza_patterns import ELIZA_PATTERNS
from anti_eliza_patterns import ANTI_ELIZA_PATTERNS

def main():
    print("ELIZA: Hello. How can I help you today?")
    eliza = Eliza(patterns=ANTI_ELIZA_PATTERNS)
    while True:
        statement = input("You: ")
        print(f"ELIZA: {eliza.respond(statement)}")
        if statement.lower().strip() == "quit":
            break

if __name__ == "__main__":
    main()