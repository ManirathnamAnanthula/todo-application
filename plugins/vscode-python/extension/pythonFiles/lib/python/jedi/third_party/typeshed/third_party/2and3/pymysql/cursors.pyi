from typing import Union, Tuple, Any, Dict, Optional, Text, Iterator, List
from .connections import Connection

Gen = Union[Tuple[Any, ...], Dict[str, Any]]

class Cursor:
    connection: Connection
    description: Tuple[Text, ...]
    rownumber: int
    rowcount: int
    arraysize: int
    messages: Any
    errorhandler: Any
    lastrowid: int
    def __init__(self, connection: Connection) -> None: ...
    def __del__(self) -> None: ...
    def close(self) -> None: ...
    def setinputsizes(self, *args): ...
    def setoutputsizes(self, *args): ...
    def nextset(self): ...
    def execute(self, query: str, args: Optional[Any] = ...) -> int: ...
    def executemany(self, query: str, args) -> int: ...
    def callproc(self, procname, args=...): ...
    def fetchone(self) -> Optional[Gen]: ...
    def fetchmany(self, size: Optional[int] = ...) -> Union[Optional[Gen], List[Gen]]: ...
    def fetchall(self) -> Optional[Tuple[Gen, ...]]: ...
    def scroll(self, value: int, mode: str = ...): ...
    def __iter__(self): ...

class DictCursor(Cursor):
    def fetchone(self) -> Optional[Dict[str, Any]]: ...
    def fetchmany(self, size: Optional[int] = ...) -> Optional[Tuple[Dict[str, Any], ...]]: ...
    def fetchall(self) -> Optional[Tuple[Dict[str, Any], ...]]: ...

class DictCursorMixin:
    dict_type: Any

class SSCursor(Cursor):
    # fetchall return type is incompatible with the supertype.
    def fetchall(self) -> List[Gen]: ...  # type: ignore
    def fetchall_unbuffered(self) -> Iterator[Tuple[Gen, ...]]: ...
    def __iter__(self) -> Iterator[Tuple[Gen, ...]]: ...
    def fetchmany(self, size: Optional[int] = ...) -> List[Gen]: ...
    def scroll(self, value: int, mode: str = ...) -> None: ...

class SSDictCursor(DictCursorMixin, SSCursor): ...
