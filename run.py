from cmd2 import Cmd

class CliPrompt(Cmd):
    """Basic command processor boilerplate"""
    prompt = ">>> "
    intro = "Basic command processor"

    def do_greet(self, line):
        print("hello")

    def do_sqlquery(self, line):
        lines = []
        l = ''

        while ';' not in l:
            l = input()
            lines.append(l)

        self.query = ' '.join(lines).replace('\t', '')

        print("Query built:")
        print('\n'.join(lines))

    def do_exit(self, line):
        return True

if __name__ == '__main__':
        CliPrompt().cmdloop()
