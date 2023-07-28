# MulMarker
A web application to identify prognostic signatures and generate reports automatically.

## Introduction
MulMarker is a comprehensive framework to identify a multigenic prognostic signature for cancer outcome prediction and patient stratification. The tool integrates the GPT's API to automatically interpret the results and evaluate whether candidate genes can work as a prognosis signature. The other highlight is that users can directly ask questions about the input, algorithms, and analysis process of the tool.

## WorkFlow
![1690528765637](https://github.com/Tina9/MulMarker/assets/16876314/94779cf3-145d-4392-b9ac-d891dd63b558)

## Requirements
MulMarker randomly divided patients into train and test groups. First, it employs univariate Cox regression analysis to screen candidate genes and uses multivariate Cox regression analysis to build the risk model with patients in the train group. KM survival analysis and log-rank test are used to evaluate the performance of the prognosis marker. Next, the patients in the test and total groups are used to validate the performance of the risk model. Mulmarker will explain the result and evaluate the possibility of the candidate genes as a prognosis biomarker automatically. To use MulMarker, required files and parameters are listed as follows:

1) Analysis Name (string): Input the name of your analysis, such as "LungCancer".

2) Chosen Genes (.txt): A txt file with Candidate genes, one gene per line. Genes in the file must be included in Expression Data, such as "MulMarker/test/chosen_genes.txt".

3) Clinical Patients (.txt): A txt file with clinical information. There are three columns: "PATIENT_ID", "OS_STATUS" and "OS_TIME". Patients in the file should be the same as the patients in Expression Data, such as "MulMarker/test/clinical_info.txt".

4) Expression Data (.txt): A txt file with RNA expression data. Each row corresponds to a gene and each column corresponds to a patient, such as "MulMarker/test/rna_info.txt".

5) Seed Number (number): Patients will be randomly divided into train group and test group when training the model. This parameter is the seed number of random grouping. We recommend you to adjust the paramneter to get a better risk model, such as "12".

6) Ratio (number): The ratio of train group and test group, such as "0.5".

## Results
#### The web page to submit data and Q&A
![84345654c5a7aae195953578d0d452a](https://github.com/Tina9/RiskModel/assets/16876314/9b2f59cb-6ea2-4ef8-b742-9c5fe0d7cba3)

#### The web page to show and explain the result
![4bbe1295aa896a00820a726016a757c](https://github.com/Tina9/RiskModel/assets/16876314/3bff5652-b790-4635-b2c3-e7031dcee57f)


