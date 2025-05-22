# Counting-Number-of-Spectra

The number of genes with at least 2 distinct peptides in all samples is 6161.
The number of genes with at least 2 distinct peptides in at least 1 sample is 10029.

I imported numpy and pandas.  I stored the tab-separated tsv file to a variable.  I stored all the df's with more than two distinct peptides as Boolean to the genes variable.  I counted the rows of the data frame using .shape[0] and checked that the sum of genes variable was equal to that.  This counts all of the values in all of the samples in the DataFrame where there are at least 2 distinct peptides.

I made a new variable to store the genes with at least two distinct peptides in at least one sample.  I then check if there is at least one sample that meets the gene1 variable's condition.  If the count of the samples is greater than 0 for each gene, that means at least one sample meets the condition.  All of the samples that meet this condition are added up and stored as a variable.
