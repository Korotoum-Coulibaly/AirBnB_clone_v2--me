#!/usr/bin/python3

class BaseModel():
    '''Contain all methods basics'''
    '''variable self is call to save information in FileStorage'''
    
    def save(self):
       self.updated_at = datetime.now()
        '''FileStorage instanciation'''
        storage = FileStorage()
        '''save data to filestorage'''
        storage.save()


    def __str__(self):
        """Returns a human-readable string representation
        of an instance."""

        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)


    def to_dict(self):
        """Returns a dictionary representation of an instance."""

        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict

