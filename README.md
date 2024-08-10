# IMVGI - Integrative Multi-omics Variant-Gene Interaction Pipeline

IMVGI is a tool designed for Integrative Multi-omics Variant-Gene Interaction analysis, applicable to any trait research.

## Project Structure

The project is organized into the following directory structure, which helps users understand the purpose of each file and folder:

```bash
IMVGI/
├── README.md # The main file that describes the project, installation instructions, and usage guidelines
├── data/ # Folder containing all the required data for the project
│ ├── WGS/ # Whole Genome Sequencing data
│ ├── epigenomic/ # Epigenomic data
│ ├── 3D_genomic/ # 3D Genomic data
│ └── transcriptomic/ # Transcriptomic data
├── scripts/ # Folder containing all the analysis scripts
│ ├── variant_calling.py # Script for variant calling
│ ├── selection_signature_analysis.py # Script for selection signature analysis
│ ├── epigenomic_annotation.py # Script for epigenomic annotation
│ ├── genomic_3d_interaction_analysis.py # Script for 3D genomic interaction analysis
│ └── wgcna_analysis.py # Script for Weighted Gene Co-expression Network Analysis (WGCNA)
├── output/ # Output folder, automatically generated, no need to upload
├── requirements.txt # File listing all the Python package dependencies
└── LICENSE # License file for the project
```

## Installation

Follow these steps to install and run the project in your local environment:

### 1. Clone this repository
First, use `git` to clone the repository to your local machine. This command copies the entire project to your computer.
```bash
git clone https://github.com/your-username/IMVGI.git
cd IMVGI
```

### 2. Install dependencies
Use pip to install all the required Python packages. These packages are listed in the requirements.txt file. Run the following command to install them:
```bash
pip install -r requirements.txt
```

## Usage
The following sections explain how to use each script to perform various analyses. Each script corresponds to a different step in the analysis process:

### 1. Variant Calling
Run the following command to perform variant calling. This script identifies variants in the genome.
```bash
python scripts/variant_calling.py
```
### 2. Selection Signature Analysis
Use this script to perform selection signature analysis, which aims to identify regions of the genome that have been preserved during selection.
```bash
python scripts/selection_signature_analysis.py
```
### 3. Epigenomic Annotation
This script annotates epigenomic data onto the genome, helping to understand the impact of variants at the epigenomic level.
```bash
python scripts/epigenomic_annotation.py
```
### 4.3D Genomic Interaction Analysis
```bash
python scripts/genomic_3d_interaction_analysis.py
```
### 5. WGCNA Analysis
Run this script to perform Weighted Gene Co-expression Network Analysis (WGCNA) to study gene co-expression patterns.
```bash
python scripts/wgcna_analysis.py
```
## Contributing
Contributions, issues, and feature requests are welcome! Feel free to submit issues or pull requests.

## License
This project is licensed under the MIT License, which allows users to freely use, modify, and distribute the code.
```bash
This version includes detailed comments that explain the purpose of each section, script, and command, enhancing clarity for users.
```


