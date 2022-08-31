from backend.src.parser_prescription import PrescriptionPaser
import pytest

def test_get_name():
    pp = PrescriptionPaser(doc_text)
    assert pp.get_field('patient') == 'Marta Sharapova'

def test_get_address():
    pp = PrescriptionPaser(doc_text)
    assert pp.get_field('patient_address') == '9 tennis court, new Russia, DC'

doc_text = '''
    Name: Marta Sharapova Date: 5/11/2022

    Address: 9 tennis court, new Russia, DC

    Prednisone 20 mg
    Lialda 2.4 gram

    Directions:

    Prednisone, Taper 5 mg every 3 days,
    Finish in 2.5 weeks a
    Lialda - take 2 pill everyday for 1 month

    Refill: 2 times'''