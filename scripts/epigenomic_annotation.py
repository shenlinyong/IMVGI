def annotate_with_epigenomics(vcf_file, epigenomic_dir, output_annotation):
    """
    Annotate variants using ATAC-seq and ChIP-seq peaks, associating them with regulatory elements.
    """
    peak_files = [os.path.join(epigenomic_dir, f) for f in os.listdir(epigenomic_dir) if f.endswith(".bed")]
    for peak_file in peak_files:
        element_type = os.path.basename(peak_file).replace(".bed", "")
        output_file = f"{output_annotation}_{element_type}.bed"
        command = f"bedtools intersect -a {vcf_file} -b {peak_file} > {output_file}"
        subprocess.run(command, shell=True, check=True)

# Example usage
output_annotation = "output/functional_annotation/variant_annotation"
annotate_with_epigenomics(output_vcf, EPIGENOMIC_DIR, output_annotation)
