# ClinicalTrialValidator
This is a edit check validator specific to the three VAERS 2025 datasets

## VAERS Dataset
- It is a annual report on vaccines safety and pharmacovigialce study where possible adverse events associated to a vaccine is reported on a voluntary basis.
- Three CSV files were used in this project featuring - 2025VAERSDATA.csv (listed general infomration such as vaccination date, sex etc), 2025VAERSSYMPTOMS.csv (listed various symptoms reported as adverse events post vaccination) and 2025VAERSVAX.csv (listed details about the vaccines recived such as route of administration and other information)
- Features 40,806 records
- Data Source: The files were sourced from vaers.hhs.gov/data/datasets.html
## CDM Approach
- Designed 12 edit check rules from 5 specific qualities including Range, Date logic, Completeness, Controlled terminology & Referential integrity checks
- Built a programme to check  if each dataset for it's compliance with the 12 rules to asses it's quality and accuracy with checks designed in accordance with GCDMP Chapter 3 and ICH E6(R2) ALCOA+ data integrity principles."
- A query is fired each time a specific record violated the set rules listing the specific row and the edit check rule it's violating.
- A list of all the queries generated is recorded in a csv file along with a summary excel report
## CDM Findings
- The report generated 9,638 queries with EC007 being the most common where 6,692 records had missing vaccination date
- Five of the edit checks that were designed generated 0 queries
- Total query rate was 23.62%
## Programme Structure
- Preprocessor.py: Edited and redefined fields of the datasets in accordance to CDASH standards
- Validator.py: Converted the 12 edit checks rule into a a automated programme
- Report.py: Generated the report.csv file listing all the queries
- Main.py: Connected all previous files and the 2025VAERS Datasets for runnig the programme
## Deliverables
- Edit Check Specification (docs/edit_check_spec.md): Formal specification document defining all 12 edit check rules, their severity levels, and clinical explanations
- Query Report (output/query.csv): Complete list of all 9,638 data quality issues generated
