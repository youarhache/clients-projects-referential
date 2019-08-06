import pytest
from projectsref.request_response_objects import request_objects as req


def test_contacts_list_request_without_params():
    request = req.ContactsListRequestObj()

    assert request.filters is None
    assert bool(request) is True


def test_contacts_list_request_empty_from_dict():
    request = req.ContactsListRequestObj.from_dict({})

    assert request.filters is None
    assert bool(request) is True


def test_contacts_list_request_empty_filters():
    request = req.ContactsListRequestObj(filters={})

    assert request.filters == {}
    assert bool(request) is True


def test_contacts_list_request_from_dict_empty_filters():
    request = req.ContactsListRequestObj.from_dict({'filters':{}})

    assert request.filters == {}
    assert bool(request) is True


def test_contacts_list_request_from_dict_with_filters_wrong():
    request = req.ContactsListRequestObj.from_dict({'filters':{'a':0}})

    assert request.has_errors()
    assert request.errors[0]['parameter'] == 'filters'
    assert bool(request) is False


def test_contacts_list_request_from_dict_with_invalid_filters():
    request = req.ContactsListRequestObj.from_dict({'filters':0})

    assert request.has_errors()
    assert request.errors[0]['parameter'] == 'filters'
    assert bool(request) is False


@pytest.mark.parametrize('key',
                        ['code__eq', 'fname__eq', 'lname__eq', 'email__eq', 'is_client__eq', 'is_primary__eq'])
def test_contacts_list_request_from_dict_accepted_filters(key):
    filters = {key:1}
    request = req.ContactsListRequestObj.from_dict({'filters': filters})

    assert request.filters == filters
    assert bool(request) is True


@pytest.mark.parametrize('key',
                        ['code__gt', 'fname__gt', 'lname__gt', 'email__gt', 'is_client__gt', 'is_primary__gt',
                        'code__lt', 'fname__lt', 'lname__lt', 'email__lt', 'is_client__lt', 'is_primary__lt'])
def test_contacts_list_request_from_dict_rejected_filters(key):
    filters = {key:1}
    request = req.ContactsListRequestObj.from_dict({'filters': filters})

    assert request.has_errors()
    assert request.errors[0]['parameter'] == 'filters'
    assert bool(request) is False
