from setuptools import setup, find_packages

setup(name='bamsurgeon',
	version='1.0',
	author='Adam Ewing',
	license='MIT',
	scripts=['bin/addindel.py',
		'bin/addsnv.py',
		'bin/addsv.py',
		'scripts/bamregions_from_vcf.py',
		'scripts/bamsplit.py',
		'scripts/bamsplit_proportion.py',
		'scripts/bsrg.py',
		'scripts/comparemapping.py',
		'scripts/covered_segments.py',
		'scripts/dedup.py',
		'scripts/evaluator.py',
		'scripts/fix_mapsplice_bam.py',
		'scripts/makevcf.py',
		'scripts/makevcf_indels.py',
		'scripts/makevcf_sv.py',
		'scripts/postprocess.py',
		'scripts/randomsites.py',
		'scripts/remove_unpaired.py',
		'scripts/rename_reads.py',
		'scripts/seperation.py',
        'scripts/match_fasta_to_bam.py'],
	packages=find_packages(),
	)
