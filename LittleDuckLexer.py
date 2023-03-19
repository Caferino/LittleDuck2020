# coding=utf-8
"""
    Tarea-3.2
    Autor: Óscar Antonio Hinojosa Salum A00821930
    Marzo 18 2023
    Programa Python "Little Duck 2020" como ejemplo de
    un analizador de léxico (LittleDuckLexer.py) y 
    un analizador de sintáxis (LittleDuckParser.py).
"""

import ply.lex as lex

# Palabras Clave

keywords = {
    'program': 'PROGRAM',
    'print': 'PRINT',
    'if': 'IF',
    'else': 'ELSE',
    'var': 'VAR',
    'int': 'INT',
    'float': 'FLOAT',

}


# Tokens

tokens = ['SEMICOLON', 'LEFTBRACKET', 'RIGHTBRACKET', 'GREATER', 'LESS', 'NOTEQUAL', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
          'LEFTPAREN', 'RIGHTPAREN', 'ID', 'CTEI', 'CTEF', 'COLON', 'EQUALS', 'CTESTRING', 'COMMA', 'PROGRAM', 'PRINT',
          'IF', 'ELSE', 'VAR', 'INT', 'FLOAT']


# Expresiones Regulares de Operadores

t_SEMICOLON = r'\;'
t_LEFTBRACKET = r'\{'
t_RIGHTBRACKET = r'\}'
t_GREATER = r'>'
t_LESS = r'<'
t_NOTEQUAL = r'<>'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'\/'
t_LEFTPAREN = r'\('
t_RIGHTPAREN = r'\)'
t_COLON = r':'
t_EQUALS = r'\='
t_CTESTRING = r'\".*\"'
t_COMMA = r'\,'
t_ignore = " \t"


# Expresiones Regulares con operaciones

# ID
def t_ID(t):
    r'[A-za-z]([A-za-z]|[0-9])*'
    t.type = keywords.get(t.value, 'ID')
    return t


# Número Flotante (float)
def t_CTEF(t):
    r'[0-9]*\.[0-9]+|[0-9]+'
    t.value = float(t.value)
    return t


# Número Entero (int)
def t_CTEI(t):
    r'\d+'
    t.value = int(t.value)
    return t


# Línea Nueva o Múltiples líneas nuevas (newlines)
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# Comentarios
def t_comment(t):
    r'\//.*'
    pass


def t_error(t):
    print("Error léxico ' {0} ' en la línea ' {1} ' ".format(t.value[0], t.lineno))
    t.lexer.skip(1)


lex.lex()