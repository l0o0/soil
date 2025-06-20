from typing import Dict, Union
from fastapi import APIRouter
from app.core.deps import DBSessionDep, PluginIDDep
from app.services.journal import get_journal_meta_by_name, get_abbreviation_by_name
from app.schemas.journal import JournalResponse

router = APIRouter(prefix="/journals", tags=["journals"])

@router.get("/cnki/{name}", response_model=JournalResponse, dependencies=[PluginIDDep])
async def read_journal(
    name: str,
    db: DBSessionDep,
):
    print(f"Fetching journal metadata for: {name}")
    cnki = await get_journal_meta_by_name(name, db)
    
    data: Dict[str, Union[str, float]] = {}
    if cnki:
        data["fhyz"] = str(cnki.fhyz)
        data["zhyz"] = str(cnki.zhyz)
    
    return JournalResponse(
        name=name,
        data=data if data else None  # 空字典转为None以符合Optional
    )

@router.get("/abbreviation/{name}", response_model=JournalResponse, dependencies=[PluginIDDep])
async def read_abbreviation(
    name: str,
    db: DBSessionDep,
):
    print(f"Fetching journal abbreviation for: {name}")
    abbr = await get_abbreviation_by_name(name, db)
    
    data: Dict[str, Union[str, float]] = {}
    if abbr:
        data["abb_with_dot"] = str(abbr.abb_with_dot)
        data["abb_no_dot"] = str(abbr.abb_no_dot)
    
    return JournalResponse(
        name=name,
        data=data if data else None  # 空字典转为None以符合Optional
    )

@router.get("/meta/info")
async def get_journal_info():
    print(f"Fetching journal metadata for: info")
    return {"message": "This is a test message"}