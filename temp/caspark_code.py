vscode_repeatable_action_map = {
    "join line": Key("csa-j"),

    # requires bracket jumper extension
    "klane": Key("ca-left"),
    "krane": Key("ca-right"),
    "krupper": Key("ca-up"),
    "krowner": Key("ca-down"),
    "shift klane": Key("csa-left"),
    "shift krane": Key("csa-right"),
    "shift krupper": Key("csa-up"),
    "shift krowner": Key("csa-down"),

    # requires bookmark extension
    "mark prev": Key("ca-j"),
    "mark next": Key("ca-l"),

    # requires the keyboard-scroll extension (once=middle, twice=top, thrice=bottom)
    "center mass": Key("c-l"),
}
vscode_action_map = {
    # overrides
    "yum new": Key("c-n"),

    # new commands
    "show settings": Key("c-comma"),
    "show shortcuts": Key("c-k, c-s"),
    "show explorer": Key("cs-e"),
    "show extensions": Key("cs-x"),
    "show search": Key("cs-f"),
    "show terminal": Key("c-backtick"),
    "show find and replace": Key("cs-h"),
    "toggle word wrap": Key("a-z"),
    "toggle sidebar": Key("c-b"),
    "toggle panel": Key("c-j"),
    "ock next": Key("c-d"),
    "ock all": Key("c-f2"),
    "ock undo": Key("c-u"),
    "palette": Key("cs-p"),
    "files": Key("c-p"),
    "recent": Key("c-e"),
    "language": Key("c-k, m"),
    "symbols": Key("c-t"),
    "line <big_n>": Key("c-g") + Text("%(big_n)s") + Pause("20") + Key("enter"),
    "comment": Key("c-slash"),
    "run this line": Key("csa-l"),

    # snippets
    "plate other": Key("c-m, c-s"),
    "plate function": Key("c-m, c-s") + Text("function"),
    "plate method": Key("c-m, c-s") + Text("method"),
    "plate if else": Key("c-m, c-s") + Text("if else"),
    "plate try": Key("c-m, c-s") + Text("try"),
    "plate class": Key("c-m, c-s") + Text("class"),

    # requires bookmark extension
    "mark set": Key("ca-k") + Pause("10"),

    # requires settings sync extension
    "settings upload": Key("sa-u"),
    "settings download": Key("sa-d"),

    # requires Find-Jump extension
    "ink <letter>": Key("a-j/20, %(letter)s"),
    "slump <letter>": Key("a-s/20, %(letter)s"),

    # requires gitlens extension
    "toggle blame": Key("cs-g, b"),
    "lens commit details": Key("cs-g, c"),
    "lens file history": Key("cs-g, h"),
    "lens repo status": Key("cs-g, s"),
    "toggle git lens": Key("cs-g, s-b"),
}
vscode_element_map = {
    "letter": letter_element,
}
vscode_environment = MyEnvironment(name="VSCode",
                                   parent=root_environment,
                                   context=AppContext(
                                       title=" - Visual Studio Code"),
                                   action_map=vscode_action_map,
                                   repeatable_action_map=vscode_repeatable_action_map,
                                   element_map=vscode_element_map)