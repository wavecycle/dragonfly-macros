# my version of keyboard.py derived from David Williams-King:
# https://github.com/dwks/aenea-grammar-simple/blob/master/keyboard.py

# from natlink import setMicState abc123
from dragonfly import(
    Key,
    Text,
    Grammar,
    MappingRule,
    Item,
    IntegerRef,
    Dictation,
    Choice,
    Config,
    Section,
    Function,
    Mimic,
)

from dragonfly.actions.keyboard import keyboard
from dragonfly.actions.typeables import typeables
if 'semicolon' not in typeables:
    typeables["semicolon"] = keyboard.get_typeable(char=';')


print('------------------------')
print("Keyboard Macros Start-Up")
print('------------------------')


release = Key("shift:up, ctrl:up, alt:up")



# def cancel_and_sleep(text=None, text2=None):
#     """Used to cancel an ongoing dictation and puts microphone to sleep.

#     This method notifies the user that the dictation was in fact canceled,
#      a message in the Natlink feedback window.
#     Then the the microphone is put to sleep.
#     Example:
#     "'random mumbling go to sleep'" => Microphone sleep.

#     """
#     print("* Dictation canceled. Going to sleep. *")
#     setMicState("sleeping")


# For repeating of characters.hello
specialCharMap = {
    "(bar|vertical)": "|", #bar|pipe
    "(dash|minus|hyphen)": "-",
    #"dit": ".",
    "comma": ",",
    "backslash": "\\",
    "underscore": "_",
    "asterisk": "*", #star|
    "colon": ":",
    "(semicolon|semi-colon)": ";",
    "at": "@",
    "[double] quote": '"',
    "single quote": "'",
    "hash": "#",
    "dollar": "$",
    "percent": "%",
    "ampersand": "&",
    "slash": "/",
    "equal": "=",
    "plus": "+",
    "space": " ",
    "(exclamation|bang)": "!",
    "question": "?",
    "caret": "^",
	"square bracket": "[",
	#"lend": "end",

	# "emulator back": "c-backspace",
	# "emulator home": "c-h",
	# "emulator overview": "c-o",
	
	# "Test charalcter": ",",

    # some other symbols I haven't imported yet, lazy sorry
    # 'ampersand': Key('ampersand'),
    # 'apostrophe': Key('apostrophe'),
    # 'asterisk': Key('asterisk'),
    # 'at': Key('at'),
    # 'backslash': Key('backslash'),
    # 'backtick': Key('backtick'),
    # 'bar': Key('bar'),
    # 'caret': Key('caret'),
    # 'colon': Key('colon'),
    # 'comma': Key('comma'),
    # 'dollar': Key('dollar'),
    # #'(dot|period)': Key('dot'),
    # 'double quote': Key('dquote'),
    # 'equal': Key('equal'),
    # 'bang': Key('exclamation'),
    # 'hash': Key('hash'),
    # 'hyphen': Key('hyphen'),
    # 'minus': Key('minus'),
    # 'percent': Key('percent'),
    # 'plus': Key('plus'),
    # 'question': Key('question'),
    # # Getting Invalid key name: 'semicolon'
    # #'semicolon': Key('semicolon'),
    # 'slash': Key('slash'),
    # '[single] quote': Key('squote'),
    # 'tilde': Key('tilde'),
    # 'underscore | score': Key('underscore'),
}

# Modifiers for the press-command.
modifierMap = {
    "alt": "a",
    "control": "c",
    "shift": "s",
    "super": "w",
}

# Modifiers for the press-command, if only the modifier is pressed.
singleModifierMap = {
    "alt": "alt",
    "control": "ctrl",
    "shift": "shift",
    "super": "win",
}

letterMap = {
    "(alpha|arch)": "a",
    "(bravo|brav) ": "b",
    "(charlie|turley|char) ": "c",
    "(delta|del) ": "d",
    "(echo|eck) ": "e",
    "(foxtrot|fox) ": "f",
    "(golf|gang) ": "g",
    "(hotel) ": "h",
    "(india|indigo|ish) ": "i",
    "(juliet|julia) ": "j",
    "(kilo) ": "k",
    "(lima|lion|line|lie) ": "l",
    "(mike) ": "m",
    "(november|noy) ": "n",
    "(Oscar|osh) ": "o",
    "(papa|poppa|pom|pop) ": "p",
    "(quebec|quiche|queen) ": "q",
    "(romeo|ree) ": "r",
    "(sierra|soy) ": "s",
    "(tango|tay) ": "t",
    "(uniform|umm) ": "u",
    "(victor|van) ": "v",
    "(whiskey|wes) ": "w",
    "(x-ray) ": "x",
    "(yankee|yaa) ": "y",
    "(zulu) ": "z",

}

