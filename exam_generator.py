import random
# Helper functions

def compute_capacities(G):
    (V,E) = G

    # First, calculate the general flow

    capacities = {}
    for e in E:
        capacities[e] = random.randint(1, 10)

    return capacities

# Question generation
def init_tex_file():
    f = open("example_test.tex", "w")
    f.write(
"""\\documentclass{article}
\\usepackage[utf8]{inputenc}
\\usepackage{tikz}

\\tikzset{v/.style = {circle, thick, minimum size=2.0mm, inner sep=0pt, draw},
    a/.style = {        thick, minimum size=2.0mm, inner sep=0pt, draw},
    b/.style = {circle, fill,  minimum size=1.8mm, inner sep=0pt, draw},
    d/.style = {}}


\\title{Auto Generated Example Test}
\\author{COMP3940}
\\date{January 2023}


\\begin{document}

\\maketitle
""")
    return f

def end_tex_file(f):
    f.write("\\end{document}")
    f.close()


def max_flow_question(f):

    # Get graph
    V = [1,2,3,4,5,6,7,8]
    E = {(1, 2), (1,4), (1,6), (2,3), (4,5), (6,7), (4,2), (4,6), (3,5), (7,5), (3,8), (5,8), (7,8)}
    G = (V, E)
    capacities = compute_capacities(G)

    # Sort out latex
    f.write("Find the maximum flow in the graph below\n")
    f.write(
"""\\begin{center}
  \\begin{tikzpicture}[scale=0.8, >=stealth]
    \\node[v, label=left :s] (s) at (0,2) {}; 
    \\foreach \\n/\\y in {a/0, b/2, c/4} \\node[v] (\\n) at (2,\\y) {};
    \\foreach \\n/\\y in {d/0, e/2, f/4} \\node[v] (\\n) at (4,\\y) {};
    \\node[v, label=right:t] (t) at (6,2) {};
""")
    f.write(f"""
    \\draw[->] (s) to[edge label'={capacities[(1,2)]}] (a);
    \\draw[->] (s) to[edge label ={capacities[(1,4)]}] (b);
    \\draw[->] (s) to[edge label ={capacities[(1,6)]}] (c);
    \\draw[->] (b) to[edge label'={capacities[(4,2)]}] (a);
    \\draw[->] (b) to[edge label ={capacities[(4,6)]}] (c);
    \\draw[->] (a) to[edge label ={capacities[(2,3)]}] (d);
    \\draw[->] (b) to[edge label ={capacities[(4,5)]}] (e);
    \\draw[->] (c) to[edge label ={capacities[(6,7)]}] (f);
    \\draw[->] (d) to[edge label ={capacities[(3,5)]}] (e);
    \\draw[->] (f) to[edge label'={capacities[(7,5)]}] (e);
    \\draw[->] (d) to[edge label'={capacities[(3,8)]}] (t);
    \\draw[->] (e) to[edge label ={capacities[(5,8)]}] (t);
    \\draw[->] (f) to[edge label ={capacities[(7,8)]}] (t);"""
    )

    f.write(
"""\\end{tikzpicture}
\\end{center}\n"""
    )


def network_flow(f):
    f.write("\\section{Network Flow}\n")
    questions = {
        "Max Flow": max_flow_question
    }
    
    for title in questions:
        questions[title](f)
    



f = init_tex_file()
network_flow(f)
end_tex_file(f)
