# tkGameOfLife
A tkInter interactive and customizable implementation of the Conway's game of life

This is an old school project of mine:
Functionalities:
 - Above the hyphen is the settings field, where you can set the size of the simulation field, the size of the cells and the rules for the simulation:
	-the original set of rules is the (2,3/3) set of rules.
	-recommended for trying out are (1,2,3,4,5/3) and (1,3,5,7/1,3,5,7), as they do funny stuff
	(more infos about the rulebooks and other interesting rulebooks: [wikipedia](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life))
-by clicking on the "Create New Simulation"-button, a field with the
 with the set properties, consisting of black pixels, is created;
-Click on the pixels of the field to turn them on or off.
The rest of the functions are self-explanatory.

Hints:
-the simulation does not work beyond the edge of the field,
 for an unaltered result, a larger window must also be created for a larger simulation
-before you start to draw a figure from pixels, you should pause a running simulation

Recommended setting:
-in(2,3/3), field(100x100), approx. in the middle, delay(20ms):
 000
 0.0
 0.0
 ...
 ...
 0.0
 0.0
 000

(0 for on;.for off)
...I personally think this is very nice...
Wikipedia knows other nice start combinations, too.
