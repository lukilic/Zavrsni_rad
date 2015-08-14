from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_pacijent_Widget(object):
    def setupUi(self, pacijent_Widget):
        pacijent_Widget.setObjectName(_fromUtf8("pacijent_Widget"))
        pacijent_Widget.resize(400, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../icrc.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        pacijent_Widget.setWindowIcon(icon)
        self.horizontalLayout_8 = QtGui.QHBoxLayout(pacijent_Widget)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pacijent_oib_pac_label = QtGui.QLabel(pacijent_Widget)
        self.pacijent_oib_pac_label.setObjectName(_fromUtf8("pacijent_oib_pac_label"))
        self.horizontalLayout.addWidget(self.pacijent_oib_pac_label)
        self.pacijent_oib_pac_lineEdit = QtGui.QLineEdit(pacijent_Widget)
        self.pacijent_oib_pac_lineEdit.setMaxLength(11)
        self.pacijent_oib_pac_lineEdit.setObjectName(_fromUtf8("pacijent_oib_pac_lineEdit"))
        self.horizontalLayout.addWidget(self.pacijent_oib_pac_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.pacijent_prezime_label = QtGui.QLabel(pacijent_Widget)
        self.pacijent_prezime_label.setObjectName(_fromUtf8("pacijent_prezime_label"))
        self.horizontalLayout_2.addWidget(self.pacijent_prezime_label)
        self.pacijent_prezime_lineEdit = QtGui.QLineEdit(pacijent_Widget)
        self.pacijent_prezime_lineEdit.setObjectName(_fromUtf8("pacijent_prezime_lineEdit"))
        self.horizontalLayout_2.addWidget(self.pacijent_prezime_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.pacijent_ime_label = QtGui.QLabel(pacijent_Widget)
        self.pacijent_ime_label.setObjectName(_fromUtf8("pacijent_ime_label"))
        self.horizontalLayout_3.addWidget(self.pacijent_ime_label)
        self.pacijent_ime_lineEdit = QtGui.QLineEdit(pacijent_Widget)
        self.pacijent_ime_lineEdit.setObjectName(_fromUtf8("pacijent_ime_lineEdit"))
        self.horizontalLayout_3.addWidget(self.pacijent_ime_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.pacijent_id_sobe_label = QtGui.QLabel(pacijent_Widget)
        self.pacijent_id_sobe_label.setObjectName(_fromUtf8("pacijent_id_sobe_label"))
        self.horizontalLayout_4.addWidget(self.pacijent_id_sobe_label)
        self.pacijent_id_sobe_lineEdit = QtGui.QLineEdit(pacijent_Widget)
        self.pacijent_id_sobe_lineEdit.setMaxLength(3)
        self.pacijent_id_sobe_lineEdit.setObjectName(_fromUtf8("pacijent_id_sobe_lineEdit"))
        self.horizontalLayout_4.addWidget(self.pacijent_id_sobe_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.pacijent_adresa_label = QtGui.QLabel(pacijent_Widget)
        self.pacijent_adresa_label.setObjectName(_fromUtf8("pacijent_adresa_label"))
        self.horizontalLayout_5.addWidget(self.pacijent_adresa_label)
        self.pacijent_adresa_lineEdit = QtGui.QLineEdit(pacijent_Widget)
        self.pacijent_adresa_lineEdit.setObjectName(_fromUtf8("pacijent_adresa_lineEdit"))
        self.horizontalLayout_5.addWidget(self.pacijent_adresa_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.pacijent_datum_rodjenja_label = QtGui.QLabel(pacijent_Widget)
        self.pacijent_datum_rodjenja_label.setObjectName(_fromUtf8("pacijent_datum_rodjenja_label"))
        self.horizontalLayout_6.addWidget(self.pacijent_datum_rodjenja_label)
        self.pacijent_datum_rodjenja_lineEdit = QtGui.QLineEdit(pacijent_Widget)
        self.pacijent_datum_rodjenja_lineEdit.setObjectName(_fromUtf8("pacijent_datum_rodjenja_lineEdit"))
        self.horizontalLayout_6.addWidget(self.pacijent_datum_rodjenja_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.pacijent_spol_label = QtGui.QLabel(pacijent_Widget)
        self.pacijent_spol_label.setObjectName(_fromUtf8("pacijent_spol_label"))
        self.horizontalLayout_7.addWidget(self.pacijent_spol_label)
        self.pacijent_spol_lineEdit = QtGui.QLineEdit(pacijent_Widget)
        self.pacijent_spol_lineEdit.setMaxLength(1)
        self.pacijent_spol_lineEdit.setObjectName(_fromUtf8("pacijent_spol_lineEdit"))
        self.horizontalLayout_7.addWidget(self.pacijent_spol_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem = QtGui.QSpacerItem(20, 13, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.pacijent_Add_button = QtGui.QPushButton(pacijent_Widget)
        self.pacijent_Add_button.setObjectName(_fromUtf8("pacijent_Add_button"))
        self.verticalLayout_2.addWidget(self.pacijent_Add_button)
        spacerItem1 = QtGui.QSpacerItem(20, 13, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_8.addLayout(self.verticalLayout_2)

        self.retranslateUi(pacijent_Widget)
        QtCore.QMetaObject.connectSlotsByName(pacijent_Widget)

    def retranslateUi(self, pacijent_Widget):
        pacijent_Widget.setWindowTitle(_translate("pacijent_Widget", "Pacijent", None))
        self.pacijent_oib_pac_label.setText(_translate("pacijent_Widget", "OIB pacijenta", None))
        self.pacijent_prezime_label.setText(_translate("pacijent_Widget", "Prezime", None))
        self.pacijent_ime_label.setText(_translate("pacijent_Widget", "Ime", None))
        self.pacijent_id_sobe_label.setText(_translate("pacijent_Widget", "ID sobe", None))
        self.pacijent_adresa_label.setText(_translate("pacijent_Widget", "Adresa", None))
        self.pacijent_datum_rodjenja_label.setText(_translate("pacijent_Widget", "Datum rodjenja (YYYY-MM-DD)", None))
        self.pacijent_spol_label.setText(_translate("pacijent_Widget", "Spol (\'M\' ili \'Z\')", None))
        self.pacijent_Add_button.setText(_translate("pacijent_Widget", "Add", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    pacijent_Widget = QtGui.QWidget()
    ui = Ui_pacijent_Widget()
    ui.setupUi(pacijent_Widget)
    pacijent_Widget.show()
    sys.exit(app.exec_())
