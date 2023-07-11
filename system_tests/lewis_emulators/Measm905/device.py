from collections import OrderedDict
from .states import DefaultState
from lewis.devices import StateMachineDevice
import random



class SimulatedMeasm905(StateMachineDevice):
    

    def _initialize_data(self):
        """
        Initialize all of the device's attributes.
        """
        self._pressure = 1

    def _get_state_handlers(self):
        return {
            'default': DefaultState(),
        }

    def _get_initial_state(self):
        return 'default'

    def _get_transition_handlers(self):
        return OrderedDict([
        ])
    
    @property
    def pressure(self):
        return self._pressure
    