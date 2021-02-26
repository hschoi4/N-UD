import math
import matplotlib.pyplot as plt
import seaborn as sns

def norm (c):
    return math.sqrt(c[2]**2+c[3]**2+c[4]**2+c[5]**2+c[6]**2+c[7]**2+c[8]**2+c[9]**2+c[10]**2+c[11]**2+c[12]**2)

def cosine (c1, c2):
    return (c1[2] * c2[2]+c1[3] * c2[3]+c1[4] * c2[4]+c1[5] * c2[5]+c1[6] * c2[6]+c1[7] * c2[7]+c1[8] * c2[8]+c1[9] * c2[9]+c1[10] * c2[10]+c1[11] * c2[11]+c1[12] * c2[12]) /(c1[1] * c2[1])


#arguments : file with counts of patterns, export (boolean), name of outfile
def create_heatmap(fic_csv, export, outfile_name):
    with open(fic_csv) as f:
        lines = f.readlines()
    
        # [data] is a list of lines, each line is a list of columns
        data = [l.rstrip().split("\t") for l in lines[1:]]
    
        # modify the [data] matrix
        for c in data:
            for i in range(2,13):    # make column 2 to 4 as integer instead of string
                c[i] = int(c[i])  
            c[1] = norm(c)        # store the norm of the vector in column 1 (instead of the number of sentences)
            
            print(c[1])
        # the matrix of cosines
        matrix = [
            [round(cosine(c1, c2), 4) for c2 in data]
            for c1 in data
        ]

    plt.figure(figsize=(9,6))
    fig = sns.heatmap(matrix, 
                      annot =True,
                      fmt = "g",
                      xticklabels =[c[0][3:] for c in data], 
                      yticklabels =[c[0][3:] for c in data], 
                      )
    
    if export:
        plt.tight_layout()
        plt.savefig("%s.pdf" %outfile_name)
    

    return matrix


create_heatmap("counts_vocab_neg.csv", True, "vocab_neg_heatmap")
