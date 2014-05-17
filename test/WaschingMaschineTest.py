import time
import unittest
import WashingMachine
from WashingMachineStates import WashingMachineState
from mock import MagicMock
from SwitchState import SwitchState

class WaschingMaschineTest(unittest.TestCase):

    def test_checkInitState(self):
        wasch = WashingMachine
        wasch.getSwitchState = MagicMock(return_value=SwitchState.ON)
        self.initAndVerifyState(wasch, WashingMachineState.START, WashingMachineState.START)
        wasch.getSwitchState = MagicMock(return_value=SwitchState.OFF)
        time.sleep(6)
        self.verifyState(wasch, WashingMachineState.IN_PROGRESS)

    def test_checkForInProgress(self):
        wasch = WashingMachine
        wasch.getSwitchState = MagicMock(return_value=SwitchState.OFF)
        self.initAndVerifyState(wasch, WashingMachineState.IN_PROGRESS, WashingMachineState.IN_PROGRESS)

    def test_checkForAfterInProgress(self):
        wasch = WashingMachine
        wasch.getSwitchState = MagicMock(return_value=SwitchState.OFF)
        self.initAndVerifyState(wasch, WashingMachineState.IN_PROGRESS, WashingMachineState.IN_PROGRESS)
        wasch.getSwitchState = MagicMock(return_value=SwitchState.ON)
        self.verifyState(wasch, WashingMachineState.FINISHING)

    def test_checkForFinishing(self):
        wasch = WashingMachine
        wasch.getSwitchState = MagicMock(return_value=SwitchState.ON)
        self.initAndVerifyState(wasch, WashingMachineState.FINISHING, WashingMachineState.FINISHING)

    def test_checkForEnd(self):
        wasch = WashingMachine
        wasch.getSwitchState = MagicMock(return_value=SwitchState.ON)
        self.initAndVerifyState(wasch, WashingMachineState.END, WashingMachineState.END)

    def test_checkFromStartToEnd(self):
        wasch = WashingMachine
        wasch.getSwitchState = MagicMock(return_value=SwitchState.ON)
        self.initAndVerifyState(wasch, WashingMachineState.START, WashingMachineState.START)
        wasch.getSwitchState = MagicMock(return_value=SwitchState.OFF)
        time.sleep(6)
        self.verifyState(wasch, WashingMachineState.IN_PROGRESS)
        wasch.getSwitchState = MagicMock(return_value=SwitchState.ON)
        self.verifyState(wasch, WashingMachineState.FINISHING)
        time.sleep(6)
        self.verifyState(wasch, WashingMachineState.END)

    def initAndVerifyState(self, wasch, initState, expectedState):
        wasch.setState(initState)
        self.verifyState(wasch, expectedState)

    def verifyState(self, wasch, expectedState):
        currentState = wasch.getState()
        self.assertEquals(currentState, expectedState, "wrong state value " + str(currentState));
