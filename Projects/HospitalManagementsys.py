class Base:
    def __init__(self, name, age, gender, ID):
        self.name = name
        self.age = age
        self.gender = gender
        self.ID = ID


class Doctor(Base):
    doctors_list = {}

    def __init__(self, name, age, gender, ID, specialization, doctor_ID):
        super().__init__(name, age, gender, ID)
        self.specialization = specialization
        self.doctor_ID = doctor_ID

    def assign_patient(self, patient_obj):
        if patient_obj:
            print("\n" + "=" * 50)
            print("        PATIENT ASSIGNMENT SLIP")
            print("=" * 50)
            print(f"Patient Name   : {patient_obj.name}")
            print(f"Assigned Doctor: {self.name}")
            print(f"Specialization : {self.specialization}")
            print(f"Doctor ID      : {self.doctor_ID}")
            print("=" * 50)

    def display_info(self):
        print("\n" + "=" * 50)
        print("            DOCTOR RECORD")
        print("=" * 50)
        print(f"Name           : {self.name}")
        print(f"Age            : {self.age}")
        print(f"Gender         : {self.gender}")
        print(f"Doctor ID      : {self.doctor_ID}")
        print(f"Specialization : {self.specialization}")
        print("=" * 50)


class Patients(Base):
    patients_list = {}

    def __init__(self, name, age, gender,ID, illness, specialization=None):
        super().__init__(name, age, gender,ID)
        self._illness = illness
        self.specialization = specialization
        Patients.patients_list[self.name] = self.specialization

    def get_illness(self):
        return self._illness
    
    def set_illness(self, Setted_illnes):
        self._illness = Setted_illnes 

    def book_apointment(self, doctor_obj):
        print("\n" + "=" * 50)
        print("          APPOINTMENT RECEIPT")
        print("=" * 50)
        if doctor_obj:
            print(f"Patient Name   : {self.name}")
            print(f"Doctor         : {doctor_obj.name}")
            print(f"Department     : {doctor_obj.specialization}")
            print("Status         : CONFIRMED")
        else:
            print("Status         : NO DOCTOR AVAILABLE")
        print("=" * 50)

    def schedule_appointment(self):
        print(f"General appointment scheduled for {self.name}")

    def view_doctor(self, doctor_obj):
        print("\n" + "=" * 50)
        print("          ASSIGNED DOCTOR")
        print("=" * 50)
        if doctor_obj:
            print(f"Doctor Name    : {doctor_obj.name}")
            print(f"Specialization : {doctor_obj.specialization}")
            print(f"Doctor ID      : {doctor_obj.doctor_ID}")
        else:
            print("No doctor assigned yet!")
        print("=" * 50)
    
    def display_info(self):
        print("\n" + "=" * 50)
        print("           PATIENT RECORD")
        print("=" * 50)
        print(f"Name           : {self.name}")
        print(f"Age            : {self.age}")
        print(f"Gender         : {self.gender}")
        print(f"Patient ID     : {self.ID}")
        print(f"Illness        : {self.get_illness()}")
        print("=" * 50)



class EmergencyPatient(Patients):
    def schedule_appointment(self):
        print(f"EMERGENCY appointment scheduled for {self.name}")


    def view_doctor(self, doctor_obj):
        print("\n" + "=" * 50)
        print("          ASSIGNED DOCTOR")
        print("=" * 50)
        if doctor_obj:
            print(f"Doctor Name    : {doctor_obj.name}")
            print(f"Specialization : {doctor_obj.specialization}")
            print(f"Doctor ID      : {doctor_obj.doctor_ID}")
        else:
            print("No doctor assigned yet!")
        print("=" * 50)

    def display_info(self):
        print("\n" + "=" * 50)
        print("           PATIENT RECORD")
        print("=" * 50)
        print(f"Name           : {self.name}")
        print(f"Age            : {self.age}")
        print(f"Gender         : {self.gender}")
        print(f"Patient ID     : {self.ID}")
        print(f"Illness        : {self.get_illness()}")
        print("=" * 50)
        


dr_Emily = Doctor("Dr. Emily",30,"Female",42501,"Cardiologist",'D101')
dr_Emily.display_info()

dr_Jonathan = Doctor("DR. Jonathan",46,"Male",43021,"Emergency ward","D102")
dr_Jonathan.display_info()

Alex = Patients("Alex",40,"Male",42506,"Heart Disease")
Alex.display_info()
print('-'*50)
print("\tPost-treatment symptom")
print('-'*50)
Alex.set_illness("Mild fever")
Alex.display_info()


Jhon = EmergencyPatient("Jhon",38,"Male",42309,'Heavy Bleeding')
Jhon.view_doctor(dr_Jonathan)
Jhon.display_info()
