class Diary:
    def __init__(self, __entries=[], __isLocked=True):
        self.__entries = __entries
        self.__isLocked = __isLocked
    def lock(self):
        self.__isLocked = True
    def unlock(self):
        self.__isLocked = False
    def add_entry(self, entry):
        if self.__isLocked == False:
            self.__entries.append(entry)
            print("entry added!")
        else:
            print("diary is locked and the entry cannot be added!")
    def get_entries(self):
        if self.__isLocked == False:
            print("diary entries:")
            for i, entry in enumerate(self.__entries,start=1):
                print(f"{i}. {entry}")
        else:
            print("diary is locked!")
