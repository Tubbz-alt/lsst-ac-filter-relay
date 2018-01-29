import lsst_ion_pump_ps_controller as lippc

import rogue
import pyrogue
import pyrogue.gui
import PyQt4.QtGui
import PyQt4.QtCore
import sys

if __name__ == "__main__":

    rogue.Logging.setFilter('pyrogue.SrpV3', rogue.Logging.Debug)
    
    with lippc.LsstIonPumpCtrlRoot() as root:
        appTop = PyQt4.QtGui.QApplication(sys.argv)
        guiTop = pyrogue.gui.GuiTop(group='Main')
        print('guiTop.addTree')
        guiTop.addTree(root)
        guiTop.resize(1000,1000)
        # Run gui
        print('appTop.exec_()')
        appTop.exec_()
