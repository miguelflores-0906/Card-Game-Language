grammar Card;

start_: program EOF;

// Outline/Blocks
program: setup_block round_block;
setup_block: setup_content+;
setup_content: setup_stmt | function_block | enum_block | obj_defn;
function_block: function_header OPEN_CB func_code_block CLOSE_CB;
function_header: FUNC IDENTIFIER OPEN_PAR formal_params? CLOSE_PAR |
    FUNC DISPBRD OPEN_PAR CLOSE_PAR;
formal_params: DATA_TYPE IDENTIFIER (COMMA DATA_TYPE IDENTIFIER)*;
enum_block: enum_header OPEN_CB enum_body CLOSE_CB;
enum_header: ENUM IDENTIFIER;
enum_body: IDENTIFIER (COMMA IDENTIFIER)*;
obj_defn: DATA_TYPE DOT_OP IDENTIFIER assign_body SEMICOLON;
round_block: ROUND OPEN_CB round_code_block CLOSE_CB;

setup_code_block: setup_stmt+;
func_code_block: func_stmt+;
func_loop_code_block: func_loop_stmt+;
round_code_block: round_stmt+;
round_loop_code_block: round_loop_stmt+;
loop_code_block: loop_stmt+;

// Statements
statement: declare_stmt  | assignee assign_body SEMICOLON |
    expression SEMICOLON | deal_stmt | draw_stmt | move_stmt | 
    play_stmt | shuffle_stmt | peek_stmt | print_stmt;

setup_stmt: statement | if_stmt | foreach_stmt | repeat_stmt;
func_stmt: statement | func_if_stmt | func_foreach_stmt | func_repeat_stmt | return_stmt;
func_loop_stmt: statement | func_loop_if_stmt | func_foreach_stmt | func_repeat_stmt | 
    return_stmt | break_stmt | continue_stmt;
round_stmt: statement | round_if_stmt | round_foreach_stmt | round_repeat_stmt | end_stmt;
round_loop_stmt: statement | round_loop_if_stmt | round_foreach_stmt | round_repeat_stmt | 
    end_stmt | break_stmt | continue_stmt;
loop_stmt: statement | loop_if_stmt | foreach_stmt | repeat_stmt | break_stmt | continue_stmt;

declare_stmt: DATA_TYPE declare_body SEMICOLON;
declare_body: declare_content (COMMA declare_content)*;
declare_content: IDENTIFIER | IDENTIFIER OPEN_SB expression CLOSE_SB | 
    IDENTIFIER assign_body | IDENTIFIER OPEN_SB expression CLOSE_SB assign_body;
assign_body: ASSIGN_OP expression | ASSIGN_OP OPEN_CB array_body CLOSE_CB |
    ASSIGN_OP OPEN_CB object_body CLOSE_CB | ASSIGN_OP COMBI OPEN_CB object_body CLOSE_CB |
    ASSIGN_OP NEW DATA_TYPE;
assignee: IDENTIFIER | assignee OPEN_SB expression CLOSE_SB | assignee DOT_OP IDENTIFIER;
entity: IDENTIFIER | entity OPEN_SB expression CLOSE_SB | entity DOT_OP IDENTIFIER |
    function_call | OPEN_PAR entity CLOSE_PAR;
array_body: expression (COMMA expression)*;
object_body: object_content (COMMA object_content)*;
object_content: IDENTIFIER COLON expression | IDENTIFIER COLON OPEN_CB array_body CLOSE_CB | 
    IDENTIFIER COLON OPEN_CB object_body CLOSE_CB;
expression: entity | INT | STRING | NULL | OPEN_PAR expression CLOSE_PAR | NOT_OP expression |
    expression operator1 expression | expression operator2 expression | 
    expression operator3 expression | expression operator4 expression | 
    expression AND_OP expression | expression OR_OP expression | pick_expr |
    getint_expr | getstr_expr | action_stack_expr;
operator1: MULT_OP | DIV_OP | MOD_OP;
operator2: ADD_OP | SUB_OP;
operator3: GT_OP | LT_OP | GEQ_OP | LEQ_OP;
operator4: EQ_OP | NEQ_OP;

// Control Sequences
if_stmt: if_header block_stmt (ELSE block_stmt)?;
if_header: IF OPEN_PAR expression CLOSE_PAR;
foreach_stmt: foreach_header loop_block_stmt;
foreach_header: FOREACH OPEN_PAR IDENTIFIER COLON entity CLOSE_PAR;
repeat_stmt: repeat_header loop_block_stmt;
repeat_header: REPEAT UNTIL? expression;

loop_if_stmt: if_header loop_block_stmt (ELSE loop_block_stmt)?;

