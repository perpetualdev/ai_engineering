from abc import ABC, abstractmethod

# Initializing a class
class Student:
  def __init__(self, name, course, level):   # This runs automatically
    print("Creating a new student...")
    self.name = name
    self.course = course
    self.level = level
    print(f"Student {name} has been created!")

# When student is created, __init__ runs automatically
josh = Student("Joshua Adeniyi", "AI Engineering", 200)

print(josh.name)
print(josh.course)

class NigerianStudent:
  def __init__(self, name, state, course):
    print(f"Step1: Creating student object...")
    self.name = name                      #   Step 2: Assign name to THIS object
    self.state_of_origin = state          #   Step 3: Assign state to THIS object
    self.course = course                  #   Step 4: Assign course to THIS object
    self.student_id = self.generate_id()  #   Step 5: Generate ID for THIS object
    print(f"Step 6: {self.name} from {self.state_of_origin} is ready!")

  def generate_id(self):
    import random
    return f"UNISAIL{random.randint(1000, 9999)}"
  
# When you create an object, here's what happens:
ayo = NigerianStudent("Ayo Daniel", "Lagos", "Street Statistics")
print(ayo.name)
print(ayo.student_id)
"""
  Step1: Creating student object...
  Step 6: Ayo Daniel from Lagos is ready!
  Ayo Daniel
  UNISAIL6964
"""

# Another Example
class PhoneUser:
  def __init__(self, name, network):
    self.name = name
    self.network = network
    self.airtime = 0
    print(f"{self.name} joined {self.network} network")

  def buy_airtime(self, amount):
    self.airtime += amount    
    return f"{self.name} now has ₦{self.airtime} airtime"
  
# Creating multiple users
abeeb = PhoneUser("Abeeb Bakare", "MTN")
onisemo = PhoneUser("Onisemo Williams", "Airtel")
# Abeeb Bakare joined MTN network
# Onisemo Williams joined Airtel network

# Each person's actions affect only their own account
print(abeeb.buy_airtime(500))   #  Abeeb Bakare now has ₦500 airtime
print(onisemo.buy_airtime(1000)) #  Onisemo Williams now has ₦1000 airtime
print(abeeb.airtime)    # 500
print(onisemo.airtime)  # 1000

# Defining the Attributes of a Student
class Student:
  def __init__(self, name, course, level, state_of_origin):
    self.name = name
    self.course = course
    self.level = level
    self.state_of_origin = state_of_origin
    self.cgpa = 0.0

# Creating a student object/instance
Fathia = Student("Fathia Abdul", "Biochemistry", 300, "Ogun State")

# Accessing attributes
print(Fathia.name)
print(Fathia.course)
print(Fathia.state_of_origin)

# _________________ TYPES OF ATTRIBUTES _____________________
# Instance Attributes - unique to each object
student1 = Student("Anthony Johnson", "Engineering", 200, "Ogun")
student2 = Student("Fadilat Hassan", "Medicine", 400, "Lagos")

print(student1.name)
print(student2.name)

# Class Attributes - shared by all objects of the class
class Student2:
  university = "Federal University of Technology Akure"

  def __init__(self, name, course):
    self.name = name
    self.course = course

student1 = Student2("Anthony Johnson", "Engineering")
student2 = Student2("Fadilat Hassan", "Medicine")

print(Student2.university)
print(student1.university)
print(student2.university)

class Student3:
  def __init__(self, name, course, level):
    # Define Attributes
    self.name = name
    self.course = course
    self.level = level
    self.cgpa = 0.0
    self.fees_paid = False
  
  # Method: what the student can do
  def pay_school_fees(self):
    self.fees_paid = True
    return f"{self.name} has paid school fees for {self.level} level"
  
  # Method: another action
  def register_courses(self):
    if self.fees_paid:
      return f"{self.name} has registered courses for {self.course}"
    else:
      return f"{self.name} must pay school fees first!"
    
  # Method: calculates CGPA
  def calculate_cgpa(self, grades):
    if grades:
      self.cgpa = sum(grades) / len(grades)
      return f"{self.name}'s CGPA is now {self.cgpa:.2f}"
    return "No grades provided"
  
# Using the METHODS set above
Abiodun = Student3("Abiodun Akinola", "Gistology", 600)
print(Abiodun.pay_school_fees())
print(Abiodun.register_courses())
print(Abiodun.calculate_cgpa([4.2, 3.8, 4.0, 3.5]))
"""
  Abiodun Akinola has paid school fees for 600 level
  Abiodun Akinola has registered courses for Gistology
  Abiodun Akinola's CGPA is now 3.88
"""

# __________________ TYPES OF METHODS __________________
# Instance Methods - work with specific object data
def pay_school_fees(self):
  return f"{self.name} has paid school fees" 

# Class Methods - work with class-level data
@classmethod
def get_university(cls):
  return cls.university

# Static Methods - don't need object or class data
@staticmethod
def academic_calendar():
  return "Academic session runs from September to July"

# Relationship Between Attributes and Methods
class BankAccount:
  def __init__(self, owner, bank_name, balance=0):
    # Attributes - what the account has
    self.owner = owner
    self.bank_name = bank_name
    self.balance = balance
    self.account_number = self.generate_account_number()
  
  # METHODS - What the account can do
  def deposit(self, amount):
    # Add money to the account
    if amount > 0:
      self.balance += amount
      return f"₦{amount:,} deposited to {self.owner}'s {self.bank_name} account. New balance: ₦{self.balance:,}"
    return "Invalid deposit amount"
  
  def withdraw(self, amount):
    # Remove money from the account
    if amount > 0 and amount <= self.balance:
      self.balance -= amount   # Method changes attribute
      return f"₦{amount:,} withdrawn from {self.owner}'s account. New balance: ₦{self.balance:,}"
    return "Insufficient funds or invalid amount"
  
  def transfer(self, amount, recipient):
    # Transfer money to another account
    if amount > 0 and amount <= self.balance:
      self.balance -= amount
      return f"₦{amount:,} transferred from {self.owner} to {recipient}. Remaining balance: ₦{self.balance:,}"
    return "Transfer failed: Insufficient funds"
  
  def check_balance(self):
    # Check current balance
    return f"{self.owner}'s {self.bank_name} account balance: ₦{self.balance:,}"
  
  def generate_account_number(self):
    # Generate a unique account number
    import random
    return f"01{random.randint(10000000, 99999999)}"
  
# Creating and using the account
adunni_account = BankAccount("Adunni Olaleye", "AXT Bank", 50000)

# Attributes (Characteristics)
print(f"Owner: {adunni_account.owner}")
print(f"Bank: {adunni_account.bank_name}")
print(f"Account Number: {adunni_account.account_number}")

# Methods (actions)
print(adunni_account.deposit(25000))
print(adunni_account.withdraw(10000))
print(adunni_account.transfer(15000, "Sunday James"))
print(adunni_account.check_balance())

class NaijaPhone:
  def __init__(self, brand, model, network_provider):
    self.brand = brand
    self.model = model
    self.network_provider = network_provider
    self.airtime_balance = 0
    self.data_balance = 0
    self.is_on = False

  def power_on(self):
    self.is_on = True
    return f"{self.brand} phone is now on. Network: {self.network_provider}"
  
  def buy_airtime(self, amount):
    self.airtime_balance += amount
    return f"₦{amount} airtime purchased. Balance: ₦{self.airtime_balance}"
  
  def make_call(self, number):
    if self.is_on and self.airtime_balance > 0:
      self.airtime_balance -= 10
      return f"Calling {number}... Remaining airtime: ₦{self.airtime_balance}"
    return "Cannot make call. Check phone power and airtime balance"
  
  def send_sms(self, message, number):
    if self.airtime_balance >= 4:
      self.airtime_balance -= 4
      return f"SMS sent to {number}: '{message}'. Remaining airtime: ₦{self.airtime_balance}"
    return "Insufficient airtime to send SMS"
  
perpy_phone = NaijaPhone("Samsung", "A101", "MTN")

# Attributes
print(f"Brand: {perpy_phone.brand}")
print(f"Model: {perpy_phone.model}")
print(f"Network Provider: {perpy_phone.network_provider}")

# Methods
print(perpy_phone.power_on())
print(perpy_phone.buy_airtime(1000))
print(perpy_phone.make_call("08069683219"))
print(perpy_phone.send_sms("I have passed my August AI Engineering exam", "08069683219"))

class BRTBus:
  def __init__(self, route, bus_number):
    self.route = route
    self.bus_number = bus_number
    self.current_stop = "Ikorodu"
    self.passenger_count = 0
    self.fare = 300

  def announce_stop(self):
    return f"Next stop: {self.current_stop}. Fare is ₦{self.fare}"
  
  def board_passengers(self, count):
    self.passenger_count += count
    return f"{count} passengers boarded. Total: {self.passenger_count}"

