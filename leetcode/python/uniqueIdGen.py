'''
Filename: /home/gbrl18/leetcode/python/uniqueIdGen.py
Path: /home/gbrl18/leetcode/python
Created Date: Sunday, January 9th 2022, 12:22:38 pm
Author: Gabriel S Santiago
'''
'''
Unique ID Generator

We need a unique ID identifier for each service.j
    - Service ID Generator. 
        - Service needs an unique ID that no other service 
            that is currently running is using.
        - No two currently running services are running with the same ID
'''




import time
class UidGenerator:
    def __init__(self) -> None:
        self.UID_STORE = set()

    @staticmethod
    def __next_id__() -> int:
        return int(time.time())

    def get_id(self) -> int:
        unique_id = UidGenerator.__next_id__()

        while unique_id in self.UID_STORE:
            unique_id = UidGenerator.__next_id__()

        self.UID_STORE.add(unique_id)

        return unique_id

    def drop_id(self, uid: int) -> bool:
        """Remove UID from uid store

        Args:
            uid (int)

        Returns:
            bool: returns `True` if UID existed, `False` otherwise.  
        """
        try:
            self.UID_STORE.remove(uid)
            return True
        except KeyError:
            return False
