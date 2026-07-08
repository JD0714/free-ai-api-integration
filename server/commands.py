from automation import type_letter, newTab


def handle_command(action, text):

    if action == "start":
        newTab(text)

    elif action == "continue":
        type_letter("B")

    elif action == "end":
        type_letter("C")

    else:
        return "Invalid command"

    return "Command executed"