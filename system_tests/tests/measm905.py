import unittest

from utils.channel_access import ChannelAccess
from utils.ioc_launcher import get_default_ioc_dir
from utils.test_modes import TestModes
from utils.testing import get_running_lewis_and_ioc, skip_if_recsim

DEVICE_PREFIX = "MEASM905_01"


IOCS = [
    {
        "name": DEVICE_PREFIX,
        "directory": get_default_ioc_dir("MEASM905"),
        "macros": {},
        "emulator": "Measm905",
    },
]


TEST_MODES = [TestModes.DEVSIM]


class Measm905Tests(unittest.TestCase):
    """
    Tests for the Measm905 IOC.
    """

    def setUp(self):
        self._lewis, self._ioc = get_running_lewis_and_ioc("Measm905", DEVICE_PREFIX)
        self.ca = ChannelAccess(device_prefix=DEVICE_PREFIX)

    @skip_if_recsim("In rec sim this test fails")
    def test_WHEN_pressure_changes_THEN_pv_also_changes(self):
        self._lewis.backdoor_set_on_device("pressure", 42)
        self.ca.assert_that_pv_is("PRESSURE", 42)
