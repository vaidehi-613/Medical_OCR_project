import re
from backend.src.parse_generic import MedicalDocParser

class PrescriptionPaser(MedicalDocParser):
    def __init__(self,text):
        MedicalDocParser.__init__(self,text)

    def parse(self):
        return{
            # 'patient_name' : self.get_name(),
            # 'patient_address' : self.get_address(),
            # 'medicines' : self.get_medicine(),
            # 'Directions' : self.get_directions(),
            # 'Refill' : self.get_refill()

            'patient_name': self.get_field('patient_name'),
            'patient_address' : self.get_field('patient_address' ),
            'medicines' : self.get_field('medicine'),
            'directions' : self.get_field('directions'),
            'refill' : self.get_field('refill')

        }

    def get_field(self,field_name):
        pattern_dict = {
            'patient_name': {'pattern': "Name:(.*)Date:" , 'flags' : 0 },
            'patient_address': {'pattern': "Address:(.*)\n" , 'flags' : 0},
            'medicine': {'pattern': "Address:[^\n]*(.*)Directions:" ,'flags' : re.DOTALL },
            'directions': {'pattern': "Directions:(.*)Refill:",'flags':re.DOTALL },
            'refill': {'pattern': 'Refill:(.*)times','flags': 0}

        }

        pattern_object = pattern_dict.get(field_name)
        if pattern_object:
            matches = re.findall(pattern_object['pattern'], self.text, flags= pattern_object['flags'])
            if len(matches) > 0:
                return matches[0].strip()

'''
    def get_name(self):
        pattern = "Name:(.*)Date:"
        matches = re.findall(pattern,self.text)
        if len(matches) >0:
            return matches[0].strip()

    def get_address(self):
        pattern = "Address:(.*)\n"
        matches = re.findall(pattern, self.text)
        if len(matches) > 0:
            return matches[0].strip()

    def get_medicine(self):
        pattern = "Address:[^\n]*(.*)Directions:"
        matches = re.findall(pattern, self.text,flags = re.DOTALL)
        if len(matches) > 0:
            return matches[0].strip()

    def get_directions(self):
        pattern = "Directions:(.*)Refill:"
        matches = re.findall(pattern,self.text, flags=re.DOTALL)
        if len(matches) >0:
            return matches.strip('\n')


    def get_refill(self):
        pattern = "Refill: (\d+) times"
        matches = re.findall(pattern, self.text,)
        if len(matches) > 0:
            return matches[0].strip()

'''

if __name__ == '__main__':

    text = """

    Name: Marta Sharapova Date: 5/11/2022

    Address: 9 tennis court, new Russia, DC

    Prednisone 20 mg
    Lialda 2.4 gram

    Directions:

    Prednisone, Taper 5 mg every 3 days,
    Finish in 2.5 weeks a
    Lialda - take 2 pill everyday for 1 month

    Refill: 2 times
    """

    pp = PrescriptionPaser(text)
    print(pp.parse())
