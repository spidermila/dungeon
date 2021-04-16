import os
import sys

try:
	from yaml.cyaml import CSafeLoader as Loader # type: ignore
except ImportError:
	from yaml import SafeLoader as Loader # type: ignore

class Map:
    def __init__(self) -> None:
        self.name = ''

class Editor:
    def __init__(self) -> None:
        self.map = None
        self.text_to_print: list = []
        self.command = ''
        self.separator_width = 40
        if sys.platform.find('linux') != -1:
            self.cls_command = 'clear'
        elif sys.platform.find('win') != -1:
            self.cls_command = 'cls'
        elif sys.platform.find('darwin') != -1:
            self.cls_command = 'clear'
        else:
            print('Unknown OS. cls will not work!')
            self.cls_command = False # type: ignore

    def minor_separator(self) -> None:
        print('-'*self.separator_width)

    def major_separator(self) -> None:
        print('='*self.separator_width)

    def cls(self) -> None:
        if self.cls_command: os.system(self.cls_command)

    def print_status_screen(self):
        self.cls()
        if self.map:
            print(f'Map: {self.map.name}')
        else:
            print(f'Map: no map loaded')

    def command_prompt(self) -> bool:
        self.minor_separator()
        command_line = input(': ')
        if len(command_line) > 0:
            self.command = command_line.split()[0]
            return True
        else:
            return False

    def print_additional_text(self) -> None:
        if len(self.text_to_print) > 0:
            self.minor_separator()
            for p in self.text_to_print:
                print(p)
            self.text_to_print = []

    def load_map(self):
        ...
        # yaml.load(document, Loader=Loader)
        # print(yaml.dump({'room':[4, 5]}))

def main():
    commands = {
        'quit commands': ['q', 'quit'],
        'help commands': ['h', 'help'],
    }
    e = Editor()
    while True:
        e.print_status_screen()
        e.print_additional_text()
        if e.command_prompt():
            if e.command.lower() in commands['quit commands']:
                exit(0)
            elif e.command.lower() in commands['help commands']:
                for c in commands:
                    e.text_to_print.append(f'{c}: {commands[c]}')



if __name__ == '__main__':
    exit(main())
