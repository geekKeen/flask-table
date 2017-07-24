# -*- coding: utf8 -*-
class Column(object):
    def __init__(self, default=None, makeup=None):
        self.value = default
        self.makeup = makeup

    def __get__(self, instance, owner):
        if self.makeup is not None:
            return self.makeup(self.value)
        return self.value

    def __set__(self, instance, value):
        if self.makeup is not None:
            self.value = self.makeup(value)
        self.value = value


class ModelMeta(type):
    def __new__(cls, classname, base, fields):
        columns = {column: fields[column].value for column in fields if isinstance(fields[column], Column)}
        fields['columns'] = columns

        return super(ModelMeta, cls).__new__(cls, classname, base, fields)


class Model(object):
    """
    Table 数据源的基类
    通过继承Model,实现 Table的可扩展性
    此类包含了针对数据的操作
    class User(Model):
        name = Column()
        email = Column()
    """
    __metaclass__ = ModelMeta

    @classmethod
    def get_result_set(cls):
        raise NotImplementedError()

    def __getitem__(self, item):
        if item not in self.__dict__:
            raise "<Model %s> don't have `%s` column" % (self.__class__.__name__, item)
        return self.__dict__[item]

    def __setattr__(self, key, value):
        if key in self.columns:
            self.__dict__[key] = value
        else:
            super(Model, self).__setattr__(key, value)
