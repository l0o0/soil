from app.models.journal import CNKIM, AbbreviationM
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


async def get_journal_meta_by_name(journal: str, db_session: AsyncSession):
    cnki = (await db_session.scalars(select(CNKIM).where(CNKIM.qkmc == journal))).first()
    return cnki


async def get_abbreviation_by_name(journal: str, db_session: AsyncSession):
    abbr = (await db_session.scalars(select(AbbreviationM).where(AbbreviationM.fullname == journal))).first()
    return abbr