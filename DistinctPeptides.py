import numpy as np
import pandas as pd

df = pd.read_csv("proteomics.summary.tsv",sep='\t')

# Find genes (columns) with at least 2 distinct peptides in all samples
genes = (df >= 2)                                   #boolean df - True if has at least 2 distinct peptides
count_samples = (genes.sum() == df.shape[0]).sum()  #adds all True values and gives total number of samples
                                                    #add all of these row values of True together 

# Find genes with at least 2 distinct peptides in at least one sample
genes1 = (df >= 2)                  #boolean df
count1 = (genes1.sum() > 0).sum()   #check if at least 1 sample meets condition
                                    #if count of samples is greater than 0 for each gene, theres at least one sample to meet conditions

print("Number of genes with at least 2 distinct peptides in all samples:", count_samples)
print("Number of genes with at least 2 distinct peptides in at least 1 sample:", count1)
