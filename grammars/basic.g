// Basic IF grammar


start: instruction

instruction: SIMPLE_MOVEMENT                -> simple_movement
           | MANIPULATE OBJECT              -> manipulate
           | EXAMINE _PREPOSITION? OBJECT   -> examine
           | options
           | help

options: ("options" | "option" | "!") option?
option: OPTION VALUE?
help: ("help" | "?") TOPIC?

SIMPLE_MOVEMENT: "n" | "s" | "e" | "w" | "u" | "d"
EXAMINE: "look" | "l"

MANIPULATE: TRAVERSE | COLLECT | USE
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
