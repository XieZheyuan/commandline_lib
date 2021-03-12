from commandline_lib import shell
from commandline_lib import exceptions
from datetime import datetime


class ExampleShell(shell.BaseShell):

    def get_welcome_message(self):
        now = str(datetime.now())
        return "Now is: " + now + " , This is a example shell by xie zheyuan!"

    def parse(self, value: str = None):
        # print(value, value=="quit", list(value))
        if value == "quit":
            raise exceptions.UserNeedQuitException
        else:
            self.echo("You input: " + value)

    def user_need_quit_action(self):
        self.echo("Do you want to quit(y/n)?")
        g = self.input()
        if g == "y":
            return True


def main():
    ex = ExampleShell()
    ex.run()


if __name__ == "__main__":
    main()
