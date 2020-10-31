from dragonfly import (Grammar, AppContext, MappingRule, Dictation,
					   Key, Text, Pause)
import studio64

#---------------------------------------------------------------------------
# Create this module's grammar and the context under which it'll be active.

grammar_context = AppContext(executable="idea64")
grammar = Grammar("Idea", context=grammar_context)

print('------------------------')
print("Idea Macros Start-Up")
print('------------------------')

idea_rule = MappingRule(
	name="Idea rule",
	mapping=studio64.studio_rule._mapping,
	extras=[           # Special elements in the specs of the mapping.
			Dictation("text"),
		   ],
)

# Add the action rule to the grammar instance.
grammar.add_rule(idea_rule)

#---------------------------------------------------------------------------
# Load the grammar instance and define how to unload it.

grammar.load()

# Unload function which will be called by natlink at unload time.
def unload():
	global grammar
	if grammar: grammar.unload()
	grammar = None