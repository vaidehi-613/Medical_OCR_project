import pytest
from backend.src.parse_patient_details import PatientDetailsParser

@pytest.fixture()
def doc_1_kathy():

    doc_text ='''
   17/12/2020

Patient Medical Record

Patient Information Birth Date

Kathy Crawford May 6 1972

(737) 988-0851 Weight’

9264 Ash Dr 95

New York City, 10005 '

United States Height:
190

In Case of Emergency
ee J
Simeone Crawford 9266 Ash Dr
New York City, New York, 10005
Home phone United States
(990) 375-4621
Work phone
Genera! Medical History
nn ee
Chicken Pox (Varicella): Measies:
IMMUNE

IMMUNE
Have you had the Hepatitis B vaccination?

No

List any Medical Problems (asthma, seizures, headaches}:

Migraine'''

    return PatientDetailsParser(doc_text)

@pytest.fixture()
def doc_2_jerry():

    document_text = '''
    Patient Medical Record

    Patient Information
    Jerry Lucas

    (279) 920-8204

    4218 Wheeler Ridge Dr
    Buffalo, New York, 14201
    United States

    In Case of Emergency

    -_ OCC OO eee

    Joe Lucas

    Home phone

    General Medical History



    Chicken Pox (Varicelia):
    IMMUNE
    Have you had the Hepatitis B vaccination?

    Yes”

    Birth Date
    May 2 1998

    Weight:
    57

    Height:
    170

    4218 Wheeler Ridge Dr
    Buffalo, New York, 14201
    United States

    Work phone

    Measles: .

    NOT IMMUNE

    List any Medical Problems (asthma, seizures, headaches):

    N/A
        '''
    return PatientDetailsParser(document_text)

def test_get_patient_name(doc_1_kathy,doc_2_jerry):
    assert doc_1_kathy.get_patient_name() == 'Kathy Crawford'
    assert doc_2_jerry.get_patient_name() == ' Jerry Lucas'






