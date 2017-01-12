import random



class Department(object):
  """Parent class for all departments

  Methods: __init__, get_name, get_supervisor
  """
  def __init__(self, name, supervisor, employee_count):
      self.name = name
      self.supervisor = supervisor
      self.size = employee_count
      self.employees = set()


  def add_employee(self, employee):
    self.employees.add(employee)
    self.size += 1


  def get_name(self):
    """Returns the name of the department"""
    return self.name


  def get_supervisor(self):
    """Returns the name of the supervisor"""
    return self.supervisor


  def get_size(self):
    """Returns the size of the department"""
    return self.size


  def meeting_notice(self, time, location="meeting room 1"):
    '''Prints off a message for informing department members of an upcoming meeting
    
    Arguments: 
      time (string)
      location (string) (optional)
    '''
    print("Everyone please gather in {} at {} for a team meeting.".format(location, time))


  def get_budget(self, budget=15000):
    """Sets and returns the budget that a department gets each year. Can pass in an integer to set the budget to a value other than the default .

    Arguments:
      budget (integer) (optional)
    """
    self.annual_budget = budget
    return self.annual_budget




class Human_Resources(Department):
  """Class for representing Human Resources department

  Methods: __init__, add_policy, get_policy
  """
  def __init__(self, name, supervisor, employee_count):
    super().__init__(name, supervisor, employee_count)
    self.policies = set()


  def add_policy(self, policy_name, policy_text):
    """Adds a policy, as a tuple, to the set of policies

    Arguments:
      policy_name (string)
      policy_text (string)
    """
    self.policies.add((policy_name, policy_text))


  def get_policy(self, policy_name):
    """Returns the details of a given policy

    Arguments:
      policy_name (string)
    """
    # definitely gotta check this out, I'm sure I did it wrong
    # return {x for x in self.policies if x[0] == policy_name}
    for policy in self.policies:
      if policy[0] == policy_name:
        return policy

    # return {policy for policy in self.policies if policy[0] == policy_name}

  def meeting_notice(self, time):
    '''Prints off a message for informing department members of an upcoming meeting
    
    Arguments: 
      time (string)
    '''
    print("Everyone please gather in {}'s office at {} for a Human Resources team meeting.".format(self.get_supervisor(), time))


  def get_budget(self, modifier= -10000):
    """Returns the annual budget for this department. Can pass in an integer to change the budget modifier from the default value for this department.

    Arguments:
      modifier (integer) (optional)
    """
    self.annual_budget = super().get_budget() + modifier
    return self.annual_budget
    





class Sales(Department):
  """Class for representing Sales department

  Methods: __init__, add_product, remove_product, new_sale
  """
  def __init__(self, name, supervisor, employee_count):
    super().__init__(name, supervisor, employee_count)
    self.products = set()


  def add_product(self, product_name, product_price):
    """Adds a product, as a tuple, to the set of products

    Arguments:
      product_name (string)
      product_price (integer)
    """
    self.products.add((product_name, product_price))

  def get_product(self, product_name):
    """Returns the details of a given policy

    Arguments:
      policy_name (string)
    """
    # definitely gotta check this out, I'm sure I did it wrong
    # return {x for x in self.products if x[0] == product_name}
    for product in self.products:
      if product[0] == product_name:
        return product


  def remove_product(self, product_name):
    """Removes a product from the set of products

    Arguments:
      product_name (string)
    """
    self.products.discard(self.get_product(product_name))


  def get_products(self):
    return self.products

  def meeting_notice(self, time):
    '''Prints off a message for informing department members of an upcoming meeting
    
    Arguments: 
      time (string)
    '''
    print("At {}, everyone please gather in the backroom for a {} team meeting.".format(time, self.get_name()))


  def get_budget(self, modifier= 1):
    """Returns the annual budget for this department. Can pass in an integer to change the budget modifier from the default value for this department.

    Arguments:
      modifier (integer) (optional)
    """
    self.annual_budget = super().get_budget() + modifier
    return self.annual_budget





