import random
def complexity_closure(f):
    operators = ["\\cap", "\\cup"]
    classes = ["\\mathbb{P}", "\\mathbb{NP}"]

    f.write("Consider 3 problems: $\\Pi \\in \\mathbb{P}$, $\\Psi \\in \\mathbb{NP}$, and $\\Phi \\in \\textit{co}-\\mathbb{NP}$.\n\n")
    f.write("Assuming that $\\mathbb P " + ["\\ne", "="][random.randint(0, 1)] + " \\mathbb{NP}$, which of the following statements are true?\n")
    
    problems = ["\\Pi", "\\Psi", "\\Phi"]
    for i in range(3):
        p1 = random.randint(0, 2)
        p2 = p1
        while p2 == p1:
            p2 = random.randint(0, 2)
        
        f.write("\\subsubsection{}\n")
        f.write(problems[p1] + operators[random.randint(0,1)] + problems[p2] + "\\in" + classes[random.randint(0, 1)] + "\n")
