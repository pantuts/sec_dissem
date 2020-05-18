#!/usr/bin/env python
# by: github.com/pantuts

from dissem_parser import DissemParser
import argparse
import json


def pretty_print(data):
    print(json.dumps(data, indent=4))


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--file', help='Dissem file', type=str, required=True)
    p.add_argument('--fields', help='List of fields you want. e.g: "accession_no,type,public_document_count"', type=str)
    p.add_argument('--company', help='If you want all company fields. You can also put it in --fields: e.g.: "company_conformed_name,company_cik"', action='store_true')
    p.add_argument('--filing', help='If you want all filing fields.', action='store_true')
    p.add_argument('--business', help='If you want all business fields.', action='store_true')
    p.add_argument('--mailing', help='If you want all mailing fields.', action='store_true')

    args = p.parse_args()
    file = args.file
    fields = args.fields
    company = args.company
    filing = args.filing
    business = args.business
    mailing = args.mailing
    all_fields = True

    for i in [fields, company, filing, business, mailing]:
        if i:
            all_fields = False

    dp = DissemParser(file)
    d = dp.process()

    if all_fields:
        pretty_print(d)
    else:
        fields = fields.split(',') if fields else []
        if fields:
            for field in fields:
                if field not in d:
                    print('[-] {} not in key fields.'.format(field))
                else:
                    print('{}: {}'.format(field, d.get(field)))
            print()
        if company:
            print('Company details:')
            pretty_print(d.get('company'))
            print()
        if filing:
            print('Filing Values details:')
            pretty_print(d.get('filing_values'))
            print()
        if business:
            print('Business Address details:')
            pretty_print(d.get('business_address'))
            print()
        if mailing:
            print('Mailing Address details:')
            pretty_print(d.get('mailing_address'))
            print()
