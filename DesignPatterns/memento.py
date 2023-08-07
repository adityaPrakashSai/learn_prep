# memento is another behavioral design pattern
# it allows object state to be captured and restored
# without exposing its internal structure

# you are not storing the object:
# the object may provide some methods to alter the object
# Object A => state a
# Object A => state b

# Movie Ghazni: Short term memory loss
# Some items so that he can go back to his original state
# these items are memento -> Christopher Nolan (Oppenheimer)


# Memento class
class EditorMemento:
    def __init__(self, content) -> None:
        self.__content = content

    def getContent(self):
        return self.__content


# Originator class
class TextEditor:
    def __init__(self) -> None:
        self.__content = ""

    def write(self, text):
        self.__content = text

    def getContent(self):
        return self.__content

    def createMemento(self):
        return EditorMemento(self.__content)

    def restoreMemento(self, memento):
        self.__content = memento.getContent()


# care taker class
class History:
    def __init__(self) -> None:
        self.states = []

    def push(self, memento):
        self.states.append(memento)

    def pop(self):
        if self.states:
            return self.states.pop()
        return None


if __name__ == "__main__":
    editor = TextEditor()
    history = History()

    editor.write("Hello")
    print(editor.getContent())
    history.push(editor.createMemento())

    editor.write("Memento Pattern Example")
    print(editor.getContent())
    editor.restoreMemento(history.pop())
    print(editor.getContent())


"""
Message (Table): MessageId, Content, UserId, State..., CreatedOn

START TRANSACTION;

CREATE INDEX IndexName1 on tableName ("ColumnName1")
CREATE INDEX IndexName2 on tableName ("ColumnName1")

COMMIT;
"""
