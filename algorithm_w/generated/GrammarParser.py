# Generated from Grammar.g4 by ANTLR 4.5.3
# encoding: utf-8
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\13")
        buf.write("T\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\5\2#\n\2\3\3\3\3\3\4\3\4\3\5")
        buf.write("\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13")
        buf.write("\7\13\67\n\13\f\13\16\13:\13\13\3\13\3\13\3\13\3\13\3")
        buf.write("\13\5\13A\n\13\3\f\3\f\3\f\3\f\3\f\7\fH\n\f\f\f\16\fK")
        buf.write("\13\f\3\r\3\r\3\r\3\r\3\r\5\rR\n\r\3\r\2\3\26\16\2\4\6")
        buf.write("\b\n\f\16\20\22\24\26\30\2\2L\2\"\3\2\2\2\4$\3\2\2\2\6")
        buf.write("&\3\2\2\2\b(\3\2\2\2\n*\3\2\2\2\f,\3\2\2\2\16.\3\2\2\2")
        buf.write("\20\60\3\2\2\2\22\62\3\2\2\2\24@\3\2\2\2\26B\3\2\2\2\30")
        buf.write("Q\3\2\2\2\32\33\5\4\3\2\33\34\5\b\5\2\34\35\5\n\6\2\35")
        buf.write("\36\5\2\2\2\36\37\5\6\4\2\37 \5\2\2\2 #\3\2\2\2!#\5\24")
        buf.write("\13\2\"\32\3\2\2\2\"!\3\2\2\2#\3\3\2\2\2$%\7\3\2\2%\5")
        buf.write("\3\2\2\2&\'\7\4\2\2\'\7\3\2\2\2()\7\5\2\2)\t\3\2\2\2*")
        buf.write("+\7\6\2\2+\13\3\2\2\2,-\7\7\2\2-\r\3\2\2\2./\7\b\2\2/")
        buf.write("\17\3\2\2\2\60\61\7\n\2\2\61\21\3\2\2\2\62\63\7\t\2\2")
        buf.write("\63\23\3\2\2\2\64A\5\26\f\2\65\67\5\26\f\2\66\65\3\2\2")
        buf.write("\2\67:\3\2\2\28\66\3\2\2\289\3\2\2\29;\3\2\2\2:8\3\2\2")
        buf.write("\2;<\5\20\t\2<=\5\b\5\2=>\5\22\n\2>?\5\24\13\2?A\3\2\2")
        buf.write("\2@\64\3\2\2\2@8\3\2\2\2A\25\3\2\2\2BC\b\f\1\2CD\5\30")
        buf.write("\r\2DI\3\2\2\2EF\f\4\2\2FH\5\30\r\2GE\3\2\2\2HK\3\2\2")
        buf.write("\2IG\3\2\2\2IJ\3\2\2\2J\27\3\2\2\2KI\3\2\2\2LM\5\f\7\2")
        buf.write("MN\5\2\2\2NO\5\16\b\2OR\3\2\2\2PR\5\b\5\2QL\3\2\2\2QP")
        buf.write("\3\2\2\2R\31\3\2\2\2\7\"8@IQ")
        return buf.getvalue()


