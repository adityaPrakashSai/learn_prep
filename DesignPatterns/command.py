# Behavioral design pattern

# Writing underlying software for performing key board and mouse
# Ctr-C => copy --- directly copy selected
# But user can drag and select using mouse ---> copy
# your business logic should not execute any request directly
# first convert your request to command and then execute that command
# Command pattern lets you also queue your request
# Command allows us to undo and redo


# Elements in command pattern
# Command, Concrete Command, Receiver (against which command is executed)
# command invoker
# client code


from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


# concrete commands


class CutCommand(Command):
    def __init__(self, textEditor) -> None:
        self._textEditor = textEditor
        self.backup = ""

    def execute(self):
        self.backup = self._textEditor.getSelectedText()
        self._textEditor.cut()

    def undo(self):
        self._textEditor.setText(self.backup)


class CopyCommand(Command):
    def __init__(self, textEditor) -> None:
        self._textEditor = textEditor

    def execute(self):
        self._textEditor.copy()

    def undo(self):
        pass


class PasteCommand(Command):
    def __init__(self, textEditor) -> None:
        self._textEditor = textEditor
        self.backup = ""

    def execute(self):
        self.backup = self._textEditor.getSelectedText()
        self._textEditor.paste()

    def undo(self):
        self._textEditor.setText(self.backup)


# receiver


class TextEditor:
    def __init__(self) -> None:
        self._content = ""

    def getSelectedText(self):
        return self._content

    def cut(self):
        self._content = ""

    def copy(self):
        pass

    def paste(self):
        self._content = "PastedContent"

    def setText(self, text):
        self._content = text

    def display(self):
        print("Content: ", self._content)


class CommandInvoker:
    def __init__(self) -> None:
        self.undoStack = []
        self.redoStack = []

    def execute(self, command):
        command.execute()
        self.undoStack.append(command)
        self.redoStack = []

    def undo(self):
        if not self.undoStack:
            print("Nothing to undo ...")
            return

        command = self.undoStack.pop()
        command.undo()
        self.redoStack.append(command)

    def redo(self):
        if not self.redoStack:
            print("Nothing to redo ...")
            return

        command = self.redoStack.pop()
        command.execute()
        self.undoStack.append(command)


if __name__ == "__main__":
    textEditor = TextEditor()
    cutCommand = CutCommand(textEditor)
    copyCommand = CopyCommand(textEditor)
    pasteCommand = PasteCommand(textEditor)

    invoker = CommandInvoker()
    invoker.execute(cutCommand)
    textEditor.display()

    invoker.execute(pasteCommand)
    textEditor.display()

    invoker.undo()
    textEditor.display()

    invoker.redo()
    textEditor.display()
