
class BaseModel(object):
    
    @staticmethod
    def not_empty(v):
        pass
        
    @property
    def parameters(self):
        raise NotImplementedError