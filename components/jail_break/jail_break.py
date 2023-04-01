
import typing
from typing import List, Dict
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

from core.workflows.abstract_workflow import AbstractWorkflow


class JailBreakIn(BaseModel):
    search_query: str


class JailBreakOut(BaseModel):
    final_result: List[Dict]


class JailBreak(AbstractWorkflow):
    def __init__(self) -> None:
        super().__init__()

    async def transform(
        self, args: JailBreakIn, callbacks: typing.Any
    ) -> JailBreakOut:
        results_dict = await super().transform(args=args, callbacks=callbacks)
        
        # Process results_dict to create final_result
        final_result = results_dict  # Modify this line as needed

        out = JailBreakOut(final_result=final_result)
        return out

load_dotenv()
jail_break_app = FastAPI()


@jail_break_app.post("/transform/")
async def transform(args: JailBreakIn) -> JailBreakOut:
    jail_break = JailBreak()
    return await jail_break.transform(args, callbacks=None)
