"""
Author: Matthew Cotton <matthewcotton.cs@gmail.com>
"""

from dndbuddy import colors
from dndbuddy import terms
from dndbuddy.Basic import alignments
from dndbuddy.Basic import armor
from dndbuddy.Basic import combat
from dndbuddy.Basic import createcharacter
from dndbuddy.Basic import hitdice
from dndbuddy.Basic import rolldice
from dndbuddy.Basic import weapons
# from dndbuddy.PHB import experience
# from dndbuddy.PHB import heightweight
# from dndbuddy.PHB import languages
# from dndbuddy.PHB import sizes
# from dndbuddy.PHB.classes import ranger
# from dndbuddy.PHB.races import halfelf


SPACE_AFTER_RESULTS = True

ESC = chr(27)
U_ARROW = ESC + "[A"
D_ARROW = ESC + "[B"
R_ARROW = ESC + "[C"
L_ARROW = ESC + "[D"

TITLE = colors.red("D&DBuddy")

WELCOME = """\
Welcome to {}!
====================
Run `help` for hints!
""".format(TITLE)

PROMPT = """[{}]> """.format(TITLE)

GOODBYE = """\nGood game!"""


INTERACTIVE_COMMANDS = [
    rolldice.RollDiceCommand,
    createcharacter.CreateCharacterCommand,
]

REFERENCE_COMMANDS = [
    combat.CombatCommand,
    hitdice.HitDiceCommand,
    # experience.ExperienceCommand,
    weapons.WeaponsCommand,
    armor.ArmorCommand,
    alignments.AlignmentsCommand,
    # languages.LanguageCommand,
    # heightweight.HeightWeightCommand,
    # sizes.SizesCommand,
    terms.TermsCommand,
]

CLASS_COMMANDS = [
    # ranger.RangerCommand,
]

RACE_COMMANDS = [
    # halfelf.HalfElfCommand,
]

COMMANDS = INTERACTIVE_COMMANDS + \
    REFERENCE_COMMANDS + \
    CLASS_COMMANDS + \
    RACE_COMMANDS


def list_commands(commands, prefix='- '):
    for command in commands:
        try:
            print(prefix + command.HELP)
        except AttributeError:
            pass


def show_help():
    print("Things D&DBuddy can do:")

    print("\nInteractive commands:")
    list_commands(INTERACTIVE_COMMANDS)
    print("\nInfo pages:")
    list_commands(REFERENCE_COMMANDS)
    print("\nClass info:")
    list_commands(CLASS_COMMANDS)
    print("\nRace info:")
    list_commands(RACE_COMMANDS)

    print("\nHelp:\nshow this menu (try `help` or `?`)")


def try_all_commands(inp):
    if inp.lower() in ['help', '?']:
        return show_help()

    for command in COMMANDS:
        if command.call(inp):
            break
    else:
        print("I don't understand `{}`.".format(inp))


def menu():

    last_command = ''

    while True:
        inp = input(PROMPT)
        if not inp:
            continue

        if inp == U_ARROW:
            inp = last_command

        try:
            try_all_commands(inp)
        except KeyboardInterrupt:
            print("Cancelled.")

        if SPACE_AFTER_RESULTS:
            print()

        last_command = inp


def main():
    print(WELCOME)

    try:
        menu()
    except KeyboardInterrupt:
        pass

    print(GOODBYE)


if __name__ == '__main__':
    main()
