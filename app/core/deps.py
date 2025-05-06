from typing import Annotated

from app.db.session import get_db_session
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from .security import verify_pluginID

DBSessionDep = Annotated[AsyncSession, Depends(get_db_session)]
PluginIDDep = Depends(verify_pluginID)

