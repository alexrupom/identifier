# done with python 3.6.3
import re

expr = input("enter the expression:\n")

print(expr)


token = re.compile(r'''
  (\s+) |                                                   # 1 whitespace
  (//)[^\n]* |                                              # 2 comments
  0[xX]([0-9A-Fa-f]+) |                                     # 3 hexadecimal integer literals
  (\d+) |                                                   # 4 integer literals
  (<<|>>) |                                                 # 5 multi-char punctuation
  ([][(){}<>=,;:*+-/]) |                                    # 6 punctuation
  (if|else|or|begin|end|while|for|do|to|int|float|char) |   #7 keywords
([A-Za-z_][A-Za-z0-9_]*) |                                  # 8 identifiers
  """(.*?)""" |                                             # 9 multi-line string literal
  "((?:[^"\n\\]|\\.)*)" |                                   # 10 regular string literal
  (.)                                                       # 11 an error!
  
''', re.DOTALL | re.VERBOSE)
scan = token.scanner(expr)

while 1:
    m = scan.match()
    if not m:
        break
    if m.lastindex == 1:
        print("whitespace", repr(m.group(m.lastindex)))

    if m.lastindex == 2:
        print("comments", repr(m.group(m.lastindex)))

    if m.lastindex == 3:
        print("hexadecimal integer literals", repr(m.group(m.lastindex)))
    if m.lastindex == 4:
        print("integer literals", repr(m.group(m.lastindex)))

    if m.lastindex == 5:
        print("multi-char punctuation", repr(m.group(m.lastindex)))

    if m.lastindex == 6:
        print("punctuation", repr(m.group(m.lastindex)))
    if m.lastindex == 7:
        print("keyword", repr(m.group(m.lastindex)))

    if m.lastindex == 8:
        print("indentifier", repr(m.group(m.lastindex)))
    if m.lastindex == 9:
        print("multi-line string literal", repr(m.group(m.lastindex)))

    if m.lastindex == 10:
        print("regular string literal", repr(m.group(m.lastindex)))
    if m.lastindex == 11:
        print("an error", repr(m.group(m.lastindex)))
