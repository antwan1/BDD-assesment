from pytest_bdd import scenario, given, when, then


# NARRATIVE: USER STORY
# As a bank representative
# I want to be able to create, edit and delete customer information
# So that customers can apply for credit cards
@scenario(': a bank representative Creating data for new customer',scenario_name="data creation")
def test_create():
    pass


@given(" the user is on the create new customer page")
def customer_user(user, customer):
    user['user'] = customer.user


@given("enters first name which is 50 characters")
@given("enters last name which is 50 characters")
def name_input(name, target_fixture="name"):
    return test_create(name=name)
