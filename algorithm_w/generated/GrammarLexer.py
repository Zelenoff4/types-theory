# Generated from Grammar.g4 by ANTLR 4.5.3
from antlr4 import *
from io import StringIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2\13")
        buf.write(":\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\3\2\3\2")
        buf.write("\3\2\3\3\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\6\7\6(\n\6")
        buf.write("\f\6\16\6+\13\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3")
        buf.write("\13\3\f\3\f\3\f\3\f\2\2\r\3\3\5\4\7\2\t\2\13\5\r\6\17")
        buf.write("\7\21\b\23\t\25\n\27\13\3\2\5\4\2C\\c|\3\2\62;\5\2\13")
        buf.write("\f\17\17\"\"9\2\3\3\2\2\2\2\5\3\2\2\2\2\13\3\2\2\2\2\r")
        buf.write("\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3")
        buf.write("\2\2\2\2\27\3\2\2\2\3\31\3\2\2\2\5\35\3\2\2\2\7 \3\2\2")
        buf.write("\2\t\"\3\2\2\2\13$\3\2\2\2\r,\3\2\2\2\17.\3\2\2\2\21\60")
        buf.write("\3\2\2\2\23\62\3\2\2\2\25\64\3\2\2\2\27\66\3\2\2\2\31")
        buf.write("\32\7n\2\2\32\33\7g\2\2\33\34\7v\2\2\34\4\3\2\2\2\35\36")
        buf.write("\7k\2\2\36\37\7p\2\2\37\6\3\2\2\2 !\t\2\2\2!\b\3\2\2\2")
        buf.write("\"#\t\3\2\2#\n\3\2\2\2$)\5\7\4\2%(\5\7\4\2&(\5\t\5\2\'")
        buf.write("%\3\2\2\2\'&\3\2\2\2(+\3\2\2\2)\'\3\2\2\2)*\3\2\2\2*\f")
        buf.write("\3\2\2\2+)\3\2\2\2,-\7?\2\2-\16\3\2\2\2./\7*\2\2/\20\3")
        buf.write("\2\2\2\60\61\7+\2\2\61\22\3\2\2\2\62\63\7\60\2\2\63\24")
        buf.write("\3\2\2\2\64\65\7^\2\2\65\26\3\2\2\2\66\67\t\4\2\2\678")
        buf.write("\3\2\2\289\b\f\2\29\30\3\2\2\2\5\2\')\3\b\2\2")
        return buf.getvalue()


class GrammarLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]


    LET = 1
    IN = 2
    VAR = 3
    EQ = 4
    LPAR = 5
    RPAR = 6
    DOT = 7
    LAMBDA = 8
    WHITESPACE = 9

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'let'", "'in'", "'='", "'('", "')'", "'.'", "'\\'" ]

    symbolicNames = [ "<INVALID>",
            "LET", "IN", "VAR", "EQ", "LPAR", "RPAR", "DOT", "LAMBDA", "WHITESPACE" ]

    ruleNames = [ "LET", "IN", "LITERAL", "DIGIT", "VAR", "EQ", "LPAR", 
                  "RPAR", "DOT", "LAMBDA", "WHITESPACE" ]

    grammarFileName = "Grammar.g4"

    def __init__(self, input=None):
        super().__init__(input)
        self.checkVersion("4.5.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


