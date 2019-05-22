from antlr4 import *

from generated.GrammarLexer import GrammarLexer
from generated.GrammarParser import GrammarParser
from CustomVisitor import CustomVisitor, Application, Abstraction, Variable, LetIn


fin = open('task3.in')
fout = open('task3.out', 'w')


class TValue:
    def __init__(self, val):
        self.val = val

    def __eq__(self, other):
        return self.val == other.val

    def replace(self, old, new):
        print(self.val, old, new)
        if self.val == old:
            self.val = new

    def checkCorrectness(self, value):
        return self == value

    def __contains__(self, item):
        if isinstance(item, TValue):
            return self == item
        elif isinstance(item, str):
            return self.val == item

    def getText(self):
        return self.val


class TImplication:
    def __init__(self, P, Q):
        self.left = P
        self.right = Q

    def checkCorrectness(self, value):
        return self.left.checkCorrectness(value) or self.right.checkCorrectness(value)

    def replace(self, old, new):
        self.left.replace(old, new)
        self.right.replace(old, new)

    def __contains__(self, item):
        return item in self.left and item in self.right

    def getText(self):
        return '({0} -> {1})'.format(self.left.getText(), self.right.getText())


class TForAll:
    def __init__(self, foralls, expr):
        self.vars = foralls
        self.expr = expr

    def checkCorrectness(self, value):
        return self.expr.checkCorrectness(value)

    def replace(self, old, new):
        self.expr.replace(old, new)

    def __contains__(self, item):
        return item in self.expr

    def getText(self):
        text = ''
        for item in self.vars:
            text += '\\' + item
        text += '.' + self.expr.getText()
        return text


typeCounter = 0
obsoleteTypeCounter = 0
reserveCounter = 0
variableCounter = 0
typeExistence = True


def getNextType():
    global typeCounter
    curType = 't' + str(typeCounter)
    typeCounter += 1
    return curType


def getNextObsoleteType():
    global obsoleteTypeCounter
    curType = 'z' + str(obsoleteTypeCounter)
    obsoleteTypeCounter += 1
    return curType


def getNextReserve():
    global reserveCounter
    curType = 'RES' + str(reserveCounter)
    reserveCounter += 1
    return curType


def getNextVariable():
    global variableCounter
    curVar = 'v' + str(variableCounter)
    variableCounter += 1
    return curVar #curwa


def checkTImplicationCorrectness(value, implication):
    return implication.checkCorrectness(value)


def doReplace(location, oldValue, newValue):
    if isinstance(location, TValue):
        if oldValue in location:
            return newValue
        else:
            return location
    elif isinstance(location, TImplication):
        return TImplication(doReplace(location.left, oldValue, newValue), doReplace(location.right, oldValue, newValue))
    elif isinstance(location, TForAll):
        return TForAll(location.vars, doReplace(location.expr, oldValue, newValue))
    elif isinstance(location, Application):
        return Application(doReplace(location.left, oldValue, newValue), doReplace(location.right, oldValue, newValue))
    elif isinstance(location, Abstraction):

        return Abstraction(doReplace(TValue(location.var), oldValue, newValue).getText(), doReplace(location.expr, oldValue, newValue))
    elif isinstance(location, Variable):
        if location.name == oldValue.getText():
            return Variable(newValue.getText())
        else:
            return location
    elif isinstance(location, LetIn):
        return LetIn(doReplace(location.var, oldValue, newValue), doReplace(location.P, oldValue, newValue), doReplace(location.Q, oldValue, newValue))


unificationMap = dict()
replacementMap = dict()


def offlineReplace(location):
    if isinstance(location, Application):
        return Application(offlineReplace(location.left), offlineReplace(location.right))
    elif isinstance(location, Variable):
        if location.name in replacementMap:
            return Variable(replacementMap[location.name])
        else:
            return location
    elif isinstance(location, Abstraction):
        if location.var in replacementMap:
            oldValue = replacementMap[location.var]
            newValue = replacementMap[location.var] = getNextVariable()
            result = offlineReplace(location.expr)
            replacementMap[location.var] = oldValue
            return Abstraction(newValue, result)
        else:
            replacementMap[location.var] = getNextVariable()
            result = offlineReplace(location.expr)
            popped = replacementMap.pop(location.var)
            return Abstraction(popped, result)
    elif isinstance(location, LetIn):
        if location.var in replacementMap:
            oldValue = replacementMap[location.var]
            newValue = replacementMap[location.var] = getNextVariable()
            P = offlineReplace(location.P)
            Q = offlineReplace(location.Q)
            replacementMap[location.var] = oldValue
            return LetIn(newValue, P, Q)
        else:
            replacementMap[location.var] = getNextVariable()
            P = offlineReplace(location.P)
            Q = offlineReplace(location.Q)
            popped = replacementMap.pop(location.var)
            return LetIn(popped, P, Q)


