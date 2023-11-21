# Generated from Card.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CardParser import CardParser
else:
    from CardParser import CardParser

# This class defines a complete listener for a parse tree produced by CardParser.
class CardListener(ParseTreeListener):

    # Enter a parse tree produced by CardParser#start_.
    def enterStart_(self, ctx:CardParser.Start_Context):
        pass

    # Exit a parse tree produced by CardParser#start_.
    def exitStart_(self, ctx:CardParser.Start_Context):
        pass


    # Enter a parse tree produced by CardParser#program.
    def enterProgram(self, ctx:CardParser.ProgramContext):
        pass

    # Exit a parse tree produced by CardParser#program.
    def exitProgram(self, ctx:CardParser.ProgramContext):
        pass


    # Enter a parse tree produced by CardParser#setup_block.
    def enterSetup_block(self, ctx:CardParser.Setup_blockContext):
        pass

    # Exit a parse tree produced by CardParser#setup_block.
    def exitSetup_block(self, ctx:CardParser.Setup_blockContext):
        pass


    # Enter a parse tree produced by CardParser#setup_content.
    def enterSetup_content(self, ctx:CardParser.Setup_contentContext):
        pass

    # Exit a parse tree produced by CardParser#setup_content.
    def exitSetup_content(self, ctx:CardParser.Setup_contentContext):
        pass


    # Enter a parse tree produced by CardParser#function_block.
    def enterFunction_block(self, ctx:CardParser.Function_blockContext):
        pass

    # Exit a parse tree produced by CardParser#function_block.
    def exitFunction_block(self, ctx:CardParser.Function_blockContext):
        pass


    # Enter a parse tree produced by CardParser#function_header.
    def enterFunction_header(self, ctx:CardParser.Function_headerContext):
        pass

    # Exit a parse tree produced by CardParser#function_header.
    def exitFunction_header(self, ctx:CardParser.Function_headerContext):
        pass


    # Enter a parse tree produced by CardParser#formal_params.
    def enterFormal_params(self, ctx:CardParser.Formal_paramsContext):
        pass

    # Exit a parse tree produced by CardParser#formal_params.
    def exitFormal_params(self, ctx:CardParser.Formal_paramsContext):
        pass


    # Enter a parse tree produced by CardParser#enum_block.
    def enterEnum_block(self, ctx:CardParser.Enum_blockContext):
        pass

    # Exit a parse tree produced by CardParser#enum_block.
    def exitEnum_block(self, ctx:CardParser.Enum_blockContext):
        pass


    # Enter a parse tree produced by CardParser#enum_header.
    def enterEnum_header(self, ctx:CardParser.Enum_headerContext):
        pass

    # Exit a parse tree produced by CardParser#enum_header.
    def exitEnum_header(self, ctx:CardParser.Enum_headerContext):
        pass


    # Enter a parse tree produced by CardParser#enum_body.
    def enterEnum_body(self, ctx:CardParser.Enum_bodyContext):
        pass

    # Exit a parse tree produced by CardParser#enum_body.
    def exitEnum_body(self, ctx:CardParser.Enum_bodyContext):
        pass


    # Enter a parse tree produced by CardParser#obj_defn.
    def enterObj_defn(self, ctx:CardParser.Obj_defnContext):
        pass

    # Exit a parse tree produced by CardParser#obj_defn.
    def exitObj_defn(self, ctx:CardParser.Obj_defnContext):
        pass


    # Enter a parse tree produced by CardParser#round_block.
    def enterRound_block(self, ctx:CardParser.Round_blockContext):
        pass

    # Exit a parse tree produced by CardParser#round_block.
    def exitRound_block(self, ctx:CardParser.Round_blockContext):
        pass


    # Enter a parse tree produced by CardParser#setup_code_block.
    def enterSetup_code_block(self, ctx:CardParser.Setup_code_blockContext):
        pass

    # Exit a parse tree produced by CardParser#setup_code_block.
    def exitSetup_code_block(self, ctx:CardParser.Setup_code_blockContext):
        pass


    # Enter a parse tree produced by CardParser#func_code_block.
    def enterFunc_code_block(self, ctx:CardParser.Func_code_blockContext):
        pass

    # Exit a parse tree produced by CardParser#func_code_block.
    def exitFunc_code_block(self, ctx:CardParser.Func_code_blockContext):
        pass


    # Enter a parse tree produced by CardParser#func_loop_code_block.
    def enterFunc_loop_code_block(self, ctx:CardParser.Func_loop_code_blockContext):
        pass

    # Exit a parse tree produced by CardParser#func_loop_code_block.
    def exitFunc_loop_code_block(self, ctx:CardParser.Func_loop_code_blockContext):
        pass


    # Enter a parse tree produced by CardParser#round_code_block.
    def enterRound_code_block(self, ctx:CardParser.Round_code_blockContext):
        pass

    # Exit a parse tree produced by CardParser#round_code_block.
    def exitRound_code_block(self, ctx:CardParser.Round_code_blockContext):
        pass


    # Enter a parse tree produced by CardParser#round_loop_code_block.
    def enterRound_loop_code_block(self, ctx:CardParser.Round_loop_code_blockContext):
        pass

    # Exit a parse tree produced by CardParser#round_loop_code_block.
    def exitRound_loop_code_block(self, ctx:CardParser.Round_loop_code_blockContext):
        pass


    # Enter a parse tree produced by CardParser#loop_code_block.
    def enterLoop_code_block(self, ctx:CardParser.Loop_code_blockContext):
        pass

    # Exit a parse tree produced by CardParser#loop_code_block.
    def exitLoop_code_block(self, ctx:CardParser.Loop_code_blockContext):
        pass


    # Enter a parse tree produced by CardParser#statement.
    def enterStatement(self, ctx:CardParser.StatementContext):
        pass

    # Exit a parse tree produced by CardParser#statement.
    def exitStatement(self, ctx:CardParser.StatementContext):
        pass


    # Enter a parse tree produced by CardParser#setup_stmt.
    def enterSetup_stmt(self, ctx:CardParser.Setup_stmtContext):
        pass

    # Exit a parse tree produced by CardParser#setup_stmt.
    def exitSetup_stmt(self, ctx:CardParser.Setup_stmtContext):
        pass


    # Enter a parse tree produced by CardParser#func_stmt.
    def enterFunc_stmt(self, ctx:CardParser.Func_stmtContext):
        pass

    # Exit a parse tree produced by CardParser#func_stmt.
    def exitFunc_stmt(self, ctx:CardParser.Func_stmtContext):
        pass


    # Enter a parse tree produced by CardParser#func_loop_stmt.
    def enterFunc_loop_stmt(self, ctx:CardParser.Func_loop_stmtContext):
        pass

    # Exit a parse tree produced by CardParser#func_loop_stmt.
    def exitFunc_loop_stmt(self, ctx:CardParser.Func_loop_stmtContext):
        pass


    # Enter a parse tree produced by CardParser#round_stmt.
    def enterRound_stmt(self, ctx:CardParser.Round_stmtContext):
        pass

    # Exit a parse tree produced by CardParser#round_stmt.
    def exitRound_stmt(self, ctx:CardParser.Round_stmtContext):
        pass


    # Enter a parse tree produced by CardParser#round_loop_stmt.
    def enterRound_loop_stmt(self, ctx:CardParser.Round_loop_stmtContext):
        pass

    # Exit a parse tree produced by CardParser#round_loop_stmt.
    def exitRound_loop_stmt(self, ctx:CardParser.Round_loop_stmtContext):
        pass


    # Enter a parse tree produced by CardParser#loop_stmt.
    def enterLoop_stmt(self, ctx:CardParser.Loop_stmtContext):
        pass

    # Exit a parse tree produced by CardParser#loop_stmt.
    def exitLoop_stmt(self, ctx:CardParser.Loop_stmtContext):
        pass


    # Enter a parse tree produced by CardParser#declare_stmt.
    def enterDeclare_stmt(self, ctx:CardParser.Declare_stmtContext):
        pass

    # Exit a parse tree produced by CardParser#declare_stmt.
    def exitDeclare_stmt(self, ctx:CardParser.Declare_stmtContext):
        pass


    # Enter a parse tree produced by CardParser#declare_body.
    def enterDeclare_body(self, ctx:CardParser.Declare_bodyContext):
        pass

    # Exit a parse tree produced by CardParser#declare_body.
    def exitDeclare_body(self, ctx:CardParser.Declare_bodyContext):
        pass


    # Enter a parse tree produced by CardParser#declare_content.
    def enterDeclare_content(self, ctx:CardParser.Declare_contentContext):
        pass

    # Exit a parse tree produced by CardParser#declare_content.
    def exitDeclare_content(self, ctx:CardParser.Declare_contentContext):
        pass


    # Enter a parse tree produced by CardParser#const_stmt.
    def enterConst_stmt(self, ctx:CardParser.Const_stmtContext):
        pass

    # Exit a parse tree produced by CardParser#const_stmt.
    def exitConst_stmt(self, ctx:CardParser.Const_stmtContext):
        pass


    # Enter a parse tree produced by CardParser#assign_body.
    def enterAssign_body(self, ctx:CardParser.Assign_bodyContext):
        pass

    # Exit a parse tree produced by CardParser#assign_body.
    def exitAssign_body(self, ctx:CardParser.Assign_bodyContext):
        pass


    # Enter a parse tree produced by CardParser#assignee.
    def enterAssignee(self, ctx:CardParser.AssigneeContext):
        pass

    # Exit a parse tree produced by CardParser#assignee.
    def exitAssignee(self, ctx:CardParser.AssigneeContext):
        pass


    # Enter a parse tree produced by CardParser#entity.
    def enterEntity(self, ctx:CardParser.EntityContext):
        pass

    # Exit a parse tree produced by CardParser#entity.
    def exitEntity(self, ctx:CardParser.EntityContext):
        pass


    # Enter a parse tree produced by CardParser#array_body.
    def enterArray_body(self, ctx:CardParser.Array_bodyContext):
        pass

    # Exit a parse tree produced by CardParser#array_body.
    def exitArray_body(self, ctx:CardParser.Array_bodyContext):
        pass


    # Enter a parse tree produced by CardParser#object_body.
    def enterObject_body(self, ctx:CardParser.Object_bodyContext):
        pass

    # Exit a parse tree produced by CardParser#object_body.
    def exitObject_body(self, ctx:CardParser.Object_bodyContext):
        pass


    # Enter a parse tree produced by CardParser#object_content.
    def enterObject_content(self, ctx:CardParser.Object_contentContext):
        pass

    # Exit a parse tree produced by CardParser#object_content.
    def exitObject_content(self, ctx:CardParser.Object_contentContext):
        pass


    # Enter a parse tree produced by CardParser#expression.
    def enterExpression(self, ctx:CardParser.ExpressionContext):
        pass

    # Exit a parse tree produced by CardParser#expression.
    def exitExpression(self, ctx:CardParser.ExpressionContext):
        pass


    # Enter a parse tree produced by CardParser#operator1.
    def enterOperator1(self, ctx:CardParser.Operator1Context):
        pass

    # Exit a parse tree produced by CardParser#operator1.
    def exitOperator1(self, ctx:CardParser.Operator1Context):
        pass


    # Enter a parse tree produced by CardParser#operator2.
    def enterOperator2(self, ctx:CardParser.Operator2Context):
        pass

    # Exit a parse tree produced by CardParser#operator2.
    def exitOperator2(self, ctx:CardParser.Operator2Context):
        pass


    # Enter a parse tree produced by CardParser#operator3.
    def enterOperator3(self, ctx:CardParser.Operator3Context):
        pass

    # Exit a parse tree produced by CardParser#operator3.
    def exitOperator3(self, ctx:CardParser.Operator3Context):
        pass


    # Enter a parse tree produced by CardParser#operator4.
    def enterOperator4(self, ctx:CardParser.Operator4Context):
        pass

    # Exit a parse tree produced by CardParser#operator4.
    def exitOperator4(self, ctx:CardParser.Operator4Context):
        pass


    # Enter a parse tree produced by CardParser#if_stmt.
    def enterIf_stmt(self, ctx:CardParser.If_stmtContext):
        pass

    # Exit a parse tree produced by CardParser#if_stmt.
    def exitIf_stmt(self, ctx:CardParser.If_stmtContext):
        pass


    # Enter a parse tree produced by CardParser#if_header.
    def enterIf_header(self, ctx:CardParser.If_headerContext):
        pass

    # Exit a parse tree produced by CardParser#if_header.
    def exitIf_header(self, ctx:CardParser.If_headerContext):
        pass


    # Enter a parse tree produced by CardParser#foreach_stmt.
    def enterForeach_stmt(self, ctx:CardParser.Foreach_stmtContext):
        pass

    # Exit a parse tree produced by CardParser#foreach_stmt.
    def exitForeach_stmt(self, ctx:CardParser.Foreach_stmtContext):
        pass


    # Enter a parse tree produced by CardParser#foreach_header.
    def enterForeach_header(self, ctx:CardParser.Foreach_headerContext):
        pass

    # Exit a parse tree produced by CardParser#foreach_header.
    def exitForeach_header(self, ctx:CardParser.Foreach_headerContext):
        pass


    # Enter a parse tree produced by CardParser#repeat_stmt.
    def enterRepeat_stmt(self, ctx:CardParser.Repeat_stmtContext):
        pass

    # Exit a parse tree produced by CardParser#repeat_stmt.
    def exitRepeat_stmt(self, ctx:CardParser.Repeat_stmtContext):
        pass


    # Enter a parse tree produced by CardParser#repeat_header.
    def enterRepeat_header(self, ctx:CardParser.Repeat_headerContext):
        pass

    # Exit a parse tree produced by CardParser#repeat_header.
    def exitRepeat_header(self, ctx:CardParser.Repeat_headerContext):
        pass


    # Enter a parse tree produced by CardParser#loop_if_stmt.
    def enterLoop_if_stmt(self, ctx:CardParser.Loop_if_stmtContext):
        pass

    # Exit a parse tree produced by CardParser#loop_if_stmt.
    def exitLoop_if_stmt(self, ctx:CardParser.Loop_if_stmtContext):
        pass


    # Enter a parse tree produced by CardParser#func_if_stmt.
    def enterFunc_if_stmt(self, ctx:CardParser.Func_if_stmtContext):
        pass

    # Exit a parse tree produced by CardParser#func_if_stmt.
    def exitFunc_if_stmt(self, ctx:CardParser.Func_if_stmtContext):
        pass


    # Enter a parse tree produced by CardParser#func_foreach_stmt.
    def enterFunc_foreach_stmt(self, ctx:CardParser.Func_foreach_stmtContext):
        pass

    # Exit a parse tree produced by CardParser#func_foreach_stmt.
    def exitFunc_foreach_stmt(self, ctx:CardParser.Func_foreach_stmtContext):
        pass


    # Enter a parse tree produced by CardParser#func_repeat_stmt.
    def enterFunc_repeat_stmt(self, ctx:CardParser.Func_repeat_stmtContext):
        pass

    # Exit a parse tree produced by CardParser#func_repeat_stmt.
    def exitFunc_repeat_stmt(self, ctx:CardParser.Func_repeat_stmtContext):
        pass


    # Enter a parse tree produced by CardParser#func_loop_if_stmt.
    def enterFunc_loop_if_stmt(self, ctx:CardParser.Func_loop_if_stmtContext):
        pass

    # Exit a parse tree produced by CardParser#func_loop_if_stmt.
    def exitFunc_loop_if_stmt(self, ctx:CardParser.Func_loop_if_stmtContext):
        pass


    # Enter a parse tree produced by CardParser#round_if_stmt.
    def enterRound_if_stmt(self, ctx:CardParser.Round_if_stmtContext):
        pass

    # Exit a parse tree produced by CardParser#round_if_stmt.
    def exitRound_if_stmt(self, ctx:CardParser.Round_if_stmtContext):
        pass


    # Enter a parse tree produced by CardParser#round_foreach_stmt.
    def enterRound_foreach_stmt(self, ctx:CardParser.Round_foreach_stmtContext):
        pass

    # Exit a parse tree produced by CardParser#round_foreach_stmt.
    def exitRound_foreach_stmt(self, ctx:CardParser.Round_foreach_stmtContext):
        pass


    # Enter a parse tree produced by CardParser#round_repeat_stmt.
    def enterRound_repeat_stmt(self, ctx:CardParser.Round_repeat_stmtContext):
        pass

    # Exit a parse tree produced by CardParser#round_repeat_stmt.
    def exitRound_repeat_stmt(self, ctx:CardParser.Round_repeat_stmtContext):
        pass


    # Enter a parse tree produced by CardParser#round_loop_if_stmt.
    def enterRound_loop_if_stmt(self, ctx:CardParser.Round_loop_if_stmtContext):
        pass

    # Exit a parse tree produced by CardParser#round_loop_if_stmt.
    def exitRound_loop_if_stmt(self, ctx:CardParser.Round_loop_if_stmtContext):
        pass


    # Enter a parse tree produced by CardParser#block_stmt.
    def enterBlock_stmt(self, ctx:CardParser.Block_stmtContext):
        pass

    # Exit a parse tree produced by CardParser#block_stmt.
    def exitBlock_stmt(self, ctx:CardParser.Block_stmtContext):
        pass


    # Enter a parse tree produced by CardParser#func_block_stmt.
    def enterFunc_block_stmt(self, ctx:CardParser.Func_block_stmtContext):
        pass

    # Exit a parse tree produced by CardParser#func_block_stmt.
    def exitFunc_block_stmt(self, ctx:CardParser.Func_block_stmtContext):
        pass


    # Enter a parse tree produced by CardParser#func_loop_block_stmt.
    def enterFunc_loop_block_stmt(self, ctx:CardParser.Func_loop_block_stmtContext):
        pass

    # Exit a parse tree produced by CardParser#func_loop_block_stmt.
    def exitFunc_loop_block_stmt(self, ctx:CardParser.Func_loop_block_stmtContext):
        pass


    # Enter a parse tree produced by CardParser#round_block_stmt.
    def enterRound_block_stmt(self, ctx:CardParser.Round_block_stmtContext):
        pass

    # Exit a parse tree produced by CardParser#round_block_stmt.
    def exitRound_block_stmt(self, ctx:CardParser.Round_block_stmtContext):
        pass


    # Enter a parse tree produced by CardParser#round_loop_block_stmt.
    def enterRound_loop_block_stmt(self, ctx:CardParser.Round_loop_block_stmtContext):
        pass

    # Exit a parse tree produced by CardParser#round_loop_block_stmt.
    def exitRound_loop_block_stmt(self, ctx:CardParser.Round_loop_block_stmtContext):
        pass


    # Enter a parse tree produced by CardParser#loop_block_stmt.
    def enterLoop_block_stmt(self, ctx:CardParser.Loop_block_stmtContext):
        pass

    # Exit a parse tree produced by CardParser#loop_block_stmt.
    def exitLoop_block_stmt(self, ctx:CardParser.Loop_block_stmtContext):
        pass


    # Enter a parse tree produced by CardParser#break_stmt.
    def enterBreak_stmt(self, ctx:CardParser.Break_stmtContext):
        pass

    # Exit a parse tree produced by CardParser#break_stmt.
    def exitBreak_stmt(self, ctx:CardParser.Break_stmtContext):
        pass


    # Enter a parse tree produced by CardParser#continue_stmt.
    def enterContinue_stmt(self, ctx:CardParser.Continue_stmtContext):
        pass

    # Exit a parse tree produced by CardParser#continue_stmt.
    def exitContinue_stmt(self, ctx:CardParser.Continue_stmtContext):
        pass


    # Enter a parse tree produced by CardParser#return_stmt.
    def enterReturn_stmt(self, ctx:CardParser.Return_stmtContext):
        pass

    # Exit a parse tree produced by CardParser#return_stmt.
    def exitReturn_stmt(self, ctx:CardParser.Return_stmtContext):
        pass


    # Enter a parse tree produced by CardParser#end_stmt.
    def enterEnd_stmt(self, ctx:CardParser.End_stmtContext):
        pass

    # Exit a parse tree produced by CardParser#end_stmt.
    def exitEnd_stmt(self, ctx:CardParser.End_stmtContext):
        pass


    # Enter a parse tree produced by CardParser#function_call.
    def enterFunction_call(self, ctx:CardParser.Function_callContext):
        pass

    # Exit a parse tree produced by CardParser#function_call.
    def exitFunction_call(self, ctx:CardParser.Function_callContext):
        pass


    # Enter a parse tree produced by CardParser#actual_params.
    def enterActual_params(self, ctx:CardParser.Actual_paramsContext):
        pass

    # Exit a parse tree produced by CardParser#actual_params.
    def exitActual_params(self, ctx:CardParser.Actual_paramsContext):
        pass


    # Enter a parse tree produced by CardParser#pick_expr.
    def enterPick_expr(self, ctx:CardParser.Pick_exprContext):
        pass

    # Exit a parse tree produced by CardParser#pick_expr.
    def exitPick_expr(self, ctx:CardParser.Pick_exprContext):
        pass


    # Enter a parse tree produced by CardParser#getint_expr.
    def enterGetint_expr(self, ctx:CardParser.Getint_exprContext):
        pass

    # Exit a parse tree produced by CardParser#getint_expr.
    def exitGetint_expr(self, ctx:CardParser.Getint_exprContext):
        pass


    # Enter a parse tree produced by CardParser#getstr_expr.
    def enterGetstr_expr(self, ctx:CardParser.Getstr_exprContext):
        pass

    # Exit a parse tree produced by CardParser#getstr_expr.
    def exitGetstr_expr(self, ctx:CardParser.Getstr_exprContext):
        pass


    # Enter a parse tree produced by CardParser#print_stmt.
    def enterPrint_stmt(self, ctx:CardParser.Print_stmtContext):
        pass

    # Exit a parse tree produced by CardParser#print_stmt.
    def exitPrint_stmt(self, ctx:CardParser.Print_stmtContext):
        pass


    # Enter a parse tree produced by CardParser#deal_stmt.
    def enterDeal_stmt(self, ctx:CardParser.Deal_stmtContext):
        pass

    # Exit a parse tree produced by CardParser#deal_stmt.
    def exitDeal_stmt(self, ctx:CardParser.Deal_stmtContext):
        pass


    # Enter a parse tree produced by CardParser#draw_stmt.
    def enterDraw_stmt(self, ctx:CardParser.Draw_stmtContext):
        pass

    # Exit a parse tree produced by CardParser#draw_stmt.
    def exitDraw_stmt(self, ctx:CardParser.Draw_stmtContext):
        pass


    # Enter a parse tree produced by CardParser#move_stmt.
    def enterMove_stmt(self, ctx:CardParser.Move_stmtContext):
        pass

    # Exit a parse tree produced by CardParser#move_stmt.
    def exitMove_stmt(self, ctx:CardParser.Move_stmtContext):
        pass


    # Enter a parse tree produced by CardParser#play_stmt.
    def enterPlay_stmt(self, ctx:CardParser.Play_stmtContext):
        pass

    # Exit a parse tree produced by CardParser#play_stmt.
    def exitPlay_stmt(self, ctx:CardParser.Play_stmtContext):
        pass


    # Enter a parse tree produced by CardParser#shuffle_stmt.
    def enterShuffle_stmt(self, ctx:CardParser.Shuffle_stmtContext):
        pass

    # Exit a parse tree produced by CardParser#shuffle_stmt.
    def exitShuffle_stmt(self, ctx:CardParser.Shuffle_stmtContext):
        pass


    # Enter a parse tree produced by CardParser#peek_stmt.
    def enterPeek_stmt(self, ctx:CardParser.Peek_stmtContext):
        pass

    # Exit a parse tree produced by CardParser#peek_stmt.
    def exitPeek_stmt(self, ctx:CardParser.Peek_stmtContext):
        pass



del CardParser