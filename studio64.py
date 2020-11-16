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

from dragonfly import (Grammar, AppContext, MappingRule, Dictation,
					   Key, Text, Pause)


#---------------------------------------------------------------------------
# Create this module's grammar and the context under which it'll be active.

grammar_context = AppContext(executable="studio64")
grammar = Grammar("Android studio", context=grammar_context)

print('--------------------------------')
print("Android Studio Macros Start-Up")
print('--------------------------------')


#---------------------------------------------------------------------------
# Create a mapping rule which maps things you can say to actions.
#
# Note the relationship between the *mapping* and *extras* keyword
#  arguments.  The extras is a list of Dragonfly elements which are
#  available to be used in the specs of the mapping.  In this example
#  the Dictation("text")* extra makes it possible to use "<text>"
#  within a mapping spec and "%(text)s" within the associated action.

studio_rule = MappingRule(
	name="Android studio rule",    # The name of the rule.
	mapping={          # The mapping dict: spec -> action.
			# syntax for multiple keypress: "tab [<n>]": Key("tab:%(n)d"),
			"android settings":			Key("ca-s"),
			"android info":				Key("a-enter"),
			"android search":			Key("cs-a"),
			"view right":				Key("as-right"),
			"view left":				Key("as-left"),

			"android run":				Key("as-f10"),
			"android apply":			Key("c-f10"),
			"android debug":			Key("as-f9"),
			"android resume":			Key("f9"),
			"android stop":				Key("c-f2"),
			"android evaluate":			Key("a-f8"),

			"step into":				Key("f7"),
			"step over":				Key("f8"),
			"step cursor":				Key("a-f9"),
			"breakpoint toggle":		Key("c-f8"),
			"android watch":			Key("a-["),
			"warning next":				Key("f2"),
			"warning previous":			Key("s-f2"),

			# testing the line for n
			#"go delete [<n>]":				Key("delete:%(n)d"),

			"log delta":				Text('Log.d(TAG, "")') + Key("left:2"),
			"log echo":					Text('Log.e(TAG, "")') + Key("left:2"),
			"toast":					Text('Toast.makeText(activity, "", Toast.LENGTH_LONG).show()') + Key("left:28"),
			"tag declare":				Text('private const val TAG = ""') + Key("left:1"),

			"line delete":				Key("s-delete"),
			"line duplicate":			Key("c-d"),

			"menu file":				Key("a-f"),
			"menu edit":				Key("a-e"),
			"menu view":				Key("a-v"),
			"menu navigate":			Key("a-n"),
			"menu code":				Key("a-c"),
			"menu analyze":				Key("a-z"),
			"menu refactor":			Key("a-r"),
			"menu build":				Key("a-b"),
			"menu run":					Key("a-u"),
			"menu tools":				Key("a-t"),
			"menu VCS":					Key("a-s"),
			"menu window":				Key("a-w"),
			"menu help":				Key("a-h"),

			"panel project":			Key("a-1"),
			"panel favorites":			Key("a-2"),
			"panel find":				Key("a-3"),
			"panel run":				Key("a-4"),
			"panel logcat":				Key("a-6"),
			"panel structure":			Key("a-7"),
			"panel terminal":			Key("a-f12"),
			
			"code left":				Key("a-left"),
			"code right":				Key("a-right"),
			# "code left [<n>]": 		Key("a-left:%(n)d"),
			# "code right [<n>]": 		Key("a-right:%(n)d"),
			"code close":				Key("c-f4"),
			# "code others":				Key(""),
			"code reformat":			Key("ca-l"),
			"block up":					Key("a-up"),
			"block down":				Key("a-down"),
			"brace jump":				Key("cs-m"),
			"comment line":				Key("c-slash"),
			"comment block":			Key("cs-slash"),
			"android select":			Key("c-w"),
			"refactor rename":			Key("s-f6"),
			"refactor options":			Key("csa-t"),
			
			
			"android override":			Key("c-o"),
			"android implement":		Key("c-i"),
			"android generate":			Key("a-insert"),
			"android construct":		Key("cs-enter"),
			"android members":			Key("c-f12"),
			"android block":			Key("ca-t"),
			"android undo":				Key("c-z"),
			"android redo":				Key("cs-z"),

			"android hierarchy":		Key("c-h"),
			"android usages":			Key("c-b"),
			
			"android help":				Key("c-q"),			

			#"design right":				Key("as-right"),
			"XML view":					Key("c-b"),

			"arrow": 					Text("->"),
			"elvis": 					Text("?:"),

			"difference right":			Key("as-right"),
			"difference left":			Key("as-left"),	
			"difference next":			Key("f7"),
			"difference previous":		Key("s-f7"),
			
			
			#  "save [file]":            Key("c-s"),
			#  "save [file] as":         Key("a-f, a"),
			#  "save [file] as <text>":  Key("a-f, a/20") + Text("%(text)s"),
			#  "find <text>":            Key("c-f/20") + Text("%(text)s\n"),
			#  "define function <text>":  Text("def ") + Text("%(text)s") + Text("():\n"),
			 
			 
			#  "to string":               Text("str") + Key("("),
			#  "to integer":              Text("int") + Key("("),
			
			# "switch to next tab":       Key("c-pgdown"),
			# "switch to previous tab":   Key("c-pgup"),
			# "close tab | file":         Key("c-f4"),

			# "debug run":                Key("f5"),
			# "debug stop":                Key("s-f5"),
			# "breakpoint":               Key("f9"),
			# "show shortcuts":           Key("c-k, c-s"),
			# "line <text>":              Key("c-g") + Text("%(text)s") + Pause("20") + Key("enter"),
			# "run this line": Key("csa-l"),
			# "comment": Key("c-slash"),
			},
	extras=[           # Special elements in the specs of the mapping.
			Dictation("text"),
		   ],
	)

# Add the action rule to the grammar instance.
grammar.add_rule(studio_rule)


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
