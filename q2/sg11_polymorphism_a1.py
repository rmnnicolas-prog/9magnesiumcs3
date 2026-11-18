class Patient:
  def __init__(self,name,bill_amount):
    self.name = name, self.bill_amount = bill_amount 
    
  def get_name(self): 
    return self.name

  def set_name(self,name): 
    self.name = name

  def get_bill_amount(self): 
    return self.bill_amount

  def set_bill_amount(self,bill_amount):
    self.bill_amount = bill_amount

  def calculate_bill(self):
    return self.bill_amount

  def display_patient_type(self):
    print("Patient Type: Regular")

class SeniorPatient(Patient):
  def calculate_bill(self):
    return self.bill_amount * 0.8

  def display_patient_type(self): 
    print("Patient Type: Senior")

class PhilhealthPatient(Patient):
  def calculate_bill(self):
    return self.bill_amount * 0.85

  def display_patient_type(self):
    print("Patient Type: Philhealth")
    

p1 = Patient("Juan Dela Cruz", 15000)
p2 = SeniorPatient("Maria Santos", 15000)
p3 = PhilhealthPatient("Pedro Reyes", 15000)

print("Regular Patient:")
p1.display_patient_type()
print("Patient Name:", p1.get_name())
print("Orginal bill", p1.get_bill_amount())
print("Final bill", p1.calculate_bill())

print("Senior Patient:")
p2.display_patient_type()
print("Patient Name:", p2.get_name())
print("Original bill", p2.get_bill_amount())
print("Final bill", p2.calculate_bill())

print("Philhealth Patient:")
p3.display_patient_type()
print("Patient Name:", p3.get_name())
print("Original bill", p3.get_bill_amount())
print("Final bill", p3.calculate_bill())


    

    





  


