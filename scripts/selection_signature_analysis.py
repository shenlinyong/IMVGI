def calculate_fst(vcf_file, population_info):
    """
    Calculate Fst values between two populations using VCFtools.
    """
    fst_output = "output/variant_calling/fst_output.txt"
    command = f"vcftools --gzvcf {vcf_file} --weir-fst-pop {population_info[0]} --weir-fst-pop {population_info[1]} --out {fst_output}"
    subprocess.run(command, shell=True, check=True)
    return fst_output

def calculate_pi(vcf_file, population_info):
    """
    Calculate Pi values within populations using VCFtools.
    """
    pi_output = []
    for pop in population_info:
        output_file = f"output/variant_calling/pi_{pop}.txt"
        command = f"vcftools --gzvcf {vcf_file} --site-pi --keep {pop} --out {output_file}"
        subprocess.run(command, shell=True, check=True)
        pi_output.append(output_file)
    return pi_output

# Example usage
population_info = ["pop1.txt", "pop2.txt"]  # Text files listing individuals in each population
fst_output = calculate_fst(output_vcf, population_info)
pi_outputs = calculate_pi(output_vcf, population_info)
