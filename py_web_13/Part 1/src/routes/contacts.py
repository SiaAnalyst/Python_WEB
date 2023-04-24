from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_limiter.depends import RateLimiter
from sqlalchemy.orm import Session

from src.services.auth import auth_service
from src.database.db import get_db
from src.schemas import ContactModel, ContactResponse
from src.database.models import User
from src.repository import contacts as repository_contacts

router = APIRouter(prefix='/contacts', tags=["contacts"])


@router.get(
    "/all",
    response_model=List[ContactResponse],
    description='No more than 1 requests per 3 minute',
    dependencies=[Depends(RateLimiter(times=15, seconds=120))]
)
async def get_contacts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db),
                       current_user: User = Depends(auth_service.get_current_user)):
    contacts = await repository_contacts.get_contacts(skip, limit, current_user, db)
    if not contacts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='NOT_FOUND')
    return contacts


@router.get(
    "/by_id/{contact_id}",
    response_model=ContactResponse,
    description='No more than 1 requests per 3 minute',
    dependencies=[Depends(RateLimiter(times=15, seconds=120))]
)
async def get_contact(contact_id: int, db: Session = Depends(get_db),
                      current_user: User = Depends(auth_service.get_current_user)):
    contact = await repository_contacts.get_contact(contact_id, current_user, db)
    if not contact:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='NOT_FOUND')
    return contact


@router.get(
    "/by_fname/{first_name}",
    response_model=List[ContactResponse],
    description='No more than 1 requests per 3 minute',
    dependencies=[Depends(RateLimiter(times=15, seconds=120))]
)
async def get_contacts_by_fname(first_name: str, db: Session = Depends(get_db),
                                current_user: User = Depends(auth_service.get_current_user)):
    contacts = await repository_contacts.get_contacts_by_fname(first_name, current_user, db)
    if not contacts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='NOT_FOUND')
    return contacts


@router.get(
    "/by_lname/{last_name}",
    response_model=List[ContactResponse],
    description='No more than 1 requests per 3 minute',
    dependencies=[Depends(RateLimiter(times=15, seconds=120))]
)
async def get_contacts_by_lname(last_name: str, db: Session = Depends(get_db),
                                current_user: User = Depends(auth_service.get_current_user)):
    contacts = await repository_contacts.get_contacts_by_lname(last_name, current_user, db)
    if not contacts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='NOT_FOUND')
    return contacts


@router.get(
    "/by_email/{email}",
    response_model=List[ContactResponse],
    description='No more than 1 requests per 3 minute',
    dependencies=[Depends(RateLimiter(times=15, seconds=120))]
)
async def get_contacts_by_email(email: str, db: Session = Depends(get_db),
                                current_user: User = Depends(auth_service.get_current_user)):
    contacts = await repository_contacts.get_contacts_by_email(email, current_user, db)
    if not contacts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='NOT_FOUND')
    return contacts


@router.post(
    "/",
    response_model=ContactResponse,
    description='No more than 1 requests per 3 minute',
    dependencies=[Depends(RateLimiter(times=15, seconds=120))]
)
async def create_contact(body: ContactModel, db: Session = Depends(get_db),
                         current_user: User = Depends(auth_service.get_current_user)):
    return await repository_contacts.create_contact(body, current_user, db)


@router.put(
    "/{contact_id}",
    response_model=ContactResponse,
    description='No more than 1 requests per 3 minute',
    dependencies=[Depends(RateLimiter(times=15, seconds=120))]
)
async def update_contact(body: ContactModel, contact_id: int, db: Session = Depends(get_db),
                         current_user: User = Depends(auth_service.get_current_user)):
    contact = await repository_contacts.update_contact(contact_id, body, current_user, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='NOT_FOUND')
    return contact


@router.delete(
    "/{contact_id}",
    response_model=ContactResponse,
    description='No more than 1 requests per 3 minute',
    dependencies=[Depends(RateLimiter(times=15, seconds=120))]
)
async def remove_contact(contact_id: int, db: Session = Depends(get_db),
                         current_user: User = Depends(auth_service.get_current_user)):
    contact = await repository_contacts.remove_contact(contact_id, current_user, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='NOT_FOUND')
    return contact

