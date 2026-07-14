import pandas as pd

def load_and_preprocess(data_path, symptoms_path, vax_path): # Loads three VAERS 2025 CSV files, selects relevant columns, renames them to CDASH-equivalent names and standardises date
    columns to ISO 8601 format.
    data = pd.read_csv(data_path, encoding="latin1")
    symptoms = pd.read_csv(symptoms_path, encoding="latin1")
    vax = pd.read_csv(vax_path, encoding="latin1")

    vax = vax[["VAERS_ID", "VAX_TYPE", "VAX_ROUTE"]]
  
    symptoms = symptoms[["VAERS_ID"]]
    
    cdashstd = {
        "VAERS_ID": "USUBJID",
        "AGE_YRS": "AGE",
        "ONSET_DATE": "AESTDTC",
        "DATEDIED": "AEDTHDTC",
        "DIED": "AESER_DEATH",
        "HOSPITAL": "AESER_HOSP",
        "VAX_DATE": "EXSTDTC",
    }
    data = data.rename(columns=cdashstd)
    vax = vax.rename(columns=cdashstd)
    symptoms = symptoms.rename(columns=cdashstd)

    date = ["AESTDTC", "AEDTHDTC", "EXSTDTC"]

    for column in date:
        data[column] = pd.to_datetime(
            data[column],
            errors="coerce"
        ).dt.strftime("%Y-%m-%d")

    return data, symptoms, vax
