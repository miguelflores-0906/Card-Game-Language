# Generated from Card.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CardParser import CardParser
else:
    from CardParser import CardParser
from os import system
import utils
# global stuff
symbol_table = {}
nested_func_cnt = -1
nested_control_cnt = -1
func_table_list = []
func_control_list = []
func_nested_control_cnt = []
control_variables = []
parameters = []

# This class defines a complete generic visitor for a parse tree produced by CardParser.

class CardVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CardParser#start_.
    def visitStart_(self, ctx:CardParser.Start_Context):
        self.visit(ctx.getChild(0))


    # Visit a parse tree produced by CardParser#program.
    def visitProgram(self, ctx:CardParser.ProgramContext):
        self.visit(ctx.getChild(0))
        self.visit(ctx.getChild(1))


    # Visit a parse tree produced by CardParser#setup_block.
    def visitSetup_block(self, ctx:CardParser.Setup_blockContext):
        for i in range(ctx.getChildCount()):
            self.visit(ctx.getChild(i))


    # Visit a parse tree produced by CardParser#setup_content.
    def visitSetup_content(self, ctx:CardParser.Setup_contentContext):
        self.visit(ctx.getChild(0))


    # Visit a parse tree produced by CardParser#function_block.
    def visitFunction_block(self, ctx:CardParser.Function_blockContext):
        identifier = self.visitFunction_header(ctx.getChild(0), ctx)
        if nested_func_cnt == -1: return

        if identifier == 'DisplayBoard': system('cls')
        check = self.visit(ctx.getChild(2))
        if check is not None: return check[1]


    # Visit a parse tree produced by CardParser#function_header.
    def visitFunction_header(self, ctx:CardParser.Function_headerContext, parent=None):
        global parameters
        if nested_func_cnt == -1:
            identifier = ctx.getChild(1).getText()
            try: self.declareIdentifier(identifier, CardParser.Function_blockContext, parent)
            except Exception as e: self.raiseError(ctx, type(e), str(e))
            # check parameters
            if ctx.getChildCount() == 5: self.visit(ctx.getChild(3))
            return
        
        if ctx.getChildCount() == 4:
            if len(parameters) != 0:
                self.raiseError(ctx, ValueError, f'Expected 0 arguments, got {len(parameters)}')
            return ctx.getChild(1).getText()
        self.visit(ctx.getChild(3))
        parameters = []

    # Visit a parse tree produced by CardParser#formal_params.
    def visitFormal_params(self, ctx:CardParser.Formal_paramsContext):
        formal_params = []
        param_names = []
        for i in range(0, ctx.getChildCount(), 3):
            data_type = ctx.getChild(i).getText()
            identifier = ctx.getChild(i + 1).getText()

            if data_type == 'int': data_type = int
            elif data_type == 'string': data_type = str
            elif data_type == 'Card': data_type = utils.Card
            elif data_type == 'Pile': data_type = utils.Pile
            elif data_type == 'Player': data_type = utils.Player
            elif data_type == 'Action': data_type = utils.Action

            formal_params.append((data_type, identifier))
            param_names.append(identifier)

        if nested_func_cnt == -1:
            if len(param_names) != len(set(param_names)):
                self.raiseError(ctx, NameError, 'Function parameters cannot have the same name')
            return
        if len(parameters) != len(formal_params):
            self.raiseError(ctx, ValueError, f'Expected {len(formal_params)} arguments, got {len(parameters)}')
        for (data_type, identifier), value in zip(formal_params, parameters):
            if value is None:
                if data_type in [utils.Card, utils.Pile, utils.Player, utils.Action]:
                    try: self.declareIdentifier(identifier, data_type, value)
                    except Exception as e: self.raiseError(ctx, type(e), str(e))
                else:
                    self.raiseError(ctx, TypeError, f'Incompatible type, expected {data_type.__name__} for parameter {identifier}')
            else:
                if not isinstance(value, data_type):
                    self.raiseError(ctx, TypeError, f'Incompatible type, expected {data_type.__name__} for parameter {identifier}')
                else:
                    try: self.declareIdentifier(identifier, data_type, value)
                    except Exception as e: self.raiseError(ctx, type(e), str(e))


    # Visit a parse tree produced by CardParser#enum_block.
    def visitEnum_block(self, ctx:CardParser.Enum_blockContext):
        identifier = self.visit(ctx.getChild(0))
        enum = self.visit(ctx.getChild(2))
        try: self.declareIdentifier(identifier, utils.Enum, enum)
        except Exception as e: self.raiseError(ctx, type(e), str(e))


    # Visit a parse tree produced by CardParser#enum_header.
    def visitEnum_header(self, ctx:CardParser.Enum_headerContext):
        return ctx.getChild(1).getText()


    # Visit a parse tree produced by CardParser#enum_body.
    def visitEnum_body(self, ctx:CardParser.Enum_bodyContext):
        enum = {}
        labels = []
        for i in range(0, ctx.getChildCount(), 2):
            labels.append(ctx.getChild(i).getText())
        if len(set(labels)) != len(labels):
            self.raiseError(ctx, KeyError, 'Duplicate names found in enum')
        for value in labels:
            enum[value] = value
        return utils.Enum(enum)


    # Visit a parse tree produced by CardParser#obj_defn.
    def visitObj_defn(self, ctx:CardParser.Obj_defnContext):
        data_type = ctx.getChild(0).getText()
        if data_type == 'int' or data_type == 'string':
            self.raiseError(ctx, TypeError, f'Cannot add attributes to {data_type}')
        identifier = ctx.getChild(2).getText()
        value = self.visit(ctx.getChild(3))

        try:
            if data_type == 'Card':
                utils.addCardAttrib(identifier, value)
            elif data_type == 'Pile':
                utils.addPileAttrib(identifier, value)
            elif data_type == 'Player':
                utils.addPlayerAttrib(identifier, value)
            elif data_type == 'Action':
                utils.addActionAttrib(identifier, value)
            else: assert False
        except Exception as e:
            if str(e)[:13] == 'Error on line':
                raise e
            self.raiseError(ctx, type(e), str(e))


    # Visit a parse tree produced by CardParser#round_block.
    def visitRound_block(self, ctx:CardParser.Round_blockContext):
        # idea is to add nested_func_cnt for this
        # treat each iteration as a function
        global nested_func_cnt
        nested_func_cnt += 1
        func_table_list.append({})
        func_control_list.append([])
        func_nested_control_cnt.append(-1)

        while True:
            assert nested_func_cnt == 0
            func_table_list[nested_func_cnt] = {}

            check = self.visit(ctx.getChild(2))
            if check is None: continue
            if not isinstance(check, tuple): continue
            assert check[0] == 'End'
            func_nested_control_cnt.pop()
            func_control_list.pop()
            func_table_list.pop()
            nested_func_cnt -= 1
            break


    # Visit a parse tree produced by CardParser#setup_code_block.
    def visitSetup_code_block(self, ctx:CardParser.Setup_code_blockContext):
        for i in range(ctx.getChildCount()):
            self.visit(ctx.getChild(i))


    # Visit a parse tree produced by CardParser#func_code_block.
    def visitFunc_code_block(self, ctx:CardParser.Func_code_blockContext):
        for i in range(ctx.getChildCount()):
            check = self.visit(ctx.getChild(i))
            if check is None: continue
            if not isinstance(check, tuple): continue
            assert check[0] == 'return'
            return check


    # Visit a parse tree produced by CardParser#func_loop_code_block.
    def visitFunc_loop_code_block(self, ctx:CardParser.Func_loop_code_blockContext):
        for i in range(ctx.getChildCount()):
            check = self.visit(ctx.getChild(i))
            if check is None: continue
            if not isinstance(check, tuple): continue
            assert check[0] in ['return', 'break', 'continue']
            return check


    # Visit a parse tree produced by CardParser#round_code_block.
    def visitRound_code_block(self, ctx:CardParser.Round_code_blockContext):
        for i in range(ctx.getChildCount()):
            check = self.visit(ctx.getChild(i))
            if check is None: continue
            if not isinstance(check, tuple): continue
            assert check[0] == 'End'
            return check


    # Visit a parse tree produced by CardParser#round_loop_code_block.
    def visitRound_loop_code_block(self, ctx:CardParser.Round_loop_code_blockContext):
        for i in range(ctx.getChildCount()):
            check = self.visit(ctx.getChild(i))
            if check is None: continue
            if not isinstance(check, tuple): continue
            assert check[0] in ['End', 'break', 'continue']
            return check


    # Visit a parse tree produced by CardParser#loop_code_block.
    def visitLoop_code_block(self, ctx:CardParser.Loop_code_blockContext):
        for i in range(ctx.getChildCount()):
            check = self.visit(ctx.getChild(i))
            if check is None: continue
            if not isinstance(check, tuple): continue
            assert check[0] in ['break', 'continue']
            return check


    # Visit a parse tree produced by CardParser#statement.
    def visitStatement(self, ctx:CardParser.StatementContext):
        if ctx.getChildCount() == 3:
            value = self.visit(ctx.getChild(1))
            return self.visitAssignee(ctx.getChild(0), value, 'set')
        return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by CardParser#setup_stmt.
    def visitSetup_stmt(self, ctx:CardParser.Setup_stmtContext):
        return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by CardParser#func_stmt.
    def visitFunc_stmt(self, ctx:CardParser.Func_stmtContext):
        return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by CardParser#func_loop_stmt.
    def visitFunc_loop_stmt(self, ctx:CardParser.Func_loop_stmtContext):
        return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by CardParser#round_stmt.
    def visitRound_stmt(self, ctx:CardParser.Round_stmtContext):
        return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by CardParser#round_loop_stmt.
    def visitRound_loop_stmt(self, ctx:CardParser.Round_loop_stmtContext):
        return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by CardParser#loop_stmt.
    def visitLoop_stmt(self, ctx:CardParser.Loop_stmtContext):
        return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by CardParser#declare_stmt.
    def visitDeclare_stmt(self, ctx:CardParser.Declare_stmtContext):
        data_type = ctx.getChild(0).getText()
        if data_type == 'int': data_type = int
        elif data_type == 'string': data_type = str
        elif data_type == 'Card': data_type = utils.Card
        elif data_type == 'Pile': data_type = utils.Pile
        elif data_type == 'Player': data_type = utils.Player
        elif data_type == 'Action': data_type = utils.Action
        assert not isinstance(data_type, str)
        self.visitDeclare_body(ctx.getChild(1), data_type)


    # Visit a parse tree produced by CardParser#declare_body.
    def visitDeclare_body(self, ctx:CardParser.Declare_bodyContext, data_type=None):
        assert data_type is not None
        for i in range(0, ctx.getChildCount(), 2):
            self.visitDeclare_content(ctx.getChild(i), data_type)


    # Visit a parse tree produced by CardParser#declare_content.
    def visitDeclare_content(self, ctx:CardParser.Declare_contentContext, data_type=None):
        assert data_type is not None
        try:
            identifier = ctx.getChild(0).getText()
            if ctx.getChildCount() == 1:
                value = None
                if data_type is int: value = 0
                elif data_type is str: value = ''
                else: value = data_type()
                assert value is not None
                return self.declareIdentifier(identifier, data_type, value)
            if ctx.getChildCount() == 2:
                value = self.visit(ctx.getChild(1))
                if value is None:
                    if data_type not in [utils.Card, utils.Pile, utils.Player, utils.Action, utils.Object]:
                        raise TypeError(f'Incompatible type, cannot set {data_type.__name__} to null')
                    return self.declareIdentifier(identifier, data_type, value)
                if isinstance(value, utils.Object):
                    if data_type not in [utils.Card, utils.Action]:
                        raise TypeError(f'Incompatible type, expected {data_type.__name__}')
                    if data_type is utils.Card: value = utils.Card(value)
                    else: value = utils.Action(value)
                if not isinstance(value, data_type):
                    raise TypeError(f'Incompatible type, expected {data_type.__name__}')
                return self.declareIdentifier(identifier, data_type, value)
            
            expression = self.visit(ctx.getChild(2))
            if not isinstance(expression, int):
                raise TypeError(f'Incompatible type, expected int')
            if expression < 0:
                raise IndexError(f'Expected nonnegative int')
            
            if ctx.getChildCount() == 4:
                arr = []
                for _ in range(expression):
                    if data_type is int: arr.append(0)
                    elif data_type is str: arr.append('')
                    else: arr.append(data_type())
                return self.declareIdentifier(identifier, data_type, arr)
            arr = self.visit(ctx.getChild(4))
            if not isinstance(arr, list): raise TypeError(f'Incompatible type, expected array of type {data_type.__name__}')
            if expression != len(arr): raise ValueError('Array size mismatch')
            
            # might be broken if list is all null but there is an actual mismatch i.e.
            # Card cards[1] = {null}; Player players[1] = cards;
            for item in arr:
                if item is None: continue
                if not isinstance(item, data_type):
                    raise TypeError(f'Incompatible type, expected array of type {data_type.__name__}')
                return self.declareIdentifier(identifier, data_type, arr)
            if data_type in [int, str]: raise TypeError(f'Incompatible type, expected array of type {data_type.__name__}')
            return self.declareIdentifier(identifier, data_type, value)

        except Exception as e:
            if str(e)[:13] == 'Error on line':
                raise e
            self.raiseError(ctx, type(e), str(e))


    # Visit a parse tree produced by CardParser#assign_body.
    def visitAssign_body(self, ctx:CardParser.Assign_bodyContext):
        if ctx.getChildCount() == 2:
            return self.visit(ctx.getChild(1))
        if ctx.getChildCount() == 3:
            data_type = ctx.getChild(2).getText()
            if data_type == 'int' or data_type == 'string':
                self.raiseError(ctx, TypeError, f'Cannot instatiate type {data_type}')
            if data_type == 'Card': return utils.Card()
            if data_type == 'Pile': return utils.Pile()
            if data_type == 'Player': return utils.Player()
            if data_type == 'Action': return utils.Action()
        if ctx.getChildCount() == 4:
            return self.visit(ctx.getChild(2))
        try:
            obj = self.visit(ctx.getChild(3))
            return obj.combination()
        except Exception as e:
            if str(e)[:13] == 'Error on line':
                raise e
            self.raiseError(ctx, type(e), str(e))


    # Visit a parse tree produced by CardParser#assignee.
    def visitAssignee(self, ctx:CardParser.AssigneeContext, value=None, mode='get'):
        try:
            if ctx.getChildCount() == 1:
                identifier = ctx.getChild(0).getText()
                if mode == 'get':
                    data_type, obj = self.visitIdentifier(identifier)
                    assert obj not in [int, str]
                    return obj
                return self.assignIdentifier(identifier, value)
            if ctx.getChildCount() == 3:
                assignee = self.visitAssignee(ctx.getChild(0))
                identifier = ctx.getChild(2).getText()
                if assignee is None: raise AttributeError(f'null has no attribute {identifier}')
                if mode == 'get':
                    obj = assignee.__getattribute__(identifier)
                    assert type(obj) not in [int, str]
                    return obj
                assignee.__setattr__(identifier, value)
                return
            
            assignee = self.visit(ctx.getChild(0))
            if not isinstance(assignee, list) and not isinstance(assignee, utils.Pile):
                data_type = 'null' if assignee is None else type(assignee).__name__
                raise TypeError(f'{data_type} is not subscriptable')
            index = self.visit(ctx.getChild(2))
            if isinstance(assignee, utils.Pile):
                raise AttributeError('Cannot directly modify Card object in Pile')
            if not isinstance(index, int):
                raise TypeError('Index must be an integer')
            if index >= len(assignee):
                raise IndexError('Index out of bounds')
            
            obj = assignee[index]
            if mode == 'get':
                assert type(obj) not in [int, str]
                return obj
            if isinstance(obj, list) or isinstance(value, list):
                raise TypeError('Cannot assign an array')
            if obj is None:
                if type(value) in [int, str]:
                    raise TypeError(f'Incompatible type, expected Card, Pile, Player, Action, or Object')
                assignee[index] = value
                return
            if value is None:
                if type(obj) in [int, str]:
                    raise TypeError(f'Incompatible type, expected {type(obj).__name__}')
                assignee[index] = value
                return
            if type(obj) is not type(value):
                raise TypeError(f'Incompatible type, expected {type(obj).__name__}')
            assignee[index] = value
        except Exception as e:
            if str(e)[:13] == 'Error on line':
                raise e
            self.raiseError(ctx, type(e), str(e))


    # Visit a parse tree produced by CardParser#entity.
    def visitEntity(self, ctx:CardParser.EntityContext):
        try:
            if ctx.getChildCount() == 1:
                child = ctx.getChild(0)
                if isinstance(child, CardParser.Function_callContext):
                    return self.visit(child)

                identifier = child.getText()
                _, value = self.visitIdentifier(identifier)
                return value
            
            if ctx.getChildCount() == 4:
                entity = self.visit(ctx.getChild(0))
                if not isinstance(entity, list) and not isinstance(entity, utils.Pile):
                    data_type = 'null' if entity is None else type(entity).__name__
                    raise TypeError(f'{data_type} is not subscriptable')
                index = self.visit(ctx.getChild(2))
                if isinstance(entity, utils.Pile):
                    return entity[index]
                if not isinstance(index, int):
                    raise TypeError('Index must be an integer')
                if index >= len(entity):
                    raise IndexError('Index out of bounds')
                return entity[index]
            
            if ctx.getChild(0).getText() == '(':
                return self.visit(ctx.getChild(1))
            entity = self.visit(ctx.getChild(0))
            identifier = ctx.getChild(2).getText()
            if entity is None: raise AttributeError(f'null has no attribute {identifier}')
            return entity.__getattribute__(identifier)
        except Exception as e:
            if str(e)[:13] == 'Error on line':
                raise e
            self.raiseError(ctx, type(e), str(e))


    # Visit a parse tree produced by CardParser#array_body.
    def visitArray_body(self, ctx:CardParser.Array_bodyContext):
        arr = []
        for i in range(0, ctx.getChildCount(), 2):
            arr.append(self.visit(ctx.getChild(i)))

        not_null = []
        for i in range(len(arr)):
            if arr[i] is not None:
                not_null.append(arr[i])
        for i in range(len(not_null)):
            if type(not_null[i]) is not type(not_null[0]):
                self.raiseError(ctx, TypeError, 'Array cannot have multiple types')
        if len(not_null) == 0: return arr
        if len(not_null) == len(arr): return arr
        if type(not_null[0]) not in [utils.Card, utils.Pile, utils.Player, utils.Action]:
            self.raiseError(ctx, TypeError, 'Array cannot have multiple types')
        return arr


    # Visit a parse tree produced by CardParser#object_body.
    def visitObject_body(self, ctx:CardParser.Object_bodyContext):
        obj = utils.Object()
        for i in range(0, ctx.getChildCount(), 2):
            identifier, value = self.visit(ctx.getChild(i))
            if obj.has(identifier):
                self.raiseError(ctx, KeyError, 'Duplicate property names found')
            obj.__setattr__(identifier, value)
        return obj


    # Visit a parse tree produced by CardParser#object_content.
    def visitObject_content(self, ctx:CardParser.Object_contentContext):
        identifier = ctx.getChild(0).getText()
        if ctx.getChildCount() == 3:
            value = self.visit(ctx.getChild(2))
            return identifier, value
        value = self.visit(ctx.getChild(3))
        return identifier, value


    # Visit a parse tree produced by CardParser#expression.
    def visitExpression(self, ctx:CardParser.ExpressionContext):
        try:
            if ctx.getChildCount() == 3:
                if ctx.getChild(0).getText() == '(':
                    return self.visit(ctx.getChild(1))
                if ctx.getChild(1).getText() == 'and':
                    left = self.visit(ctx.getChild(0))
                    if not isinstance(left, int):
                        raise TypeError('Incompatible type, expected int')
                    left = bool(left)
                    if not left:
                        return 0
                    right = self.visit(ctx.getChild(2))
                    if not isinstance(right, int):
                        raise TypeError('Incompatible type, expected int')
                    right = bool(right)
                    return int(left and right)
                if ctx.getChild(1).getText() == 'or':
                    left = self.visit(ctx.getChild(0))
                    if not isinstance(left, int):
                        raise TypeError('Incompatible type, expected int')
                    left = bool(left)
                    if left:
                        return 1
                    right = self.visit(ctx.getChild(2))
                    if not isinstance(right, int):
                        raise TypeError('Incompatible type, expected int')
                    right = bool(right)
                    return int(left or right)
                
                left = self.visit(ctx.getChild(0))
                right = self.visit(ctx.getChild(2))
                op = self.visit(ctx.getChild(1))
                if op == '*':
                    if isinstance(left, int) and isinstance(right, int):
                        return left * right
                    return utils.Pile(left, right, 'mul')
                if op == '/':
                    if not isinstance(left, int) or not isinstance(right, int):
                        raise TypeError('Incompatible type, expected int')
                    if right == 0:
                        raise ZeroDivisionError('Division by zero error')
                    return left // right
                if op == '%':
                    if not isinstance(left, int) or not isinstance(right, int):
                        raise TypeError('Incompatible type, expected int')
                    if right == 0:
                        raise ZeroDivisionError('Modulo by zero error')
                    return left % right
                if op == '+':
                    if isinstance(left, int) and isinstance(right, int):
                        return left + right
                    if type(left) in [int, str] and type(right) in [int, str]:
                        return str(left) + str(right)
                    return utils.Pile(left, right, 'add')
                if op == '-':
                    if not isinstance(left, int) or not isinstance(right, int):
                        raise TypeError('Incompatible type, expected int')
                    return left - right
                if op == '>':
                    if not isinstance(left, int) or not isinstance(right, int):
                        raise TypeError('Incompatible type, expected int')
                    return int(left > right)
                if op == '<':
                    if not isinstance(left, int) or not isinstance(right, int):
                        raise TypeError('Incompatible type, expected int')
                    return int(left < right)
                if op == '>=':
                    if not isinstance(left, int) or not isinstance(right, int):
                        raise TypeError('Incompatible type, expected int')
                    return int(left >= right)
                if op == '<=':
                    if not isinstance(left, int) or not isinstance(right, int):
                        raise TypeError('Incompatible type, expected int')
                    return int(left <= right)
                if op == '==':
                    if type(left) is utils.Enum:
                        raise TypeError('The operation \'==\' is not defined for enum')
                    if type(left) is CardParser.Function_callContext:
                        raise TypeError('The operation \'==\' is not defined for function')
                    if type(left) is list:
                        raise TypeError('The operation \'==\' is not defined for array')
                    if type(right) is utils.Enum:
                        raise TypeError('The operation \'==\' is not defined for enum')
                    if type(right) is CardParser.Function_callContext:
                        raise TypeError('The operation \'==\' is not defined for function')
                    if type(right) is list:
                        raise TypeError('The operation \'==\' is not defined for array')
                    if left is None:
                        if right is None:
                            return 1
                        if isinstance(right, int) or isinstance(right, str):
                            raise TypeError(f'Incompatible types, null and {type(right).__name__}')
                        return 0
                    if right is None:
                        if isinstance(left, int) or isinstance(left, str):
                            raise TypeError(f'Incompatible types, {type(left).__name__} and null')
                        return 0
                    if type(left) is not type(right):
                        raise TypeError(f'Incompatible types, {type(left).__name__} and {type(right).__name__}')
                    return int(left == right)
                if op == '!=':
                    if type(left) is utils.Enum:
                        raise TypeError('The operation \'!=\' is not defined for enum')
                    if type(left) is CardParser.Function_callContext:
                        raise TypeError('The operation \'!=\' is not defined for function')
                    if type(left) is list:
                        raise TypeError('The operation \'!=\' is not defined for array')
                    if type(right) is utils.Enum:
                        raise TypeError('The operation \'!=\' is not defined for enum')
                    if type(right) is CardParser.Function_callContext:
                        raise TypeError('The operation \'!=\' is not defined for function')
                    if type(right) is list:
                        raise TypeError('The operation \'!=\' is not defined for array')
                    if left is None:
                        if right is None:
                            return 0
                        if isinstance(right, int) or isinstance(right, str):
                            raise TypeError(f'Incompatible types, null and {type(right).__name__}')
                        return 1
                    if right is None:
                        if isinstance(left, int) or isinstance(left, str):
                            raise TypeError(f'Incompatible types, {type(left).__name__} and null')
                        return 1
                    if type(left) is not type(right):
                        raise TypeError(f'Incompatible types, {type(left).__name__} and {type(right).__name__}')
                    return int(left != right)
            if ctx.getChildCount() == 2:
                assert ctx.getChild(0).getText() == 'not'
                val = self.visit(ctx.getChild(1))
                if not isinstance(val, int):
                    raise TypeError('Incompatible type, expected int')
                return int(not bool(val))
            child = ctx.getChild(0)
            if issubclass(type(child), ParserRuleContext):
                return self.visit(child)

            value = child.getText()
            if value[0] == '"':
                return value[1:-1]
            if value == 'null':
                return None
            return int(value)
        except Exception as e:
            if str(e)[:13] == 'Error on line':
                raise e
            self.raiseError(ctx, type(e), str(e))


    # Visit a parse tree produced by CardParser#operator1.
    def visitOperator1(self, ctx:CardParser.Operator1Context):
        return ctx.getChild(0).getText()


    # Visit a parse tree produced by CardParser#operator2.
    def visitOperator2(self, ctx:CardParser.Operator2Context):
        return ctx.getChild(0).getText()


    # Visit a parse tree produced by CardParser#operator3.
    def visitOperator3(self, ctx:CardParser.Operator3Context):
        return ctx.getChild(0).getText()


    # Visit a parse tree produced by CardParser#operator4.
    def visitOperator4(self, ctx:CardParser.Operator4Context):
        return ctx.getChild(0).getText()


    # Visit a parse tree produced by CardParser#if_stmt.
    def visitIf_stmt(self, ctx:CardParser.If_stmtContext):
        result = self.visit(ctx.getChild(0)) 
        global nested_control_cnt
        if bool(result):
            control_variables.append({})
            nested_control_cnt += 1
            res = self.visit(ctx.getChild(1))
            nested_control_cnt -= 1
            control_variables.pop()
            return res
        if ctx.getChildCount() == 4:
            control_variables.append({})
            nested_control_cnt += 1
            res = self.visit(ctx.getChild(3))
            nested_control_cnt -= 1
            control_variables.pop()
            return res


    # Visit a parse tree produced by CardParser#if_header.
    def visitIf_header(self, ctx:CardParser.If_headerContext):
        result = self.visit(ctx.getChild(2))
        if not isinstance(result, int):
            data_type = 'null' if result is None else type(result).__name__
            self.raiseError(ctx, TypeError, f'Cannot evaluate truth value of type {data_type}')
        return result

    # Visit a parse tree produced by CardParser#foreach_stmt.
    def visitForeach_stmt(self, ctx:CardParser.Foreach_stmtContext):
        identifier, data = self.visit(ctx.getChild(0))
        data_type = utils.Card
        if isinstance(data, list): # hopefully list is not full of just null
            for item in data:
                if item is None: continue
                data_type = type(item)
                break
        control_variables.append({})
        global nested_control_cnt
        nested_control_cnt += 1
        for item in data:
            control_variables[nested_control_cnt] = {}
            control_variables[nested_control_cnt][identifier] = (data_type, item)
            check = self.visit(ctx.getChild(1))
            if check is None: continue
            if not isinstance(check, tuple): continue
            if check[0] == 'break': break
        nested_control_cnt -= 1
        control_variables.pop()


    # Visit a parse tree produced by CardParser#foreach_header.
    def visitForeach_header(self, ctx:CardParser.Foreach_headerContext):
        identifier = ctx.getChild(2).getText()
        entity = self.visit(ctx.getChild(4))

        # don't allow enum as iterable ig
        if type(entity) not in [utils.Pile, list]:
            data_type = 'null' if entity is None else type(entity).__name__
            self.raiseError(ctx, TypeError, f'Type {data_type} is not iterable')
        return identifier, entity


    # Visit a parse tree produced by CardParser#repeat_stmt.
    def visitRepeat_stmt(self, ctx:CardParser.Repeat_stmtContext):
        loop_type, value = self.visit(ctx.getChild(0))
        global nested_control_cnt
        if loop_type == 'count':
            if value <= 0: return

            control_variables.append({})
            nested_control_cnt += 1
            for _ in range(value):
                control_variables[nested_control_cnt] = {}
                check = self.visit(ctx.getChild(1))
                if check is None: continue
                if not isinstance(check, tuple): continue
                if check[0] == 'break': break
            nested_control_cnt -= 1
            control_variables.pop()
            return
        
        assert loop_type == 'logic'
        control_variables.append({})
        nested_control_cnt += 1
        while value == 0:
            control_variables[nested_control_cnt] = {}
            check = self.visit(ctx.getChild(1))
            if not isinstance(check, tuple): continue
            if check is not None and check[0] == 'break': break
            _, value = self.visit(ctx.getChild(0))
        nested_control_cnt -= 1
        control_variables.pop()


    # Visit a parse tree produced by CardParser#repeat_header.
    def visitRepeat_header(self, ctx:CardParser.Repeat_headerContext):
        if ctx.getChildCount() == 2:
            count = self.visit(ctx.getChild(1))
            if not isinstance(count, int):
                self.raiseError(ctx, TypeError, f'Incompatible type, expected int as loop count')
            return ('count', count)
        
        value = self.visit(ctx.getChild(2))
        if not isinstance(value, int):
            data_type = 'null' if value is None else type(value).__name__
            self.raiseError(ctx, TypeError, f'Cannot evaluate truth value of type {data_type}')
        return ('logic', value)


    # Visit a parse tree produced by CardParser#loop_if_stmt.
    def visitLoop_if_stmt(self, ctx:CardParser.Loop_if_stmtContext):
        result = self.visit(ctx.getChild(0)) 
        global nested_control_cnt
        if bool(result):
            control_variables.append({})
            nested_control_cnt += 1
            res = self.visit(ctx.getChild(1))
            nested_control_cnt -= 1
            control_variables.pop()
            return res
        if ctx.getChildCount() == 4:
            control_variables.append({})
            nested_control_cnt += 1
            res = self.visit(ctx.getChild(3))
            nested_control_cnt -= 1
            control_variables.pop()
            return res


    # Visit a parse tree produced by CardParser#func_if_stmt.
    def visitFunc_if_stmt(self, ctx:CardParser.Func_if_stmtContext):
        result = self.visit(ctx.getChild(0)) 
        if bool(result):
            func_control_list[nested_func_cnt].append({})
            func_nested_control_cnt[nested_func_cnt] += 1
            res = self.visit(ctx.getChild(1))
            func_nested_control_cnt[nested_func_cnt] -= 1
            func_control_list[nested_func_cnt].pop()
            return res
        if ctx.getChildCount() == 4:
            func_control_list[nested_func_cnt].append({})
            func_nested_control_cnt[nested_func_cnt] += 1
            res = self.visit(ctx.getChild(3))
            func_nested_control_cnt[nested_func_cnt] -= 1
            func_control_list[nested_func_cnt].pop()
            return res


    # Visit a parse tree produced by CardParser#func_foreach_stmt.
    def visitFunc_foreach_stmt(self, ctx:CardParser.Func_foreach_stmtContext):
        identifier, data = self.visit(ctx.getChild(0))
        data_type = utils.Card
        if isinstance(data, list): # hopefully list is not full of just null
            for item in data:
                if item is None: continue
                data_type = type(item)
                break

        assert nested_func_cnt >= 0
        func_control_list[nested_func_cnt].append({})
        func_nested_control_cnt[nested_func_cnt] += 1
        for item in data:
            idx = func_nested_control_cnt[nested_func_cnt]
            func_control_list[nested_func_cnt][idx] = {}
            func_control_list[nested_func_cnt][nested_control_cnt][identifier] = (data_type, item)
            check = self.visit(ctx.getChild(1))
            if check is None: continue
            if not isinstance(check, tuple): continue
            if check[0] == 'break': break
            if check[0] == 'return':
                func_nested_control_cnt[nested_func_cnt] -= 1
                func_control_list[nested_func_cnt].pop()
                return check
        func_nested_control_cnt[nested_func_cnt] -= 1
        func_control_list[nested_func_cnt].pop()


    # Visit a parse tree produced by CardParser#func_repeat_stmt.
    def visitFunc_repeat_stmt(self, ctx:CardParser.Func_repeat_stmtContext):
        loop_type, value = self.visit(ctx.getChild(0))
        if loop_type == 'count':
            if value <= 0: return

            assert nested_func_cnt >= 0
            func_control_list[nested_func_cnt].append({})
            func_nested_control_cnt[nested_func_cnt] += 1
            for _ in range(value):
                idx = func_nested_control_cnt[nested_func_cnt]
                func_control_list[nested_func_cnt][idx] = {}
                check = self.visit(ctx.getChild(1))
                if check is None: continue
                if not isinstance(check, tuple): continue
                if check[0] == 'break': break
                if check[0] == 'return':
                    func_nested_control_cnt[nested_func_cnt] -= 1
                    func_control_list[nested_func_cnt].pop()
                    return check
            func_nested_control_cnt[nested_func_cnt] -= 1
            func_control_list[nested_func_cnt].pop()
            return
        
        assert loop_type == 'logic'
        assert nested_func_cnt >= 0
        func_control_list[nested_func_cnt].append({})
        func_nested_control_cnt[nested_func_cnt] += 1
        while value == 0:
            idx = func_nested_control_cnt[nested_func_cnt]
            func_control_list[nested_func_cnt][idx] = {}
            check = self.visit(ctx.getChild(1))
            if not isinstance(check, tuple): continue
            if check is not None:
                if check[0] == 'break': break
                if check[0] == 'return':
                    func_nested_control_cnt[nested_func_cnt] -= 1
                    func_control_list[nested_func_cnt].pop()
                    return check
            _, value = self.visit(ctx.getChild(0))
        func_nested_control_cnt[nested_func_cnt] -= 1
        func_control_list[nested_func_cnt].pop()


    # Visit a parse tree produced by CardParser#func_loop_if_stmt.
    def visitFunc_loop_if_stmt(self, ctx:CardParser.Func_loop_if_stmtContext):
        result = self.visit(ctx.getChild(0)) 
        if bool(result):
            func_control_list[nested_func_cnt].append({})
            func_nested_control_cnt[nested_func_cnt] += 1
            res = self.visit(ctx.getChild(1))
            func_nested_control_cnt[nested_func_cnt] -= 1
            func_control_list[nested_func_cnt].pop()
            return res
        if ctx.getChildCount() == 4:
            func_control_list[nested_func_cnt].append({})
            func_nested_control_cnt[nested_func_cnt] += 1
            res = self.visit(ctx.getChild(3))
            func_nested_control_cnt[nested_func_cnt] -= 1
            func_control_list[nested_func_cnt].pop()
            return res


    # Visit a parse tree produced by CardParser#round_if_stmt.
    def visitRound_if_stmt(self, ctx:CardParser.Round_if_stmtContext):
        result = self.visit(ctx.getChild(0)) 
        if bool(result):
            func_control_list[nested_func_cnt].append({})
            func_nested_control_cnt[nested_func_cnt] += 1
            res = self.visit(ctx.getChild(1))
            func_nested_control_cnt[nested_func_cnt] -= 1
            func_control_list[nested_func_cnt].pop()
            return res
        if ctx.getChildCount() == 4:
            func_control_list[nested_func_cnt].append({})
            func_nested_control_cnt[nested_func_cnt] += 1
            res = self.visit(ctx.getChild(3))
            func_nested_control_cnt[nested_func_cnt] -= 1
            func_control_list[nested_func_cnt].pop()
            return res


    # Visit a parse tree produced by CardParser#round_foreach_stmt.
    def visitRound_foreach_stmt(self, ctx:CardParser.Round_foreach_stmtContext):
        identifier, data = self.visit(ctx.getChild(0))
        data_type = utils.Card
        if isinstance(data, list): # hopefully list is not full of just null
            for item in data:
                if item is None: continue
                data_type = type(item)
                break

        assert nested_func_cnt >= 0
        func_control_list[nested_func_cnt].append({})
        func_nested_control_cnt[nested_func_cnt] += 1
        for item in data:
            idx = func_nested_control_cnt[nested_func_cnt]
            func_control_list[nested_func_cnt][idx] = {}
            func_control_list[nested_func_cnt][nested_control_cnt][identifier] = (data_type, item)
            check = self.visit(ctx.getChild(1))
            if check is None: continue
            if not isinstance(check, tuple): continue
            if check[0] == 'break': break
            if check[0] == 'End':
                func_nested_control_cnt[nested_func_cnt] -= 1
                func_control_list[nested_func_cnt].pop()
                return check
        func_nested_control_cnt[nested_func_cnt] -= 1
        func_control_list[nested_func_cnt].pop()


    # Visit a parse tree produced by CardParser#round_repeat_stmt.
    def visitRound_repeat_stmt(self, ctx:CardParser.Round_repeat_stmtContext):
        loop_type, value = self.visit(ctx.getChild(0))
        if loop_type == 'count':
            if value <= 0: return

            assert nested_func_cnt >= 0
            func_control_list[nested_func_cnt].append({})
            func_nested_control_cnt[nested_func_cnt] += 1
            for _ in range(value):
                idx = func_nested_control_cnt[nested_func_cnt]
                func_control_list[nested_func_cnt][idx] = {}
                check = self.visit(ctx.getChild(1))
                if check is None: continue
                if not isinstance(check, tuple): continue
                if check[0] == 'break': break
                if check[0] == 'End':
                    func_nested_control_cnt[nested_func_cnt] -= 1
                    func_control_list[nested_func_cnt].pop()
                    return check
            func_nested_control_cnt[nested_func_cnt] -= 1
            func_control_list[nested_func_cnt].pop()
            return
        
        assert loop_type == 'logic'
        assert nested_func_cnt >= 0
        func_control_list[nested_func_cnt].append({})
        func_nested_control_cnt[nested_func_cnt] += 1
        while value == 0:
            idx = func_nested_control_cnt[nested_func_cnt]
            func_control_list[nested_func_cnt][idx] = {}
            check = self.visit(ctx.getChild(1))
            if not isinstance(check, tuple): continue
            if check is not None:
                if check[0] == 'break': break
                if check[0] == 'End':
                    func_nested_control_cnt[nested_func_cnt] -= 1
                    func_control_list[nested_func_cnt].pop()
                    return check
            _, value = self.visit(ctx.getChild(0))
        func_nested_control_cnt[nested_func_cnt] -= 1
        func_control_list[nested_func_cnt].pop()


    # Visit a parse tree produced by CardParser#round_loop_if_stmt.
    def visitRound_loop_if_stmt(self, ctx:CardParser.Round_loop_if_stmtContext):
        result = self.visit(ctx.getChild(0)) 
        if bool(result):
            func_control_list[nested_func_cnt].append({})
            func_nested_control_cnt[nested_func_cnt] += 1
            res = self.visit(ctx.getChild(1))
            func_nested_control_cnt[nested_func_cnt] -= 1
            func_control_list[nested_func_cnt].pop()
            return res
        if ctx.getChildCount() == 4:
            func_control_list[nested_func_cnt].append({})
            func_nested_control_cnt[nested_func_cnt] += 1
            res = self.visit(ctx.getChild(3))
            func_nested_control_cnt[nested_func_cnt] -= 1
            func_control_list[nested_func_cnt].pop()
            return res


    # Visit a parse tree produced by CardParser#block_stmt.
    def visitBlock_stmt(self, ctx:CardParser.Block_stmtContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        return self.visit(ctx.getChild(1))


    # Visit a parse tree produced by CardParser#func_block_stmt.
    def visitFunc_block_stmt(self, ctx:CardParser.Func_block_stmtContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        return self.visit(ctx.getChild(1))


    # Visit a parse tree produced by CardParser#func_loop_block_stmt.
    def visitFunc_loop_block_stmt(self, ctx:CardParser.Func_loop_block_stmtContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        return self.visit(ctx.getChild(1))


    # Visit a parse tree produced by CardParser#round_block_stmt.
    def visitRound_block_stmt(self, ctx:CardParser.Round_block_stmtContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        return self.visit(ctx.getChild(1))


    # Visit a parse tree produced by CardParser#round_loop_block_stmt.
    def visitRound_loop_block_stmt(self, ctx:CardParser.Round_loop_block_stmtContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        return self.visit(ctx.getChild(1))


    # Visit a parse tree produced by CardParser#loop_block_stmt.
    def visitLoop_block_stmt(self, ctx:CardParser.Loop_block_stmtContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        return self.visit(ctx.getChild(1))


    # Visit a parse tree produced by CardParser#break_stmt.
    def visitBreak_stmt(self, ctx:CardParser.Break_stmtContext):
        return ('break', None)


    # Visit a parse tree produced by CardParser#continue_stmt.
    def visitContinue_stmt(self, ctx:CardParser.Continue_stmtContext):
        return ('continue', None)


    # Visit a parse tree produced by CardParser#return_stmt.
    def visitReturn_stmt(self, ctx:CardParser.Return_stmtContext):
        if ctx.getChildCount() == 2:
            return ('return', None)
        return ('return', self.visit(ctx.getChild(1)))


    # Visit a parse tree produced by CardParser#end_stmt.
    def visitEnd_stmt(self, ctx:CardParser.End_stmtContext):
        return ('End', None)


    # Visit a parse tree produced by CardParser#function_call.
    def visitFunction_call(self, ctx:CardParser.Function_callContext):
        identifier = ctx.getChild(0).getText()
        func = None
        try: 
            data_type, func = self.visitIdentifier(identifier)
            if data_type is not CardParser.Function_blockContext:
                raise TypeError(f'{identifier} is not a function')
        except Exception as e:
            self.raiseError(ctx, type(e), str(e))
        if ctx.getChildCount() == 4:
            self.visit(ctx.getChild(2))
        
        # increment func counter and append new func table
        global nested_func_cnt
        nested_func_cnt += 1
        func_table_list.append({})
        func_control_list.append([])
        func_nested_control_cnt.append(-1)
        value = self.visit(func)
        func_nested_control_cnt.pop()
        func_control_list.pop()
        func_table_list.pop()
        nested_func_cnt -= 1
        return value


    # Visit a parse tree produced by CardParser#actual_params.
    def visitActual_params(self, ctx:CardParser.Actual_paramsContext):
        global parameters
        assert(len(parameters) == 0)
        for i in range(0, ctx.getChildCount(), 2):
            parameters.append(self.visit(ctx.getChild(i)))


    # Visit a parse tree produced by CardParser#pick_expr.
    def visitPick_expr(self, ctx:CardParser.Pick_exprContext):
        entity = self.visit(ctx.getChild(2))
        if isinstance(entity, utils.Pile):
            return entity.pick()
        if not isinstance(entity, list):
            data_type = 'null' if entity is None else type(entity).__name__
            self.raiseError(ctx, TypeError, f'Cannot pick from object of type {data_type}')
        try:
            idx = int(input())
            if idx >= len(entity): raise
            return entity[idx]
        except:
            return None


    # Visit a parse tree produced by CardParser#getint_expr.
    def visitGetint_expr(self, ctx:CardParser.Getint_exprContext):
        try:
            return utils.GetInt()
        except Exception as e:
            self.raiseError(ctx, type(e), str(e))


    # Visit a parse tree produced by CardParser#getstr_expr.
    def visitGetstr_expr(self, ctx:CardParser.Getstr_exprContext):
        return utils.GetString()


    # Visit a parse tree produced by CardParser#print_stmt.
    def visitPrint_stmt(self, ctx:CardParser.Print_stmtContext):
        print_type = ctx.getChild(0).getText()
        output = self.visit(ctx.getChild(2))
        if type(output) not in [int, str]:
            data_type = 'null' if output is None else type(output).__name__
            self.raiseError(ctx, TypeError, f'Cannot print object of type {data_type}')

        if print_type == 'Print':
            print(output, end='')
        else:
            assert print_type == 'Println'
            print(output)


    # Visit a parse tree produced by CardParser#deal_stmt.
    def visitDeal_stmt(self, ctx:CardParser.Deal_stmtContext):
        count = self.visit(ctx.getChild(1))
        entity1 = self.visit(ctx.getChild(3))
        entity2 = self.visit(ctx.getChild(5))

        try:
            if not isinstance(count, int):
                raise TypeError('Incompatible type, expected deal count of type int')
            if not isinstance(entity1, utils.Pile):
                raise TypeError('Incompatible type, expected to deal from Pile')
            if type(entity2) not in [utils.Player, list]:
                raise TypeError('Incompatible type, expected to deal to Player or Player array')
            if isinstance(entity2, list):
                for item in entity2:
                    if item is None:
                        raise ValueError('Array must not contain null')
                    elif not isinstance(item, utils.Player):
                        raise TypeError('Incompatible type, expected to deal to Player or Player array')
                entity1.deal(count, entity2)
                return
            entity1.deal(count, [entity2])
        except Exception as e:
            self.raiseError(ctx, type(e), str(e))


    # Visit a parse tree produced by CardParser#draw_stmt.
    def visitDraw_stmt(self, ctx:CardParser.Draw_stmtContext):
        player = self.visit(ctx.getChild(0))
        if not isinstance(player, utils.Player):
            self.raiseError(ctx, TypeError, 'Incompatible type, expected Player to draw')
        
        if ctx.getChildCount() == 5:
            pile = self.visit(ctx.getChild(3))
            if not isinstance(pile, utils.Pile):
                self.raiseError(ctx, TypeError, 'Incompatible type, expected to draw from Pile')
            try: player.draw(pile)
            except Exception as e: self.raiseError(ctx, type(e), str(e))
            return
        if ctx.getChildCount() == 6:
            count = self.visit(ctx.getChild(2))
            pile = self.visit(ctx.getChild(4))
            if not isinstance(count, int):
                raise TypeError('Incompatible type, expected draw count of type int')
            if not isinstance(pile, utils.Pile):
                raise TypeError('Incompatible type, expected to draw from Pile')
            try: player.draw(pile, count)
            except Exception as e: self.raiseError(ctx, type(e), str(e))
            return
        pile = self.visit(ctx.getChild(5))
        if not isinstance(pile, utils.Pile):
            self.raiseError(ctx, TypeError, 'Incompatible type, expected to draw from Pile')
        while True: # pretest loop
            expression = self.visit(ctx.getChild(3))
            if not isinstance(expression, int):
                data_type = 'null' if expression is None else type(expression).__name__
                self.raiseError(ctx, TypeError, f'Cannot evaluate truth value of type {data_type}')
            if expression == 0: break
            try: player.draw(pile)
            except Exception as e: self.raiseError(ctx, type(e), str(e))


    # Visit a parse tree produced by CardParser#move_stmt.
    def visitMove_stmt(self, ctx:CardParser.Move_stmtContext):
        card = self.visit(ctx.getChild(1))
        pile1 = self.visit(ctx.getChild(3))
        pile2 = self.visit(ctx.getChild(5))

        if not isinstance(card, utils.Card):
            self.raiseError(ctx, TypeError, 'Incompatible type, expected to move Card')
        if not isinstance(pile1, utils.Pile):
            self.raiseError(ctx, TypeError, 'Incompatible type, expected to move from Pile')
        if not isinstance(pile2, utils.Pile):
            self.raiseError(ctx, TypeError, 'Incompatible type, expected to move to Pile')
        
        try: pile1.move(card, pile2)
        except Exception as e: self.raiseError(ctx, type(e), str(e))


    # Visit a parse tree produced by CardParser#play_stmt.
    def visitPlay_stmt(self, ctx:CardParser.Play_stmtContext):
        player = self.visit(ctx.getChild(0))
        card = self.visit(ctx.getChild(2))
        pile = self.visit(ctx.getChild(4))

        if not isinstance(player, utils.Player):
            self.raiseError(ctx, TypeError, 'Incompatible type, expected Player to play')
        if not isinstance(card, utils.Card):
            self.raiseError(ctx, TypeError, 'Incompatible type, expected to play Card')
        if not isinstance(pile, utils.Pile):
            self.raiseError(ctx, TypeError, 'Incompatible type, expected to play to Pile')

        try: player.play(card, pile)
        except Exception as e: self.raiseError(ctx, type(e), str(e))


    # Visit a parse tree produced by CardParser#shuffle_stmt.
    def visitShuffle_stmt(self, ctx:CardParser.Shuffle_stmtContext):
        pile = self.visit(ctx.getChild(1))
        if not isinstance(pile, utils.Pile):
            self.raiseError(ctx, TypeError, 'Incompatible type, can only shuffle Pile')
        pile.shuffle()


    # Visit a parse tree produced by CardParser#peek_stmt.
    def visitPeek_stmt(self, ctx:CardParser.Peek_stmtContext):
        count = self.visit(ctx.getChild(1))
        pile = self.visit(ctx.getChild(3))

        if not isinstance(count, int):
            self.raiseError(ctx, TypeError, 'Incompatible type, expected peek count of type int')
        if not isinstance(pile, utils.Pile):
            self.raiseError(ctx, TypeError, 'Incompatible type, expected to peek from pile')

        try: pile.peek(count)
        except Exception as e: self.raiseError(ctx, type(e), str(e))
    

    # Visit a parse tree produced by CardParser#action_stack_expr.
    def visitAction_stack_expr(self, ctx:CardParser.Action_stack_exprContext):
        identifier = ctx.getChild(2).getText()
        if identifier == 'push':
            if ctx.getChildCount() == 5:
                self.raiseError(ctx, ValueError, 'Attribute push requires an argument')
            expression = self.visit(ctx.getChild(4))
            try: utils.push(expression)
            except Exception as e: self.raiseError(ctx, type(e), str(e))
        elif identifier == 'pop':
            if ctx.getChildCount() == 6:
                self.raiseError(ctx, ValueError, 'Expected 0 arguments, got 1')
            try: return utils.pop()
            except Exception as e: self.raiseError(ctx, type(e), str(e))
        else:
            self.raiseError(ctx, AttributeError, f'ActionStack has no attribute {identifier}')
    
    
    def visitIdentifier(self, identifier:str):
        if nested_func_cnt >= 0:
            if func_nested_control_cnt[nested_func_cnt] >= 0:
                for i in range(func_nested_control_cnt[nested_func_cnt], -1, -1):
                    if identifier in func_control_list[nested_func_cnt][i].keys():
                        return func_control_list[nested_func_cnt][i][identifier]
            if identifier in func_table_list[nested_func_cnt].keys():
                return func_table_list[nested_func_cnt][identifier]
        if nested_control_cnt >= 0:
            for i in range(nested_control_cnt, -1, -1):
                if identifier in control_variables[i].keys():
                    return control_variables[i][identifier]
        if identifier in symbol_table.keys():
            return symbol_table[identifier]
        raise NameError(f'Name {identifier} is not defined')

    def declareIdentifier(self, identifier:str, data_type, value):
        if nested_func_cnt >= 0:
            if func_nested_control_cnt[nested_func_cnt] >= 0:
                idx = func_nested_control_cnt[nested_func_cnt]
                if identifier in func_control_list[nested_func_cnt][idx].keys():
                    raise NameError(f'Name {identifier} was already declared')
                func_control_list[nested_func_cnt][idx][identifier] = (data_type, value)
            else:    
                if identifier in func_table_list[nested_func_cnt].keys():
                    raise NameError(f'Name {identifier} was already declared')
                func_table_list[nested_func_cnt][identifier] = (data_type, value)
        elif nested_control_cnt >= 0:
            if identifier in control_variables[nested_control_cnt].keys():
                raise NameError(f'Name {identifier} was already declared')
            control_variables[nested_control_cnt][identifier] = (data_type, value)
        else:
            if identifier in symbol_table.keys():
                raise NameError(f'Name {identifier} was already declared')
            symbol_table[identifier] = (data_type, value)

    def assignIdentifier(self, identifier:str, value):
        if nested_func_cnt >= 0:
            if func_nested_control_cnt[nested_func_cnt] >= 0:
                for i in range(func_nested_control_cnt[nested_func_cnt], -1, -1):
                    if identifier in func_control_list[nested_func_cnt][i].keys():
                        data_type, old_value = func_control_list[nested_func_cnt][i][identifier]
                        if value is None:
                            if data_type not in [utils.Card, utils.Pile, utils.Player, utils.Action, utils.Object]:
                                raise TypeError(f'Incompatible type, expected {data_type.__name__}')
                        elif isinstance(old_value, list):
                            raise TypeError('Cannot assign an array')
                        elif not isinstance(value, data_type):
                            raise TypeError(f'Incompatible type, expected {data_type.__name__}')
                        func_control_list[nested_func_cnt][i][identifier] = (data_type, value)
                        return
            if identifier in func_table_list[nested_func_cnt].keys():
                data_type, old_value = func_table_list[nested_func_cnt][identifier]
                if value is None:
                    if data_type not in [utils.Card, utils.Pile, utils.Player, utils.Action, utils.Object]:
                        raise TypeError(f'Incompatible type, expected {data_type.__name__}')
                elif isinstance(old_value, list):
                    raise TypeError('Cannot assign an array')
                elif not isinstance(value, data_type):
                    raise TypeError(f'Incompatible type, expected {data_type.__name__}')
                func_table_list[nested_func_cnt][identifier] = (data_type, value)
                return
        if nested_control_cnt >= 0:
            for i in range(nested_control_cnt, -1, -1):
                if identifier in control_variables[i].keys():
                    data_type, old_value = control_variables[i][identifier]
                    if value is None:
                        if data_type not in [utils.Card, utils.Pile, utils.Player, utils.Action, utils.Object]:
                            raise TypeError(f'Incompatible type, expected {data_type.__name__}')
                    elif isinstance(old_value, list):
                        raise TypeError('Cannot assign an array')
                    elif not isinstance(value, data_type):
                        raise TypeError(f'Incompatible type, expected {data_type.__name__}')
                    control_variables[i][identifier] = (data_type, value)
                    return
        if identifier in symbol_table.keys():
            data_type, old_value = symbol_table[identifier]
            if data_type in [utils.Enum, CardParser.Function_blockContext]:
                raise ValueError(f'Cannot modify value of {identifier}')
            if value is None:
                if data_type not in [utils.Card, utils.Pile, utils.Player, utils.Action, utils.Object]:
                    raise TypeError(f'Incompatible type, expected {data_type.__name__}')
            elif isinstance(old_value, list):
                raise TypeError('Cannot assign an array')
            elif not isinstance(value, data_type):
                raise TypeError(f'Incompatible type, expected {data_type.__name__}')
            symbol_table[identifier] = (data_type, value)
            return
        raise NameError(f'Name {identifier} is not defined')
    
    def raiseError(self, ctx, error_type, error_msg):
        line = ctx.start.line
        raise error_type(f'Error on line {line}: {error_msg}')

# del CardParser