# MulMarker
A framework for identifying potential multi-gene prognostic signatures. The web application can be accessed at https://mulmarker.azurewebsites.net/.

## Introduction
MulMarker is a comprehensive framework for identifying potential multi-gene prognostic signatures across various diseases. MulMarker comprises three core modules: a GPT-driven chatbot for addressing user queries, a module for identifying multi-gene prognostic signatures, and a module for generating tailored reports.

![Figure1](https://github.com/Tina9/MulMarker/assets/16876314/d079408a-da5e-4915-8ca8-2a0773c85a19)

## Requirements
MulMarker randomly divides patients into training and test groups. In the training group, it first employs univariate regression analysis to screen genes and then constructs a risk model using multivariate regression analysis. The combination of the identified genes is considered to be a potential prognostic signature. A KM survival analysis and a log-rank test are used to evaluate the performance of the prognosis signature. Next, the signature is evaluated in the test group and total dataset using KM survival analysis and log-rank test. Finally, MulMarker generates a report based on the analysis results to explain the findings. To use MulMarker, required files and parameters are listed as follows:

1) Analysis Name (string): Input the name of your analysis, such as "LungCancer".

2) Chosen Genes (.txt): A txt file with Candidate genes, one gene per line. Genes in the file must be included in Expression Data, such as "MulMarker/test/chosen_genes.txt".

3) Clinical Patients (.txt): A txt file with clinical information. There are three columns: "PATIENT_ID", "OS_STATUS" and "OS_TIME". Patients in the file should be the same as the patients in Expression Data, such as "MulMarker/test/clinical_info.txt".

4) Quantified Data (.txt): A txt file for transcriptomic and proteomic data. Each row corresponds to a gene and each column corresponds to a patient, such as "MulMarker/test/rna_info.txt".

5) Seed Number (number): Patients will be randomly divided into train group and test group when training the model. This parameter is the seed number of random grouping. We recommend you to adjust the paramneter to get a better risk model, such as "12".

6) Ratio (number): The ratio of train group and test group, such as "0.5".

## Results
#### To submit data and Q&A
![1692358944276](https://github.com/Tina9/MulMarker/assets/16876314/e075caf8-c00d-46ec-8ffc-22a5d3e7b5b5)

#### To present and explain the result
![4bbe1295aa896a00820a726016a757c](https://github.com/Tina9/RiskModel/assets/16876314/3bff5652-b790-4635-b2c3-e7031dcee57f)