class Advertising(Department):
  """Class for representing Advertising department

  Methods: __init__, new_advertisement, get_advertisement
  """

  def __init__(self, name, supervisor, employee_count):
    super().__init__(name, supervisor, employee_count)
    self.advertisements = set()


  def new_advertisement(self, ad_product_name, ad_description, ad_budget):
    """Adds a new advertisement, as a tuple, to the set of advertisements

    Arguments:
      ad_product_name (string)
      ad_description (string)
      ad_budget (integer)
    """
    self.advertisements.add((ad_product_name, ad_description, ad_budget))


  def get_advertisement(self, product_name):
    """Returns a tuple that contains all the info for one advertisement

    Arguments:
      product_name
    """
    for ad in self.advertisements:
      if ad[0] == product_name:
        return ad

  def meeting_notice(self, time="immediately"):
    '''Prints off a message for informing department members of an upcoming meeting
    
    Arguments: 
      time (string) (optional)
    '''
    print("Get to {}'s office {} if you want to keep your job in Advertising!".format(self.get_supervisor(), time))


  def get_budget(self, modifier= 2000):
    """Returns the annual budget for this department. Can pass in an integer to change the budget modifier from the default value for this department.

    Arguments:
      modifier (integer) (optional)
    """
    self.annual_budget = super().get_budget() + modifier
    return self.annual_budget






class Research_and_Development(Department):
  """Class for representing Research and Development department

  Methods: __init__, new_concept, get_concept
  """

  def __init__(self, name, supervisor, employee_count):
    super().__init__(name, supervisor, employee_count)
    self.concepts = set()


  def new_concept(self, concept_title, concept_description, concept_budget):
    """Creates a new concept, as a tuple, and adds it to the set of concepts

    Arguments:
      concept_title (string)
      concept_description (string)
      concept_budget (integer)
    """
    self.concepts.add((concept_title, concept_description, concept_budget))


  def get_concept(self, concept_title):
    """Returns the details of a development concept when given the concept's name

    Arguments:
      concept_title (string)
    """
    for concept in self.concepts:
      if concept[0] == concept_title:
        return concept


  def meeting_notice(self, time):
    '''Prints off a message for informing department members of an upcoming meeting
    
    Arguments: 
      time (string)
    '''
    print("Everyone please be in the group video chat at {} for a R & D group meeting".format(time))


  def get_budget(self, modifier= 99999999):
    """Returns the annual budget for this department. Can pass in an integer to change the budget modifier from the default value for this department.

    Arguments:
      modifier (integer) (optional)
    """
    self.annual_budget = super().get_budget() + modifier
    return self.annual_budget









# Create a new class to represent an Employee.
# It's constructor should accept two parameters.
# First name of employee
# Last name of employee
# Define a method named eat() that will allow it to be invoked with the following four signatures.

# eat() - Will select a random restaurant name from a list of strings, print to console that the employee at at that restaurant, and also return the restaurant.
# eat(food="sandwich") - Will output that the employee ate that specific food at the office.
# eat(companions=[Sam, Dean, Alice]) - Will select a random restaurant name from a list of strings, print to console that the employee at that restaurant, and also output the first name of each employee in the specified list.
# eat("pizza", [Sam, Dean, Alice]) - Will select a random restaurant name from a list of strings, print to console that the employee at that restaurant, and ordered the specified food, with the first name of the teammates specified in the list.

# Note: Notice that this signature doesn't require that the parameters to be named

class Employee(object):
  """Class for representing an employee

  Methods: __init__, eat
  """

  def __init__(self, first_name, last_name):
    self.first_name = first_name
    self.last_name = last_name

    # if department != None
    # self.department = department
    # self.department.add_employee(self)



  def eat(self, food=None, companions=None):
    restaurants = ("Olive Garden", "McDonalds", "Gojo", "Kroger")
    lunch_companions = ""
    if food==None and companions==None:
      print_statement = "{} {} ate at {}.".format(self.first_name, self.last_name, random.choice(restaurants))
    if food!=None and companions==None:
      print_statement = "{} ate {} at the office.".format(self.first_name, food)
    if food==None and companions!=None:
      for companion in companions:
        lunch_companions += "{}, ".format(companion.first_name)
      print_statement = "{} ate at {} with {}.".format(self.first_name, random.choice(restaurants), lunch_companions[0:-2])
    if food!=None and companions!=None:
      for companion in companions:
        lunch_companions += "{}, ".format(companion.first_name)
      print_statement = "{} went to {} with {} and ate {}.".format(self.first_name, random.choice(restaurants), lunch_companions[0:-2], food)


    print(print_statement)



