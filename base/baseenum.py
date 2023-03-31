from enum import Enum


class EnumBase(Enum):

    @property
    def code(self):
        return self.value

    @code.getter
    def code(self):
        return self.value[0]

    @property
    def desc(self):
        return self.value

    @desc.getter
    def desc(self):
        return self.value[1]
