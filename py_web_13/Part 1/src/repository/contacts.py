from typing import List
from datetime import datetime, timedelta
from sqlalchemy import and_

from sqlalchemy import extract, func
from sqlalchemy.orm import Session

from src.database.models import Contact, User
from src.schemas import ContactModel, ContactUpdate


async def get_contacts(skip: int, limit: int, user: User, db: Session) -> List[Contact]:
    return db.query(Contact).filter(Contact.user_id == user.id).offset(skip).limit(limit).all()


async def get_contact(contact_id: int, user: User, db: Session) -> Contact:
    return db.query(Contact).filter(and_(Contact.user_id == user.id, Contact.id == contact_id)).first()


async def get_users_by_info(contact_info: str, user: User, db: Session) -> List[User]:
    response = []
    info_by_first_name = db.query(Contact).filter(
        and_(Contact.user_id == user.id, func.lower(Contact.first_name).like(f'%{contact_info.lower()}%'))).all()
    if info_by_first_name:
        for n in info_by_first_name:
            response.append(n)
    info_by_last_name = db.query(Contact).filter(
        and_(Contact.user_id == user.id, func.lower(Contact.last_name).like(f'%{contact_info.lower()}%'))).all()
    if info_by_last_name:
        for n in info_by_last_name:
            response.append(n)
    info_by_email = db.query(Contact).filter(
        and_(Contact.user_id == user.id, Contact.email.like(f'%{contact_info}%'))).all()
    if info_by_email:
        for n in info_by_email:
            response.append(n)

    return response


async def get_contacts_by_birthday(user: User, db: Session) -> List[Contact]:
    today = datetime.today().date()
    next_week = today + timedelta(days=7)

    contacts = db.query(Contact).filter(and_(Contact.user_id == user.id,
                                             extract('month', Contact.birthday) == next_week.month,
                                             extract('day', Contact.birthday) <= next_week.day,
                                             extract('day', Contact.birthday) >= today.day,
                                             )).all()

    birthday_contacts = []
    for contact in contacts:
        bday_this_year = contact.birthday.replace(year=today.year)
        if bday_this_year >= today:
            birthday_contacts.append(contact)
    return birthday_contacts


async def create_contact(body: ContactModel, user: User, db: Session) -> Contact:
    contact = Contact(first_name=body.first_name, last_name=body.last_name, email=body.email, phone=body.phone,
                      birthday=body.birthday, user_id=user.id)
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact


async def update_contact(contact_id: int, body: ContactUpdate, user: User, db: Session) -> Contact | None:
    contact = db.query(Contact).filter(and_(Contact.user_id == user.id, Contact.id == contact_id)).first()
    if contact:
        contact.first_name = body.first_name
        contact.last_name = body.last_name
        contact.email = body.email
        contact.phone = body.phone
        contact.birthday = body.birthday
        db.commit()
    return contact


async def remove_contact(contact_id: int, user: User, db: Session) -> Contact | None:
    contact = db.query(Contact).filter(and_(Contact.user_id == user.id, Contact.id == contact_id)).first()
    if contact:
        db.delete(contact)
        db.commit()
    return contact

