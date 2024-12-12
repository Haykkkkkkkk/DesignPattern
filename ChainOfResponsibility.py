# Abstract handler
class Handler:
    def __init__(self, successor=None):
        self._successor = successor

    def handle(self, request):
        if self._successor:
            return self._successor.handle(request)
        return "Request cannot be handled"

# Concrete handlers
class HandlerA(Handler):
    def handle(self, request):
        if request == "A":
            return "HandlerA processed the request"
        else:
            return super().handle(request)

class HandlerB(Handler):
    def handle(self, request):
        if request == "B":
            return "HandlerB processed the request"
        else:
            return super().handle(request)

# Client code
handler_chain = HandlerA(HandlerB())

requests = ["A", "B", "C"]
for request in requests:
    result = handler_chain.handle(request)
    print(f"Request: {request} -> {result}")
