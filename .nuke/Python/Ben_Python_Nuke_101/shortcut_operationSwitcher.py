#----------------------------------------------------------------------------
# shortcut_operationSwitcher.py
# Version: 1.0.0
# Author: Frank Shao
#
# Last Modified by: Frank Shao
# Last Updated: Aug. 17, 2020
#----------------------------------------------------------------------------

#----------------------------------------------------------------------------
# Usage:
# 
# Ctrl + Shift + S toggles between over/under, mask/stencil, plus/from, etc.
#----------------------------------------------------------------------------

import nuke

# Define function.
def shortcut_operationSwitcher():

	# Create variable for easier access to nuke.selectedNode()
	node = nuke.selectedNode()

	# Create Dictionary with keys & values being the opposite operations.
	merge_ops = {'over':'under', 'mask':'stencil', 'plus':'from', 'multiply':'divide', 'max':'min', 'conjoint-over':'disjoint-over'}

	# Check if the selected node is a Merge node.
	if node.Class() == 'Merge2':

		# Set a variable that holds the current value of the 'operation' knob.
		current_op = node['operation'].value()

		# Search for the current value of the 'operation' knob in our dictionary's keys.
		if current_op in merge_ops.keys():

			# If a match is found, (e.g. the current operation is 'mask', and there is a key in our dictionary called 'mask'),
			# get the value of the matching key from our dictionary (stencil, in this e.g.), and set the operation knob of our selected node
			# to said value.
			node['operation'].setValue(merge_ops[node['operation'].value()])

		# However, if no match is found, do the same thing but search the keys in the dictionary & set the matching value instead.
		elif current_op in merge_ops.values():

			node['operation'].setValue(merge_ops.keys()[merge_ops.values().index(current_op)])


# Add menu item.
nuke.menu('Nuke').addCommand('Edit/Shortcuts/Toggle Operation to Opposite', 'shortcut_operationSwitcher.shortcut_operationSwitcher()', 'ctrl+shift+s')