abeokuta_sango = BRTBus("abeokuta_to_sango", "ATX 546 09B")

# Attributes
print(f"Route: {abeokuta_sango.route}")
print(f"Bus Number: {abeokuta_sango.bus_number}")

# Methods
print(abeokuta_sango.announce_stop())
print(abeokuta_sango.board_passengers(10))

class MarketTrader:
  def __init__(self, name, market_name, goods):
    self.name = name
    self.market_name = market_name
    self.goods = goods
    self.daily_sales = 0

  def advertise_goods(self):
    return f"{self.name} at {self.market_name}: Fresh {', '.join(self.goods)} available!"
  
  def make_sale(self, amount):
    self.daily_sales += amount
    return f"Sale made! Today's total: ₦{self.daily_sales:,}"

oniatarodo = MarketTrader("Seriki Ahmed", "Atarodo", ["Ata rodo", "Tomato", "Eja Kika"])

# Attributes
print(f"Trader Name: {oniatarodo.name}")
print(f"Market Name: {oniatarodo.market_name}")
print(oniatarodo.goods)

# Methods
print(oniatarodo.advertise_goods())
print(oniatarodo.make_sale(2500))

# ____________________ ENCAPSULATION ____________________
class NigerianBankAccount:
  def __init__(self, owner, initial_balance=0):
    self.owner = owner
    self._balance = initial_balance    # Protected attribute
    self.__pin = "1234"               # Private attribute
    self._transaction_history = []    # Protected attribute
  
  # Public methods - anyone can use these
  def deposit(self, amount):
    if amount > 0:
      self._balance += amount
      self._transaction_history.append(f"Deposited ₦{amount}")
      return f"₦{amount:,} deposited successfully"
    return "Invalid deposit amount"
  
  def withdraw(self, amount, pin):
    if self.__verify_pin(pin):  # Uses private method
      if amount <= self._balance:
        self._balance -= amount
        self._transaction_history.append(f"Withdrew ₦{amount:,}")
        return f"₦{amount:,} withdrawn successfully"
      return "Insufficient funds"
    return "Invalid PIN"
  
  def check_balance(self, pin):
    if self.__verify_pin(pin):
      return f"Current balance: ₦{self._balance:,}"
    return "Invalid PIN"
  
  # Private method - only the class can use this
  def __verify_pin(self, entered_pin):
    return entered_pin == self.__pin
  
  # Protected method - subclasses can use this
  def _get_transaction_history(self):
    return self._transaction_history.copy()
  
ibrahim_acct = NigerianBankAccount("Ibrahim Orekunrin", 50000)

# Public interfaces work
print(ibrahim_acct.deposit(10000))
print(ibrahim_acct.withdraw(5000, "1234"))
print(ibrahim_acct.check_balance("1234"))

# This won't work - Private/Protected Data
# print(ibrahim_acct.__pin)   #  AttributeError: 'NigerianBankAccount' object has no attribute '__pin'
# print(ibrahim_acct.__verify_pin("1234"))   #  AttributeError: 'NigerianBankAccount' object has no attribute '__verify_pin'

# _____________________ ABSTRACTION _____________________
# Abstract base class 
class NigerianStudent(ABC):
  def __init__(self, name, course, level):
    self.name = name
    self.course = course
    self.level = level
    self.fees_paid = False
  
  # Concrete method - all students can do this
  def pay_school_fees(self, amount):
    self.fees_paid = True
    return f"{self.name} paid ₦{amount:,} school fees"
  
  # Abstract method - each type of student implements differently
  @abstractmethod
  def study_method(self):
    pass

  @abstractmethod
  def take_exam(self):
    pass

# Concrete classes - specific implementations
class MedicalStudent(NigerianStudent):
  def study_method(self):
    return f"{self.name} studies anatomy books and practices on cadavers"
  
  def take_exam(self):
    return f"{self.name} takes practical exam in the anatomy lab"
  
class EngineeringStudent(NigerianStudent):
  def study_method(self):
    return f"{self.name} solves mathematical problems and builds prototypes"
  
  def take_exam(self):
    return f"{self.name} takes exam with calculations and technical drawings"
  
class ComputerScienceStudent(NigerianStudent):
  def study_method(self):
    return f"{self.name} codes programs and debugs software"
  
  def take_exam(self):
    return f"{self.name} takes practical programming exam on computer"
