from typing import Optional
from pydantic import BaseModel


class Post(BaseModel):
    id: int
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


class CreatePost(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None
