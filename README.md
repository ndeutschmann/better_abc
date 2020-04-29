# Better Abstract Basic Classes
Python ABC with a simple @abstract_property decorated checked after instantiation

Entirely based on [this StackOverflow answer](https://stackoverflow.com/questions/23831510/abstract-attribute-not-property/50381071#50381071) by [krassowski](https://stackoverflow.com/users/6646912/krassowski).

## Example:

```
from better_abc import BetterABC,abstract_property

class AbstractClassWithAbstractAttribute(BetterABC):
  @abstract_property
  def prop(self):
    pass
    
  otherprop = abstract_property()
    
class ClassWithProperty(AbstractClassWithAbstractAttribute)
  def __init__(self,propvalue=12):
    self.prop = 12
    self.otherprop = "a string"
```
