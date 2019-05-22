# Generated from Grammar.g4 by ANTLR 4.5.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GrammarParser import GrammarParser
else:
    from generated.GrammarParser import GrammarParser

# This class defines a complete generic visitor for a parse tree produced by GrammarParser.

class GrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GrammarParser#expression.
    def visitExpression(self, ctx:GrammarParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#let.
    def visitLet(self, ctx:GrammarParser.LetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#myIn.
    def visitMyIn(self, ctx:GrammarParser.MyInContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#var.
    def visitVar(self, ctx:GrammarParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#myEquals.
    def visitMyEquals(self, ctx:GrammarParser.MyEqualsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#lpar.
    def visitLpar(self, ctx:GrammarParser.LparContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#rpar.
    def visitRpar(self, ctx:GrammarParser.RparContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#myLabmda.
    def visitMyLabmda(self, ctx:GrammarParser.MyLabmdaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#dot.
    def visitDot(self, ctx:GrammarParser.DotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#abstraction.
    def visitAbstraction(self, ctx:GrammarParser.AbstractionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#application.
    def visitApplication(self, ctx:GrammarParser.ApplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#atom.
    def visitAtom(self, ctx:GrammarParser.AtomContext):
        return self.visitChildren(ctx)



del GrammarParser