# generate uppercase versions of every letter
upperLetterMap = {}
for letter in letterMap: #(upper|sky)
    upperLetterMap["(sky) " + letter] = letterMap[letter].upper()
letterMap.update(upperLetterMap)

numberMap = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

controlKeyMap = {
    "left": "left",
    "right": "right",
    "up": "up",
    "down": "down",
    "page up": "pgup",
    "page down": "pgdown",
    "home": "home",
    "end": "end",
    "space": "space",
    "(enter|return|slap|slop)": "enter",
    "escape": "escape",
    "(tab|stab)": "tab",
    "backspace": "backspace",
	"delete": "delete"
}

# F1 to F12. (do these actually work?)
functionKeyMap = {
    'function one': 'f1',
    'function two': 'f2',
    'function three': 'f3',
    'function four': 'f4',
    'function five': 'f5',
    'function six': 'f6',
    'function seven': 'f7',
    'function eight': 'f8',
    'function nine': 'f9',
    'function ten': 'f10',
    'function eleven': 'f11',
    'function twelve': 'f12',
}

pressKeyMap = {}
pressKeyMap.update(letterMap)
pressKeyMap.update(numberMap)
pressKeyMap.update(controlKeyMap)
pressKeyMap.update(functionKeyMap)


def handle_word(text):
    #words = map(list, text)
    #print text
    words = str(text).split()
    print 'word (', words, ')'
    if len(words) > 0:
        Text(words[0]).execute()
        if len(words) > 1:
            Mimic(' '.join(words[1:])).execute()


