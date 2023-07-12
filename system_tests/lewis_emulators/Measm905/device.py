from collections import OrderedDict
from .states import DefaultState
from lewis.devices import StateMachineDevice



class SimulatedMeasm905(StateMachineDevice):
    

    def _initialize_data(self):
        """
        Initialize all of the device's attributes.
        """
        self.pressure = 1
        self.test_thing = 47

    def _get_state_handlers(self):
        return {
            'default': DefaultState(),
        }

    def _get_initial_state(self):
        return 'default'

    def _get_transition_handlers(self):
        return OrderedDict([
        ])
  