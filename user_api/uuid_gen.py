from typing import Optional, Union
import uuid

# /c:/Coding/android/server stuff/user_api/uuid_gen.py


class UUIDGenerator:
    """
    Simple UUID generator.

    Methods:
        gen_uuid(version=4, namespace=None, name=None) -> str
            Generate a UUID string.
            - version 1: uuid1()
            - version 3: uuid3(namespace, name)  (requires namespace and name)
            - version 4: uuid4()
            - version 5: uuid5(namespace, name)  (requires namespace and name)
    """

    def __init__(self, default_version: int = 4) -> None:
        self.default_version = default_version

    def gen_uuid(
        self,
        version: Optional[int] = None,
        namespace: Optional[Union[uuid.UUID, str]] = None,
        name: Optional[str] = None,
    ) -> str:
        """
        Generate a UUID and return it as a string.

        Args:
            version: UUID version to generate (1, 3, 4, or 5). If None, uses default_version.
            namespace: Namespace UUID (uuid.UUID or string) required for v3 and v5.
            name: Name string required for v3 and v5.

        Returns:
            UUID string.

        Raises:
            ValueError: on invalid version or missing namespace/name for v3/v5.
        """
        ver = version if version is not None else self.default_version

        if ver == 1:
            u = uuid.uuid1()
        elif ver == 3:
            if namespace is None or name is None:
                raise ValueError("version 3 requires namespace and name")
            ns = uuid.UUID(namespace) if isinstance(namespace, str) else namespace
            u = uuid.uuid3(ns, name)
        elif ver == 4:
            u = uuid.uuid4()
        elif ver == 5:
            if namespace is None or name is None:
                raise ValueError("version 5 requires namespace and name")
            ns = uuid.UUID(namespace) if isinstance(namespace, str) else namespace
            u = uuid.uuid5(ns, name)
        else:
            raise ValueError("unsupported UUID version: must be 1, 3, 4, or 5")

        return str(u)
    
gen = UUIDGenerator()
print(gen.gen_uuid())  # Example usage