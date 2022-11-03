class Field(object):
    value = ''
    checked = False

    def __init__(self, passedId):
        self.value = str(passedId)
