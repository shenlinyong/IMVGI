from rpy2.robjects import r, pandas2ri
from rpy2.robjects.packages import importr

# Ensure R packages are installed
r('if (!requireNamespace("WGCNA", quietly = TRUE)) install.packages("WGCNA")')

def run_wgcna(expression_data, trait_data):
    """
    Run WGCNA on expression data to identify coexpression modules associated with the trait.
    """
    pandas2ri.activate()
    WGCNA = importr('WGCNA')
    
    # Example of running WGCNA (this is a high-level abstraction; actual steps include network construction, module detection, etc.)
    expression_df = pd.read_csv(expression_data, index_col=0)
    trait_df = pd.read_csv(trait_data, index_col=0)
    
    # Ensure data is in proper format and aligned
    expression_matrix = expression_df.values
    traits = trait_df.values
    
    # Network construction
    adjacency_matrix = WGCNA.adjacency(expression_matrix, power=6)
    TOM = WGCNA.TOMsimilarity(adjacency_matrix)
    modules = WGCNA.cutreeDynamic(dendro=TOM, method="hybrid", minClusterSize=30)
    
    # Module-trait correlation
    module_trait_corr = WGCNA.cor(traits, modules)
    
    # Save results
    np.savetxt("output/coexpression_analysis/module_trait_correlations.txt", module_trait_corr, fmt='%.4f')

# Example usage
run_wgcna("path/to/expression_data.csv", PHENOTYPIC_DATA)
