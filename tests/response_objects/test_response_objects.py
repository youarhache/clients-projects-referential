import pytest
from projectsref.request_response_objects import response_objects as resp
from projectsref.request_response_objects import request_objects as req


@pytest.fixture
def response_value():
    return {'key': ['value1', 'value2']}


@pytest.fixture
def response_type():
    return 'ResponseError'


@pytest.fixture
def response_message():
    return 'This is a response error'


def test_response_success_is_true(response_value):
    assert bool(resp.ResponseSuccess(response_value)) is True


def test_response_success_has_type_and_value(response_value):
    response = resp.ResponseSuccess(response_value)
    assert response.type == resp.ResponseSuccess.SUCCESS
    assert response.value == response_value


def test_response_failure_is_false(response_type, response_message):
    assert bool(resp.ResponseFailure(response_type, response_message)) is False


def test_response_failure_has_type_and_message(response_type, response_message):
    response = resp.ResponseFailure(response_type, response_message)
    assert response.type == response_type
    assert response.message == response_message


def test_response_failure_contains_value(response_type, response_message):
    response = resp.ResponseFailure(response_type, response_message)
    assert response.value == {
    'type': response_type, 'message': response_message}


def test_response_failure_initialisation_with_exception():
    response = resp.ResponseFailure(
    response_type, Exception("Juste un message d'erreur"))
    assert bool(response) is False
    assert response.type == response_type
    assert response.message == "Exception: Juste un message d'erreur"


def test_response_failure_from_empty_invalid_request_object():
    response = resp.ResponseFailure.build_from_invalid_request_object(
    req.InvalidRequestObj())
    assert bool(response) is False
    assert response.type == resp.ResponseFailure.PARAMETERS_ERROR


def test_response_failure_from_invalid_request_object_with_errors():
    request_object = req.InvalidRequestObj()
    request_object.add_error('monParam', 'Champ obligatoir')
    request_object.add_error('monParam', "Ne peut pas être vide")
    response = resp.ResponseFailure.build_from_invalid_request_object(
    request_object)
    assert bool(response) is False
    assert response.type == resp.ResponseFailure.PARAMETERS_ERROR
    assert response.message == "monParam: Champ obligatoir\nmonParam: Ne peut pas être vide"


def test_response_failure_build_resource_error():
    response = resp.ResponseFailure.build_resource_error("test message")
    assert bool(response) is False
    assert response.type == resp.ResponseFailure.RESOURCE_ERROR
    assert response.message == "test message"


def test_response_failure_build_parameters_error():
    response = resp.ResponseFailure.build_parameters_error("test message")
    assert bool(response) is False
    assert response.type == resp.ResponseFailure.PARAMETERS_ERROR
    assert response.message == "test message"


def test_response_failure_build_system_error():
    response = resp.ResponseFailure.build_system_error("test message")
    assert bool(response) is False
    assert response.type == resp.ResponseFailure.SYSTEM_ERROR
    assert response.message == "test message"