# Generated from Grammar.g4 by ANTLR 4.5.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GrammarParser import GrammarParser
else:
    from generated.GrammarParser import GrammarParser

# This class defines a complete listener for a parse tree produced by GrammarParser.
class GrammarListener(ParseTreeListener):

    # Enter a parse tree produced by GrammarParser#expression.
    def enterExpression(self, ctx:GrammarParser.ExpressionContext):
        pass

    # Exit a parse tree produced by GrammarParser#expression.
    def exitExpression(self, ctx:GrammarParser.ExpressionContext):
        pass


    # Enter a parse tree produced by GrammarParser#let.
    def enterLet(self, ctx:GrammarParser.LetContext):
        pass

    # Exit a parse tree produced by GrammarParser#let.
    def exitLet(self, ctx:GrammarParser.LetContext):
        pass


    # Enter a parse tree produced by GrammarParser#myIn.
    def enterMyIn(self, ctx:GrammarParser.MyInContext):
        pass

    # Exit a parse tree produced by GrammarParser#myIn.
    def exitMyIn(self, ctx:GrammarParser.MyInContext):
        pass


    # Enter a parse tree produced by GrammarParser#var.
    def enterVar(self, ctx:GrammarParser.VarContext):
        pass

    # Exit a parse tree produced by GrammarParser#var.
    def exitVar(self, ctx:GrammarParser.VarContext):
        pass


    # Enter a parse tree produced by GrammarParser#myEquals.
    def enterMyEquals(self, ctx:GrammarParser.MyEqualsContext):
        pass

    # Exit a parse tree produced by GrammarParser#myEquals.
    def exitMyEquals(self, ctx:GrammarParser.MyEqualsContext):
        pass


    # Enter a parse tree produced by GrammarParser#lpar.
    def enterLpar(self, ctx:GrammarParser.LparContext):
        pass

    # Exit a parse tree produced by GrammarParser#lpar.
    def exitLpar(self, ctx:GrammarParser.LparContext):
        pass


    # Enter a parse tree produced by GrammarParser#rpar.
    def enterRpar(self, ctx:GrammarParser.RparContext):
        pass

    # Exit a parse tree produced by GrammarParser#rpar.
    def exitRpar(self, ctx:GrammarParser.RparContext):
        pass


    # Enter a parse tree produced by GrammarParser#myLabmda.
    def enterMyLabmda(self, ctx:GrammarParser.MyLabmdaContext):
        pass

    # Exit a parse tree produced by GrammarParser#myLabmda.
    def exitMyLabmda(self, ctx:GrammarParser.MyLabmdaContext):
        pass


    # Enter a parse tree produced by GrammarParser#dot.
    def enterDot(self, ctx:GrammarParser.DotContext):
        pass

    # Exit a parse tree produced by GrammarParser#dot.
    def exitDot(self, ctx:GrammarParser.DotContext):
        pass


    # Enter a parse tree produced by GrammarParser#abstraction.
    def enterAbstraction(self, ctx:GrammarParser.AbstractionContext):
        pass

    # Exit a parse tree produced by GrammarParser#abstraction.
    def exitAbstraction(self, ctx:GrammarParser.AbstractionContext):
        pass


    # Enter a parse tree produced by GrammarParser#application.
    def enterApplication(self, ctx:GrammarParser.ApplicationContext):
        pass

    # Exit a parse tree produced by GrammarParser#application.
    def exitApplication(self, ctx:GrammarParser.ApplicationContext):
        pass


    # Enter a parse tree produced by GrammarParser#atom.
    def enterAtom(self, ctx:GrammarParser.AtomContext):
        pass

    # Exit a parse tree produced by GrammarParser#atom.
    def exitAtom(self, ctx:GrammarParser.AtomContext):
        pass


