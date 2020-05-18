# sec_dissem
SEC Dissem filetype parser

# Available fields:

accession_no\
type\
public_document_count\
filing_date\
filing_date_change\
effectiveness_date\
company_conformed_name\
company_cik\
company_assigned_sic\
company_irs_no\
company\
filing_values_form_type\
filing_values_act\
filing_values_file_no\
filing_values_film_no\
filing_values\
business_address_street1\
business_address_street2\
business_address_city\
business_address_state\
business_address_zip\
business_address\
mailing_address_street1\
mailing_address_street2\
mailing_address_city\
mailing_address_state\
mailing_address_zip\
mailing_address

# Usage:

--fields available fields separated by comma\
--company\
--filing\
--business\
--mailing

```
python sample.py --file ExampleFile.dissem
```
This this will output all the data.

```
python sample.py --file ExampleFile.dissem --fields accession_no,type,public_document_count,filing_date,filing_date_change,company_cik --company --business --filing --mailing
```
```
python sample.py --file ExampleFile.dissem --fields accession_no
python sample.py --file ExampleFile.dissem --fields accession_no --company
```

This will output specific fields.

#### A beer or two is enough ;)