from typing import Any

from bson.objectid import ObjectId
from pymongo.database import Database
from pymongo.results import DeleteResult, UpdateResult


class ShanyrakRepository:
    def __init__(self, database: Database):
        self.database = database

    def create_shanyrak(self, shanyrak_id: str, data: dict[str, Any]):
        data["shanyrak_id"] = ObjectId(shanyrak_id)
        insert_result = self.database["shanyraks"].insert_one(data)
        return insert_result.inserted_id

    def get_shanyrak(self, shanyrak_id: str,) -> dict:
        shanyrak = self.database["shanyraks"].find_one(
            {"_id": ObjectId(shanyrak_id)},
        )
        return shanyrak
           
    def update_shanyrak(self, shanyrak_id: str, data: dict):
        self.database["shanyraks"].update_one(
            filter={"_id": ObjectId(shanyrak_id)},
            update={
                "$set": {
                    "type": data["type"],
                    "price": data["price"],
                    "address": data["address"],
                    "area": data["area"],
                    "rooms_counr": data["rooms_count"],
                    "description": data["description"]
                }
            },
        )

    def delete_shanyrak(self, shanyrak_id: str):
        self.database["shanyraks"].delete_one(
            {"_id": shanyrak_id}
        )



