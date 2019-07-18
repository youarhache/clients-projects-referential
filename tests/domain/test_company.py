import uuid
from projectsref.domain import company as c
from datetime import datetime


def test_company_model_init():
    code = str(uuid.uuid4())
    my_datetime = datetime.now()
    co = c.Company(code, name="Test Companie", group = "Grand Groupe", last_visited = my_datetime)
    assert co.code == code
    assert co.name == "Test Companie"
    assert co.group == "Grand Groupe"
    assert co.last_visited == my_datetime


def test_company_model_from_dict():
    code = str(uuid.uuid4())
    my_datetime = datetime.now().date
    dico = {
        "code" : code,
        "name" : "Test Companie",
        "group" : "Grand Groupe",
        "last_visited" : my_datetime
    }

    cpny = c.Company.from_dict(dico)
    assert cpny.code == code
    assert cpny.name == "Test Companie"
    assert cpny.group == "Grand Groupe"
    assert cpny.last_visited == my_datetime


def test_company_model_to_dict():
    code = str(uuid.uuid4())
    my_datetime = datetime.now().date
    dico = {
        "code" : code,
        "name" : "Test Companie",
        "group" : "Grand Groupe",
        "last_visited" : my_datetime
    }
    cpny = c.Company.from_dict(dico)
    assert dico == cpny.to_dict()
    

def test_company_model_equal():
    code = str(uuid.uuid4())
    my_datetime = datetime.now().date
    dico = {
        "code" : code,
        "name" : "Test Companie",
        "group" : "Grand Groupe",
        "last_visited" : my_datetime
    }
    cpny1 = c.Company.from_dict(dico)
    cpny2 = c.Company.from_dict(dico)

    assert cpny1 == cpny2