#
# This file is part of Dragonfly.
# (c) Copyright 2007, 2008 by Christo Butcher
# Licensed under the LGPL.
#
#   Dragonfly is free software: you can redistribute it and/or modify it 
#   under the terms of the GNU Lesser General Public License as published 
#   by the Free Software Foundation, either version 3 of the License, or 
#   (at your option) any later version.
#
#   Dragonfly is distributed in the hope that it will be useful, but 
#   WITHOUT ANY WARRANTY; without even the implied warranty of 
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU 
#   Lesser General Public License for more details.
#
#   You should have received a copy of the GNU Lesser General Public 
#   License along with Dragonfly.  If not, see 
#   <http://www.gnu.org/licenses/>.
#

"""
    This module is a simple example of Dragonfly use.

    It shows how to use Dragonfly's Grammar, AppContext, and MappingRule
    classes.  This module can be activated in the same way as other
    Natlink macros by placing it in the "My Documents\Natlink folder" or
    "Program Files\NetLink/MacroSystem".

"""

# Changed Name of Intellij IDEA to "Kotlin" For easy start
print("Kotlin grammar file")
print("-------------------")

from dragonfly import (Grammar, AppContext, MappingRule, Dictation,
                       Key, Text, Pause)


#---------------------------------------------------------------------------
# Create this module's grammar and the context under which it'll be active.

grammar_context = AppContext(executable="code")
grammar = Grammar("vscode_example", context=grammar_context)


#---------------------------------------------------------------------------
# Create a mapping rule which maps things you can say to actions.
#
# Note the relationship between the *mapping* and *extras* keyword
#  arguments.  The extras is a list of Dragonfly elements which are
#  available to be used in the specs of the mapping.  In this example
#  the Dictation("text")* extra makes it possible to use "<text>"
#  within a mapping spec and "%(text)s" within the associated action.

code_rule = MappingRule(
    name="example",    # The name of the rule.
    mapping={          # The mapping dict: spec -> action.
             "save [file]":            Key("c-s"),
             "save [file] as":         Key("a-f, a"),
             "save [file] as <text>":  Key("a-f, a/20") + Text("%(text)s"),
             "find <text>":            Key("c-f/20") + Text("%(text)s\n"),
             "define function <text>":  Text("def ") + Text("%(text)s") + Text("():\n"),
             
             
             "to string":               Text("str") + Key("("),
             "to integer":              Text("int") + Key("("),
            
            "switch to next tab":       Key("c-pgdown"),
            "switch to previous tab":   Key("c-pgup"),
            "close tab | file":         Key("c-f4"),

            "debug run":                Key("f5"),
            "debug stop":                Key("s-f5"),
            "breakpoint":               Key("f9"),
            "show shortcuts":           Key("c-k, c-s"),
            "line <text>":              Key("c-g") + Text("%(text)s") + Pause("20") + Key("enter"),
            "run this line": Key("csa-l"),
            "comment": Key("c-slash"),
            },
    extras=[           # Special elements in the specs of the mapping.
            Dictation("text"),
           ],
    )

# Add the action rule to the grammar instance.
grammar.add_rule(code_rule)


#---------------------------------------------------------------------------
# Load the grammar instance and define how to unload it.

grammar.load()

# Unload function which will be called by natlink at unload time.
def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None


#             "equals":                  Text("= "),
#             "plus equals":             Text("+= "),
#            "double equals":             Text("== "),