func_if_stmt: if_header func_block_stmt (ELSE func_block_stmt)?;
func_foreach_stmt: foreach_header func_loop_block_stmt;
func_repeat_stmt: repeat_header func_loop_block_stmt;
func_loop_if_stmt: if_header func_loop_block_stmt (ELSE func_loop_block_stmt)?;

round_if_stmt: if_header round_block_stmt (ELSE round_block_stmt)?;
round_foreach_stmt: foreach_header round_loop_block_stmt;
round_repeat_stmt: repeat_header round_loop_block_stmt;
round_loop_if_stmt: if_header round_loop_block_stmt (ELSE round_loop_block_stmt)?;

block_stmt: OPEN_CB setup_code_block CLOSE_CB | statement;
func_block_stmt: OPEN_CB func_code_block CLOSE_CB | func_stmt;
func_loop_block_stmt: OPEN_CB func_loop_code_block CLOSE_CB | func_loop_stmt;
round_block_stmt: OPEN_CB round_code_block CLOSE_CB | round_stmt;
round_loop_block_stmt: OPEN_CB round_loop_code_block CLOSE_CB | round_loop_stmt;
loop_block_stmt: OPEN_CB loop_code_block CLOSE_CB | loop_stmt;

break_stmt: BREAK SEMICOLON;
continue_stmt: CONTINUE SEMICOLON;
return_stmt: RETURN SEMICOLON | RETURN expression SEMICOLON;
end_stmt: END SEMICOLON;
function_call: DISPBRD OPEN_PAR CLOSE_PAR | IDENTIFIER OPEN_PAR actual_params? CLOSE_PAR;
actual_params: expression (COMMA expression)*;

// I/O
pick_expr: PICK FROM entity;
getint_expr: GETINT;
getstr_expr: GETSTR;
print_stmt: PRINT OPEN_PAR expression CLOSE_PAR SEMICOLON | 
    PRINTLN OPEN_PAR expression CLOSE_PAR SEMICOLON;

// Special Statements
deal_stmt: DEAL expression FROM entity TO entity SEMICOLON;
draw_stmt: entity DRAW (UNTIL? expression)? FROM entity SEMICOLON;
move_stmt: MOVE entity FROM entity TO entity SEMICOLON;
play_stmt: entity PLAY entity TO entity SEMICOLON;
shuffle_stmt: SHUFFLE entity SEMICOLON;
peek_stmt: PEEK expression FROM entity SEMICOLON;
action_stack_expr: ACTION_STACK DOT_OP IDENTIFIER OPEN_PAR expression? CLOSE_PAR;

// Special Characters
OPEN_CB : '{';
CLOSE_CB : '}';
OPEN_PAR : '(' ;
CLOSE_PAR : ')' ;
OPEN_SB: '[';
CLOSE_SB: ']';
SEMICOLON : ';';
COLON : ':';
COMMA: ',';

// Types, Objects, and Literals
DATA_TYPE : 'int' | 'string' | 'Card' | 'Player' | 'Pile' | 'Action';
INT : '-'?[0-9]+;
STRING : '"' (~["])+ '"';
ACTION_STACK: 'ActionStack';
NULL: 'null';

// Operators
ADD_OP: '+';
SUB_OP: '-';
MULT_OP: '*';
DIV_OP: '/';
MOD_OP: '%';
EQ_OP: '==';
NEQ_OP: '!=';
GEQ_OP: '>=';
GT_OP: '>';
LEQ_OP: '<=';
LT_OP: '<';
AND_OP: 'and';
OR_OP: 'or';
NOT_OP: 'not';
ASSIGN_OP: '=';
DOT_OP: '.';

//game
IF : 'if';
ELSE : 'else';
FOREACH : 'foreach';
REPEAT : 'repeat';
UNTIL : 'until';
BREAK: 'break';
CONTINUE: 'continue';
NEW: 'new';
FUNC: 'function';
RETURN: 'return';
ENUM: 'enum';
COMBI : 'Combination';
ROUND : 'Round';
END : 'End';
DISPBRD : 'DisplayBoard';

//I-O
PICK : 'Pick';
GETINT : 'GetInt';
GETSTR: 'GetString';
PRINT: 'Print';
PRINTLN : 'Println';

//targets
TO : 'To';
FROM: 'From';

//card actions
DEAL : 'Deal';
DRAW : 'Draw';
MOVE : 'Move';
PLAY : 'Play';
SHUFFLE : 'Shuffle';
PEEK : 'Peek';

//identifier
IDENTIFIER : [_a-zA-Z][_0-9a-zA-Z]*;

// comment
COMMENT: '//' ~[\n\r]* -> skip ;

WS : [ \t\n\r]+ -> skip ;