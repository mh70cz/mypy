"""
Bite 196. Create a JS-like dict object
"""

class JsObject(dict):
    """A Python dictionary that provides attribute-style access
       just like a JS object:

       obj = JsObject()
       obj.cool = True
       obj.foo = 'bar'

       Try this on a regular dict and you get
       AttributeError: 'dict' object has no attribute 'foo'
    """
    
    def __setattr__(self, att, val):
        self.__setitem__(att, val)
        
    def __getattr__(self, att):
        return self.__getitem__(att)
    
    def __delattr__(self, att):
        self.__delitem__(att)
        
    
    
    
    
"""
__getattr__ = dict.get
__setattr__ = dict.__setitem__
__delattr__ = dict.__delitem__
    
    
    
def __init__(self, *args, **kwargs):
    super().__init__(self, *args, **kwargs)
    self.__dict__ = self    
"""    