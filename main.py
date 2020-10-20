from PyQt5 import QtCore, QtGui, QtWidgets
from counter import Ui_MainWindow
import sys
import datetime


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()

x_bool = 0
v_book = []
v_book_lcd_7 = []
v_book_lcd_8 = []
v_book_lcd_9 = []
v_book_lcd_10 = []


def main():

	
	ui.setupUi(MainWindow)
	MainWindow.show()

	day_list = []

	current_date = str(datetime.date.today())

	daycount_file = open('daycount.txt','r')

	p_liner = daycount_file.readlines()
	liner = [i[0:-1] for i in p_liner]
	
	#if liner[0] != current_date:
		#pass


	ui.label_5.setGeometry(QtCore.QRect(300, 270, 0, 0))
	ui.label_6.setGeometry(QtCore.QRect(300, 270, 0, 0))
	ui.label_7.setGeometry(QtCore.QRect(300, 270, 0, 0))
	ui.label_8.setGeometry(QtCore.QRect(300, 270, 0, 0))

	ui.lineEdit_3.setGeometry(QtCore.QRect(350, 270, 0, 0))
	ui.lineEdit_4.setGeometry(QtCore.QRect(350, 270, 0, 0))
	ui.lineEdit_5.setGeometry(QtCore.QRect(350, 270, 0, 0))
	ui.lineEdit_6.setGeometry(QtCore.QRect(350, 270, 0, 0))

	ui.pushButton.setGeometry(QtCore.QRect(20, 490, 201, 61))
	ui.pushButton_2.setGeometry(QtCore.QRect(230, 490, 0, 0))
	ui.pushButton.clicked.connect(get_count)
	ui.pushButton_4.clicked.connect(change)
	ui.pushButton_2.clicked.connect(record)
	ui.pushButton_3.clicked.connect(visual)
	ui.lineEdit.textEdited.connect(line_finder)
	
	sys.exit(app.exec_())

	
def booker_name():
	
	
	file = open('base.txt','r')
	book_t = []
	fileread = file.readlines()
	fileread_t = [i.lower() for i in fileread]
	
	counter = list(range(0,len(fileread_t),6))

	for i in counter:
		
		book_t.append(fileread[i])

	book_t.sort()

	return book_t


def combobox():
	
	
	set_t = ui.comboBox.currentText()
	ui.lineEdit.setText(set_t)


def booker():
	
	
	file = open('base.txt','r')
	book_t = []
	fileread = file.readlines()
	for i in fileread:
		book_t.append(i[:-1])
	return book_t


def record():
	

	t_file = open('base.txt','a')

	name_t = str(ui.lineEdit.text()) + '\n'
	name = name_t.capitalize()

	w_4 = str(ui.lineEdit_2.text()) + '\n'
	w_2 = str(ui.lineEdit_3.text()) + '\n'
	w_1 = str(ui.lineEdit_4.text()) + '\n'
	w_3 = str(ui.lineEdit_5.text()) + '\n'
	w_0 = str(ui.lineEdit_6.text()) + '\n'

	
	bool_val = 0

	if len(w_4) < 2:
		bool_val = 0
	elif len(w_2) < 2:
		bool_val = 0
	elif len(w_1) < 2:
		bool_val = 0
	elif len(w_3) < 2:
		bool_val = 0
	elif len(w_0) < 2:
		bool_val = 0
	elif len(name_t) < 2:
		bool_val = 0
	else: bool_val = 1 


	if bool_val == 1:
		
		t_file.write(name)
		t_file.write(w_0)
		t_file.write(w_1)
		t_file.write(w_2)
		t_file.write(w_3)
		t_file.write(w_4)

		ui.comboBox.addItem(name)
		ui.label_3.setText("Продукт записан!")
		
		ui.lineEdit.clear()
		ui.lineEdit_2.clear()

		ui.lineEdit_2.clear()
		ui.lineEdit_3.clear()
		ui.lineEdit_4.clear()
		ui.lineEdit_5.clear()
		ui.lineEdit_6.clear()

	else: ui.label_3.setText("Заполните все поля!")

	if bool_val == 0:
		ui.lcdNumber.display('ERROR')

	else: ui.lcdNumber.display('0')


def resetter():
	
	
	reset_file = open('daycount.txt','w')
	reset_file.write('')
	reset_file.close()


def daycounter(common,n_1,n_2,n_3,n_4):
	
	day_file = open('daycount.txt','a')

	current_date = datetime.date.today()

	date_reborn = str(current_date)

	day_file.write(date_reborn[0:10] + '\n')
	day_file.write(str(n_4) + '\n')
	day_file.write(str(n_2) + '\n')
	day_file.write(str(n_1) + '\n')
	day_file.write(str(n_3) + '\n')
	day_file.write(str(common) + '\n')


def visual():

	
	ui.comboBox.setGeometry(QtCore.QRect(20, 400, 0, 0))
	ui.lineEdit.clear()
	ui.lcdNumber.display('0')
	ui.lcdNumber_2.display('0')
	
	ui.label_5.setGeometry(QtCore.QRect(300, 190, 51, 20))
	ui.label_6.setGeometry(QtCore.QRect(290, 220, 51, 20))
	ui.label_7.setGeometry(QtCore.QRect(290, 250, 51, 20))
	ui.label_8.setGeometry(QtCore.QRect(290, 280, 51, 20))

	ui.lineEdit_3.setGeometry(QtCore.QRect(350, 190, 81, 20))
	ui.lineEdit_4.setGeometry(QtCore.QRect(350, 220, 81, 20))
	ui.lineEdit_5.setGeometry(QtCore.QRect(350, 250, 81, 20))
	ui.lineEdit_6.setGeometry(QtCore.QRect(350, 280, 81, 20))

	ui.label.setText('Калорийность:')
	ui.label_3.setText("Режим записи")
	
	ui.pushButton.setGeometry(QtCore.QRect(230, 490, 0, 0))
	ui.pushButton_2.setGeometry(QtCore.QRect(230, 490, 201, 61))


def get_value(x):
	
	
	book = booker()
	
	t_kal = book.index(x) + 1
	t_0 = book.index(x) + 2
	t_1 = book.index(x) + 3
	t_2 = book.index(x) + 4
	t_3 = book.index(x) + 5

	ret_book = []

	ret_book.append(book[t_kal])
	ret_book.append(book[t_0])
	ret_book.append(book[t_1])
	ret_book.append(book[t_2])
	ret_book.append(book[t_3])

	return ret_book


def get_count():
	

	combobox()

	try:

		ispal_t = str(ui.lineEdit.text())

		ispal = ispal_t.capitalize()
		
		val_name_list = get_value(ispal)

		vari = ui.lineEdit_2.text()
		
		if len(vari) < 1:
		
			vari = 100

		weight = int(vari) / 100
		
		val_5 = val_name_list[0]
		val_3 = val_name_list[1]
		val_2 = val_name_list[2]
		val_4 = val_name_list[3]
		val_1 = val_name_list[4]
		
		rested_1 = float(val_1) * float(weight)
		rested_2 = float(val_2) * float(weight)
		rested_3 = float(val_3) * float(weight)
		rested_4 = float(val_4) * float(weight)
		rested_5 = float(val_5) * float(weight)

		v_book.append(rested_1)
		v_book_lcd_7.append(rested_2)
		v_book_lcd_8.append(rested_3)
		v_book_lcd_9.append(rested_4)
		v_book_lcd_10.append(rested_5)

		if len(ispal) < 1:
		
			ui.lcdNumber.display('ERROR')
	
		else: ui.lcdNumber.display(int(val_1)*weight)

	except ValueError:
		ui.lcdNumber.display('ERROR')
		ui.label_3.setText("Ошибка! Такого продукта нет")
	
	vidget()
	daycounter(int(rested_1),int(rested_2),int(rested_3),int(rested_4),int(rested_5))

	ui.lineEdit_2.clear()
	ui.lineEdit.clear()


def dayget():
	pass
	#getter = open('daycount.txt','r')
	#list_line = getter.readlines()


def change():
	
	
	ui.label_5.setGeometry(QtCore.QRect(300, 270, 0, 0))
	ui.label_6.setGeometry(QtCore.QRect(300, 270, 0, 0))
	ui.label_7.setGeometry(QtCore.QRect(300, 270, 0, 0))
	ui.label_8.setGeometry(QtCore.QRect(300, 270, 0, 0))

	ui.lineEdit_3.setGeometry(QtCore.QRect(350, 270, 0, 0))
	ui.lineEdit_4.setGeometry(QtCore.QRect(350, 270, 0, 0))
	ui.lineEdit_5.setGeometry(QtCore.QRect(350, 270, 0, 0))
	ui.lineEdit_6.setGeometry(QtCore.QRect(350, 270, 0, 0))

	ui.label.setText("Количество, гр.")
	
	ui.comboBox.setGeometry(QtCore.QRect(20, 400, 261, 41))

	ui.label_3.setText("Рассчет каллорий")
	ui.pushButton.setGeometry(QtCore.QRect(20, 490, 201, 61))
	ui.pushButton_2.setGeometry(QtCore.QRect(230, 490, 0, 0))
	ui.lineEdit.clear()
	ui.lineEdit_2.clear()


def vidget():

	
	t_list = [int(i) for i in v_book]
	t_list_2 = [int(i) for i in v_book_lcd_7]
	t_list_3 = [int(i) for i in v_book_lcd_8]
	t_list_4 = [int(i) for i in v_book_lcd_9]
	t_list_5 = [int(i) for i in v_book_lcd_10]
	

	t_sum = sum(t_list)
	t2_sum = sum(v_book_lcd_7)
	t3_sum = sum(v_book_lcd_8)
	t4_sum = sum(v_book_lcd_9)
	t5_sum = sum(v_book_lcd_10)
	
	ui.lcdNumber_2.display(t_sum)
	ui.lcdNumber_7.display(t2_sum)
	ui.lcdNumber_8.display(t3_sum)
	ui.lcdNumber_9.display(t4_sum)
	ui.lcdNumber_10.display(t4_sum / 12)


def finder(f_value):

	
	finder_t = booker_name()
	finder_t_2 = [i[:-1] for i in finder_t]
	finder_book = [i.lower() for i in finder_t_2]
	t_book = []
	
	for i in finder_book:
	
		find_index = i.find(f_value)

		if find_index >= 0:

			t_book.append(i)
	
	return t_book


def line_finder():
	
	
	t_val = ui.lineEdit.text()

	get = finder(t_val)

	ui.comboBox.clear()

	for i in get:

		ui.comboBox.addItem(i)


if __name__ == "__main__":
	main()
