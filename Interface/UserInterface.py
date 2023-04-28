from typing import Any


class PersonMeta(type):
    def __instancecheck__(self, __instance: Any) -> bool:
        return super().__instancecheck__(type(__instance))
    
    def __subclasscheck__(self, __subclass: type) -> bool:
        return (hasattr(__subclass, "displayUserInformation") and callable(__subclass.displayUserInformation))
    

class PersonInterface(metaclass=PersonMeta):
    pass 

__all__ = ['PersonInterface']