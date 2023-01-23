import random
from maxflow import *
from matchings import *
from complexity import *

# Tex file
def init_tex_file():
    f = open("example_test.tex", "w")
    f.write(
"""\\documentclass{article}
\\usepackage[utf8]{inputenc}
\\usepackage{tikz}
\\usepackage{amsmath}
\\usepackage{amssymb}
\\tikzset{v/.style = {circle, thick, minimum size=2.0mm, inner sep=0pt, draw},
    a/.style = {        thick, minimum size=2.0mm, inner sep=0pt, draw},
    b/.style = {circle, fill,  minimum size=1.8mm, inner sep=0pt, draw},
    d/.style = {}}


\\title{COMP3940 Auto Generated Example Test}
\\author{https://github.com/rnash-01/3940-practice}
\\date{January 2023}


\\begin{document}

\\maketitle
""")
    return f

def end_tex_file(f):
    f.write("\\end{document}")
    f.close()

# Question generation

def network_flow(f):
    f.write("\\section{Network Flow}\n")

    # ~~~ PRACTICE QUESTIONS FOR NETWORK FLOW GO HERE ~~~
    questions = [max_flow_question]     # append your function names from maxflow.py here
    
    for question in questions:
        question(f)

def matchings(f):
    f.write("\\section{Matchings}\n")

    # ~~~ PRACTICE QUESTIONS FOR MATCHINGS GO HERE ~~~
    questions = [matching_examples]     # append your function names from matchings.py here
    
    for question in questions:
        question(f)
    
    f.write("\n")
    
def complexity(f):
    f.write("\\section{Complexity Theory}\n")

    # ~~~ PRACTICE QUESTIONS FOR COMPLEXITY THEORY GO HERE ~~~
    questions = [complexity_closure]     # append your function names from complexity.py here
    
    for question in questions:
        question(f)
    
# MAIN SCRIPT
f = init_tex_file()

# SECTION 1 - NETWORK FLOW
network_flow(f)

# SECTION 2 - MATCHINGS
matchings(f)

# SECTION 3 - COMPLEXITY THEORY
complexity(f)

# End tex file
end_tex_file(f)
