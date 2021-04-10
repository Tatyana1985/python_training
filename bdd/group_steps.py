import random

import pytest
from pytest_bdd import given, when, then

from model.group import Group

@pytest.fixture
@given('a group list')
def group_list(db):
    return db.get_group_list()

@pytest.fixture
@given('a group with <name>, <header> and <footer>')
def new_group(name, header, footer):
    return Group(name=name, header=header, footer=footer)

@pytest.fixture
@when('I add the group to the list')
def add_new_group(app, new_group):
    app.group.create(new_group)

@pytest.fixture
@then('the new group list is equal to the old list with the added group')
def verify_group_added(db, group_list):
    old_groups = group_list
    new_groups = db.get_group_list()
    old_groups.append(new_group)
    assert old_groups == new_groups

@pytest.fixture
@given('a non-empty group list')
def non_empty_group_list(db, app):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    return db.get_group_list()

@pytest.fixture
@given('a random group from the list')
def random_group(non_empty_group_list):
    return random.choice(non_empty_group_list)

@pytest.fixture
@when('I delete the group from the list')
def delete_group(app, random_group):
    app.group.delete_group_by_id(random_group.id)

@pytest.fixture
@then('the new list is equal to the old list without the deleted group')
def verify_group_delete(db, non_empty_group_list, random_group, app ):
    old_groups = non_empty_group_list
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups.remove(random_group)
    assert old_groups == new_groups

