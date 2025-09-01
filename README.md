# Molecular weight

The model is simply an implementation of the function Descriptors.MolWt of the chemoinformatics package RDKIT. It takes as input a small molecule (SMILES) and calculates its molecular weight in g/mol.

This model was incorporated on 2021-09-13.Last packaged on 2025-09-01.

## Information
### Identifiers
- **Ersilia Identifier:** `eos3b5e`
- **Slug:** `molecular-weight`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Property calculation or prediction`
- **Biomedical Area:** `Any`
- **Target Organism:** `Any`
- **Tags:** `Molecular weight`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `1`
- **Output Consistency:** `Fixed`
- **Interpretation:** Calculated molecular weight (g/mol)

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| mol_weight | float | high | The calculated molecular weight of the molecule in g/mol |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos3b5e](https://hub.docker.com/r/ersiliaos/eos3b5e)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos3b5e.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos3b5e.zip)

### Resource Consumption
- **Model Size (Mb):** `1`
- **Environment Size (Mb):** `455`
- **Image Size (Mb):** `477.14`

**Computational Performance (seconds):**
- 10 inputs: `26.74`
- 100 inputs: `16.44`
- 10000 inputs: `27.2`

### References
- **Source Code**: [https://github.com/rdkit/rdkit](https://github.com/rdkit/rdkit)
- **Publication**: [https://www.rdkit.org/docs/RDKit_Book.html](https://www.rdkit.org/docs/RDKit_Book.html)
- **Publication Type:** `Other`
- **Publication Year:** `2010`
- **Ersilia Contributor:** [miquelduranfrigola](https://github.com/miquelduranfrigola)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [BSD-3-Clause](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos3b5e
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos3b5e
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
