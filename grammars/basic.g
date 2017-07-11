// Basic IF grammar


start: instruction

instruction: simple_movement
           | examine
           | manipulate
           | options
           | help

options: ("options" | "option" | "!") option?
option: OPTION VALUE?
help: ("help" | "?") TOPIC?

simple_movement: NORTH
               | SOUTH
               | EAST
               | WEST
               | UP
               | DOWN
NORTH: "n" | "go n" | "north" | "go north"
SOUTH: "s" | "go s" | "south" | "go south"
EAST: "e" | "go e" | "east" | "go east"
WEST: "w" | "go w" | "west" | "go west"
UP: "u" | "go u" | "up" | "go up"
DOWN: "d" | "go d" | "down" | "go down"

examine: LOOK (_PREPOSITION? OBJECT)?
manipulate: (TRAVERSE | COLLECT | USE) OBJECT

LOOK: "look" | "l"
TRAVERSE: "enter" | "leave"
COLLECT: "get" | "drop"
USE: "open" | "close" | "use" | "press" | "flip"

OBJECT: TOKEN
LOCATION: TOKEN
OPTION: TOKEN
VALUE: TOKEN
TOPIC: TOKEN
_PREPOSITION: "at" | "in" | "on" | "with" | "into" | "from" | "under"
            | "above" | "below" | "onto" | "across" | "off"
            | "toward" | "inside" | "outside" | "over"
            | "around" | "behind" | "for"

TOKEN: (LETTER | INT | "_" | "-" | "#" | "@" | "$")+

%import common.LETTER
%import common.INT
%import common.WS
%ignore WS
