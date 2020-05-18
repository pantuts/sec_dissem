#!/usr/bin/env python
# by: github.com/pantuts

import re


class DissemParser:
    def __init__(self, file):
        self._file = file
        self._data_str = None
        self.data = {}
        self.read()

    def read(self):
        with open(self._file, 'r') as f:
            self._data_str = f.read()

    def process(self):
        self.data = {
            'accession_no': self._accession_number(),
            'type': self._type(),
            'public_document_count': self._pub_doc_count(),
            'filing_date': self._filing_date(),
            'filing_date_change': self._filing_date_change(),
            'effectiveness_date': self._effectiveness_date(),

            'company_conformed_name': self._company_data().get('conformed_name'),
            'company_cik': self._company_data().get('cik'),
            'company_assigned_sic': self._company_data().get('assigned_sic'),
            'company_irs_no': self._company_data().get('irs_no'),
            'company': self._company_data(),

            'filing_values_form_type': self._filing_values().get('form_type'),
            'filing_values_act': self._filing_values().get('act'),
            'filing_values_file_no': self._filing_values().get('file_no'),
            'filing_values_film_no': self._filing_values().get('film_no'),
            'filing_values': self._filing_values(),

            'business_address_street1': self._biz_addr().get('street1'),
            'business_address_street2': self._biz_addr().get('street2'),
            'business_address_city': self._biz_addr().get('city'),
            'business_address_state': self._biz_addr().get('state'),
            'business_address_zip': self._biz_addr().get('zip'),
            'business_address': self._biz_addr(),

            'mailing_address_street1': self._mail_addr().get('street1'),
            'mailing_address_street2': self._mail_addr().get('street2'),
            'mailing_address_city': self._mail_addr().get('city'),
            'mailing_address_state': self._mail_addr().get('state'),
            'mailing_address_zip': self._mail_addr().get('zip'),
            'mailing_address': self._mail_addr()
        }
        return self.data

    def _accession_number(self):
        try:
            return re.findall(r'\<ACCESSION-NUMBER\>(.*)', self._data_str)[0]
        except Exception:
            return ''

    def _type(self):
        try:
            return re.findall(r'\<TYPE\>(.*)', self._data_str)[0]
        except Exception:
            return ''

    def _pub_doc_count(self):
        try:
            return re.findall(r'\<PUBLIC-DOCUMENT-COUNT\>(.*)', self._data_str)[0]
        except Exception:
            return ''

    def _filing_date(self):
        try:
            return re.findall(r'\<FILING-DATE\>(.*)', self._data_str)[0]
        except Exception:
            return ''

    def _filing_date_change(self):
        try:
            return re.findall(r'\<DATE-OF-FILING-DATE-CHANGE\>(.*)', self._data_str)[0]
        except Exception:
            return ''

    def _effectiveness_date(self):
        try:
            return re.findall(r'\<EFFECTIVENESS-DATE\>(.*)', self._data_str)[0]
        except Exception:
            return ''

    def _company_data(self):
        _company = ''
        try:
            _company = re.findall(r'\<COMPANY-DATA\>\n.+?\<\/COMPANY-DATA\>', self._data_str, re.DOTALL)[0]
        except Exception:
            pass

        d = {
            'conformed_name': '',
            'cik': '',
            'assigned_sic': '',
            'irs_no': ''
        }
        if _company:
            try:
                d['conformed_name'] = re.findall(r'\<CONFORMED-NAME\>(.*)', _company)[0]
            except Exception:
                pass
            try:
                d['cik'] = re.findall(r'\<CIK\>(.*)', _company)[0]
            except Exception:
                pass
            try:
                d['assigned_sic'] = re.findall(r'\<ASSIGNED-SIC\>(.*)', _company)[0]
            except Exception:
                pass
            try:
                d['irs_no'] = re.findall(r'\<IRS-NUMBER\>(.*)', _company)[0]
            except Exception:
                pass
        return d

    def _filing_values(self):
        _values = ''
        try:
            _values = re.findall(r'\<FILING-VALUES\>\n.+?\<\/FILING-VALUES\>', self._data_str, re.DOTALL)[0]
        except Exception:
            pass

        d = {
            'form_type': '',
            'act': '',
            'file_no': '',
            'film_no': ''
        }
        if _values:
            try:
                d['form_type'] = re.findall(r'\<FORM-TYPE\>(.*)', _values)[0]
            except Exception:
                pass
            try:
                d['act'] = re.findall(r'\<ACT\>(.*)', _values)[0]
            except Exception:
                pass
            try:
                d['file_no'] = re.findall(r'\<FILE-NUMBER\>(.*)', _values)[0]
            except Exception:
                pass
            try:
                d['film_no'] = re.findall(r'\<FILM-NUMBER\>(.*)', _values)[0]
            except Exception:
                pass
        return d

    def _biz_addr(self):
        _addr = ''
        try:
            _addr = re.findall(r'\<BUSINESS-ADDRESS\>\n.+?\<\/BUSINESS-ADDRESS\>', self._data_str, re.DOTALL)[0]
        except Exception:
            pass

        d = {
            'street1': '',
            'street2': '',
            'city': '',
            'state': '',
            'zip': ''
        }
        if _addr:
            try:
                d['street1'] = re.findall(r'\<STREET1\>(.*)', _addr)[0]
            except Exception:
                pass
            try:
                d['street2'] = re.findall(r'\<STREET2\>(.*)', _addr)[0]
            except Exception:
                pass
            try:
                d['city'] = re.findall(r'\<CITY\>(.*)', _addr)[0]
            except Exception:
                pass
            try:
                d['state'] = re.findall(r'\<STATE\>(.*)', _addr)[0]
            except Exception:
                pass
            try:
                d['zip'] = re.findall(r'\<ZIP\>(.*)', _addr)[0]
            except Exception:
                pass
        return d

    def _mail_addr(self):
        _addr = ''
        try:
            _addr = re.findall(r'\<MAIL-ADDRESS\>\n.+?\<\/MAIL-ADDRESS\>', self._data_str, re.DOTALL)[0]
        except Exception:
            pass

        d = {
            'street1': '',
            'street2': '',
            'city': '',
            'state': '',
            'zip': ''
        }
        if _addr:
            try:
                d['street1'] = re.findall(r'\<STREET1\>(.*)', _addr)[0]
            except Exception:
                pass
            try:
                d['street2'] = re.findall(r'\<STREET2\>(.*)', _addr)[0]
            except Exception:
                pass
            try:
                d['city'] = re.findall(r'\<CITY\>(.*)', _addr)[0]
            except Exception:
                pass
            try:
                d['state'] = re.findall(r'\<STATE\>(.*)', _addr)[0]
            except Exception:
                pass
            try:
                d['zip'] = re.findall(r'\<ZIP\>(.*)', _addr)[0]
            except Exception:
                pass
        return d
