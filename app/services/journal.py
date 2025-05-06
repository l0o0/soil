from app.models.journal import CNKI as CNKIModel
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


async def get_journal_meta_by_name(journal: str, db_session: AsyncSession):
    cnki = (await db_session.scalars(select(CNKIModel).where(CNKIModel.qkmc == journal))).first()
    return cnki