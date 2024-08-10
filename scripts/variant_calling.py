def variant_calling(wgs_dir, output_vcf):
    """
    Calls variants from WGS data using GATK HaplotypeCaller.
    """
    bam_files = [os.path.join(wgs_dir, f) for f in os.listdir(wgs_dir) if f.endswith(".bam")]
    for bam_file in bam_files:
        sample_name = os.path.basename(bam_file).replace(".bam", "")
        output_gvcf = f"output/variant_calling/{sample_name}.g.vcf.gz"
        
        command = (
            f"gatk HaplotypeCaller -R ref_genome.fa -I {bam_file} -O {output_gvcf} "
            "--emit-ref-confidence GVCF"
        )
        subprocess.run(command, shell=True, check=True)
    
    # Combine GVCFs
    combined_vcf = "output/variant_calling/combined.g.vcf.gz"
    command = f"gatk CombineGVCFs -R ref_genome.fa --variant output/variant_calling/*.g.vcf.gz -O {combined_vcf}"
    subprocess.run(command, shell=True, check=True)
    
    # Genotype GVCFs
    output_vcf = f"output/variant_calling/final_variants.vcf.gz"
    command = f"gatk GenotypeGVCFs -R ref_genome.fa -V {combined_vcf} -O {output_vcf}"
    subprocess.run(command, shell=True, check=True)
    
    return output_vcf

# Example usage
output_vcf = variant_calling(WGS_DIR, "output/variant_calling/final_variants.vcf.gz")
