# Edit Check Specification

## Study: VAERS-2025

**Document Title:** Edit Check Specification

**Version:** 1.0

**Date:** 13 July 2025

**Author:** Moksha Shrivastava

**Reference Standard:** GCDMP Chapter 3, ICH E6(R2), ALCOA+



### Edit Checks

Edit checks are a part of data quality metric system that compare entered clinical data against predefined criteria to detect any data entry error that may compromise it's reliability and accuracy. When a dataset or it's component fails an edit check, it usually generates a query for site staff to review and resolve.

|S.No.|Check ID|Severity Level|Check Type|File(s)|Original Field(s)|CDASH Field(s)|Edit Check Rule|Error Message|
|-|-|-|-|-|-|-|-|-|
|1.|EC-001|Minor|Range|2025VAERSDATA|HOSPDAYS|HOSPDAYS|When HOSPDAYS is present, value must be greater than or equal to 1|A hospitalized subject must have hospital days >=1|
|2.|EC-002|Minor|Range|2025VAERSDATA|NUMDAYS|NUMDAYS|The field range must be between -3 and 730|NUMDAYS must be between -3 and 730 when not null.|
|3.|EC-003|Critical|Date Logic|2025VAERSDATA|ONSET\_DATE, VAX\_DATE|AESTDTC, EXSTDTC|Adverse event onset must be on or after vaccination date|Adverse event onset date can not be before vaccination date|
|4.|EC-004|Critical|Date Logic|2025VAERSDATA|DATEDIED, ONSET\_DATE|AEDTHDTC, AESTDTC|Date of death must be on or after Adverse event onset|Date died can not be before onset date of Adverse Event|
|5.|EC-005|Major|Completeness|2025VAERSDATA|DIED, DATEDIED|AESER\_DEATH, AEDTHDTC|If subject is marked dead, then date of death must be listed|The subject is marked dead but date of death is absent|
|6.|EC-006|Major|Completeness|2025VAERSDATA|HOSPITAL, HOSPDAYS|AESER\_HOSP, HOSPDAYS|If subject is marked as hospitalized, number of hospitalized date must be present|The subject is marked hospitalized but number of days hospitalized is absent|
|7.|EC-007|Critical|Completeness|2025VAERSDATA|VAX\_DATE|EXSTDTC|Date of vaccination can not be empty|The date of vaccination for the subject is absent|
|8.|EC-008|Critical|Completeness|2025VAERSVAX|VAX\_TYPE|VAX\_TYPE|Type of vaccination must not be empty|The type of vaccination for the subject is absent|
|9.|EC-009|Critical|Controlled Terminology|2025VAERSVAX|VAX\_ROUTE|VAX\_ROUTE|The field must only contain the following values - UN, ID, IM, SC, IN, PO, SYR, JET, OT|Entered value for vaccination route is invalid|
|10.|EC-010|Minor|Controlled Terminology|2025VAERSDATA|V\_ADMINBY|V\_ADMINBY|The field must only contain the following values - PUB, PVT, MIL, PHM, SCH, SEN, WRK, OTH, UNK|Entered value for administerer is invalid|
|11.|EC-011|Major|Controlled Terminology|2025VAERSDATA|SEX|SEX|The field must only contain the following values - F, M, U or null|Entered value for sex is invalid|
|12.|EC-012|Critical|Referential Integrity|2025VAERSVAX, 2025VAERSSYMPTOMS, 2025VAERSDATA|VAERS\_ID|USUBJID|USUBJID in VAERSSYMPTOMS and VAERSVAX must exist in VAERSDATA|Subject ID in VAERS2025SYMPTOMS.csv not found in VAERS2025DATA.csv file; Subject ID in VAERS2025VAX.csv not found in VAERS2025DATA.csv file|

\# Edit Check Specification

\## Study: VAERS-2025

\*\*Document Title:\*\* Edit Check Specification

\*\*Version:\*\* 1.0

\*\*Date:\*\* July 2025

\*\*Author:\*\* \[your name]

\*\*Reference Standard:\*\* GCDMP Chapter 3, ICH E6(R2) ALCOA+



\### Edit Checks

Edit checks are a part of data quality metric system that compare entered clinical data against predefined criteria to detect any data entry error that may compromise it's reliability and accuracy. When a dataset or it's component fails an edit check, it usually generates a query for site staff to review and resolve.

|S.No.|Check ID|Severity Level|Check Type|File(s)|Original Field(s)|CDASH Field(s)|Edit Check Rule|Error Message|
|-|-|-|-|-|-|-|-|-|
|1.|EC-001|Minor|Range|2025VAERSDATA|HOSPDAYS|HOSPDAYS|When HOSPDAYS is present, value must be greater than or equal to 1|A hospitalized subject must have hospital days >=1|
|2.|EC-002|Minor|Range|2025VAERSDATA|NUMDAYS|NUMDAYS|The field range must be between -3 and 730|NUMDAYS must be between -3 and 730 when not null.|
|3.|EC-003|Critical|Date Logic|2025VAERSDATA|ONSET\_DATE, VAX\_DATE|AESTDTC, EXSTDTC|Adverse event onset must be on or after vaccination date|Adverse event onset date can not be before vaccination date|
|4.|EC-004|Critical|Date Logic|2025VAERSDATA|DATEDIED, ONSET\_DATE|AEDTHDTC, AESTDTC|Date of death must be on or after Adverse event onset|Date died can not be before onset date of Adverse Event|
|5.|EC-005|Major|Completeness|2025VAERSDATA|DIED, DATEDIED|AESER\_DEATH, AEDTHDTC|If subject is marked dead, then date of death must be listed|The subject is marked dead but date of death is absent|
|6.|EC-006|Major|Completeness|2025VAERSDATA|HOSPITAL, HOSPDAYS|AESER\_HOSP, HOSPDAYS|If subject is marked as hospitalized, number of hospitalized date must be present|The subject is marked hospitalized but number of days hospitalized is absent|
|7.|EC-007|Critical|Completeness|2025VAERSDATA|VAX\_DATE|EXSTDTC|Date of vaccination can not be empty|The date of vaccination for the subject is absent|
|8.|EC-008|Critical|Completeness|2025VAERSVAX|VAX\_TYPE|VAX\_TYPE|Type of vaccination must not be empty|The type of vaccination for the subject is absent|
|9.|EC-009|Critical|Controlled Terminology|2025VAERSVAX|VAX\_ROUTE|VAX\_ROUTE|The field must only contain the following values - UN, ID, IM, SC, IN, PO, SYR, JET, OT|Entered value for vaccination route is invalid|
|10.|EC-010|Minor|Controlled Terminology|2025VAERSDATA|V\_ADMINBY|V\_ADMINBY|The field must only contain the following values - PUB, PVT, MIL, PHM, SCH, SEN, WRK, OTH, UNK|Entered value for administerer is invalid|
|11.|EC-011|Major|Controlled Terminology|2025VAERSDATA|SEX|SEX|The field must only contain the following values - F, M, U or null|Entered value for sex is invalid|
|12.|EC-012|Critical|Referential Integrity|2025VAERSVAX, 2025VAERSSYMPTOMS, 2025VAERSDATA|VAERS\_ID|USUBJID|USUBJID in VAERSSYMPTOMS and VAERSVAX must exist in VAERSDATA|Subject ID in VAERS2025SYMPTOMS.csv not found in VAERS2025DATA.csv file; Subject ID in VAERS2025VAX.csv not found in VAERS2025DATA.csv file|



