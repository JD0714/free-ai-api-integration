from automation import doStart, doContinue, doEnd


def handle_command(action, text):

    if action == "start":
        return doStart(text)

    elif action == "continue": 
        return doContinue(text)

    elif action == "end":
        return doEnd()

    else:
        return "Invalid command"