class Department(object):
  """Parent class for all departments

  Methods: __init__, get_name, get_supervisor
  """
  def __init__(self, name, supervisor, employee_count):
      self.name = name
      self.supervisor = supervisor
      self.size = employee_count


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




if __name__ == '__main__':


  ########################################################### bangazon_01

  # Create some instances of each department.
  # Assign values to the properties of each.

  HR = Human_Resources("Human Resources", "Bob", 2)
  HR.add_policy("No Jerks", "If you are a jerk, you will be fired.")
  print(HR.get_policy("No Jerks"))

  Sales = Sales("Sales", "Janette", 5)
  Sales.add_product("Slinky", 6.00)
  Sales.add_product("Rubber Band Ball", 2.00)
  print("Products before removal: ", Sales.get_products())
  Sales.remove_product("Rubber Band Ball")
  print("Products after removal: ", Sales.get_products())

  Ads = Advertising("Advertising", "Adolf", 1000000)
  Ads.new_advertisement("Slinky", "We need a high-budget spot to air during the superbowl that truly represents the power of the slinky", 9.99)
  print(Ads.get_advertisement("Slinky"))

  R_and_D = Research_and_Development("Research & Development", "Santa", 99)
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









