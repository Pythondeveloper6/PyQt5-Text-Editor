import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Main(QMainWindow):
    def __init__(self, parent = None):
        QMainWindow.__init__(self,parent)
        self.filename = ""
        self.initUI()


    def Menubar(self):
        menubar = self.menuBar()
        file = menubar.addMenu("File")
        edit = menubar.addMenu("Edit")
        view = menubar.addMenu("View")

        file.addAction(self.newAction)
        file.addAction(self.openAction)
        file.addAction(self.saveAction)



    def Toolbar(self):
        self.newAction = QAction("New" , self)
        self.newAction.triggered.connect(self.new)
        self.newAction.setShortcut("Ctrl+N")
        self.newAction.setStatusTip("Create a new document from scratch.")
        
        self.openAction = QAction("Open" , self)
        self.openAction.triggered.connect(self.open)
        self.openAction.setShortcut("Ctrl+O")
        self.openAction.setStatusTip("Open existing document")

        self.saveAction = QAction("Save" , self)
        self.saveAction.triggered.connect(self.save)
        self.saveAction.setShortcut("Ctrl+S")
        self.saveAction.setStatusTip("Save document")
        
        self.addToolBarBreak()


    def Formatbar(self):
        fontbox = QFontComboBox(self)
        fontbox.currentFontChanged.connect(lambda font: self.text.setCurrentFont(font))
        fontSize = QSpinBox(self)
        fontSize.setSuffix(" pt")
        fontSize.valueChanged.connect(lambda size: self.text.setFontPointSize(size))
        fontSize.setValue(14)
   
        fontColor = QAction(QIcon("icons/font-color.png"),"Change font color",self)
        fontColor.triggered.connect(self.fontColorChanged)

        backColor = QAction(QIcon("icons/highlight.png"),"Change background color",self)
        backColor.triggered.connect(self.highlight)

        boldAction = QAction(QIcon("icons/bold.png"),"Bold",self)
        boldAction.triggered.connect(self.bold)

        italicAction = QAction(QIcon("icons/italic.png"),"Italic",self)
        italicAction.triggered.connect(self.italic)

        underlAction = QAction(QIcon("icons/underline.png"),"Underline",self)
        underlAction.triggered.connect(self.underline)

        strikeAction = QAction(QIcon("icons/strike.png"),"Strike-out",self)
        strikeAction.triggered.connect(self.strike)

        alignLeft = QAction(QIcon("icons/align-left.png"),"Align left",self)
        alignLeft.triggered.connect(self.alignLeft)

        alignCenter = QAction(QIcon("icons/align-center.png"),"Align center",self)
        alignCenter.triggered.connect(self.alignCenter)

        alignRight = QAction(QIcon("icons/align-right.png"),"Align right",self)
        alignRight.triggered.connect(self.alignRight)

        alignJustify = QAction(QIcon("icons/align-justify.png"),"Align justify",self)
        alignJustify.triggered.connect(self.alignJustify)
        
        self.formatbar = self.addToolBar("Format")
        self.formatbar.addWidget(fontbox)
        self.formatbar.addWidget(fontSize)
        self.formatbar.addSeparator()
        self.formatbar.addAction(fontColor)
        self.formatbar.addAction(backColor)

        self.formatbar.addSeparator()

        self.formatbar.addAction(boldAction)
        self.formatbar.addAction(italicAction)
        self.formatbar.addAction(underlAction)
        self.formatbar.addAction(strikeAction)

        self.formatbar.addSeparator()
        self.formatbar.addAction(alignLeft)
        self.formatbar.addAction(alignCenter)
        self.formatbar.addAction(alignRight)
        self.formatbar.addAction(alignJustify)


    def new(self):
        window = Main(self)
        window.show()

    def open(self):
        self.filename = QFileDialog.getOpenFileName(self, 'Open File',".","(*.txt)")
        if self.filename:
            with open(self.filename,"txt") as file:
                self.text.setText(file.read())

    def save(self):
        if not self.filename:
          self.filename =QFileDialog.getSaveFileName(self, 'Save File')

        if not self.filename.endswith(".txt"):
          self.filename += ".txt"
          
        with open(self.filename,"txt") as file:
            file.write(self.text.toHtml())

    def fontColorChanged(self):
        color = QColorDialog.getColor()
        self.text.setTextColor(color)
        
    def highlight(self):
       color = QColorDialog.getColor()
       self.text.setTextBackgroundColor(color)
        
    def bold(self):
        if self.text.fontWeight() == QFont.Bold:
            self.text.setFontWeight(QFont.Normal)
        else:
            self.text.setFontWeight(QFont.Bold)
    
    def italic(self):
        state = self.text.fontItalic()
        self.text.setFontItalic(not state)

    def underline(self):
        state = self.text.fontUnderline()
        self.text.setFontUnderline(not state)

    def strike(self):
        fmt = self.text.currentCharFormat()
        fmt.setFontStrikeOut(not fmt.fontStrikeOut())
        self.text.setCurrentCharFormat(fmt)
        
    def alignLeft(self):
        self.text.setAlignment(Qt.AlignLeft)

    def alignRight(self):
        self.text.setAlignment(Qt.AlignRight)

    def alignCenter(self):
        self.text.setAlignment(Qt.AlignCenter)
    
    def alignJustify(self):
        self.text.setAlignment(Qt.AlignJustify)

    def initUI(self):
        self.text = QTextEdit(self)
        self.Toolbar()
        self.Formatbar()
        self.Menubar()
        self.setWindowTitle("Text Editor")
        self.text.setTabStopWidth(33)
        self.setCentralWidget(self.text)
        self.statusbar = self.statusBar()
        self.setGeometry(100,100,900,600)



def main():
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
