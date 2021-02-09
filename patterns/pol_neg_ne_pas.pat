pattern { 
N1 [Polarity="Neg", form = "ne"| "n'" |"Ne" | "N'"];
N2 [Polarity="Neg", form = "pas"|"Pas"];
V -[advmod]->N1;
V -[advmod]->N2;
}