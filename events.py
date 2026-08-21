class EventBus:
    """
    Internal messaging system for Trios
    """

    def __init__(self):
        self.listeners = {}


    def subscribe(self, event_name, callback):

        if event_name not in self.listeners:
            self.listeners[event_name] = []

        if callback not in self.listeners[event_name]:
            self.listeners[event_name].append(callback)



    def unsubscribe(self, event_name, callback):

        if event_name in self.listeners:
            if callback in self.listeners[event_name]:
                self.listeners[event_name].remove(callback)



    def emit(self, event_name, data=None):

        if event_name not in self.listeners:
            return

        for callback in self.listeners[event_name]:
            callback(data)



    def has_event(self, event_name):

        return event_name in self.listeners



    def listener_count(self, event_name):

        if event_name not in self.listeners:
            return 0

        return len(self.listeners[event_name])



events = EventBus()