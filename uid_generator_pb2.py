"""Minimal protobuf-compatible UID payload used by app.py.

The original repository imports this generated module but does not include it.
The application only relies on the ``id`` and ``teamXdarks`` fields when
building the profile-check request, so this module provides those fields and
serializes them using protobuf varints.
"""


def _encode_varint(value: int) -> bytes:
    encoded = bytearray()
    value = int(value)
    while value > 0x7F:
        encoded.append((value & 0x7F) | 0x80)
        value >>= 7
    encoded.append(value & 0x7F)
    return bytes(encoded)


class uid_generator:
    """UID profile-check payload expected by the existing application."""

    def __init__(self) -> None:
        self.id = 0
        self.teamXdarks = 0

    def SerializeToString(self) -> bytes:
        payload = bytearray()
        if self.id:
            payload.extend(b"\x08")
            payload.extend(_encode_varint(self.id))
        if self.teamXdarks:
            payload.extend(b"\x10")
            payload.extend(_encode_varint(self.teamXdarks))
        return bytes(payload)
