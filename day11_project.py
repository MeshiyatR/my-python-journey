# DAY 11 PROJECT - Hospital Management System
# 12th May 2026

class Person:
    def __init__(self, name, age, phone):
        self.name = name
        self.age = age
        self.phone = phone

    def display(self):
        print(f"  Name  : {self.name}")
        print(f"  Age   : {self.age}")
        print(f"  Phone : {self.phone}")

class Doctor(Person):
    def __init__(self, name, age, phone,
                 specialization, fee):
        super().__init__(name, age, phone)
        self.specialization = specialization
        self.fee = fee
        self.patients = []

    def add_patient(self, patient):
        self.patients.append(patient)
        print(f"Patient {patient.name} assigned to Dr. {self.name}")

    def display(self):
        print("=" * 40)
        print("        DOCTOR DETAILS")
        print("=" * 40)
        super().display()
        print(f"  Spec  : {self.specialization}")
        print(f"  Fee   : Rs {self.fee}")
        print(f"  Patients: {len(self.patients)}")
        print("=" * 40)

class Patient(Person):
    def __init__(self, name, age, phone,
                 disease, doctor):
        super().__init__(name, age, phone)
        self.disease = disease
        self.doctor = doctor
        self.prescriptions = []

    def add_prescription(self, medicine):
        self.prescriptions.append(medicine)
        print(f"Prescription added: {medicine}")

    def display(self):
        print("=" * 40)
        print("        PATIENT DETAILS")
        print("=" * 40)
        super().display()
        print(f"  Disease : {self.disease}")
        print(f"  Doctor  : Dr. {self.doctor.name}")
        print(f"  Prescriptions:")
        for med in self.prescriptions:
            print(f"    → {med}")
        print("=" * 40)

class Hospital:
    def __init__(self, name):
        self.name = name
        self.doctors = []
        self.patients = []

    def add_doctor(self, doctor):
        self.doctors.append(doctor)
        print(f"Dr. {doctor.name} joined {self.name}")

    def add_patient(self, patient):
        self.patients.append(patient)
        print(f"Patient {patient.name} admitted")

    def display_all(self):
        print(f"\n{'=' * 40}")
        print(f"  {self.name}")
        print(f"{'=' * 40}")
        print(f"  Total Doctors : {len(self.doctors)}")
        print(f"  Total Patients: {len(self.patients)}")
        print(f"{'=' * 40}")

# Main program
hospital = Hospital("Python Medical Center")

doc1 = Doctor("Ahmed Khan", 45,
              "0300-1234567", "Cardiologist", 2000)
doc2 = Doctor("Sara Ali", 38,
              "0321-9876543", "Neurologist", 2500)

hospital.add_doctor(doc1)
hospital.add_doctor(doc2)

patient1 = Patient("Ali", 28,
                   "0313-1122334", "Headache", doc2)
patient2 = Patient("Bilal Hassan", 35,
                   "0312-5544332", "Heart Issue", doc1)

hospital.add_patient(patient1)
hospital.add_patient(patient2)

doc1.add_patient(patient2)
doc2.add_patient(patient1)

patient1.add_prescription("Paracetamol 500mg")
patient1.add_prescription("Vitamin B12")
patient2.add_prescription("Aspirin 75mg")
patient2.add_prescription("Beta Blockers")

while True:
    print("\n1 - View hospital summary")
    print("2 - View doctor details")
    print("3 - View patient details")
    print("4 - Quit")

    choice = input("\nEnter choice (1/2/3/4): ")

    if choice == "1":
        hospital.display_all()

    elif choice == "2":
        print("\n1. Dr. Ahmed Khan")
        print("2. Dr. Sara Ali")
        doc_choice = input("Select doctor: ")
        if doc_choice == "1":
            doc1.display()
        elif doc_choice == "2":
            doc2.display()

    elif choice == "3":
        print("\n1. Ali")
        print("2. Bilal Hassan")
        pat_choice = input("Select patient: ")
        if pat_choice == "1":
            patient1.display()
        elif pat_choice == "2":
            patient2.display()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")