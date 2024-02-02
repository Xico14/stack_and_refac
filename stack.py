# Описание класса Stack
class Stack:
    """
        Класс представляет собой структуру данных стек.
    """
    def __init__(self):
        """
            Инициализация пустого стека.
        """
        self.items = []

    def is_empty(self):
        """
            Проверяет, пуст ли стек.
        """
        return self.items == []

    def push(self, item):
        """
            Добавляет элемент в стек.
        """
        self.items.append(item)

    def pop(self):
        """
            Удаляет и возвращает верхний элемент стека.
        """
        return self.items.pop()

    def peek(self):
        """
            Возвращает верхний элемент стека, не удаляя его.
        """
        return self.items[len(self.items)-1]

    def size(self):
        """
            Возвращает количество элементов в стеке.
        """
        return len(self.items)

def is_balanced(symbols):
    """
        Проверяет, сбалансированы ли скобки в строке symbols.
    """
    stack = Stack()
    for symbol in symbols:
        if symbol in "([{":
            stack.push(symbol)
        elif symbol in ")]}":
            if stack.is_empty():
                return False
            else:
                top = stack.pop()
                if (symbol == ")" and top != "(") or \
                    (symbol == "]" and top != "[") or \
                    (symbol == "}" and top != "{"):
                        return False
    return stack.is_empty()

# Примеры использования
print(is_balanced("((([{}]))))"))  
print(is_balanced("[([])((([[[]]])))]{()}"))
print(is_balanced("{{[()]}}"))
print(is_balanced("}{"))
print(is_balanced("{{[(])]}}"))