# %% [markdown]
# # Command Line Bioinformatics: Exploring File Formats
#
# **Duration**: 2 hours  
# **Goals**:  
# - Learn to explore bioinformatics file formats without memorizing their structures.  
# - Master basic command-line tools like `grep`, `awk`, `sort`, and `less` for data exploration.  
# - Develop skills in checking documentation (e.g., `man`, `--help`) and piping commands efficiently.  
#
# This notebook is designed for new bioinformatics students. You’ll use pre-installed tools to investigate common file formats: FASTA, FASTQ, GFF, and BED. No additional installations are required for the main exercises.

# %% [markdown]
# ## Setup
#
# Before starting, ensure you have:
# - Access to a "Data" directory containing example files: `*.fasta`, `*.fastq`, `*.gff`, `*.bed`.
# - A terminal or Jupyter notebook environment with standard UNIX tools installed (`cat`, `grep`, `awk`, etc.).
#
# Let’s verify the example files are present:

# %%
# List the contents of the Data directory
!ls Data/

# %% [markdown]
# **Task**: Run the command above. Do you see files ending in `.fasta`, `.fastq`, `.gff`, and `.bed`? If not, let your instructor know!

# %% [markdown]
# ## Resources
#
# Here are the command-line tools we’ll use (all standard and pre-installed):
# - `cat`: Concatenates and displays file contents.
# - `less`: Views files page by page (use `q` to quit).
# - `grep`: Searches for patterns in files.
# - `sort`: Sorts lines alphabetically or numerically.
# - `uniq`: Removes or counts duplicate lines (use with `sort`).
# - `file`: Identifies file types.
# - `awk`: Processes text and extracts fields.
# - `head`: Shows the first few lines of a file.
# - `tail`: Shows the last few lines of a file.
# - `wc`: Counts lines, words, or characters.
# - `gzip`/`gunzip`: Compresses or decompresses files (e.g., `.gz`).
#
# **External Resources**:  
# - [BED Format FAQ](https://genome.ucsc.edu/FAQ/FAQformat.html)  
# - [Learning Bioinformatics at Home](https://github.com/harvardinformatics/learning-bioinformatics-at-home)

# %% [markdown]
# ## Workflow: Using Command-Line Tools
#
# Let’s build a workflow for exploring files. Try these commands step-by-step:
#
# ### 1. Check Documentation
# Use `man` or `--help` to learn about tools:
# ```bash
# man grep  # Shows the manual for grep
# ls --help  # Displays help for ls
# ```
#
# ### 2. Navigate Directories
# Check your location and move around:
# ```bash
# /home/user/CM515-course-2025/modules/07_BioFile_Formats
# cd Data/  # Enter the Data directory
# pwd       # Confirm your location
# ```
#
# ### 3. List Files
# Explore the "Data" directory:
# ```bash
# ls Data/          # List files
# ls Data/ -lh      # List with sizes and human-readable format
# ls Data/ -lt      # Sort by modification time
# ```
#
# ### 4. Check File Types
# Identify what kind of files you’re working with:
# ```bash
# file Data/Animals.fasta  # Example output: ASCII text
# ```
#
# ### 5. Check File Sizes
# Assess file sizes to understand your data:
# ```bash
# ls Data/ -lh  # Human-readable sizes
# du -h Data/Animals.fasta  # Specific file size
# ```
#
# **Task**: Write a command to list files in "Data/" sorted by reverse modification time. Run it below:

# %%
# Your command here
!

# %% [markdown]
# **Solution**: `!ls Data/ -ltr`

# %% [markdown]
# ## Task 1: Describe the Tools
#
# Use `man` or `--help` to write a short sentence describing each tool’s purpose. Example:  
# - `cat`: "Displays the entire contents of a file to the screen."
#
# Fill in the rest:

# %%
# cat - "Displays the entire contents of a file to the screen."
# grep - 
# less - 
# head - 
# tail - 
# file - 
# awk - 
# wc - 
# sort - 
# uniq - 
# gzip - 
# gunzip - 

# %% [markdown]
# **Hint**: Run `man grep` or `grep --help` to get started. After completing this, compare with a classmate!

# %% [markdown]
# ## Piping Commands Together
#
# Piping (`|`) lets you chain commands. Here’s an example with a FASTA file:
#
# ### Example: Exploring FASTA Headers
# ```bash
# grep "^>" Data/Animals.fasta  # Extract headers (lines starting with ">")
# ```
# - Count sequences:
# ```bash
# grep "^>" Data/Animals.fasta | wc -l
# ```
# - Sort headers alphabetically:
# ```bash
# grep "^>" Data/Animals.fasta | sort
# ```
# - Count unique headers:
# ```bash
# grep "^>" Data/Animals.fasta | sort | uniq -c
# ```

# %% [markdown]
# **Task**: Run the commands above. What do the outputs tell you about `Animals.fasta`?

# %% [markdown]
# ## Exploring Bioinformatics File Formats
#
# Now, let’s dive into specific file formats. We’ll check if files are compressed, peek at their contents, and extract useful information.

# %% [markdown]
# ### FASTA Files (e.g., `*.fasta`, `*.fa`, `*.fna`)
#
# FASTA files store sequences (DNA, RNA, or protein) with headers starting with `>`.
#
# #### Step 1: Check the File
# ```bash
# file Data/Pan_paniscus.cds.fa.gz
# ```
# Output might say "gzip compressed data," so unzip it:

# %%
!gunzip Data/Pan_paniscus.cds.fa.gz

