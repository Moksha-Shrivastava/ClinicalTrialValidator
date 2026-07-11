import pandas as pd
class Validator:
    def __init__(self, data, symptoms, vax):
        self.data = data
        self.symptoms = symptoms
        self.vax = vax 
        self.queries = []
    def datediedcheck (self):
        for index, row in  self.data.iterrows():
            if row["AESER_DEATH"] == "Y" and pd.isna(row["AEDTHDTC"]):
                self.queries.append({"User ID": row["USUBJID"], "Query": "The subject is marked dead but date of death is absent", "Error":"EC 005, Major"})
    def hospcheck (self):
        for index, row in  self.data.iterrows():
            if row["AESER_HOSP"] =="Y" and pd.isna(row["HOSPDAYS"]):
                self.queries.append({"User ID": row["USUBJID"], "Query": "The subject is marked hopitalized but number of days hospitalized is absent", "Error": "EC006, Major"})
    def vaxdatecheck (self):
        for index, row in  self.data.iterrows():
            if pd.isna(row["EXSTDTC"]):
                self.queries.append({"User ID": row["USUBJID"], "Query": "The date of vaccination for the subject is absent", "Error":"EC 007, Critical"})
    def vaxtypecheck (self):
        for index, row in  self.vax.iterrows():
            if pd.isna(row["VAX_TYPE"]):
                self.queries.append({"User ID": row["USUBJID"], "Query": "The type of vaccination for the subject is absent", "Error":"EC 008, Critical"})
    def hospdayscheck (self):
        for index, row in  self.data.iterrows():
            if not pd.isna(row["HOSPDAYS"]) and row["HOSPDAYS"] <1:
                self.queries.append({"User ID": row["USUBJID"], "Query": "A hospitalized subject must have hospital days >=1", "Error":"EC 001, Minor"})
    def numdayscheck (self):
        for index, row in  self.data.iterrows():
            if not pd.isna(row["NUMDAYS"]) and (row["NUMDAYS"] < -3 or row["NUMDAYS"] > 730):
               self.queries.append({"User ID": row["USUBJID"], "Query": "The value must be between -3 and 730", "Error":"EC 002, Minor"}) 
    def aecheck (self):
        for index, row in  self.data.iterrows():
            if not pd.isna(row["AESTDTC"]) and not pd.isna(row["EXSTDTC"]) and row["AESTDTC"] < row["EXSTDTC"]:
                self.queries.append({"User ID": row["USUBJID"], "Query": "Adverse event onset date can not be before vaccination date", "Error":"EC 003, Critical"})
    def deathdatecheck (self):
        for index, row in  self.data.iterrows():
            if not pd.isna(row["AEDTHDTC"]) and not pd.isna(row["AESTDTC"]) and row["AEDTHDTC"] < row["AESTDTC"]:
                self.queries.append({"User ID": row["USUBJID"], "Query": "Date died can not be before onset date of Adverse Event", "Error":"EC 004, Critical"})
    def vaxroutecheck (self):
            for index, row in  self.vax.iterrows():
                valid = ["UN", "ID", "IM", "SC", "IN", "PO", "SYR", "JET", "OT"]
                if not pd.isna(row["VAX_ROUTE"]) and row["VAX_ROUTE"] not in valid:
                    self.queries.append({"User ID": row["USUBJID"], "Query": "Entered value for vaccination route is invalid", "Error":"EC 009, Critical"})
    def admincheck (self):
            for index, row in  self.data.iterrows():
                valids = ["PUB", "PVT", "MIL", "PHM", "SCH", "SEN", "WRK", "OTH", "UNK"]
                if not pd.isna(row["V_ADMINBY"]) and row["V_ADMINBY"] not in valids:
                    self.queries.append({"User ID": row["USUBJID"], "Query": "Entered value for administerer is invalid", "Error":"EC 0010, Minor"}) 
    def sexcheck (self):
            for index, row in  self.data.iterrows():
                validv = ["F", "M", "U"]
                if not pd.isna(row["SEX"]) and row["SEX"] not in validv:
                    self.queries.append({"User ID": row["USUBJID"], "Query": "Entered value for sex is invalid", "Error":"EC 0011, Major"})
    def refidcheck (self):
        dataid = set(self.data["USUBJID"])
        for index, row in self.symptoms.iterrows():
            if row["USUBJID"] not in dataid:
                self.queries.append({"User ID": row["USUBJID"], "Query": "Subject ID in VAERS2025SYMPTOMS.csv not found in VAERS2025DATA.csv file", "Error":"EC 0012, Critical"})
        for index, row in self.vax.iterrows():
            if row["USUBJID"] not in dataid:
                self.queries.append({"User ID": row["USUBJID"], "Query": "Subject ID in VAERS2025VAX.csv not found in VAERS2025DATA.csv file", "Error":"EC 0012, Critical"})

from Preprocessor import load_and_preprocess

a = data, symptoms, vax = load_and_preprocess( r'C:\Users\admin\Desktop\Python\2025VAERSDATA.csv', r'C:\Users\admin\Desktop\Python\2025VAERSSYMPTOMS.csv', r'C:\Users\admin\Desktop\Python\2025VAERSVAX.csv')
v = Validator (data, symptoms, vax)
v.datediedcheck()
v.hospcheck()
v.vaxdatecheck()
v.vaxtypecheck()
v.hospdayscheck()
v.numdayscheck()
v.aecheck()
v.deathdatecheck()
v.vaxroutecheck()
v.admincheck()
v.sexcheck()
v.refidcheck()

print(f"Total queries generated: {len(v.queries)}")
print(v.queries[:5])