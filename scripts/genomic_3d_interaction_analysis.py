def map_variants_to_genes_3d(annotation_files, hic_data, output_interactions):
    """
    Map annotated variants to their potential target genes using 3D genome data.
    """
    for annotation_file in annotation_files:
        interaction_output = f"{output_interactions}_{os.path.basename(annotation_file).replace('.bed', '')}.txt"
        command = f"3D_genome_tool --annotated_variants {annotation_file} --hic_data {hic_data} --output {interaction_output}"
        subprocess.run(command, shell=True, check=True)

# Example usage
annotation_files = [f"output/functional_annotation/{f}" for f in os.listdir("output/functional_annotation") if f.endswith(".bed")]
map_variants_to_genes_3d(annotation_files, GENOMIC_3D_DIR, "output/3D_genomic_analysis/variant_gene_interactions")
