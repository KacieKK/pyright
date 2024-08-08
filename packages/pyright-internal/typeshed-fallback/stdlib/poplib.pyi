import socket
import ssl
import sys
from builtins import list as _list  # conflicts with a method named "list"
from re import Pattern
from typing import Any, BinaryIO, Final, NoReturn, overload
from typing_extensions import TypeAlias

__all__ = ["POP3", "error_proto", "POP3_SSL"]

_LongResp: TypeAlias = tuple[bytes, list[bytes], int]

class error_proto(Exception): ...

POP3_PORT: Final = 110
POP3_SSL_PORT: Final = 995
CR: Final = b"\r"
LF: Final = b"\n"
CRLF: Final = b"\r\n"
HAVE_SSL: bool

class POP3:
    encoding: str
    host: str
    port: int
    sock: socket.socket
    file: BinaryIO
    welcome: bytes
    def __init__(self, host: str, port: int = 110, timeout: float = ...) -> None: ...
    def getwelcome(self) -> bytes: ...
    def set_debuglevel(self, level: int) -> None: ...
    def user(self, user: str) -> bytes: ...
    def pass_(self, pswd: str) -> bytes: ...
    def stat(self) -> tuple[int, int]: ...
    def list(self, which: Any | None = None) -> _LongResp: ...
    def retr(self, which: Any) -> _LongResp: ...
    def dele(self, which: Any) -> bytes: ...
    def noop(self) -> bytes: ...
    def rset(self) -> bytes: ...
    def quit(self) -> bytes: ...
    def close(self) -> None: ...
    def rpop(self, user: str) -> bytes: ...
    timestamp: Pattern[str]
    def apop(self, user: str, password: str) -> bytes: ...
    def top(self, which: Any, howmuch: int) -> _LongResp: ...
    @overload
    def uidl(self) -> _LongResp: ...
    @overload
    def uidl(self, which: Any) -> bytes: ...
    def utf8(self) -> bytes: ...
    def capa(self) -> dict[str, _list[str]]: ...
    def stls(self, context: ssl.SSLContext | None = None) -> bytes: ...

class POP3_SSL(POP3):
    if sys.version_info >= (3, 12):
        def __init__(
            self, host: str, port: int = 995, *, timeout: float = ..., context: ssl.SSLContext | None = None
        ) -> None: ...
        def stls(self, context: Any = None) -> NoReturn: ...
    else:
        def __init__(
            self,
            host: str,
            port: int = 995,
            keyfile: str | None = None,
            certfile: str | None = None,
            timeout: float = ...,
            context: ssl.SSLContext | None = None,
        ) -> None: ...
        # "context" is actually the last argument, but that breaks LSP and it doesn't really matter because all the arguments are ignored
        def stls(self, context: Any = None, keyfile: Any = None, certfile: Any = None) -> NoReturn: ...
