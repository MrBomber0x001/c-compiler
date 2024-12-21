class Parser:
    def __init__(self):
        self.rules = {}
        self.input_string = None
        self.stack = []

    def get_rules(self):
        print("Grammars 👇")
        while True:
            print("Enter rule number 1 for non-terminal 'S': ", end="")
            rule1_s = input()
            print("Enter rule number 2 for non-terminal 'S': ", end="")
            rule2_s = input()
            print("Enter rule number 1 for non-terminal 'B': ", end="")
            rule1_b = input()
            print("Enter rule number 2 for non-terminal 'B': ", end="")
            rule2_b = input()

            self.rules = {
                'S': [rule1_s, rule2_s],
                'B': [rule1_b, rule2_b]
            }

            if self.is_grammar_simple():
                break
            else:
                print("The Grammar isn't simple.")
                print("Try again")

    def is_grammar_simple(self):
        for non_terminal, rules in self.rules.items():
            for rule in rules:
                if len(rule.split()) > 2:
                    return False
        return True

    def parse(self, input_string):
        self.input_string = input_string
        self.stack = ['$', 'S']
        self.index = 0
        return self.parse_stack()

    def parse_stack(self):
        while self.stack:
            top = self.stack.pop()
            if top == '$':
                return self.index == len(self.input_string)
            elif top in self.rules:
                for rule in reversed(self.rules[top]):
                    self.stack.extend(rule.split()[::-1])
            elif top == self.input_string[self.index]:
                self.index += 1
            else:
                return False
        return True


def main():
    parser = Parser()
    parser.get_rules()

    while True:
        print("Enter the string want to be checked: ", end="")
        input_string = input()
        if parser.parse(input_string):
            print("Your input String is Accepted.")
        else:
            print("Your input String is Rejected.")

        print("======================")
        print("1-Another Grammar.")
        print("2-Another String.")
        print("3-Exit")
        print("Enter ur choice : ", end="")
        choice = input()
        if choice == '1':
            parser = Parser()
            parser.get_rules()
        elif choice == '2':
            continue
        else:
            break


if __name__ == "__main__":
    main()
