import sys
from antlr4 import *
from antlr_src.CardLexer import CardLexer
from antlr_src.CardParser import CardParser
from antlr_src.CardVisitor import CardVisitor

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = CardLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CardParser(stream)
    tree = parser.start_()
    if parser.getNumberOfSyntaxErrors() > 0:
        print("syntax errors")
    else:
        vinterp = CardVisitor()
        vinterp.visit(tree)

if __name__ == '__main__':
    main(sys.argv)