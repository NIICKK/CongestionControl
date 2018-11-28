from PyQt4 import QtCore, QtGui
import yaml
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # Set Window
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setFixedSize(MainWindow.size())
        MainWindow.setWindowTitle("Status")

        # Set Icon
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)

        # Set container
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Set font for head labels
        headLabelFont = QtGui.QFont()
        headLabelFont.setPointSize(12)
        headLabelFont.setBold(True)
        headLabelFont.setItalic(False)
        headLabelFont.setWeight(75)

        # Set font for sub-labels
        subLabelFont = QtGui.QFont()
        subLabelFont.setPointSize(11)
        subLabelFont.setBold(True)
        subLabelFont.setWeight(75)

        # Set currentFiles label
        self.currentFiles = QtGui.QLabel(self.centralwidget)
        self.currentFiles.setGeometry(QtCore.QRect(9, 9, 103, 18))
        self.currentFiles.setFont(headLabelFont)
        self.currentFiles.setObjectName("currentFiles")
        self.currentFiles.setText("Current Files:")

        # Set Files table
        self.filesTable = QtGui.QTableWidget(0, 3,parent=self.centralwidget)
        self.filesTable.setGeometry(QtCore.QRect(9, 30, 781, 192))
        self.filesTable.setProperty("showDropIndicator", False)
        self.filesTable.setDragDropOverwriteMode(False)
        self.filesTable.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.filesTable.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.filesTable.setCornerButtonEnabled(False)
        self.filesTable.setObjectName("filesTable")
        self.filesTable.verticalHeader().setVisible(False)
        self.filesTable.verticalHeader().setHighlightSections(False)
        self.filesTable.setHorizontalHeaderLabels(["File Name", "Size", "Hosts"])
        self.filesTable.setColumnWidth(0, 260)
        self.filesTable.setColumnWidth(1, 120)
        self.filesTable.setColumnWidth(2, 399)

        # Set networkStatus label
        self.networkStatus = QtGui.QLabel(self.centralwidget)
        self.networkStatus.setGeometry(QtCore.QRect(9, 260, 124, 18))
        self.networkStatus.setFont(headLabelFont)
        self.networkStatus.setObjectName("networkStatus")
        self.networkStatus.setText("Network Status:")

        # Set network status labels
        self.band_label = QtGui.QLabel(self.centralwidget)
        self.band_label.setGeometry(QtCore.QRect(9, 290, 85, 17))
        self.band_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.band_label.setObjectName("band_label")
        self.band_label.setFont(subLabelFont)
        self.band_label.setText("Bandwidth:")

        self.band = QtGui.QLabel(self.centralwidget)
        self.band.setGeometry(QtCore.QRect(100, 290, 100, 17))
        self.band.setObjectName("band")
        self.band.setText("0 Mbps")


        self.avail_label = QtGui.QLabel(self.centralwidget)
        self.avail_label.setGeometry(QtCore.QRect(310, 290, 75, 17))
        self.avail_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.avail_label.setObjectName("avail_label")
        self.avail_label.setFont(subLabelFont)
        self.avail_label.setText("Available:")

        self.avail = QtGui.QLabel(self.centralwidget)
        self.avail.setGeometry(QtCore.QRect(390, 290, 100, 17))
        self.avail.setObjectName("avail")
        self.avail.setText("0 Mbps")


        self.thresh_label = QtGui.QLabel(self.centralwidget)
        self.thresh_label.setGeometry(QtCore.QRect(600, 290, 76, 17))
        self.thresh_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.thresh_label.setObjectName("thresh_label")
        self.thresh_label.setFont(subLabelFont)
        self.thresh_label.setText("Threshold:")

        self.thresh = QtGui.QLabel(self.centralwidget)
        self.thresh.setGeometry(QtCore.QRect(683, 290, 100, 17))
        self.thresh.setObjectName("thresh")
        self.thresh.setText("0 Mbps")

        # Set the active users label and table
        self.users_label = QtGui.QLabel(self.centralwidget)
        self.users_label.setGeometry(QtCore.QRect(9, 360, 100, 18))
        self.users_label.setText("Active Users:")
        self.users_label.setFont(headLabelFont)
        self.users_label.setObjectName("users_label")

        self.usersTable = QtGui.QTableWidget(0, 2,parent=self.centralwidget)
        self.usersTable.setGeometry(QtCore.QRect(9, 380, 781, 192))
        self.usersTable.setProperty("showDropIndicator", False)
        self.usersTable.setDragDropOverwriteMode(False)
        self.usersTable.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.usersTable.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.usersTable.setCornerButtonEnabled(False)
        self.usersTable.setObjectName("usersTable")
        self.usersTable.verticalHeader().setVisible(False)
        self.usersTable.verticalHeader().setHighlightSections(False)
        self.usersTable.setHorizontalHeaderLabels(["IP", "Port"])
        self.usersTable.setColumnWidth(0, 390)
        self.usersTable.setColumnWidth(1, 389)


        MainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Now lets fill up the data, and timeout every 10 seconds to update
        self.setData()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.setData)
        self.timer.start(1000)


    def setData(self):
        with open('config.yaml', 'r') as yamlFile:
            print("Log: Updating data..")
            cfg = yaml.load(yamlFile)

            # Set the files table:
            filesNum = len(cfg['file_info'])
            self.filesTable.setRowCount(filesNum)
            r = 0
            for fname in cfg['file_info']:
                self.filesTable.setItem(r, 0, QtGui.QTableWidgetItem(fname))
                self.filesTable.setItem(r, 1, QtGui.QTableWidgetItem(str(cfg['file_info'][fname]['file_size'])))
                hosts = ''
                for h in cfg['file_info'][fname]['hostsWithFile']:
                    hosts += '{}:{}; '.format(h['ip'], h['port'])
                self.filesTable.setItem(r, 2, QtGui.QTableWidgetItem(hosts))
                r +=1

            # Now set the network status labels
            self.band.setText("{} Mbps".format(cfg["network_info"]["bandwidth"]))
            self.avail.setText("{} Mbps".format(cfg["network_info"]["available"]))
            self.thresh.setText("{} Mbps".format(cfg["network_info"]["threshold"]))

            # Set the users table:
            usersNum = len(cfg['network_info']['activeUsers'])
            self.usersTable.setRowCount(usersNum)
            r = 0
            for user in cfg['network_info']['activeUsers']:
                self.usersTable.setItem(r, 0, QtGui.QTableWidgetItem(user['ip']))
                self.usersTable.setItem(r, 1, QtGui.QTableWidgetItem(str(user['port'])))
                r +=1

            print("Log: Data updated.")




if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

