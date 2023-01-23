import random

# ~~~ Helper functions ~~~
def valid_matching(G):
    (V,E) = G
    V = set(V)
    E = [e for e in E]  # convert to list
    M = []
    M_comp = E
    saturated = set()
    unsaturated = V

    M_size = random.randint(2, len(E) - 1)
    
    i = 0
    while (len(unsaturated) > 1 and i < M_size and len(E) > 0):
        try:
            e_index = random.randint(0, len(E) - 1)
        except:
            e_index = 0

        e = E[e_index]
        while ((e[0] in saturated or e[1] in saturated)):
            E.pop(e_index)
            
            if (len(E) == 0):
                e = None
                e_index = None
                break
            
            try:
                e_index = random.randint(0, len(E) - 1)
            except:
                e_index = 0

            e = E[e_index]

        if e != None:
            M.append(e)
            E.pop(e_index)

            # Add vertices to list of saturated edges
            v1 = e[0]
            v2 = e[1]

            saturated = saturated.union({v1, v2})
        
        i+=1
    
    return M

def random_matching(G):
    (V, E) = G
    E = [e for e in E]
    M = []
    random.shuffle(E)
    
    # Add a few random matchings into the set which may or may not be valid
    for i in range(random.randint(0, len(E) - 1)):
        M.append(E[i])
    
    return M
        

def make_simple_graph():
    V = [1,2,3,4]
    E = {(1,2), (1,3), (2,4), (3,4), (2,3)}
    

    return (V,E)


# Question generation
# Question: "Which of these are matchings"
def matching_examples(f):
    f.write("For the following graphs and matchings select which are matchings and which are not. ")
    f.write("For each, if they are a matching, state whether or not they have an augmenting path.\n")

    G = make_simple_graph()
    (V, E) = G
    previous_matchings = []
    for i in range(4):
        matching = [valid_matching, random_matching][random.randint(0, 1)](G)
        
        previous_matchings.append(matching)

        f.write(
"""
\\subsubsection{"""+str(i+1)+"""}
\\begin{center}
    \\begin{tikzpicture}[scale=0.8, >=stealth]
        \\node[v] (a) at (0,2) {}; 
        \\foreach \\n/\y in {b/0, c/4} \\node[v] (\\n) at (2,\\y) {};
        \\node[v] (d) at (4,2) {};
"""
        )

        # Draw actual edges
        for e in E:
            f.write(
f"""
        \\draw {"[color=red]" if e in matching else ""} ({chr(96 + e[0])}) -- ({chr(96 + e[1])});"""
            )

        f.write(
"""
    \\end{tikzpicture}
\\end{center}
"""
        )


