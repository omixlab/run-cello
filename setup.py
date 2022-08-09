from setuptools import setup, find_packages

setup(
    name="run-cello",
    version='0.1.7',
    packages=find_packages(),
    author="Frederico Schmitt Kremer",
    author_email="fred.s.kremer@gmail.com",
    description="Find protein sub-cellular location in FASTA files using Cello.",
    keywords="bioinformatics",
    entry_points = {'console_scripts':[
        'run-cello   = cello:main'
        ]},
    install_requires = [
        requirement.strip('\n') for requirement in open("requirements.txt")
    ]
)
