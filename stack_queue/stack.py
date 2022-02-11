# Development of stack classes around lists and deque

class Stack():

    def __init__(self):

        self._items = list()    

    def push(self, item):

        self._items.append(item)

    def pop(self):

        return self._items.pop()


if __name__ == '__main__':

    stack = Stack()

    # Inclusão de elementos na pilha
    stack.push('primeiro')
    stack.push('segundo')
    stack.push('terceiro')

    # Remoção do último elemento adicionado

    removed_item = stack.pop()

    print(removed_item)
