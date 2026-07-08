from automation import type_letter, new_tab


def handle_command(action, text):

    if action == "start":
        return new_tab(text)

    elif action == "continue":
        type_letter("B")

    elif action == "end":
        type_letter("C")

    else:
        return "Invalid command"

    return "Command executed"