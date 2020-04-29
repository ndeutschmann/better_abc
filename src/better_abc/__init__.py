"""Slight extension of the native python ABC
Provides its own ABC and ABCMeta that allow the use of the abstract_attribute function/decorator

Usage:
Define an abstract class inheriting from `better_abc.ABC` or that has `better_abc.ABCMeta` as its metaclass
Define a class attribute as attr = better_abc.abstract_attribute()` or decorate a method with `@abstract_attribute`
to register it as a special abstract property that is checked after `__init__` is called,
i.e. child classes can define `attr = <value>` *in the __init__* function as a natural attribute.
"""
from abc import abstractmethod,abstractclassmethod,abstractstaticmethod,abstractproperty
from .abc_meta import ABCMeta,abstract_attribute


class ABC(metaclass=ABCMeta):
    """Helper class that provides a standard way to create an ABC using
    inheritance.
    """
    pass
