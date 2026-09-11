# Data

Dataset: IBM Transactions for Anti Money Laundering (AML)

File used: HI-Small_Trans.csv

Source: IBM AML-Data dataset, downloaded from the Kaggle distribution linked by IBM.

License: CDLA-Sharing-1.0

Downloaded: 11 September 2026

Raw data location: data/raw/HI-Small_Trans.csv

The raw dataset is synthetic and is not committed to Git.

## Initial EDA findings

- The dataset contains 5,078,345 transactions covering 1–18 September 2022.
- The target is extremely imbalanced: about 99.9% of transactions are class 0 and about 0.1% are class 1.
- Cheque is the most common payment format; Bitcoin is the least common.
- Transaction amounts are highly skewed, with a small number of extremely large values.
- For US-dollar payments, transactions are concentrated more heavily in the middle amount ranges than at the extremes.

## Open questions

- How are laundering-labelled transactions distributed across time and payment formats?
- Which columns will be valid features at prediction time?
- Should the 9 exact duplicate rows be removed during cleaning?