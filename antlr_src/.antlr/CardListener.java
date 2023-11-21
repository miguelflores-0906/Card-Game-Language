// Generated from c:/Users/User/Documents/School/A.Y. 2023-2024 Term 1/CSC617M/MP Final/antlr_src/Card.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link CardParser}.
 */
public interface CardListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link CardParser#start_}.
	 * @param ctx the parse tree
	 */
	void enterStart_(CardParser.Start_Context ctx);
	/**
	 * Exit a parse tree produced by {@link CardParser#start_}.
	 * @param ctx the parse tree
	 */
	void exitStart_(CardParser.Start_Context ctx);
	/**
	 * Enter a parse tree produced by {@link CardParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(CardParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link CardParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(CardParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link CardParser#setup_block}.
	 * @param ctx the parse tree
	 */
	void enterSetup_block(CardParser.Setup_blockContext ctx);
	/**
	 * Exit a parse tree produced by {@link CardParser#setup_block}.
	 * @param ctx the parse tree
	 */
	void exitSetup_block(CardParser.Setup_blockContext ctx);
	/**
	 * Enter a parse tree produced by {@link CardParser#setup_content}.
	 * @param ctx the parse tree
	 */
	void enterSetup_content(CardParser.Setup_contentContext ctx);
	/**
	 * Exit a parse tree produced by {@link CardParser#setup_content}.
	 * @param ctx the parse tree
	 */
	void exitSetup_content(CardParser.Setup_contentContext ctx);
	/**
	 * Enter a parse tree produced by {@link CardParser#function_block}.
	 * @param ctx the parse tree
	 */
	void enterFunction_block(CardParser.Function_blockContext ctx);
	/**
	 * Exit a parse tree produced by {@link CardParser#function_block}.
	 * @param ctx the parse tree
	 */
	void exitFunction_block(CardParser.Function_blockContext ctx);
	/**
	 * Enter a parse tree produced by {@link CardParser#function_header}.
	 * @param ctx the parse tree
	 */
	void enterFunction_header(CardParser.Function_headerContext ctx);
	/**
	 * Exit a parse tree produced by {@link CardParser#function_header}.
	 * @param ctx the parse tree
	 */
	void exitFunction_header(CardParser.Function_headerContext ctx);
	/**
	 * Enter a parse tree produced by {@link CardParser#formal_params}.
	 * @param ctx the parse tree
	 */
	void enterFormal_params(CardParser.Formal_paramsContext ctx);
	/**
	 * Exit a parse tree produced by {@link CardParser#formal_params}.
	 * @param ctx the parse tree
	 */
	void exitFormal_params(CardParser.Formal_paramsContext ctx);
	/**
	 * Enter a parse tree produced by {@link CardParser#enum_block}.
	 * @param ctx the parse tree
	 */
	void enterEnum_block(CardParser.Enum_blockContext ctx);
	/**
	 * Exit a parse tree produced by {@link CardParser#enum_block}.
	 * @param ctx the parse tree
	 */
	void exitEnum_block(CardParser.Enum_blockContext ctx);
	/**
	 * Enter a parse tree produced by {@link CardParser#enum_header}.
	 * @param ctx the parse tree
	 */
	void enterEnum_header(CardParser.Enum_headerContext ctx);
	/**
	 * Exit a parse tree produced by {@link CardParser#enum_header}.
	 * @param ctx the parse tree
	 */
	void exitEnum_header(CardParser.Enum_headerContext ctx);
	/**
	 * Enter a parse tree produced by {@link CardParser#enum_body}.
	 * @param ctx the parse tree
	 */
	void enterEnum_body(CardParser.Enum_bodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link CardParser#enum_body}.
	 * @param ctx the parse tree
	 */
	void exitEnum_body(CardParser.Enum_bodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link CardParser#obj_defn}.
	 * @param ctx the parse tree
	 */
	void enterObj_defn(CardParser.Obj_defnContext ctx);
	/**
	 * Exit a parse tree produced by {@link CardParser#obj_defn}.
	 * @param ctx the parse tree
	 */
	void exitObj_defn(CardParser.Obj_defnContext ctx);
	/**
	 * Enter a parse tree produced by {@link CardParser#round_block}.
	 * @param ctx the parse tree
	 */
	void enterRound_block(CardParser.Round_blockContext ctx);
	/**
	 * Exit a parse tree produced by {@link CardParser#round_block}.
	 * @param ctx the parse tree
	 */
	void exitRound_block(CardParser.Round_blockContext ctx);
	/**
	 * Enter a parse tree produced by {@link CardParser#setup_code_block}.
	 * @param ctx the parse tree
	 */
	void enterSetup_code_block(CardParser.Setup_code_blockContext ctx);
	/**
	 * Exit a parse tree produced by {@link CardParser#setup_code_block}.
	 * @param ctx the parse tree
	 */
	void exitSetup_code_block(CardParser.Setup_code_blockContext ctx);
	/**
	 * Enter a parse tree produced by {@link CardParser#func_code_block}.
	 * @param ctx the parse tree
	 */
	void enterFunc_code_block(CardParser.Func_code_blockContext ctx);
	/**
	 * Exit a parse tree produced by {@link CardParser#func_code_block}.
	 * @param ctx the parse tree
	 */
	void exitFunc_code_block(CardParser.Func_code_blockContext ctx);
	/**
	 * Enter a parse tree produced by {@link CardParser#func_loop_code_block}.
	 * @param ctx the parse tree
	 */
	void enterFunc_loop_code_block(CardParser.Func_loop_code_blockContext ctx);
	/**
	 * Exit a parse tree produced by {@link CardParser#func_loop_code_block}.
	 * @param ctx the parse tree
	 */
	void exitFunc_loop_code_block(CardParser.Func_loop_code_blockContext ctx);
	/**
	 * Enter a parse tree produced by {@link CardParser#round_code_block}.
	 * @param ctx the parse tree
	 */
	void enterRound_code_block(CardParser.Round_code_blockContext ctx);
	/**
	 * Exit a parse tree produced by {@link CardParser#round_code_block}.
	 * @param ctx the parse tree
	 */
	void exitRound_code_block(CardParser.Round_code_blockContext ctx);
	/**
	 * Enter a parse tree produced by {@link CardParser#round_loop_code_block}.
	 * @param ctx the parse tree
	 */
	void enterRound_loop_code_block(CardParser.Round_loop_code_blockContext ctx);
	/**
	 * Exit a parse tree produced by {@link CardParser#round_loop_code_block}.
	 * @param ctx the parse tree
	 */
	void exitRound_loop_code_block(CardParser.Round_loop_code_blockContext ctx);
	/**
	 * Enter a parse tree produced by {@link CardParser#loop_code_block}.
	 * @param ctx the parse tree
	 */
	void enterLoop_code_block(CardParser.Loop_code_blockContext ctx);
	/**
	 * Exit a parse tree produced by {@link CardParser#loop_code_block}.
	 * @param ctx the parse tree
	 */
	void exitLoop_code_block(CardParser.Loop_code_blockContext ctx);
	/**
	 * Enter a parse tree produced by {@link CardParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(CardParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CardParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(CardParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CardParser#setup_stmt}.
	 * @param ctx the parse tree
	 */
	void enterSetup_stmt(CardParser.Setup_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link CardParser#setup_stmt}.
	 * @param ctx the parse tree
	 */
	void exitSetup_stmt(CardParser.Setup_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link CardParser#func_stmt}.
	 * @param ctx the parse tree
	 */
	void enterFunc_stmt(CardParser.Func_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link CardParser#func_stmt}.
	 * @param ctx the parse tree
	 */
	void exitFunc_stmt(CardParser.Func_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link CardParser#func_loop_stmt}.
	 * @param ctx the parse tree
	 */
	void enterFunc_loop_stmt(CardParser.Func_loop_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link CardParser#func_loop_stmt}.
	 * @param ctx the parse tree
	 */
	void exitFunc_loop_stmt(CardParser.Func_loop_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link CardParser#round_stmt}.
	 * @param ctx the parse tree
	 */
	void enterRound_stmt(CardParser.Round_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link CardParser#round_stmt}.
	 * @param ctx the parse tree
	 */
	void exitRound_stmt(CardParser.Round_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link CardParser#round_loop_stmt}.
	 * @param ctx the parse tree
	 */
	void enterRound_loop_stmt(CardParser.Round_loop_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link CardParser#round_loop_stmt}.
	 * @param ctx the parse tree
	 */
	void exitRound_loop_stmt(CardParser.Round_loop_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link CardParser#loop_stmt}.
	 * @param ctx the parse tree
	 */
	void enterLoop_stmt(CardParser.Loop_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link CardParser#loop_stmt}.
	 * @param ctx the parse tree
	 */
	void exitLoop_stmt(CardParser.Loop_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link CardParser#declare_stmt}.
	 * @param ctx the parse tree
	 */
	void enterDeclare_stmt(CardParser.Declare_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link CardParser#declare_stmt}.
	 * @param ctx the parse tree
	 */
	void exitDeclare_stmt(CardParser.Declare_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link CardParser#declare_body}.
	 * @param ctx the parse tree
	 */
	void enterDeclare_body(CardParser.Declare_bodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link CardParser#declare_body}.
	 * @param ctx the parse tree
	 */
	void exitDeclare_body(CardParser.Declare_bodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link CardParser#declare_content}.
	 * @param ctx the parse tree
	 */
	void enterDeclare_content(CardParser.Declare_contentContext ctx);
	/**
	 * Exit a parse tree produced by {@link CardParser#declare_content}.
	 * @param ctx the parse tree
	 */
	void exitDeclare_content(CardParser.Declare_contentContext ctx);
	/**
	 * Enter a parse tree produced by {@link CardParser#const_stmt}.
	 * @param ctx the parse tree
	 */
	void enterConst_stmt(CardParser.Const_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link CardParser#const_stmt}.
	 * @param ctx the parse tree
	 */
	void exitConst_stmt(CardParser.Const_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link CardParser#assign_body}.
	 * @param ctx the parse tree
	 */
	void enterAssign_body(CardParser.Assign_bodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link CardParser#assign_body}.
	 * @param ctx the parse tree
	 */
	void exitAssign_body(CardParser.Assign_bodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link CardParser#assignee}.
	 * @param ctx the parse tree
	 */
	void enterAssignee(CardParser.AssigneeContext ctx);
	/**
	 * Exit a parse tree produced by {@link CardParser#assignee}.
	 * @param ctx the parse tree
	 */
	void exitAssignee(CardParser.AssigneeContext ctx);
	/**
	 * Enter a parse tree produced by {@link CardParser#entity}.
	 * @param ctx the parse tree
	 */
	void enterEntity(CardParser.EntityContext ctx);
	/**
	 * Exit a parse tree produced by {@link CardParser#entity}.
	 * @param ctx the parse tree
	 */
	void exitEntity(CardParser.EntityContext ctx);
	/**
	 * Enter a parse tree produced by {@link CardParser#array_body}.
	 * @param ctx the parse tree
	 */
	void enterArray_body(CardParser.Array_bodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link CardParser#array_body}.
	 * @param ctx the parse tree
	 */
	void exitArray_body(CardParser.Array_bodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link CardParser#object_body}.
	 * @param ctx the parse tree
	 */
	void enterObject_body(CardParser.Object_bodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link CardParser#object_body}.
	 * @param ctx the parse tree
	 */
	void exitObject_body(CardParser.Object_bodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link CardParser#object_content}.
	 * @param ctx the parse tree
	 */
	void enterObject_content(CardParser.Object_contentContext ctx);
	/**
	 * Exit a parse tree produced by {@link CardParser#object_content}.
	 * @param ctx the parse tree
	 */
	void exitObject_content(CardParser.Object_contentContext ctx);
	/**
	 * Enter a parse tree produced by {@link CardParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(CardParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link CardParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(CardParser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link CardParser#operator1}.
	 * @param ctx the parse tree
	 */
	void enterOperator1(CardParser.Operator1Context ctx);
	/**
	 * Exit a parse tree produced by {@link CardParser#operator1}.
	 * @param ctx the parse tree
	 */
	void exitOperator1(CardParser.Operator1Context ctx);
	/**
	 * Enter a parse tree produced by {@link CardParser#operator2}.
	 * @param ctx the parse tree
	 */
	void enterOperator2(CardParser.Operator2Context ctx);
	/**
	 * Exit a parse tree produced by {@link CardParser#operator2}.
	 * @param ctx the parse tree
	 */
	void exitOperator2(CardParser.Operator2Context ctx);
	/**
	 * Enter a parse tree produced by {@link CardParser#operator3}.
	 * @param ctx the parse tree
	 */
	void enterOperator3(CardParser.Operator3Context ctx);
	/**
	 * Exit a parse tree produced by {@link CardParser#operator3}.
	 * @param ctx the parse tree
	 */
	void exitOperator3(CardParser.Operator3Context ctx);
	/**
	 * Enter a parse tree produced by {@link CardParser#operator4}.
	 * @param ctx the parse tree
	 */
	void enterOperator4(CardParser.Operator4Context ctx);
	/**
	 * Exit a parse tree produced by {@link CardParser#operator4}.
	 * @param ctx the parse tree
	 */
	void exitOperator4(CardParser.Operator4Context ctx);
	/**
	 * Enter a parse tree produced by {@link CardParser#if_stmt}.
	 * @param ctx the parse tree
	 */
	void enterIf_stmt(CardParser.If_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link CardParser#if_stmt}.
	 * @param ctx the parse tree
	 */
	void exitIf_stmt(CardParser.If_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link CardParser#if_header}.
	 * @param ctx the parse tree
	 */
	void enterIf_header(CardParser.If_headerContext ctx);
	/**
	 * Exit a parse tree produced by {@link CardParser#if_header}.
	 * @param ctx the parse tree
	 */
	void exitIf_header(CardParser.If_headerContext ctx);
	/**
	 * Enter a parse tree produced by {@link CardParser#foreach_stmt}.
	 * @param ctx the parse tree
	 */
	void enterForeach_stmt(CardParser.Foreach_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link CardParser#foreach_stmt}.
	 * @param ctx the parse tree
	 */
	void exitForeach_stmt(CardParser.Foreach_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link CardParser#foreach_header}.
	 * @param ctx the parse tree
	 */
	void enterForeach_header(CardParser.Foreach_headerContext ctx);
	/**
	 * Exit a parse tree produced by {@link CardParser#foreach_header}.
	 * @param ctx the parse tree
	 */
	void exitForeach_header(CardParser.Foreach_headerContext ctx);
	/**
	 * Enter a parse tree produced by {@link CardParser#repeat_stmt}.
	 * @param ctx the parse tree
	 */
	void enterRepeat_stmt(CardParser.Repeat_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link CardParser#repeat_stmt}.
	 * @param ctx the parse tree
	 */
	void exitRepeat_stmt(CardParser.Repeat_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link CardParser#repeat_header}.
	 * @param ctx the parse tree
	 */
	void enterRepeat_header(CardParser.Repeat_headerContext ctx);
	/**
	 * Exit a parse tree produced by {@link CardParser#repeat_header}.
	 * @param ctx the parse tree
	 */
	void exitRepeat_header(CardParser.Repeat_headerContext ctx);
	/**
	 * Enter a parse tree produced by {@link CardParser#loop_if_stmt}.
	 * @param ctx the parse tree
	 */
	void enterLoop_if_stmt(CardParser.Loop_if_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link CardParser#loop_if_stmt}.
	 * @param ctx the parse tree
	 */
	void exitLoop_if_stmt(CardParser.Loop_if_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link CardParser#func_if_stmt}.
	 * @param ctx the parse tree
	 */
	void enterFunc_if_stmt(CardParser.Func_if_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link CardParser#func_if_stmt}.
	 * @param ctx the parse tree
	 */
	void exitFunc_if_stmt(CardParser.Func_if_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link CardParser#func_foreach_stmt}.
	 * @param ctx the parse tree
	 */
	void enterFunc_foreach_stmt(CardParser.Func_foreach_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link CardParser#func_foreach_stmt}.
	 * @param ctx the parse tree
	 */
	void exitFunc_foreach_stmt(CardParser.Func_foreach_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link CardParser#func_repeat_stmt}.
	 * @param ctx the parse tree
	 */
	void enterFunc_repeat_stmt(CardParser.Func_repeat_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link CardParser#func_repeat_stmt}.
	 * @param ctx the parse tree
	 */
	void exitFunc_repeat_stmt(CardParser.Func_repeat_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link CardParser#func_loop_if_stmt}.
	 * @param ctx the parse tree
	 */
	void enterFunc_loop_if_stmt(CardParser.Func_loop_if_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link CardParser#func_loop_if_stmt}.
	 * @param ctx the parse tree
	 */
	void exitFunc_loop_if_stmt(CardParser.Func_loop_if_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link CardParser#round_if_stmt}.
	 * @param ctx the parse tree
	 */
	void enterRound_if_stmt(CardParser.Round_if_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link CardParser#round_if_stmt}.
	 * @param ctx the parse tree
	 */
	void exitRound_if_stmt(CardParser.Round_if_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link CardParser#round_foreach_stmt}.
	 * @param ctx the parse tree
	 */
	void enterRound_foreach_stmt(CardParser.Round_foreach_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link CardParser#round_foreach_stmt}.
	 * @param ctx the parse tree
	 */
	void exitRound_foreach_stmt(CardParser.Round_foreach_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link CardParser#round_repeat_stmt}.
	 * @param ctx the parse tree
	 */
	void enterRound_repeat_stmt(CardParser.Round_repeat_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link CardParser#round_repeat_stmt}.
	 * @param ctx the parse tree
	 */
	void exitRound_repeat_stmt(CardParser.Round_repeat_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link CardParser#round_loop_if_stmt}.
	 * @param ctx the parse tree
	 */
	void enterRound_loop_if_stmt(CardParser.Round_loop_if_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link CardParser#round_loop_if_stmt}.
	 * @param ctx the parse tree
	 */
	void exitRound_loop_if_stmt(CardParser.Round_loop_if_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link CardParser#block_stmt}.
	 * @param ctx the parse tree
	 */
	void enterBlock_stmt(CardParser.Block_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link CardParser#block_stmt}.
	 * @param ctx the parse tree
	 */
	void exitBlock_stmt(CardParser.Block_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link CardParser#func_block_stmt}.
	 * @param ctx the parse tree
	 */
	void enterFunc_block_stmt(CardParser.Func_block_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link CardParser#func_block_stmt}.
	 * @param ctx the parse tree
	 */
	void exitFunc_block_stmt(CardParser.Func_block_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link CardParser#func_loop_block_stmt}.
	 * @param ctx the parse tree
	 */
	void enterFunc_loop_block_stmt(CardParser.Func_loop_block_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link CardParser#func_loop_block_stmt}.
	 * @param ctx the parse tree
	 */
	void exitFunc_loop_block_stmt(CardParser.Func_loop_block_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link CardParser#round_block_stmt}.
	 * @param ctx the parse tree
	 */
	void enterRound_block_stmt(CardParser.Round_block_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link CardParser#round_block_stmt}.
	 * @param ctx the parse tree
	 */
	void exitRound_block_stmt(CardParser.Round_block_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link CardParser#round_loop_block_stmt}.
	 * @param ctx the parse tree
	 */
	void enterRound_loop_block_stmt(CardParser.Round_loop_block_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link CardParser#round_loop_block_stmt}.
	 * @param ctx the parse tree
	 */
	void exitRound_loop_block_stmt(CardParser.Round_loop_block_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link CardParser#loop_block_stmt}.
	 * @param ctx the parse tree
	 */
	void enterLoop_block_stmt(CardParser.Loop_block_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link CardParser#loop_block_stmt}.
	 * @param ctx the parse tree
	 */
	void exitLoop_block_stmt(CardParser.Loop_block_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link CardParser#break_stmt}.
	 * @param ctx the parse tree
	 */
	void enterBreak_stmt(CardParser.Break_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link CardParser#break_stmt}.
	 * @param ctx the parse tree
	 */
	void exitBreak_stmt(CardParser.Break_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link CardParser#continue_stmt}.
	 * @param ctx the parse tree
	 */
	void enterContinue_stmt(CardParser.Continue_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link CardParser#continue_stmt}.
	 * @param ctx the parse tree
	 */
	void exitContinue_stmt(CardParser.Continue_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link CardParser#return_stmt}.
	 * @param ctx the parse tree
	 */
	void enterReturn_stmt(CardParser.Return_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link CardParser#return_stmt}.
	 * @param ctx the parse tree
	 */
	void exitReturn_stmt(CardParser.Return_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link CardParser#end_stmt}.
	 * @param ctx the parse tree
	 */
	void enterEnd_stmt(CardParser.End_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link CardParser#end_stmt}.
	 * @param ctx the parse tree
	 */
	void exitEnd_stmt(CardParser.End_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link CardParser#function_call}.
	 * @param ctx the parse tree
	 */
	void enterFunction_call(CardParser.Function_callContext ctx);
	/**
	 * Exit a parse tree produced by {@link CardParser#function_call}.
	 * @param ctx the parse tree
	 */
	void exitFunction_call(CardParser.Function_callContext ctx);
	/**
	 * Enter a parse tree produced by {@link CardParser#actual_params}.
	 * @param ctx the parse tree
	 */
	void enterActual_params(CardParser.Actual_paramsContext ctx);
	/**
	 * Exit a parse tree produced by {@link CardParser#actual_params}.
	 * @param ctx the parse tree
	 */
	void exitActual_params(CardParser.Actual_paramsContext ctx);
	/**
	 * Enter a parse tree produced by {@link CardParser#pick_expr}.
	 * @param ctx the parse tree
	 */
	void enterPick_expr(CardParser.Pick_exprContext ctx);
	/**
	 * Exit a parse tree produced by {@link CardParser#pick_expr}.
	 * @param ctx the parse tree
	 */
	void exitPick_expr(CardParser.Pick_exprContext ctx);
	/**
	 * Enter a parse tree produced by {@link CardParser#getint_expr}.
	 * @param ctx the parse tree
	 */
	void enterGetint_expr(CardParser.Getint_exprContext ctx);
	/**
	 * Exit a parse tree produced by {@link CardParser#getint_expr}.
	 * @param ctx the parse tree
	 */
	void exitGetint_expr(CardParser.Getint_exprContext ctx);
	/**
	 * Enter a parse tree produced by {@link CardParser#getstr_expr}.
	 * @param ctx the parse tree
	 */
	void enterGetstr_expr(CardParser.Getstr_exprContext ctx);
	/**
	 * Exit a parse tree produced by {@link CardParser#getstr_expr}.
	 * @param ctx the parse tree
	 */
	void exitGetstr_expr(CardParser.Getstr_exprContext ctx);
	/**
	 * Enter a parse tree produced by {@link CardParser#print_stmt}.
	 * @param ctx the parse tree
	 */
	void enterPrint_stmt(CardParser.Print_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link CardParser#print_stmt}.
	 * @param ctx the parse tree
	 */
	void exitPrint_stmt(CardParser.Print_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link CardParser#deal_stmt}.
	 * @param ctx the parse tree
	 */
	void enterDeal_stmt(CardParser.Deal_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link CardParser#deal_stmt}.
	 * @param ctx the parse tree
	 */
	void exitDeal_stmt(CardParser.Deal_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link CardParser#draw_stmt}.
	 * @param ctx the parse tree
	 */
	void enterDraw_stmt(CardParser.Draw_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link CardParser#draw_stmt}.
	 * @param ctx the parse tree
	 */
	void exitDraw_stmt(CardParser.Draw_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link CardParser#move_stmt}.
	 * @param ctx the parse tree
	 */
	void enterMove_stmt(CardParser.Move_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link CardParser#move_stmt}.
	 * @param ctx the parse tree
	 */
	void exitMove_stmt(CardParser.Move_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link CardParser#play_stmt}.
	 * @param ctx the parse tree
	 */
	void enterPlay_stmt(CardParser.Play_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link CardParser#play_stmt}.
	 * @param ctx the parse tree
	 */
	void exitPlay_stmt(CardParser.Play_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link CardParser#shuffle_stmt}.
	 * @param ctx the parse tree
	 */
	void enterShuffle_stmt(CardParser.Shuffle_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link CardParser#shuffle_stmt}.
	 * @param ctx the parse tree
	 */
	void exitShuffle_stmt(CardParser.Shuffle_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link CardParser#peek_stmt}.
	 * @param ctx the parse tree
	 */
	void enterPeek_stmt(CardParser.Peek_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link CardParser#peek_stmt}.
	 * @param ctx the parse tree
	 */
	void exitPeek_stmt(CardParser.Peek_stmtContext ctx);
}