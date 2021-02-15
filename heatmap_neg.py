import math
import matplotlib.pyplot as plt
import seaborn as sns

def norm (c):
    return math.sqrt(c[2]**2+c[3]**2+c[4]**2)

def cosine (c1, c2):
    return (c1[2] * c2[2]+c1[3] * c2[3]+c1[4] * c2[4])/(c1[1] * c2[1])


#arguments : file with counts of patterns, export (boolean), name of outfile
def create_heatmap(fic_csv, export, outfile_name):
    with open(fic_csv) as f:
        lines = f.readlines()
    
        # [data] is a list of lines, each line is a list of columns
        data = [l.rstrip().split("\t") for l in lines[1:]]
    
        # modify the [data] matrix
        for c in data:
            for i in range(2,5):    # make column 2 to 4 as integer instead of string
                c[i] = int(c[i])  
            c[1] = norm(c)        # store the norm of the vector in column 1 (instead of the number of sentences)
    
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
    
    return fig.show()


create_heatmap("counts_pol_neg.csv", True, "pol_neg_heatmap")