def unify(l, r):
    global typeExistence
    
    leftPart = []
    rightPart = []
    for eq in l:
        leftPart.append(eq)
    for eq in r:
        rightPart.append(eq)

    i = 0
    while i < len(leftPart):
        if isinstance(leftPart[i], TValue):
            if isinstance(rightPart[i], TValue):
                if leftPart[i] == rightPart[i]:
                    unificationMap[leftPart[i].getText()] = rightPart[i]
                    leftPart.pop(i)
                    rightPart.pop(i)
                    i -= 1
                else:
                    unificationMap[leftPart[i].getText()] = rightPart[i]
                    for j in range(len(leftPart)):
                        if j != i:
                            leftPart[j] = doReplace(leftPart[j], leftPart[i], rightPart[i])
                            rightPart[j] = doReplace(rightPart[j], leftPart[i], rightPart[i])

            elif isinstance(rightPart[i], (TImplication, TForAll)):
                unificationMap[leftPart[i].getText()] = rightPart[i]
                for j in range(len(leftPart)):
                    if j != i:
                        leftPart[j] = doReplace(leftPart[j], leftPart[i], rightPart[i])
                        rightPart[j] = doReplace(rightPart[j], leftPart[i], rightPart[i])

        elif isinstance(leftPart[i], TImplication):
            if isinstance(rightPart[i], TValue):
                leftPart.append(rightPart[i])
                rightPart.append(leftPart[i])
                leftPart.pop(i)
                rightPart.pop(i)
                i -= 1
            elif isinstance(rightPart[i], TImplication):
                leftPart.append(leftPart[i].left)
                leftPart.append(leftPart[i].right)
                rightPart.append(rightPart[i].left)
                rightPart.append(rightPart[i].right)
                leftPart.pop(i)
                rightPart.pop(i)
                i -= 1
            elif isinstance(rightPart, TForAll):
                typeExistence = False

        for j in range(len(leftPart)):
            if isinstance(leftPart[j], TValue):
                if isinstance(rightPart[j], (TImplication, TForAll)):
                    if rightPart[j].checkCorrectness(leftPart[j]):
                        typeExistence = False
                        break

        if not typeExistence:
            return dict()

        i += 1

    system = dict()

    for i in range(len(leftPart)):
        system[leftPart[i].getText()] = rightPart[i]

    return system


def discardForall(TYPE):
    if isinstance(TYPE, TForAll):
        ans = TYPE.expr
        for var in TYPE.vars:
            ans = doReplace(ans, TValue(var), TValue(getNextObsoleteType()))
        return ans
    elif isinstance(TYPE, TImplication):
        return TImplication(discardForall(TYPE.left), discardForall(TYPE.right))
    elif isinstance(TYPE, TValue):
        return TYPE


def substitution(s, context):
    if s is None:
        return context

    if context is None:
        return s

    if isinstance(context, (TImplication, TValue, TForAll)):
        if context.getText() in s:
            return s[context.getText()]
        else:
            return context

    result = dict()
    for key, value in context.items():
        result[key] = value

    for key, value in s.items():
        result[key] = value
        for rkey, rvalue in result.items():
            result[rkey] = doReplace(rvalue, TValue(key), value)

    return result


def substituteFromUMap(TYPE):
    return unificationMap[TYPE.getText()] if TYPE.getText() in unificationMap else TYPE


equations = [[], []]


def getFreeValues(TYPE):
    if isinstance(TYPE, TValue):
        return [TYPE.getText()]
    elif isinstance(TYPE, TImplication):
        left = getFreeValues(TYPE.left)
        right = getFreeValues(TYPE.right)
        res = list(set(left).union(set(right)))
        return sorted(res)
    elif isinstance(TYPE, TForAll):
        right = getFreeValues(TYPE.expr)
        res = []
        for item in right:
            if item not in TYPE.vars and item not in res:
                res.append(item)
        return sorted(res)


def eqToDict(l):
    if isinstance(l, dict):
        return l
    res = dict()
    if len(l) > 1:
        for i in range(len(l[0])):
            res[l[0][i].getText()] = l[1][i]
    return res