class Full_Time(object):
  """Describes full-time employees"""

  def __init__(self):
    self.hours_per_week = 40



class Part_Time(object):
  """Describes part-time employees"""

  def __init__(self):
    self.hours_per_week = 24
    

class Authorized_Employee(object):
  """Describes employees with security authorization

  Methods: get_authorization_level, set_authorization_level
  """
  def __init__(self, auth_level=0):
    """Initializes employee's authorization level
    
    Arguments:
      auth_level (integer 0 - 5) (optional)
    """
    self.authorization_level = auth_level

  def get_authorization_level(self):
    """Returns this employee's authorization level"""
    return self.authorization_level

  def set_authorization_level(self, new_auth_level):
    """Changes employee's authorization level

    Arguments: 
      new_auth_level (integer 0 - 5)
    """
    self.authorization_level = new_auth_level


class Human_Resources_Employee(Employee, Full_Time, Authorized_Employee):
  """Describes human resources employees"""

  def __init__(self, first_name, last_name):
    # Note that we can't use super() any more because there is
    # more than one class being inherited from. Because of that
    # we have to call the constructor of each parent class individually
    Employee.__init__(self, first_name, last_name)
    Full_Time.__init__(self)
    Authorized_Employee.__init__(self, 2)







if __name__ == '__main__':


  ########################################################### bangazon_01

  # Create some instances of each department.
  # Assign values to the properties of each.

  HR = Human_Resources("Human Resources", "Bob", 1)
  HR.add_policy("No Jerks", "If you are a jerk, you will be fired.")
  print(HR.get_policy("No Jerks"))

  Sales = Sales("Sales", "Janette", 1)
  Sales.add_product("Slinky", 6.00)
  Sales.add_product("Rubber Band Ball", 2.00)
  print("Products before removal: ", Sales.get_products())
  Sales.remove_product("Rubber Band Ball")
  print("Products after removal: ", Sales.get_products())

  Ads = Advertising("Advertising", "Adolf", 1)
  Ads.new_advertisement("Slinky", "We need a high-budget spot to air during the superbowl that truly represents the power of the slinky", 9.99)
  print(Ads.get_advertisement("Slinky"))

  R_and_D = Research_and_Development("Research & Development", "Santa", 1)
  R_and_D.new_concept("The Levitating Toaster", "It's a toaster that levitates", 1234567.00)
  print(R_and_D.get_concept("The Levitating Toaster"))



  print("Use print() to output the name of each of your department instances.")
  print(HR.get_name())
  print(Sales.get_name())
  print(Ads.get_name())
  print(R_and_D.get_name())



  ############################################################ bangazon_02



  # Override

  R_and_D.meeting_notice("2 AM")
  Ads.meeting_notice()
  Sales.meeting_notice("3 PM")
  HR.meeting_notice("Noon")


  # Override, but use parent


  print(HR.get_budget())
  print(Sales.get_budget())
  print(Ads.get_budget())
  print(R_and_D.get_budget())







  ############################################################ bangazon_03


  Sam = Employee("Sam", "Phillips")
  Allie = Employee("Allie", "Guillory")
  Hunter = Employee("Hunter", "Bates")
  Sam.eat()
  Sam.eat(food="Truffles")
  Sam.eat(companions=[Allie, Hunter])
  Sam.eat("Watermelon", [Allie, Hunter])




  ############################################################ bangazon_04


  Bob = Human_Resources_Employee("Bob", "Barker")
  print("Bob works {} hours per week".format(Bob.hours_per_week))
  print("{}'s authorization level is {}".format(Bob.first_name, Bob.authorization_level))