class GrammarParser ( Parser ):

    grammarFileName = "Grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'let'", "'in'", "<INVALID>", "'='", "'('", 
                     "')'", "'.'", "'\\'" ]

    symbolicNames = [ "<INVALID>", "LET", "IN", "VAR", "EQ", "LPAR", "RPAR", 
                      "DOT", "LAMBDA", "WHITESPACE" ]

    RULE_expression = 0
    RULE_let = 1
    RULE_myIn = 2
    RULE_var = 3
    RULE_myEquals = 4
    RULE_lpar = 5
    RULE_rpar = 6
    RULE_myLabmda = 7
    RULE_dot = 8
    RULE_abstraction = 9
    RULE_application = 10
    RULE_atom = 11

    ruleNames =  [ "expression", "let", "myIn", "var", "myEquals", "lpar", 
                   "rpar", "myLabmda", "dot", "abstraction", "application", 
                   "atom" ]

    EOF = Token.EOF
    LET=1
    IN=2
    VAR=3
    EQ=4
    LPAR=5
    RPAR=6
    DOT=7
    LAMBDA=8
    WHITESPACE=9

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.5.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def let(self):
            return self.getTypedRuleContext(GrammarParser.LetContext,0)


        def var(self):
            return self.getTypedRuleContext(GrammarParser.VarContext,0)


        def myEquals(self):
            return self.getTypedRuleContext(GrammarParser.MyEqualsContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ExpressionContext,i)


        def myIn(self):
            return self.getTypedRuleContext(GrammarParser.MyInContext,0)


        def abstraction(self):
            return self.getTypedRuleContext(GrammarParser.AbstractionContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = GrammarParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_expression)
        try:
            self.state = 32
            token = self._input.LA(1)
            if token in [GrammarParser.LET]:
                self.enterOuterAlt(localctx, 1)
                self.state = 24
                self.let()
                self.state = 25
                self.var()
                self.state = 26
                self.myEquals()
                self.state = 27
                self.expression()
                self.state = 28
                self.myIn()
                self.state = 29
                self.expression()

            elif token in [GrammarParser.VAR, GrammarParser.LPAR, GrammarParser.LAMBDA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 31
                self.abstraction()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LetContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LET(self):
            return self.getToken(GrammarParser.LET, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_let

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLet" ):
                listener.enterLet(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLet" ):
                listener.exitLet(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLet" ):
                return visitor.visitLet(self)
            else:
                return visitor.visitChildren(self)




    def let(self):

        localctx = GrammarParser.LetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_let)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(GrammarParser.LET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MyInContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IN(self):
            return self.getToken(GrammarParser.IN, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_myIn

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMyIn" ):
                listener.enterMyIn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMyIn" ):
                listener.exitMyIn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMyIn" ):
                return visitor.visitMyIn(self)
            else:
                return visitor.visitChildren(self)




    def myIn(self):

        localctx = GrammarParser.MyInContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_myIn)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.match(GrammarParser.IN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VarContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(GrammarParser.VAR, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_var

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar" ):
                listener.enterVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar" ):
                listener.exitVar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)




    def var(self):

        localctx = GrammarParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(GrammarParser.VAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MyEqualsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(GrammarParser.EQ, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_myEquals

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMyEquals" ):
                listener.enterMyEquals(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMyEquals" ):
                listener.exitMyEquals(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMyEquals" ):
                return visitor.visitMyEquals(self)
            else:
                return visitor.visitChildren(self)




    def myEquals(self):

        localctx = GrammarParser.MyEqualsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_myEquals)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(GrammarParser.EQ)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LparContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAR(self):
            return self.getToken(GrammarParser.LPAR, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_lpar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLpar" ):
                listener.enterLpar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLpar" ):
                listener.exitLpar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLpar" ):
                return visitor.visitLpar(self)
            else:
                return visitor.visitChildren(self)




    def lpar(self):

        localctx = GrammarParser.LparContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_lpar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(GrammarParser.LPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RparContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RPAR(self):
            return self.getToken(GrammarParser.RPAR, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_rpar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRpar" ):
                listener.enterRpar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRpar" ):
                listener.exitRpar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRpar" ):
                return visitor.visitRpar(self)
            else:
                return visitor.visitChildren(self)




    def rpar(self):

        localctx = GrammarParser.RparContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_rpar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(GrammarParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MyLabmdaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LAMBDA(self):
            return self.getToken(GrammarParser.LAMBDA, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_myLabmda

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMyLabmda" ):
                listener.enterMyLabmda(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMyLabmda" ):
                listener.exitMyLabmda(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMyLabmda" ):
                return visitor.visitMyLabmda(self)
            else:
                return visitor.visitChildren(self)




    def myLabmda(self):

        localctx = GrammarParser.MyLabmdaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_myLabmda)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(GrammarParser.LAMBDA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DotContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(GrammarParser.DOT, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_dot

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDot" ):
                listener.enterDot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDot" ):
                listener.exitDot(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDot" ):
                return visitor.visitDot(self)
            else:
                return visitor.visitChildren(self)




    def dot(self):

        localctx = GrammarParser.DotContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_dot)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(GrammarParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AbstractionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def application(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ApplicationContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ApplicationContext,i)


        def myLabmda(self):
            return self.getTypedRuleContext(GrammarParser.MyLabmdaContext,0)


        def var(self):
            return self.getTypedRuleContext(GrammarParser.VarContext,0)


        def dot(self):
            return self.getTypedRuleContext(GrammarParser.DotContext,0)


        def abstraction(self):
            return self.getTypedRuleContext(GrammarParser.AbstractionContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_abstraction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAbstraction" ):
                listener.enterAbstraction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAbstraction" ):
                listener.exitAbstraction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAbstraction" ):
                return visitor.visitAbstraction(self)
            else:
                return visitor.visitChildren(self)




    def abstraction(self):

        localctx = GrammarParser.AbstractionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_abstraction)
        self._la = 0 # Token type
        try:
            self.state = 62
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 50
                self.application(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 54
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==GrammarParser.VAR or _la==GrammarParser.LPAR:
                    self.state = 51
                    self.application(0)
                    self.state = 56
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 57
                self.myLabmda()
                self.state = 58
                self.var()
                self.state = 59
                self.dot()
                self.state = 60
                self.abstraction()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ApplicationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self):
            return self.getTypedRuleContext(GrammarParser.AtomContext,0)


        def application(self):
            return self.getTypedRuleContext(GrammarParser.ApplicationContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_application

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterApplication" ):
                listener.enterApplication(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitApplication" ):
                listener.exitApplication(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitApplication" ):
                return visitor.visitApplication(self)
            else:
                return visitor.visitChildren(self)



    def application(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = GrammarParser.ApplicationContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_application, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.atom()
            self._ctx.stop = self._input.LT(-1)
            self.state = 71
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = GrammarParser.ApplicationContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_application)
                    self.state = 67
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 68
                    self.atom() 
                self.state = 73
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class AtomContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lpar(self):
            return self.getTypedRuleContext(GrammarParser.LparContext,0)


        def expression(self):
            return self.getTypedRuleContext(GrammarParser.ExpressionContext,0)


        def rpar(self):
            return self.getTypedRuleContext(GrammarParser.RparContext,0)


        def var(self):
            return self.getTypedRuleContext(GrammarParser.VarContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = GrammarParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_atom)
        try:
            self.state = 79
            token = self._input.LA(1)
            if token in [GrammarParser.LPAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 74
                self.lpar()
                self.state = 75
                self.expression()
                self.state = 76
                self.rpar()

            elif token in [GrammarParser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 78
                self.var()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[10] = self.application_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def application_sempred(self, localctx:ApplicationContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         




