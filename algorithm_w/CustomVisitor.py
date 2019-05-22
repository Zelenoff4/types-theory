from generated.GrammarParser import GrammarParser
from generated.GrammarVisitor import ParseTreeVisitor


class Variable:
    def __init__(self, name_):
        self.name = name_

    def getText(self):
        return self.name


class Application:
    def __init__(self, P, Q):
        self.left = P
        self.right = Q

    def getText(self):
        return self.left.getText() + ' ' + self.right.getText()


class Abstraction:
    def __init__(self, var_, expr_):
        self.var = var_
        self.expr = expr_

    def getText(self):
        return '(\\' + self.var + '.(' + self.expr.getText() + '))'


class LetIn:
    def __init__(self, var, P, Q):
        self.var = var
        self.P = P
        self.Q = Q

    def getText(self):
        return 'let {0} = ({1}) in ({2})'.format(self.var, self.P.getText(), self.Q.getText())


class CustomVisitor(ParseTreeVisitor):
    # Visit a parse tree produced by GrammarParser#expression.
    def visitExpression(self, ctx:GrammarParser.ExpressionContext):
        children = ctx.children
        if len(children) > 1:
            return LetIn(
                self.visitVar(children[1]),
                self.visitExpression(children[3]),
                self.visitExpression(children[5])
            )
            # return Application(
            #     Abstraction(self.visitVar(children[1]), self.visitExpression(children[5])),
            #     self.visitExpression(children[3])
            # )
        else:
            return self.visitAbstraction(children[0])

    # Visit a parse tree produced by GrammarParser#abstraction.
    def visitAbstraction(self, ctx: GrammarParser.AbstractionContext):
        children = ctx.children
        if len(children) > 1:
            return Abstraction(
                self.visitVar(children[1]),
                self.visitAbstraction(children[3])
            )
        else:
            return self.visitApplication(children[0])


    # Visit a parse tree produced by GrammarParser#application.
    def visitApplication(self, ctx: GrammarParser.ApplicationContext):
        children = ctx.children
        if len(children) > 1:
            return Application(
                self.visitApplication(children[0]),
                self.visitAtom(children[1])
            )
        else:
            return self.visitAtom(children[0])

    # Visit a parse tree produced by GrammarParser#atom.
    def visitAtom(self, ctx: GrammarParser.AtomContext):
        children = ctx.children
        if len(children) > 1:
            return self.visitExpression(children[1])
        else:
            return Variable(self.visitVar(children[0]))

    # Visit a parse tree produced by GrammarParser#let.
    def visitLet(self, ctx:GrammarParser.LetContext):
        return ctx.getText()


    # Visit a parse tree produced by GrammarParser#myIn.
    def visitMyIn(self, ctx:GrammarParser.MyInContext):
        return ctx.getText()


    # Visit a parse tree produced by GrammarParser#var.
    def visitVar(self, ctx:GrammarParser.VarContext):
        return ctx.getText()


    # Visit a parse tree produced by GrammarParser#myEquals.
    def visitMyEquals(self, ctx:GrammarParser.MyEqualsContext):
        return ctx.getText()


    # Visit a parse tree produced by GrammarParser#lpar.
    def visitLpar(self, ctx:GrammarParser.LparContext):
        return ctx.getText()


    # Visit a parse tree produced by GrammarParser#rpar.
    def visitRpar(self, ctx:GrammarParser.RparContext):
        return ctx.getText()


    # Visit a parse tree produced by GrammarParser#myLabmda.
    def visitMyLabmda(self, ctx:GrammarParser.MyLabmdaContext):
        return ctx.getText()


    # Visit a parse tree produced by GrammarParser#dot.
    def visitDot(self, ctx:GrammarParser.DotContext):
        return ctx.getText()

