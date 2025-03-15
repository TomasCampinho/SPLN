from lark import Lark, Transformer, v_args
import re

#todo: completar isto de maneira a fazer tabela pt - tetum, e resto (lixo) para outro ficheiro DONE
#maybe: fazer um sistema de reescrita textual 
#like this:
#   defr a(t):
#       the ==> o
#       cat ==> gato
#       (\w+) =e=> dic.get(\1, \1)
#       ...
#
#   def transform_a(t):
#       t = re.sub(r'\bthe\b', 'o', t)
#       t = re.sub(r'\bcat\b', 'gato', t)
#       t = re.sub(r'(\w+)', lambda m: dic.get(m.group(1), m.group(1)), t)
#       return t
#       ...

gramatica = r"""
    start: (PAR_COM_PARENTESIS | pt_line | tt_line | FIG_LINE | UNKNOWN_LINE)*
    PAR_COM_PARENTESIS.2: /(\b\w+\b)+ \(.+\)/

    pt_line: PT_LINE UNKNOWN_LINE*
    PT_LINE.3: /PORTUGUÊS: .*/

    tt_line: TETUN_LINE UNKNOWN_LINE*
    TETUN_LINE.3: /TETUN: .*/

    FIG_LINE.3: /Figura: \d\- (\b\w+\b)+ \(.+\)/

    UNKNOWN_LINE.1: /.+/

    %import common.NEWLINE
    %ignore NEWLINE
"""

ex= r"""
Tangram (Tangram) .................................................................................................................. 120
Teorema (Teorema) ................................................................................................................... 121
Termo (Termu) .......................................................................................................................... 121
Tetraedro (Tetraedru) ................................................................................................................ 121
Trapézio (Trapéziu) ................................................................................................................... 121
Triângulo (Triángulu)................................................................................................................ 122
Trigonometria (Trigonometria) ................................................................................................. 122
Unidade (Unidade) .................................................................................................................... 122
Valor Absoluto (Valór Absolutu) .............................................................................................. 122
Valor Médio (Valór Médiu) ...................................................................................................... 122
Variável (Variavel).................................................................................................................... 122

Vertical (Vertikál) ..................................................................................................................... 123
Vértice (Vértise) ........................................................................................................................ 123
Volume (Volume) ..................................................................................................................... 123
Tabela de nomes Tétum – Português (Tabela hosi naran Tetun - Portugés) ............................. 124

Abscissa (Absisa)

Figura 1- Eixo X-Y com abscissas (Eixu X-Y ho absisa)
"""

parser = Lark(gramatica, parser = 'lalr')
tree = parser.parse(ex)

#print(tree.pretty())

@v_args(inline=True)
class T(Transformer):

    def start(self, *items):
        return items
    
    def PAR_COM_PARENTESIS(self, items):
        return ('pt-tt', re.split(r' *[()]', items.value))
    
    def PT_LINE(self, items):
        return ('pt', items.value.split(': ')[1])
    
    def pt_line(self, pt, *items):
        return ('pt', pt[1] + '\n' + '\n'.join(items))

    def TETUN_LINE(self, items):
        return ('tt', items.value.split(': ')[1])
    
    def tt_line(self, tt, *items):
        return ('tt', tt[1] + '\n' + '\n'.join(items))
    
    def FIG_LINE(self, items):
        return ('fig', items.value)
    
    def UNKNOWN_LINE(self, items):
        return items.value
    
tree = T().transform(tree)

pt_tt_lines = []
other_lines = []

for e in tree:
    if e[0] == 'pt-tt':
        pt_tt_lines.append(e[1])
    elif isinstance(e, tuple) and e[0] in ['pt', 'tt']:
        pt_tt_lines.append(e)
    elif isinstance(e, str) and re.match(r'.*\(.*\)', e):
        pt_tt_lines.append(re.split(r' *[()]', e))
    else:
        other_lines.append(e)

with open('pt_tt_table.txt', 'w') as f:
    f.write("Português\t\t\t\t\t\t\t\t\t\t\tTetum\n")
    f.write("-" * 60 + "\n")
    for line in pt_tt_lines:
        if isinstance(line, list):
            f.write(f"{line[0].strip():<50}\t{line[1].strip():<50}\n")
        else:
            f.write(f"{line[0].strip():<50}\t{line[1].strip():<50}\n")

with open('other_lines.txt', 'w') as f:
    for line in other_lines:
        f.write(f"{line}\n")