grammarCfg = Config("multi edit")
grammarCfg.cmd = Section("Language section")
grammarCfg.cmd.map = Item(
    {
        # Navigation keys.
        "up [<n>]": Key("up:%(n)d"),
        "down [<n>]": Key("down:%(n)d"),
        "left [<n>]": Key("left:%(n)d"),
        "right [<n>]": Key("right:%(n)d"),
        "page up [<n>]": Key("pgup:%(n)d"),
        "page down [<n>]": Key("pgdown:%(n)d"),
        #"up <n> (page|pages)": Key("pgup:%(n)d"),
        #"down <n> (page|pages)": Key("pgdown:%(n)d"),
        #"left <n> (word|words)": Key("c-left/3:%(n)d/10"),
        #"right <n> (word|words)": Key("c-right/3:%(n)d/10"),

		# Android emulator, couldn't get own file working
		"emulator back":			Key("c-backspace"),
		"emulator home":			Key("c-h"),
		"emulator overview":		Key("c-o"),
		"emulator left":			Key("c-left"),
		"emulator right":			Key("c-right"),

		"browser address": Key("a-d"),		

        "home": Key("home"),
        "(end|bend|lend|dole)": Key("end"),
        "doc home": Key("c-home/3"),
        "doc end": Key("c-end/3"),
        # Functional keys.
        "space": release + Key("space"),
        "space [<n>]": release + Key("space:%(n)d"),
        "(enter|slap|slop) [<n>]": release + Key("enter:%(n)d"),
        "tab [<n>]": Key("tab:%(n)d"),
		"delete [<n>]":	Key("delete:%(n)d"),
        "delete line": Key("s-delete"),
        #"delete [this] line": Key("home, s-end, del"),  # @IgnorePep8
        "backspace [<n>]": release + Key("backspace:%(n)d"),
        "application key": release + Key("apps/3"),
        "win key": release + Key("win/3"),
        #"paste [that]": Function(paste_command),
        #"copy [that]": Function(copy_command),
        "cut [that]": release + Key("c-x/3"),
        "select all": release + Key("c-a/3"),
        "[(hold|press)] alt": Key("alt:down/3"),
        "release alt": Key("alt:up"),
        "[(hold|press)] shift": Key("shift:down/3"),
        "release shift": Key("shift:up"),
        "[(hold|press)] control": Key("ctrl:down/3"),
        "release control": Key("ctrl:up"),
        "release [all]": release,
        "press key <pressKey>": Key("%(pressKey)s"),
        # Closures.
        "angle brackets": Key("langle, rangle, left/3"),
        "[square] brackets": Key("lbracket, rbracket, left/3"),
        "[curly] braces": Key("lbrace, rbrace, left/3"),
        "(parens|parentheses)": Key("lparen, rparen, left/3"),
        "quotes": Key("dquote/3, dquote/3, left/3"),
        "backticks": Key("backtick:2, left"),
        "single quotes": Key("squote, squote, left/3"),
        # Shorthand multiple characters.
        "double <char>": Text("%(char)s%(char)s"),
        "triple <char>": Text("%(char)s%(char)s%(char)s"),
        #ESCAPE
		"escape": Key("escape"),
		"double escape": Key("escape, escape"),  # Exiting menus.
        # Punctuation and separation characters, for quick editing.
        "colon [<n>]": Key("colon/2:%(n)d"),
        "semi-colon [<n>]": Key("semicolon/2:%(n)d"),
        "comma [<n>]": Key("comma/2:%(n)d"),
        "(dot|period|dit|point)": Key("dot"),  # cannot be followed by a repeat count
        "(dash|hyphen|minus) [<n>]": Key("hyphen/2:%(n)d"),
        "underscore [<n>]": Key("underscore/2:%(n)d"),
        "<letters>": Text("%(letters)s"),
        "<char>": Text("%(char)s"),

        'langle [<n>]': Key('langle:%(n)d'),
        'lace [<n>]':   Key('lbrace:%(n)d'),
        '(lack|lair) [<n>]':   Key('lbracket:%(n)d'),
        #'(laip|len) [<n>]':   Key('lparen:%(n)d'),
        'len [<n>]':    Key('lparen:%(n)d'),
        'rangle [<n>]': Key('rangle:%(n)d'),
        'race [<n>]':   Key('rbrace:%(n)d'),
        '(rack|rare) [<n>]':   Key('rbracket:%(n)d'),
        #'(raip|ren|wren) [<n>]':   Key('rparen:%(n)d'),
        '(ren|wren) [<n>]':   Key('rparen:%(n)d'),

        "act [<n>]": Key("escape:%(n)d"),
        "calm [<n>]": Key("comma:%(n)d"),
        #'into': Key('space,bar,space'),
        'care':        Key('home'),
        '(dole|doll)': Key('end'), #doll|
        'chuck [<n>]':       Key('del:%(n)d'),
        'scratch [<n>]':     Key('backspace:%(n)d'),
        "visual": Key("v"),
        "visual line": Key("s-v"),
        "visual block": Key("c-v"),
        "doc save": Key("c-s"),


        'gope [<n>]':  Key('pgup:%(n)d'),
        #'drop [<n>]':  Key('pgdown:%(n)d'),

        'lope [<n>]':  Key('c-left:%(n)d'),
        '(yope|rope) [<n>]':  Key('c-right:%(n)d'),
        '(hill scratch|hatch) [<n>]': Key('c-backspace:%(n)d'),

        'hexadecimal': Text("0x"),
        'suspend': Key('c-z'),

        'word <text>': Function(handle_word),
        'number <num>': Text("%(num)d"),
        'change <text> to <text2>': Key("home, slash") + Text("%(text)s") + Key("enter, c, e") + Text("%(text2)s") + Key("escape"),

        # Text corrections.
        "(add|fix) missing space": Key("c-left/3, space, c-right/3"),
        "(delete|remove) (double|extra) (space|whitespace)": Key("c-left/3, backspace, c-right/3"),  # @IgnorePep8
        "(delete|remove) (double|extra) (type|char|character)": Key("c-left/3, del, c-right/3"),  # @IgnorePep8
        # Microphone sleep/cancel started dictation.
        # "[<text>] (go to sleep|cancel and sleep) [<text2>]": Function(cancel_and_sleep),  # @IgnorePep8
    },
    namespace={
        "Key": Key,
        "Text": Text,
    }
)


class KeystrokeRule(MappingRule):
    exported = False
    mapping = grammarCfg.cmd.map
    extras = [
        IntegerRef("n", 1, 100),
        IntegerRef("num", 0, 1000000),
        Dictation("text"),
        Dictation("text2"),
        Choice("char", specialCharMap),
        Choice("letters", letterMap),
        Choice("modifier1", modifierMap),
        Choice("modifier2", modifierMap),
        Choice("modifierSingle", singleModifierMap),
        Choice("pressKey", pressKeyMap),
    ]
    defaults = {
        "n": 1,
    }
