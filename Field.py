class Field(object):
    ID = 0
    value = ''
    checked = False

    def __init__(self, passedId):
        self.id = passedId
        self.value = str(passedId)
