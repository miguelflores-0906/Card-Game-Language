# Generated from Card.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CardParser import CardParser
else:
    from CardParser import CardParser

import utils

# global stuff
symbol_table = {}
nested_func_cnt = -1
func_table_list = []
parameters = []

# This class defines a complete generic visitor for a parse tree produced by CardParser.

class CardVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CardParser#start_.
    def visitStart_(self, ctx:CardParser.Start_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CardParser#program.
    def visitProgram(self, ctx:CardParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CardParser#setup_block.
    def visitSetup_block(self, ctx:CardParser.Setup_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CardParser#setup_content.
    def visitSetup_content(self, ctx:CardParser.Setup_contentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CardParser#function_block.
    def visitFunction_block(self, ctx:CardParser.Function_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CardParser#function_header.
    def visitFunction_header(self, ctx:CardParser.Function_headerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CardParser#formal_params.
    def visitFormal_params(self, ctx:CardParser.Formal_paramsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CardParser#enum_block.
    def visitEnum_block(self, ctx:CardParser.Enum_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CardParser#enum_header.
    def visitEnum_header(self, ctx:CardParser.Enum_headerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CardParser#enum_body.
    def visitEnum_body(self, ctx:CardParser.Enum_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CardParser#obj_defn.
    def visitObj_defn(self, ctx:CardParser.Obj_defnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CardParser#round_block.
    def visitRound_block(self, ctx:CardParser.Round_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CardParser#setup_code_block.
    def visitSetup_code_block(self, ctx:CardParser.Setup_code_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CardParser#func_code_block.
    def visitFunc_code_block(self, ctx:CardParser.Func_code_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CardParser#func_loop_code_block.
    def visitFunc_loop_code_block(self, ctx:CardParser.Func_loop_code_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CardParser#round_code_block.
    def visitRound_code_block(self, ctx:CardParser.Round_code_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CardParser#round_loop_code_block.
    def visitRound_loop_code_block(self, ctx:CardParser.Round_loop_code_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CardParser#loop_code_block.
    def visitLoop_code_block(self, ctx:CardParser.Loop_code_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CardParser#statement.
    def visitStatement(self, ctx:CardParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CardParser#setup_stmt.
    def visitSetup_stmt(self, ctx:CardParser.Setup_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CardParser#func_stmt.
    def visitFunc_stmt(self, ctx:CardParser.Func_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CardParser#func_loop_stmt.
    def visitFunc_loop_stmt(self, ctx:CardParser.Func_loop_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CardParser#round_stmt.
    def visitRound_stmt(self, ctx:CardParser.Round_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CardParser#round_loop_stmt.
    def visitRound_loop_stmt(self, ctx:CardParser.Round_loop_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CardParser#loop_stmt.
    def visitLoop_stmt(self, ctx:CardParser.Loop_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CardParser#declare_stmt.
    def visitDeclare_stmt(self, ctx:CardParser.Declare_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CardParser#declare_body.
    def visitDeclare_body(self, ctx:CardParser.Declare_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CardParser#declare_content.
    def visitDeclare_content(self, ctx:CardParser.Declare_contentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CardParser#const_stmt.
    def visitConst_stmt(self, ctx:CardParser.Const_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CardParser#assign_body.
    def visitAssign_body(self, ctx:CardParser.Assign_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CardParser#assignee.
    def visitAssignee(self, ctx:CardParser.AssigneeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CardParser#entity.
    def visitEntity(self, ctx:CardParser.EntityContext):
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
        return entity.__getattribute__(identifier)


    # Visit a parse tree produced by CardParser#array_body.
    def visitArray_body(self, ctx:CardParser.Array_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CardParser#object_body.
    def visitObject_body(self, ctx:CardParser.Object_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CardParser#object_content.
    def visitObject_content(self, ctx:CardParser.Object_contentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CardParser#expression.
    def visitExpression(self, ctx:CardParser.ExpressionContext):
        if ctx.getChildCount() == 3:
            if ctx.getChild(0).getText() == '(':
                return self.visit(ctx.getChild(1))
            if ctx.getChild(1).getText() == 'and':
                left = self.visit(ctx.getChild(0))
                right = self.visit(ctx.getChild(2))
                if not isinstance(left, int) or not isinstance(right, int):
                    raise TypeError('Incompatible type, expected int')
                left = left == 1
                right = right == 1
                return int(left and right)
            if ctx.getChild(1).getText() == 'or':
                left = self.visit(ctx.getChild(0))
                right = self.visit(ctx.getChild(2))
                if not isinstance(left, int) or not isinstance(right, int):
                    raise TypeError('Incompatible type, expected int')
                left = left == 1
                right = right == 1
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
                if left is None:
                    if right is None:
                        return 1
                    if isinstance(right, int) or isinstance(right, str):
                        raise TypeError('Incompatible type')
                    return 0
                if right is None:
                    if isinstance(left, int) or isinstance(left, str):
                        raise TypeError('Incompatible type')
                    return 0
                if type(left) is not type(right):
                    raise TypeError(f'Incompatible types, {type(left).__name__} and {type(right).__name__}')
                return int(left == right)
            if op == '!=':
                if left is None:
                    if right is None:
                        return 0
                    if isinstance(right, int) or isinstance(right, str):
                        raise TypeError('Incompatible type')
                    return 1
                if right is None:
                    if isinstance(left, int) or isinstance(left, str):
                        raise TypeError('Incompatible type')
                    return 1
                if type(left) is not type(right):
                    raise TypeError(f'Incompatible types, {type(left).__name__} and {type(right).__name__}')
                return int(left != right)
        if ctx.getChildCount() == 2:
            assert(ctx.getChild(0).getText() == 'not')
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
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CardParser#if_header.
    def visitIf_header(self, ctx:CardParser.If_headerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CardParser#foreach_stmt.
    def visitForeach_stmt(self, ctx:CardParser.Foreach_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CardParser#foreach_header.
    def visitForeach_header(self, ctx:CardParser.Foreach_headerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CardParser#repeat_stmt.
    def visitRepeat_stmt(self, ctx:CardParser.Repeat_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CardParser#repeat_header.
    def visitRepeat_header(self, ctx:CardParser.Repeat_headerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CardParser#loop_if_stmt.
    def visitLoop_if_stmt(self, ctx:CardParser.Loop_if_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CardParser#func_if_stmt.
    def visitFunc_if_stmt(self, ctx:CardParser.Func_if_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CardParser#func_foreach_stmt.
    def visitFunc_foreach_stmt(self, ctx:CardParser.Func_foreach_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CardParser#func_repeat_stmt.
    def visitFunc_repeat_stmt(self, ctx:CardParser.Func_repeat_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CardParser#func_loop_if_stmt.
    def visitFunc_loop_if_stmt(self, ctx:CardParser.Func_loop_if_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CardParser#round_if_stmt.
    def visitRound_if_stmt(self, ctx:CardParser.Round_if_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CardParser#round_foreach_stmt.
    def visitRound_foreach_stmt(self, ctx:CardParser.Round_foreach_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CardParser#round_repeat_stmt.
    def visitRound_repeat_stmt(self, ctx:CardParser.Round_repeat_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CardParser#round_loop_if_stmt.
    def visitRound_loop_if_stmt(self, ctx:CardParser.Round_loop_if_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CardParser#block_stmt.
    def visitBlock_stmt(self, ctx:CardParser.Block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CardParser#func_block_stmt.
    def visitFunc_block_stmt(self, ctx:CardParser.Func_block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CardParser#func_loop_block_stmt.
    def visitFunc_loop_block_stmt(self, ctx:CardParser.Func_loop_block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CardParser#round_block_stmt.
    def visitRound_block_stmt(self, ctx:CardParser.Round_block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CardParser#round_loop_block_stmt.
    def visitRound_loop_block_stmt(self, ctx:CardParser.Round_loop_block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CardParser#loop_block_stmt.
    def visitLoop_block_stmt(self, ctx:CardParser.Loop_block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CardParser#break_stmt.
    def visitBreak_stmt(self, ctx:CardParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CardParser#continue_stmt.
    def visitContinue_stmt(self, ctx:CardParser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CardParser#return_stmt.
    def visitReturn_stmt(self, ctx:CardParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CardParser#end_stmt.
    def visitEnd_stmt(self, ctx:CardParser.End_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CardParser#function_call.
    def visitFunction_call(self, ctx:CardParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CardParser#actual_params.
    def visitActual_params(self, ctx:CardParser.Actual_paramsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CardParser#pick_expr.
    def visitPick_expr(self, ctx:CardParser.Pick_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CardParser#getint_expr.
    def visitGetint_expr(self, ctx:CardParser.Getint_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CardParser#getstr_expr.
    def visitGetstr_expr(self, ctx:CardParser.Getstr_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CardParser#print_stmt.
    def visitPrint_stmt(self, ctx:CardParser.Print_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CardParser#deal_stmt.
    def visitDeal_stmt(self, ctx:CardParser.Deal_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CardParser#draw_stmt.
    def visitDraw_stmt(self, ctx:CardParser.Draw_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CardParser#move_stmt.
    def visitMove_stmt(self, ctx:CardParser.Move_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CardParser#play_stmt.
    def visitPlay_stmt(self, ctx:CardParser.Play_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CardParser#shuffle_stmt.
    def visitShuffle_stmt(self, ctx:CardParser.Shuffle_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CardParser#peek_stmt.
    def visitPeek_stmt(self, ctx:CardParser.Peek_stmtContext):
        return self.visitChildren(ctx)
    
    # Visit a parse tree produced by CardParser#action_stack_expr.
    def visitAction_stack_expr(self, ctx:CardParser.Action_stack_exprContext):
        return self.visitChildren(ctx)
    
    def visitIdentifier(self, identifier:str):
        if nested_func_cnt >= 0:
            if identifier in func_table_list[nested_func_cnt].keys():
                return func_table_list[nested_func_cnt][identifier]
        if identifier in symbol_table.keys():
            return symbol_table[identifier]
        raise NameError(f'Name {identifier} is not defined')

    def declareIdentifier(self, identifier:str, data_type, value):
        if nested_func_cnt >= 0:
            if identifier in func_table_list[nested_func_cnt].keys():
                raise NameError(f'Name {identifier} was already declared')
            func_table_list[nested_func_cnt][identifier] = (data_type, value)
        else:
            if identifier in symbol_table.keys():
                raise NameError(f'Name {identifier} was already declared')
            symbol_table[identifier] = (data_type, value)

    def assignIdentifier(self, identifier:str, value):
        if nested_func_cnt >= 0:
            if identifier in func_table_list[nested_func_cnt].keys():
                data_type, _ = func_table_list[nested_func_cnt][identifier]
                if value is None:
                    if data_type not in [utils.Card, utils.Pile, utils.Player, utils.Action, dict]:
                        raise TypeError(f'Incompatible type, expected {data_type.__name__}')
                elif not isinstance(value, data_type):
                    raise TypeError(f'Incompatible type, expected {data_type.__name__}')
                func_table_list[nested_func_cnt][identifier] = (data_type, value)
                return

        if identifier in symbol_table.keys():
            data_type, _ = symbol_table[identifier]
            if value is None:
                if data_type not in [utils.Card, utils.Pile, utils.Player, utils.Action, dict]:
                    raise TypeError(f'Incompatible type, expected {data_type.__name__}')
            elif not isinstance(value, data_type):
                raise TypeError(f'Incompatible type, expected {data_type.__name__}')
            symbol_table[identifier] = (data_type, value)
            return
        raise NameError(f'Name {identifier} is not defined')

del CardParser