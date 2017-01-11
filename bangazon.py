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


 class HumanResources(Department):
    """Class for representing Human Resources department

    Methods: __init__, add_policy, get_policy
    """

    def __init__(self, name, supervisor, employee_count):
      super().__init__(name, supervisor, employee_count)
      self.policies = {}

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

      return {x for x in self.policies if x[0] == policy_name}

class Sales(Department):
  """Class for representing Sales department

  Methods: __init__, add_product, remove_product, new_sale
  """

  def __init__(self, name, supervisor, employee_count):
    super().__init__(name, supervisor, employee_count)
    self.products = {}
















    