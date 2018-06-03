#!/usr/bin/python

import os
import subprocess


def generateBedFile(fasta_file, reference_database_folder):
    bed_file = open(reference_database_folder + "/" + "bed.file", "w");
    seq_id = "";
    seq = "";
    with open(fasta_file) as file:
        for line in file:
            line = line.rstrip("\n");
            if(">" in line):
                if(seq_id != ""):
                    bed_file.write(seq_id + "\t" + "0" + "\t" + str(len(seq) - 1) + "\n");
                array = line.split(" ");
                seq_id = array[0].replace(">", "");
                seq = "";
            else:
                seq += line;
    bed_file.write(seq_id + "\t" + "0" + "\t" + str(len(seq) - 1) + "\n");
    bed_file.close();


sra_file_path = "";
hisat2_path = "/home/yiwang/data/biotools/hisat2";
scalpel_path = "/home/yiwang/data/biotools/scalpel-0.5.3";
thread_number = 6;

"""
sra_file_name = os.path.basename(sra_file_path).replace(".sra", "");
sra_file_folder = os.path.abspath(os.path.join(sra_file_path, ".."));
sra_command = "fastq-dump --split-3 " + sra_file_path;

subprocess.call(sra_command.split);

fastq1_path = sra_file_folder + "/" + sra_file_name + "_1.fastq";
fastq2_path = sra_file_folder + "/" + sra_file_name + "_2.fastq";
"""


sra_file_folder = "/home/yiwang/data/Public/microexon";
sra_file_name = "AT1G73370";
fastq1_path = "/home/yiwang/data/Public/microexon/sequence_1.fastq";
fastq2_path = "/home/yiwang/data/Public/microexon/sequence_2.fastq";
reference_seq_path = "/home/yiwang/data/Public/microexon/AT1G73370_O.fasta";

result_folder = sra_file_folder + "/" + "result";
if(not os.path.exists(result_folder)):
    os.makedirs(result_folder);

reference_database_folder = sra_file_folder + "/" + "reference_database";


#indexing on genome to speed up mapping
if(not os.path.exists(reference_database_folder)):
    os.makedirs(reference_database_folder);
    hisat2_build_command = hisat2_path + "/" + "hisat2-build -p " + str(thread_number) + " " + reference_seq_path + " " + reference_database_folder + "/" + "reference";
    subprocess.call(hisat2_build_command, shell = True);
    generateBedFile(reference_seq_path, reference_database_folder);


#mapping transcripton sequences to reference CDS and save to sam file
mapping_alignment_path = result_folder + "/" + sra_file_name + ".sam";
hisat2_command = hisat2_path + "/" + "hisat2 " + " -p " + str(thread_number) + " -x " + reference_database_folder + "/" + "reference" + " -1 " + fastq1_path + " -2 " + fastq2_path + " -S " + mapping_alignment_path;
subprocess.call(hisat2_command, shell = True);


# convert sam file to bam file, cause scalpel need bam file
sam_to_bam_command = "samtools view -bS " + result_folder + "/" + sra_file_name + ".sam" + " > " + result_folder + "/" + sra_file_name + ".bam";
subprocess.call(sam_to_bam_command, shell = True);


# todo
# if not use scalpel, we need to parse sam file and find microexon




# sort transcripton in sam file or bam file
bam_sorted_command = "samtools sort " + result_folder + "/" + sra_file_name + ".bam" + " > " + result_folder + "/" + sra_file_name + ".sorted.bam";
subprocess.call(bam_sorted_command, shell = True);


# find microexon in bam file , and generate a vcf file
indel_command = scalpel_path + "/" + "scalpel-discovery --single --bam " + result_folder + "/" + sra_file_name + ".sorted.bam" + " --bed " + reference_database_folder + "/" + "bed.file" + " --ref " + reference_seq_path + " --dir " + result_folder + "/" + "vcf";
print(scalpel_path + "/" + "scalpel-discovery --single --bam " + result_folder + "/" + sra_file_name + ".sorted.bam" + " --bed " + reference_database_folder + "/" + "bed.file" + " --ref " + reference_seq_path);
subprocess.call(indel_command, shell = True);