from PyQt5 import QtWidgets, QtCore, QtGui
import pandas as pd
import numpy as np


class Ui_MainWindow(object):
    def setupUi(self, wizard):
        wizard.setObjectName("wizard")
        wizard.setWindowTitle("Grid World")

    def createIntroPage(self):
        self.page = QtWidgets.QWizardPage()
        self.page.setTitle("Introduction")

        self.label = QtWidgets.QLabel(self.page)
        self.label.setText("This wizard will help you watch how our robot find its way to the destination! ")
        self.label.setFont(QtGui.QFont('Arial', 11))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)

        self.label2 = QtWidgets.QLabel(self.page)
        self.label2.setText("Let's Go!")
        self.label2.setFont(QtGui.QFont('Arial', 11))
        self.label2.setWordWrap(True)
        self.label2.setAlignment(QtCore.Qt.AlignCenter)
        self.layout = QtWidgets.QVBoxLayout(self.page)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.label2)
        self.page.setLayout(self.layout)

        return self.page

    def createInputsPage(self):
        self.page2 = QtWidgets.QWizardPage()
        self.page2.setTitle("Getting Your Desired Inputs!")
        self.page2.setSubTitle("Please fill these fields.")

        self.vertical_Label = QtWidgets.QLabel(self.page2)
        self.vertical_Label.setText("Vertical Length:")

        self.verticalLineEdit = QtWidgets.QLineEdit(self.page2)

        self.horizLabel = QtWidgets.QLabel(self.page2)
        self.horizLabel.setText("Horizontal Length:")

        self.horizLineEdit = QtWidgets.QLineEdit(self.page2)

        self.NumIter = QtWidgets.QLabel(self.page2)
        self.NumIter.setText("Number Of Iterations:")

        self.iterLineEdit = QtWidgets.QLineEdit(self.page2)

        self.pybutton = QtWidgets.QPushButton(self.page2)
        self.pybutton.setText('Get')
        self.pybutton.clicked.connect(self.GetNumbers)

        self.pybutton1 = QtWidgets.QPushButton(self.page2)
        self.pybutton1.setText('Get')
        self.pybutton1.clicked.connect(self.Action)

        self.pybutton2 = QtWidgets.QPushButton(self.page2)
        self.pybutton2.setText('Find Best Path')

        self.start = QtWidgets.QLabel(self.page2)
        self.start.setText("Blocks:")

        self.state = QtWidgets.QLabel(self.page2)
        self.state.setText("Start State:")

        self.listWidget2 = QtWidgets.QListWidget(self.page2)
        # self.listWidget2.itemSelectionChanged.connect(self.on_change)

        # self.comboBox = QtWidgets.QComboBox(self.page2)
        # self.comboBox.setGeometry(QtCore.QRect(40, 40, 491, 31))
        # self.comboBox.setObjectName(("comboBox"))

        self.listWidget = QtWidgets.QListWidget(self.page2)
        self.listWidget.itemSelectionChanged.connect(self.on_change)

        self.layout2 = QtWidgets.QGridLayout(self.page2)
        self.layout2.setGeometry(QtCore.QRect(0, 0, 500, 300))
        self.layout2.addWidget(self.vertical_Label, 0, 0)
        self.layout2.addWidget(self.verticalLineEdit, 0, 1)
        self.layout2.addWidget(self.horizLabel, 1, 0)
        self.layout2.addWidget(self.horizLineEdit, 1, 1)
        self.layout2.addWidget(self.NumIter, 2, 0)
        self.layout2.addWidget(self.iterLineEdit, 2, 1)
        self.layout2.addWidget(self.pybutton, 3, 0)
        self.layout2.addWidget(self.start, 4, 0)
        self.layout2.addWidget(self.state, 5, 0)
        self.layout2.addWidget(self.listWidget, 4, 1)
        self.layout2.addWidget(self.pybutton1, 6, 0)
        self.layout2.addWidget(self.listWidget2, 5, 1)
        self.layout2.addWidget(self.pybutton2, 7, 0)
        self.page2.setLayout(self.layout2)
        self.layout2.setSpacing(30)

        return self.page2

    def LastPage(self):

        self.page3 = QtWidgets.QWizardPage()

        self.graphicsView = QtWidgets.QGraphicsView(self.page3)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 500, 400))
        self.pybutton2.clicked.connect(self.showpath)

        self.graphicsView2 = QtWidgets.QGraphicsView(self.page3)
        self.graphicsView2.setGeometry(QtCore.QRect(0, 450, 50, 50))
        self.graphicsView3 = QtWidgets.QGraphicsView(self.page3)
        self.graphicsView3.setGeometry(QtCore.QRect(0, 550, 50, 50))

        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.graphicsView3.setPalette(palette)

        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.graphicsView2.setPalette(palette)

        self.label_path = QtWidgets.QLabel(self.page3)
        self.label_path.setText("Most Efficient Path")
        self.label_path.setGeometry(
            QtCore.QRect(75, 450, 150, 50))

        self.label_block = QtWidgets.QLabel(self.page3)
        self.label_block.setText("Blocks")
        self.label_block.setGeometry(
            QtCore.QRect(75, 550, 50, 50))
        return self.page3

    def showpath(self):

        start = (int(self.CurrentState[0][1]), int(self.CurrentState[0][4]))
        for i in range(self.m):
            for j in range(self.n):
                self.graphicsView = QtWidgets.QGraphicsView(self.page3)
                self.graphicsView.setGeometry(
                    QtCore.QRect(j * (500 / self.n), i * (400 / self.m), 500 / self.n, 400 / self.m))
                if (i, j) in self.MEP:
                    palette = QtGui.QPalette()
                    brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                    brush.setStyle(QtCore.Qt.SolidPattern)
                    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
                    brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                    brush.setStyle(QtCore.Qt.SolidPattern)
                    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
                    brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
                    brush.setStyle(QtCore.Qt.SolidPattern)
                    palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
                    self.graphicsView.setPalette(palette)
                if (i, j) in self.B:
                    palette = QtGui.QPalette()
                    brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
                    brush.setStyle(QtCore.Qt.SolidPattern)
                    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
                    brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
                    brush.setStyle(QtCore.Qt.SolidPattern)
                    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
                    brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
                    brush.setStyle(QtCore.Qt.SolidPattern)
                    palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
                    self.graphicsView.setPalette(palette)

        self.label_start = QtWidgets.QLabel(self.page3)
        self.label_start.setText("Start")
        self.label_start.setGeometry(
            QtCore.QRect(start[1] * (500 / self.n), start[0] * (400 / self.m), 500 / self.n, 400 / self.m))
        self.label_start.setAlignment(QtCore.Qt.AlignCenter)

        self.label_reward = QtWidgets.QLabel(self.page3)
        self.label_reward.setText("Reward!")
        self.label_reward.setGeometry(
            QtCore.QRect((self.n - 1) * (500 / self.n), (self.m - 1) * (400 / self.m), 500 / self.n, 400 / self.m))
        self.label_reward.setAlignment(QtCore.Qt.AlignCenter)

    def GetNumbers(self):

        self.m = int(self.verticalLineEdit.text())

        self.n = int(self.horizLineEdit.text())

        All_States = []
        for i in range(self.m):
            for j in range(self.n):
                All_States.append((i, j))
        print(All_States)

        self.listWidget.addItems(["{}".format(All_States[i]) for i in range(len(All_States))])
        self.listWidget.setSelectionMode(QtWidgets.QListWidget.MultiSelection)

        self.listWidget2.addItems(["{}".format(All_States[i]) for i in range(len(All_States))])

    def on_change(self):

        self.Block = [item.text() for item in self.listWidget.selectedItems()]

    def Action(self):
        self.CurrentState = [item.text() for item in self.listWidget2.selectedItems()]

        print(self.Block)
        m = self.m
        n = self.n
        GW = np.array(np.zeros(shape=(m, n)))
        print(GW)
        blocks = self.Block
        for j in range(len(blocks)):
            blocks[j] = (int(blocks[j][1]), int(blocks[j][4]))

        for i in blocks:
            GW[i] = 1
        GW[m - 1, n - 1] = 2
        print(GW)
        # Reward Matrix
        R = np.array(np.ones(shape=(m, n)))
        R = (-1) * R
        R[m - 1, n - 1] = 500
        print(R)

        # Extract State Positions:
        state_idx = []
        for i in range(m):
            for j in range(n):
                if GW[i, j] == 0 or GW[i, j] == 2:
                    state_idx.append((i, j))

        print(state_idx)

        s = pd.Series(data=state_idx, index=range(len(state_idx)))

        t = pd.Series(data=range(len(state_idx)), index=state_idx)
        print(t)
        print(t[(1, 3)])
        q = t[(1, 3)] + 2
        print(q)
        # Q-Matrix
        actions_list = ['up', 'down', 'left', 'right']
        print(actions_list)
        Q = np.array(np.zeros(shape=(len(state_idx), 4)))
        print(Q)

        gamma = 0.9
        alpha = 0.5

        iterations = int(self.iterLineEdit.text())

        def Sample_Next_Action(state, p):
            q = np.random.rand(1, 1)

            max_index = np.where(np.max(Q[state_idx.index(state),]) == Q[state_idx.index(state),])[0]
            if max_index.shape[0] > 1:
                max_index = int(np.random.choice(max_index, size=1))
            else:
                max_index = int(max_index)
            if max_index == 0:
                if 0 < q < p:
                    next_action = 'up'
                else:
                    next_action = np.random.choice(['down', 'left', 'right'], size=1)
            elif max_index == 1:
                if 0 < q < p:
                    next_action = 'down'
                else:
                    next_action = np.random.choice(['up', 'left', 'right'], size=1)

            elif max_index == 2:
                if 0 < q < p:
                    next_action = 'left'
                else:
                    next_action = np.random.choice(['up', 'down', 'right'], size=1)
            else:
                if 0 < q < p:
                    next_action = 'right'
                else:
                    next_action = np.random.choice(['up', 'down', 'left'], size=1)
            return next_action

        def Sample_Next_State(current_state, action):
            if action == 'up':
                if current_state[0] == 0:
                    next_state = current_state
                elif (current_state[0] - 1, current_state[1]) in blocks:
                    next_state = current_state
                else:
                    next_state = (current_state[0] - 1, current_state[1])
            if action == 'down':
                if current_state[0] == m - 1:
                    next_state = current_state
                elif (current_state[0] + 1, current_state[1]) in blocks:
                    next_state = current_state
                else:
                    next_state = (current_state[0] + 1, current_state[1])
            if action == 'left':
                if current_state[1] == 0:
                    next_state = current_state
                elif (current_state[0], current_state[1] - 1) in blocks:
                    next_state = current_state
                else:
                    next_state = (current_state[0], current_state[1] - 1)
            if action == 'right':
                if current_state[1] == n - 1:
                    next_state = current_state
                elif (current_state[0], current_state[1] + 1) in blocks:
                    next_state = current_state
                else:
                    next_state = (current_state[0], current_state[1] + 1)
            return next_state

        def Update(sample_next_state, current_state, action, gamma, alpha):
            if action == 'up':
                action_num = 0
            elif action == 'down':
                action_num = 1
            elif action == 'left':
                action_num = 2
            else:
                action_num = 3
            max_index_next = \
                np.where(np.max(Q[state_idx.index(sample_next_state),]) == Q[state_idx.index(sample_next_state),])[
                    0]
            if max_index_next.shape[0] > 1:
                max_index_next = int(np.random.choice(max_index_next, size=1))
            else:
                max_index_next = int(max_index_next)

            max_value = Q[state_idx.index(sample_next_state), max_index_next]
            Q[state_idx.index(current_state), action_num] = (1 - alpha) * Q[
                state_idx.index(current_state), action_num] + alpha * (
                                                                    R[sample_next_state] + gamma * max_value)
            print('max_value', R[sample_next_state] + gamma * max_value)
            if np.max(Q) > 0:
                return np.sum(Q / np.max(Q) * 100)
            else:
                return 0

        # Training

        for i in range(iterations):
            scores = []
            current_state_idx = int(np.random.choice(len(state_idx), size=1))
            current_state = s[current_state_idx]
            steps = [current_state]
            while current_state != (m - 1, n - 1):
                action = Sample_Next_Action(state=current_state, p=0.25 + i * (0.75 / (iterations - 1)))
                Next_state = Sample_Next_State(current_state, action)
                score = Update(Next_state, current_state, action, gamma, alpha)
                scores.append(score)
                steps.append(Next_state)
                current_state = Next_state
            print("Most Efficient Path")
            print(steps)
        print("Trained Q Matrix")
        print(Q / np.max(Q) * 100)
        print((int(self.CurrentState[0][1]), int(self.CurrentState[0][4])))

        # show steps"
        current_state = (int(self.CurrentState[0][1]), int(self.CurrentState[0][4]))
        steps = [current_state]
        while current_state != (m - 1, n - 1):
            action = Sample_Next_Action(state=current_state, p=1)
            Next_state = Sample_Next_State(current_state, action)
            score = Update(Next_state, current_state, action, gamma, alpha)
            scores.append(score)
            steps.append(Next_state)
            current_state = Next_state
        print("Most Efficient Path")
        print(steps)
        self.B = blocks
        self.MEP = steps


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    wizard = QtWidgets.QWizard()
    wizard.setGeometry(0, 0, 800, 600)
    ui = Ui_MainWindow()
    ui.setupUi(wizard)
    wizard.addPage(ui.createIntroPage())
    wizard.addPage(ui.createInputsPage())
    wizard.addPage(ui.LastPage())
    wizard.show()
    sys.exit(app.exec_())
