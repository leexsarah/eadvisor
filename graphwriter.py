treestruct = """
    101  -> {311}
    311  -> {315 362}
    2701 -> {2702}
    2702 -> {335}
    1501 -> {1502}
    1502 -> {338}
    338  -> {335}
    120 -> {121}
    121 -> {131} 
    131 -> {223 254 301 311 332 240} 
    240 -> {440}
    254 -> {351}
    351 -> {471}
    301 -> {323 335}
    335 -> {481}\n"""

csDict = {'101':('ENG 101','blue'),
          '120':('CPSC 120','blue'), 
          '121':('CPSC 121','blue'), 
          '131':('CPSC 131','blue'),
          '1501':('MATH 150A','blue'),
          '1502':('MATH 150B','blue'), 
          '223':('CPSC 223','blue'),
          '240':('CPSC 240','blue'),
          '254':('CPSC 254','blue'),
          '2701':('MATH 270A ','blue'),
          '2702':('MATH 270B ','blue'),
          '301':('CPSC 301','blue'),
          '311':('CPSC 311','blue'),
          '315':('CPSC 315','blue'),
          '323':('CPSC 323','blue'),
          '332':('CPSC 332','blue'),
          '335':('CPSC 335','blue'),
          '338':('MATH 338','blue'),
          '351':('CPSC 351','blue'),
          '362':('CPSC 362','blue'),
          '440':('CPSC 440','blue'),
          '471':('CPSC 471','blue'),
          '481':('CPSC 481','blue'),
          }

shape = "shape = rect, "
style = "style = rounded, "

output = ""
for i in csDict:
  output = output + "    " + i + ' [label = "' + csDict[i][0] + '"' + " " + shape + style + " " + "color = " + csDict[i][1] + "];\n"

output = output + '\n'

text_file = open("graph.dot", "w")
text_file.write("digraph titangraph {\n")
text_file.write(output)
text_file.write(treestruct)
text_file.write("}")
























text_file.close()
