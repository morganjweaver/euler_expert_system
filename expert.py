import argparse

'''This program was implemented for a data science workshop with a focus on expert systems, specifically Euler's summation.
 It takes in a set of variables and attempts to return a Boolean answer indicating whether a scenario is theoretically 
 possible.  The problem is of the form: 
'There are 30 coins and 5 pockets, and no 2 pockets may be equal but one pocket must have 10 coins and another 2 coins.'
So for this, the word problem can be translated to the variables a,b,c and {d1, d2...} of the input mapping
 [30,5,2, {10,2}].  The command line program may be run as: python3 expert.py -a 30 -b 5 -c 2 -req 5 2'''

def gaussum(x):
    return (x*(x+1))/2

def cb_check(a,b,k,must):
    answer = "False!"
    if (k == 1) & ((a/b) >= must[0]):
        answer = "True!"
    if ((k == 0) & (a%b == 0)):
        answer = "True!"
    return answer

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument('-a', '--numcoins', type=int, help='channel id to scrape')
    ap.add_argument('-b', '--numpockets', type=int, help='file to save out')
    ap.add_argument('-c', '--numcanthave', type=int, help = 'no x pockets can be equal; 0 for ANY can be equal')
    ap.add_argument('-req', '--exactnumlist', nargs='+', type=int, help='list of pockets with constraints, eg 2 3 10 '
                                                                        'must have these coin counts')
    # Parse command line arguments
    args = vars(ap.parse_args())
    a = args['numcoins']
    b = args['numpockets']
    c = args['numcanthave']

    # Set default variables to avoid null/Nonetype errors
    Sd = 0
    k = 0
    answer = False

    # Parse the constraints list and set k and Sum of constraints accordingly
    if args['exactnumlist'] != None:
        must = args['exactnumlist']
        k = len(must)
        Sd = sum(list(must))

    if (b < k) | (b < c):
        print("False!\n")
    else:
        a_eq = (gaussum(b-k-1)+Sd)
        if a >= a_eq:
            if (c <= (b-1)) & (c != 1):
                print("True!")
            elif c == b:
                print(cb_check(a,b,k,must))
            else:
                print("False!")
        else: # c < a_eq
            if c == 0:
                print("False!")
            else:
                if a >= (gaussum((b-c+1)-k-1)+Sd):
                    print("True!")
                else:
                    print("False!")



