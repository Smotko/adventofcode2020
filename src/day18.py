from .utils import *
import ply.lex as lex


tokens = (
    "NUMBER",
    "PLUS",
    "TIMES",
    "LPAREN",
    "RPAREN",
)

t_PLUS = r"\+"
t_TIMES = r"\*"
t_LPAREN = r"\("
t_RPAREN = r"\)"

t_ignore = " "


def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)


def t_NUMBER(t):
    r"\d+"
    t.value = int(t.value)
    return t


def t_error(t):
    error("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()


import ply.yacc as yacc

# Get the token map from the lexer.  This is required.


def p_expression_plus(p):
    "expression : expression PLUS factor"
    p[0] = p[1] + p[3]


def p_expression_minus(p):
    "expression : expression TIMES factor"
    p[0] = p[1] * p[3]


def p_expression_term(p):
    "expression : factor"
    p[0] = p[1]


def p_factor_num(p):
    "factor : NUMBER"
    p[0] = p[1]


def p_factor_expr(p):
    "factor : LPAREN expression RPAREN"
    p[0] = p[2]


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")


# Build the parser
parser = yacc.yacc()


def compute(inp):
    lexer.input(inp)
    result = parser.parse(inp)
    info(result)
    return result


def run():
    assert compute("1 + 2 * 3 + 4 * 5 + 6") == 71
    assert compute("1 + (2 * 3) + (4 * (5 + 6))") == 51
    info(sum(compute(i) for i in get_input(18)))