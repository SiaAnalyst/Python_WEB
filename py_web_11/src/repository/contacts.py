from typing import List
from datetime import datetime, timedelta

from sqlalchemy import extract, func
from sqlalchemy.orm import Session
from sqlalchemy import and_

from src.database.models import Contact
from src.schemas import ContactModel, ContactUpdate


async def get_contacts(skip: int, limit: int, db: Session) -> List[Contact]:
    """
    The function returns a list of contacts.

    :param skip: int: Skip the first n records
    :param limit: int: Limit the number of contacts returned
    :param db: Session: Access the database
    :return: A list of contacts
    """
    return db.query(Contact).offset(skip).limit(limit).all()


async def get_contact(contact_id: int, db: Session) -> Contact:
    """
    The function returns a contact from the database.

    :param contact_id: int: Get the contact with that id
    :param db: Session: Access the database
    :return: A contact object
    """
    return db.query(Contact).filter(Contact.id == contact_id).first()


async def get_contacts_by_fname(first_name: str, db: Session) -> List[Contact]:
    """
    The function returns a list of contacts that match the first name provided.

    :param first_name: str: Filter the contacts by first name
    :param db: Session: Pass the database session to the function
    :return: A list of contacts with the matching first name
    """
    return db.query(Contact).filter(func.lower(Contact.first_name).like(f'%{first_name.lower()}%')).all()


async def get_contacts_by_lname(last_name: str, db: Session) -> List[Contact]:
    """
    The function returns a list of contacts that match the last name provided.

    :param last_name: str: Define the last name of the contact you are searching for
    :param db: Session: Access the database
    :return: A list of contacts with the last name matching the query
    """
    return db.query(Contact).filter(func.lower(Contact.last_name).like(f'%{last_name.lower()}%')).all()


async def get_contacts_by_email(email: str, db: Session) -> List[Contact]:
    """
    The function returns a list of contacts that match the email provided.

    :param email: str: Filter the contacts by email
    :param db: Session: Access the database
    :return: A list of contacts that match the email
    :doc-author: Trelent
    """
    return db.query(Contact).filter(Contact.email.like(f'%{email}%')).all()


async def get_contacts_by_birthday(db: Session) -> List[Contact]:
    """
    The function returns a list of contacts whose birthday is within the next week.

    :param db: Session: Pass in the database session
    :return: A list of contacts whose birthday is within the next 7 days
    """
    today = datetime.today().date()
    next_week = today + timedelta(days=7)

    contacts = db.query(Contact).filter(and_(extract('month', Contact.birthday) == next_week.month,
                                             extract('day', Contact.birthday) <= next_week.day,
                                             extract('day', Contact.birthday) >= today.day,
                                             )).all()

    birthday_contacts = []
    for contact in contacts:
        bday_this_year = contact.birthday.replace(year=today.year)
        if bday_this_year >= today:
            birthday_contacts.append(contact)
    return birthday_contacts


async def create_contact(body: ContactModel, db: Session) -> Contact:
    """
    The function creates a new contact in the database.

    :param body: ContactModel: Pass in the json data from the request body
    :param db: Session: Connect to the database
    :return: A contact object
    """
    contact = Contact(first_name=body.first_name, last_name=body.last_name, email=body.email, phone=body.phone,
                      birthday=body.birthday)
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact


async def update_contact(contact_id: int, body: ContactUpdate, db: Session) -> Contact | None:
    """
    The function updates a contact in the database.

    :param contact_id: int: Identify which contact to update
    :param body: ContactUpdate: Pass the json data to the function
    :param db: Session: Pass the database session to the function
    :return: A contact object, which is a model
    """
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        contact.first_name = body.first_name
        contact.last_name = body.last_name
        contact.email = body.email
        contact.phone = body.phone
        contact.birthday = body.birthday
        db.commit()
    return contact


async def remove_contact(contact_id: int, db: Session) -> Contact | None:
    """
    The function removes a contact from the database.

    :param contact_id: int: Identify the contact to be removed
    :param db: Session: Pass the database session to the function
    :return: A contact object
    """
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        db.delete(contact)
        db.commit()
    return contact