def W(context, expression):
    if isinstance(expression, Variable):
        expression = expression.name
        if expression not in context:
            context[expression] = TValue(getNextType())
        returnType = discardForall(context[expression])

        return dict(), returnType
    elif isinstance(expression, Abstraction):
        localG = dict()
        for key, value in context.items():
            localG[key] = value
        localG[expression.var] = TValue(getNextType())

        system1, rightPart = W(localG, expression.expr)

        newSystem1 = dict()
        for key, value in system1.items():
            newSystem1[key] = value

        if localG[expression.var].getText() in newSystem1:
            localG[expression.var] = newSystem1[localG[expression.var].getText()]

        leftPart = localG.pop(expression.var)

        return system1, TImplication(substitution(newSystem1, leftPart), rightPart)

    elif isinstance(expression, Application):

        system1, leftPart = W(context, expression.left)



        newSystem1 = dict()
        for key, value in system1.items():
            newSystem1[key] = value

        system2, rightPart = W(substitution(newSystem1, context), expression.right)

        newSystem2 = dict()
        for key, value in system2.items():
            newSystem2[key] = value

        newType = TValue(getNextType())

        eq = [
            [
                substitution(newSystem2, leftPart)
            ],
            [
                TImplication(rightPart, newType)
            ]
        ]

        system3 = doUnify(eq)

        return substitution(system3, substitution(newSystem2, newSystem1)), substitution(system3, newType)

    elif isinstance(expression, LetIn):
        system1, leftPart = W(context, expression.P)

        newSystem1 = dict()
        for key, value in system1.items():
            newSystem1[key] = value

        localG = dict()
        for key, value in context.items():
            localG[key] = value

        localG[expression.var] = TForAll(getFreeValues(leftPart), leftPart)

        system2, rightPart = W(substitution(newSystem1, localG), expression.Q)

        newSystem2 = dict()
        for key, value in system2.items():
            newSystem2[key] = value

        return substitution(newSystem1, newSystem2), rightPart


def makeSystem(system, expression, unificator):
    if isinstance(expression, Variable):
        expression = expression.getText()
        if expression not in system:
            system[expression] = TValue(getNextType())
        returnType = discardForall(system[expression])
        return system, returnType, eqToDict(unificator)

    elif isinstance(expression, Abstraction):
        system[expression.var] = TValue(getNextType())
        s1, rightPart, un1 = makeSystem(system, expression.expr, unificator)
        newS1 = dict()
        for key, value in un1.items():
            newS1[key] = value
        leftPart = system[expression.var]
        system.pop(expression.var)
        return system, TImplication(substitution(newS1, leftPart), rightPart), newS1

    elif isinstance(expression, Application):
        s1, leftPart, un1 = makeSystem(system, expression.left, unificator)
        newS1 = dict()
        for key, value in un1.items():
            newS1[key] = value
        s2, rightPart, un2 = makeSystem(system, expression.right, unificator)
        newS2 = dict()
        for key, value in un2.items():
            newS2[key] = value
        curType = TValue(getNextType())
        equations[0].append(leftPart)
        equations[1].append(TImplication(rightPart, curType))
        unificator = [[], []]
        unificator[0].append(substitution(newS2, leftPart))
        unificator[1].append(TImplication(rightPart, curType))
        s3 = doUnify(unificator)
        return system, substitution(s3, curType), substitution(s3, substitution(newS2, newS1))

    elif isinstance(expression, LetIn):
        s1, leftPart, un1 = makeSystem(system, expression.P, unificator)
        newS1 = dict()
        for key, value in un1.items():
            newS1[key] = value
        system[expression.var] = TForAll(getFreeValues(leftPart), leftPart)
        s2, rightPart, un2 = makeSystem(system, expression.Q, unificator)
        newS2 = dict()
        for key, value in un2.items():
            newS1[key] = value
        system.pop(expression.var)
        return system, rightPart, substitution(newS1, newS2)


def printList(l):
    if len(l) == 0:
        return
    for i in range(len(l[0])):
        print('{0} = {1}'.format(l[0][i].getText(), l[1][i].getText()))


def doUnify(equations):
    res = unify(equations[0], equations[1])
    return res


def printDict(d):
    for key, value in d.items():
        print('{0}: {1}'.format(key, value.getText()))


def solve():
    global typeCounter, typeExistence, system
    dataStream = FileStream(fin.name)
    lexer = GrammarLexer(dataStream)
    stream = CommonTokenStream(lexer)
    parser = GrammarParser(stream)
    tree = parser.expression()
    visitor = CustomVisitor()
    newTree = visitor.visit(tree)
    replacedTree = offlineReplace(newTree)
    system = dict()
    resultSystem, TYPE = W(system, replacedTree)

    if typeExistence:
        print('final type:', TYPE.getText(), file = fout)
    else:
        print("Expression has no type", file = fout)
        return


def main():
    solve()


if __name__ == '__main__':
    main()