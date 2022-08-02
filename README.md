# Run Cello

Find protein sub-cellular location in FASTA files using [Cello](http://cello.life.nctu.edu.tw/).

## Installing

```
$ pip install run-cello
```

## Usage

```
$ run-cello -i tests/proteins.fasta -o tests/proteins.csv -t gram-
```

### Sample Output

|protein_id           |location     |
|---------------------|-------------|
|sp&#124;A5A616&#124;MGTS_ECOLI |Cytoplasmic  |
|sp&#124;B1X6B7&#124;HCHA_ECODH |Periplasmic  |
|sp&#124;B1XAK8&#124;FADB_ECODH |Cytoplasmic  |
|sp&#124;C4ZQN7&#124;HCHA_ECOBW |Periplasmic  |
|sp&#124;C5A020&#124;FADB_ECOBW |Cytoplasmic  |
|sp&#124;O32583&#124;THIS_ECOLI |Cytoplasmic  |
|sp&#124;P00350&#124;6PGD_ECOLI |Cytoplasmic  |
|sp&#124;P00363&#124;FRDA_ECOLI |Cytoplasmic  |
|sp&#124;P00370&#124;DHE4_ECOLI |Cytoplasmic  |
|sp&#124;P00393&#124;NDH_ECOLI  |Cytoplasmic  |
|sp&#124;P00448&#124;SODM_ECOLI |Periplasmic  |
|sp&#124;P00452&#124;RIR1_ECOLI |Cytoplasmic  |
|sp&#124;P00490&#124;PHSM_ECOLI |Cytoplasmic  |
|sp&#124;P00509&#124;AAT_ECOLI  |Cytoplasmic  |
|sp&#124;P00550&#124;PTM3C_ECOLI|InnerMembrane|

