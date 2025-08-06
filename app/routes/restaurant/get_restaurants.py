from fastapi import status, HTTPException, APIRouter,Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from ...database import get_db
from ... import oauth2,models
from . import schemas

router=APIRouter(prefix="/get_restaurants",tags=["Get Restaurants"])

@router.get("/all",response_model=list[schemas.RestaurantOut])
async def get_all_restaurants(user:models.Users=Depends(oauth2.get_current_user),db:AsyncSession=Depends(get_db)):
    res=await db.execute(select(models.Restaurants))
    res=res.scalars().all()
    if(not res):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No Restaurants Found!")
    
    return res
