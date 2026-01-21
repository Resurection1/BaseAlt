from dataclasses import dataclass


@dataclass(frozen=True)
class Package:
    name: str
    version: str
    release: str
    arch: str

    @property
    def version_release(self) -> str:
        return f"{self.version}-{self.release}"
