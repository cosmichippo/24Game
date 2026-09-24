from random import randint
import sys
# solver

def sum(a,b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    return a / b

# find a nice way to store info together, maybe a queue of like [a, b, + c, -, d]
# pop, if in ops, apply function. else, if type "integer", save to either a , b, last result
# save info 



def solve(a, b, c, d):

    all_sets = []
    for i in range(4):
        for j in range(4):
            for k in range(4):
                all_sets.append((i, j, k))

    ops = [sum, sub, mul, div]
    key = {sum: '+', sub: '-', mul: '*', div:'/'}
    while len(all_sets) > 0:
        #index = randint(0, len(all_sets)-1)
        (i, j, k) = all_sets.pop()
        # solve all 
        x = ops[i]; y=ops[j]; z = ops[k]
        # need to add how everything changes
        # need to create different permutations of a, b, c, d
        resultant = z(y(x(a, b), c), d)
        if resultant == 24:
            # solved
            return f"[({a}{key[x]}{b}){key[y]}{c}]{key[z]}{d}"
    return None

def get_perms(a,b,c,d):
    return [
    (a, b, c, d),
    (a, b, d, c),
    (a, c, b, d),
    (a, c, d, b),
    (a, d, b, c),
    (a, d, c, b),
    (b, c, d, a),
    (b, c, a, d),
    (b, d, a, c),
    (b, d, c, a),
    (b, a, c, d),
    (b, a, d, c),
    (c, d, a, b),
    (c, d, b, a),
    (c, b, a, d),
    (c, b, d, a),
    (c, a, b, d),
    (c, a, d, b),
    (d, a, b, c),
    (d, a, c, b),
    (d, b, c, a),
    (d, b, a, c),
    (d, c, b, a),
    (d, c, a, b)
    ]

def get_soln_allPerms(a, b, c, d):
                                       #1, 1, 1, 2 
                                       #1, 1, 10, 2 
                                       #1, 10, 10, 2
    permutations_of_inputs = get_perms(a, b,c, d)
    # need to try all permutations of 
    # there's a way to hardcode this    

    soln_strings = set()
    for perm in permutations_of_inputs:
        (w, x, y, z) = perm
        # print(w, x, y, z)
        out = solve(w, x, y, z)
        if out != None:
            soln_strings.add(out) 
            print(out)
    return soln_strings

def main():
    # treat special number 10 like 1 
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    c = int(sys.argv[3])
    d = int(sys.argv[4])

    vals = []
    input_combo = [a, b, c, d]
    # since i am already getting all permutations of values
    # in solve_allPerms
    # i only have to focus on swapping out 10s with 1s
    #  

    cp = input_combo.copy()
    vals.append(cp.copy())
    for i in range(4):
        if cp[i] == 1:
            cp[i] = 10
            vals.append(cp.copy())
    for variant in vals:
        get_soln_allPerms(*variant)
    return 0

if __name__ == "__main__":
    main()