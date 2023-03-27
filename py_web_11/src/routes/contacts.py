from typing import List

from fastapi import APIRouter, Depends, HTTPException, Path, status
from sqlalchemy.orm import Session
from datetime import date, timedelta

from src.database.connect_db import get_db
from src.database.models import Contact
from src.schemas import ContactModel, ContactResponse
from src.repository import contacts as repository_contacts

router = APIRouter(prefix='/contacts', tags=["contacts"])


@router.get(
    "/",
    response_model=List[ContactResponse]
)
async def get_contacts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    The function returns a list of contacts.
    It takes in an optional skip and limit parameter to paginate the results.

    :param skip: int: Skip the first n contacts
    :param limit: int: Limit the number of contacts returned
    :param db: Session: Pass the database session to the repository layer
    :return: A list of contact objects
    """

    contacts = await repository_contacts.get_contacts(skip, limit, db)
    if not contacts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='NOT_FOUND')
    return contacts


@router.get(
    "/by_id/{contact_id}",
    response_model=ContactResponse
)
async def get_contact(contact_id: int, db: Session = Depends(get_db)):
    """
    The function returns a contact by its id.

    :param contact_id: int: Identify the contact that is to be read
    :param db: Session: Get the database session
    :return: A contact object
    """
    contact = await repository_contacts.get_contact(contact_id, db)
    if not contact:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='NOT_FOUND')
    return contact


@router.get(
    "/by_fname/{first_name}",
    response_model=List[ContactResponse]
)
async def get_contacts_by_fname(first_name: str, db: Session = Depends(get_db)):
    """
    The function returns a list of contacts with the given first name.
    It takes in a string representing the first name and returns a list of contacts.

    :param first_name: str: Pass the first name of a contact to be searched for
    :param db: Session: Get the database connection
    :return: A list of contacts with the specified first name
    """
    contacts = await repository_contacts.get_contacts_by_fname(first_name, db)
    if not contacts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='NOT_FOUND')
    return contacts


@router.get(
    "/by_lname/{last_name}",
    response_model=List[ContactResponse]
)
async def get_contacts_by_lname(last_name: str, db: Session = Depends(get_db)):
    """
    The function returns a list of contacts with the specified last name.
    It takes in a string representing the last name and returns a list of contacts.

    :param last_name: str: Pass the last name of the contact to be searched for
    :param db: Session: Pass the database session to the repository layer
    :return: A list of contacts with the specified last name
    """
    contacts = await repository_contacts.get_contacts_by_lname(last_name, db)
    if not contacts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='NOT_FOUND')
    return contacts


@router.get(
    "/by_email/{email}",
    response_model=List[ContactResponse])
async def get_contacts_by_email(email: str, db: Session = Depends(get_db)):
    """
    The function returns a list of contacts with the specified email address.

    :param email: str: Filter the contacts by email
    :param db: Session: Pass the database session to the function
    :return: A list of contacts
    """

    contacts = await repository_contacts.get_contacts_by_email(email, db)
    if not contacts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='NOT_FOUND')
    return contacts


@router.post(
    "/",
    response_model=ContactResponse
)
async def create_contact(body: ContactModel, db: Session = Depends(get_db)):
    """
    The function creates a new contact in the database.
    It takes a ContactModel object as input, and returns the newly created contact.

    :param body: ContactModel: Validate the data that is passed to the function
    :param db: Session: Get the database connection from the dependency injection
    :return: A contact model object, which is a pydantic model
    """
    return await repository_contacts.create_contact(body, db)


@router.put(
    "/{contact_id}",
    response_model=ContactResponse
)
async def update_contact(body: ContactModel, contact_id: int, db: Session = Depends(get_db)):
    """
    The function updates a contact in the database.

    :param body: ContactModel: Pass the contact information to be updated
    :param contact_id: int: Identify the contact to be updated
    :param db: Session: Pass the database session to the repository layer
    :return: A contact model object
    """
    contact = await repository_contacts.update_contact(contact_id, body, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='NOT_FOUND')
    return contact


@router.delete(
    "/{contact_id}",
    response_model=ContactResponse
)
async def remove_contact(contact_id: int, db: Session = Depends(get_db)):
    """
    The function removes a contact from the database.

    :param contact_id: int: Specify the contact id of the contact to be removed
    :param db: Session: Get the database session
    :return: A contact object
    """
    contact = await repository_contacts.remove_contact(contact_id, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='NOT_FOUND')
    return contact