# %% [markdown]
# #### Step 2: Peek at the Contents
# ```bash
# head -n 10 Data/Pan_paniscus.cds.fa
# ```
# Notice the `>` headers and sequence lines. Are they wrapped (broken into fixed-length lines)?

# %%
!head -n 10 Data/Pan_paniscus.cds.fa

# %% [markdown]
# #### Step 3: Count Sequences
# ```bash
# grep -c "^>" Data/Pan_paniscus.cds.fa
# ```

# %%
!grep -c "^>" Data/Pan_paniscus.cds.fa

# %% [markdown]
# #### Step 4: Remove Line Wrapping
# FASTA files often wrap sequences at 60–80 characters. To make them single-line:
# ```bash
# awk '/^>/ {print (NR==1?"":"\n") $0; next} {printf "%s", $0} END {print ""}' Data/Pan_paniscus.cds.fa > Data/Pan_paniscus_singleline.fa
# ```
# This prints headers on new lines and joins sequence lines.

# %%
!awk '/^>/ {print (NR==1?"":"\n") $0; next} {printf "%s", $0} END {print ""}' Data/Pan_paniscus.cds.fa > Data/Pan_paniscus_singleline.fa
!head -n 4 Data/Pan_paniscus_singleline.fa

# %% [markdown]
# **Why?** Removing wrapping simplifies some analyses (e.g., calculating sequence length).
#
# #### Step 5: Calculate Sequence Lengths
# ```bash
# grep -v "^>" Data/Pan_paniscus_singleline.fa | awk '{print length($0)}'
# ```

# %%
!grep -v "^>" Data/Pan_paniscus_singleline.fa | awk '{print length($0)}'

# %% [markdown]
# **Task**: What’s the longest sequence in this file? Modify the command above to find out.

# %% [markdown]
# ### FASTQ Files (e.g., `*.fastq`, `*.fq`)
#
# FASTQ files store sequences with quality scores (4 lines per record: header, sequence, `+`, quality).
#
# #### Step 1: Check and Peek
# ```bash
# file Data/Covid_1.fastq
# head -n 8 Data/Covid_1.fastq  # 8 lines = 2 records
# ```

# %%
!head -n 8 Data/Covid_1.fastq

# %% [markdown]
# #### Step 2: Count Sequences
# Headers start with `@`:
# ```bash
# grep -c "^@" Data/Covid_1.fastq
# ```

# %%
!grep -c "^@" Data/Covid_1.fastq

# %% [markdown]
# #### Step 3: Extract Sequence Lengths
# Sequences are the 2nd line of each 4-line block:
# ```bash
# awk 'NR%4==2 {print length($0)}' Data/Covid_1.fastq
# ```

# %%
!awk 'NR%4==2 {print length($0)}' Data/Covid_1.fastq

# %% [markdown]
# **Task**: How would you count sequences with length > 100? Hint: Add a condition to the `awk` command.

# %% [markdown]
# ### GFF Files (e.g., `*.gff`, `*.gff3`)
#
# GFF files store genomic features in tab-separated columns (e.g., chromosome, start, end).
#
# #### Step 1: Peek
# ```bash
# head -n 10 Data/example.gff
# ```

# %%
!head -n 10 Data/example.gff

# %% [markdown]
# #### Step 2: Extract Genes
# Filter for "gene" features (column 3):
# ```bash
# grep -v "^#" Data/example.gff | awk '$3=="gene"'
# ```

# %%
!grep -v "^#" Data/example.gff | awk '$3=="gene"'

# %% [markdown]
# #### Step 3: Calculate Feature Lengths
# Length = end (col 5) - start (col 4) + 1:
# ```bash
# grep -v "^#" Data/example.gff | awk '$3=="gene" {print $5-$4+1}'
# ```

# %%
!grep -v "^#" Data/example.gff | awk '$3=="gene" {print $5-$4+1}'

# %% [markdown]
# **Task**: How many genes are in this file? Combine `grep` and `wc`.

# %% [markdown]
# ### BED Files (e.g., `*.bed`)
#
# BED files describe genomic regions with at least 3 columns (chromosome, start, end).
#
# #### Step 1: Peek
# ```bash
# head -n 10 Data/example.bed
# ```

# %%
!head -n 10 Data/example.bed

# %% [markdown]
# #### Step 2: Calculate Region Lengths
# Length = end (col 3) - start (col 2):
# ```bash
# awk '{print $3-$2}' Data/example.bed
# ```

# %%
!awk '{print $3-$2}' Data/example.bed

# %% [markdown]
# **Task**: Sort the regions by length (largest first). Hint: Use `sort -n`.

# %% [markdown]
# ## Wrap-Up
#
# You’ve explored FASTA, FASTQ, GFF, and BED files using standard tools! Key takeaways:
# - Use `file`, `head`, and `grep` to understand file structure.
# - Chain commands with `|` to analyze data efficiently.
# - Check documentation when stuck (`man`, `--help`).
#
# **Next Steps**: Try these techniques on your own datasets!

# %% [markdown]
# ## Advanced Section (Optional)
#
# For advanced users, install tools like `bioawk` or `seqtk` using a conda environment:
#
# ### Set Up Conda
# ```bash
# conda env create -f environment.yml
# conda activate Bio
# ```
#
# ### Example with bioawk
# Calculate mean Phred scores for FASTQ:
# ```bash
# bioawk -c fastx '{print $name, meanqual($qual)}' Data/Covid_1.fastq
# ```
#
# This section is optional and requires installation, so it’s separate from the main exercises.
