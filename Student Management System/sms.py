from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from sqlite3 import *
from matplotlib import pyplot as plt
import numpy as np
import requests
import bs4

res = requests.get("https://ipinfo.io/")
data = res.json()
city = data['city']
	
a1 = "http://api.openweathermap.org/data/2.5/weather?units=metric"
a2 = "&q=" + city
a3 = "&appid=" + "c6e315d09197cec231495138183954bd"
wa = a1 + a2 + a3
res1 = requests.get(wa)
data = res1.json()
main = data['main']
temp = main['temp']
	
	
qa = "https://www.brainyquote.com/quote_of_the_day"
result = requests.get(qa)
information = bs4.BeautifulSoup(result.text, 'html.parser')
info = information.find('img', {'class':'p-qotd'})
msg = info['alt']


# - - FUNCTIONS - - - - - - - - - -
def validate(rv, nv, mv):
	r = rv; n = nv; m = mv

	if r == "":
		showerror('Error', 'Rno cannot be blank.')
		add_window_ent_rno.delete(0,END)
		upd_window_ent_rno.delete(0,END)
		add_window_ent_name.delete(0,END)
		upd_window_ent_name.delete(0,END)
		add_window_ent_marks.delete(0,END)
		upd_window_ent_marks.delete(0,END)
		add_window_ent_rno.focus()
		upd_window_ent_rno.focus()
		return(None,None,None)
	elif r.isalpha() == True:
		showerror('Error', 'Rno can have integers only')
		add_window_ent_rno.delete(0,END)
		upd_window_ent_rno.delete(0,END)
		add_window_ent_name.delete(0,END)
		upd_window_ent_name.delete(0,END)
		add_window_ent_marks.delete(0,END)
		upd_window_ent_marks.delete(0,END)
		add_window_ent_rno.focus()
		upd_window_ent_rno.focus()
		return(None,None,None)		
	elif int(r) <= 0:
		showerror('Error', 'Rno should be positive integers.')
		add_window_ent_rno.delete(0,END)
		upd_window_ent_rno.delete(0,END)
		add_window_ent_name.delete(0,END)
		upd_window_ent_name.delete(0,END)
		add_window_ent_marks.delete(0,END)
		upd_window_ent_marks.delete(0,END)
		add_window_ent_rno.focus()
		upd_window_ent_rno.focus()
		return(None,None,None)
	elif n == "":
		showerror('Error', 'Name cannot be blank.')
		add_window_ent_name.delete(0,END)
		upd_window_ent_name.delete(0,END)
		add_window_ent_rno.delete(0,END)
		upd_window_ent_rno.delete(0,END)
		add_window_ent_marks.delete(0,END)
		upd_window_ent_marks.delete(0,END)
		add_window_ent_name.focus()
		upd_window_ent_name.focus()
		return(None,None,None)
	elif not n.isalpha():
		showerror('Error', 'Name cannot be numeric')
		add_window_ent_name.delete(0,END)
		upd_window_ent_name.delete(0,END)
		add_window_ent_rno.delete(0,END)
		upd_window_ent_rno.delete(0,END)
		add_window_ent_marks.delete(0,END)
		upd_window_ent_marks.delete(0,END)
		add_window_ent_name.focus()
		upd_window_ent_name.focus()
		return(None,None,None)
	elif (len(n)) < 2:
		showerror('Error', 'Please enter a valid name.')
		add_window_ent_name.delete(0,END)
		upd_window_ent_name.delete(0,END)
		add_window_ent_rno.delete(0,END)
		upd_window_ent_rno.delete(0,END)
		add_window_ent_marks.delete(0,END)
		upd_window_ent_marks.delete(0,END)
		add_window_ent_name.focus()
		upd_window_ent_name.focus()
		return(None,None,None)
	elif m == "":
		showerror('Error', 'Marks cannot be blank.')
		add_window_ent_marks.delete(0,END)
		upd_window_ent_marks.delete(0,END)
		add_window_ent_rno.delete(0,END)
		upd_window_ent_rno.delete(0,END)
		add_window_ent_name.delete(0,END)
		upd_window_ent_name.delete(0,END)
		add_window_ent_marks.focus()
		upd_window_ent_marks.focus()
		return(None,None,None)
	elif m.isalpha() == True:
		showerror('Error', 'Marks can be integers only')
		add_window_ent_marks.delete(0,END)
		upd_window_ent_marks.delete(0,END)
		add_window_ent_rno.delete(0,END)
		upd_window_ent_rno.delete(0,END)
		add_window_ent_name.delete(0,END)
		upd_window_ent_name.delete(0,END)
		add_window_ent_marks.focus()
		upd_window_ent_marks.focus()
		return(None,None,None)
	elif int(m) < 0 or int(m) > 100: 
		showerror('Error', 'Marks should be in range 0-100.')
		add_window_ent_marks.delete(0,END)
		upd_window_ent_marks.delete(0,END)
		add_window_ent_rno.delete(0,END)
		upd_window_ent_rno.delete(0,END)
		add_window_ent_name.delete(0,END)
		upd_window_ent_name.delete(0,END)
		add_window_ent_marks.focus()
		upd_window_ent_marks.focus()
		return(None,None,None)
	else:
		vrno = int(r); vname = n; vmarks = int(m)
		return(vrno, vname, vmarks)

def fn1():
	main_window.withdraw()
	add_window.deiconify()

def fn2():
	add_window.withdraw()
	main_window.deiconify()
	add_window_ent_rno.delete(0,END)
	add_window_ent_name.delete(0,END)
	add_window_ent_marks.delete(0,END)
	add_window_ent_rno.focus()

def fn3():
	main_window.withdraw()
	view_window.deiconify()
	view_window_st_data.delete(1.0, END)
	info = ""
	con = None
	try:
		con = connect("sms.db")
		cursor = con.cursor()
		sql = "select * from student"
		cursor.execute(sql)
		data = cursor.fetchall()
		for d in data:
			info = info + " rno: " + str(d[0]) + " name: " + str(d[1]) + " marks: " + str(d[2]) + "\n"
		view_window_st_data.insert(INSERT, info)
	except Exception as e:
		showerror("Issue", e)
	finally:
		if con is not None:
			con.close()
def fn4():
	view_window.withdraw()
	main_window.deiconify()

def fn5():
	con = None
	rno = add_window_ent_rno.get()
	name = add_window_ent_name.get()
	marks = add_window_ent_marks.get()
	db_rno=[]
	vrno, vname, vmarks = validate(rno, name, marks)
	if vrno != None:
		try:
			con = connect("sms.db")					
			cursor = con.cursor()
			get_rno = "Select rno from student"
			cursor.execute(get_rno)
			data = cursor.fetchall()
			for d in data:
				db_rno.append(d[0])
			if vrno in db_rno:
				showerror("Warning", "Roll no. is already in use.")
				con.rollback()
			else:
				sql = "insert into student values('%d', '%s', '%d')"
				cursor.execute(sql % (vrno, vname, vmarks))
				con.commit()
				showinfo("Success", "record added")				
			add_window_ent_rno.delete(0, END)
			add_window_ent_name.delete(0, END)
			add_window_ent_marks.delete(0, END)
			add_window_ent_rno.focus()		
		except Exception as e:
			showerror("Issue", e)
			add_window_ent_rno.delete(0, END)
			add_window_ent_name.delete(0, END)
			add_window_ent_marks.delete(0, END)
			add_window_ent_rno.focus()
		finally:
			if con is not None:
				con.close()
def fn6():
	main_window.withdraw()
	upd_window.deiconify()

def fn7():
	con = None		
	rno = upd_window_ent_rno.get()
	name = upd_window_ent_name.get()
	marks = upd_window_ent_marks.get()
	vrno, vname, vmarks = validate(rno, name, marks)
	if vrno != None:
		try:
			con = connect("sms.db")
			cursor = con.cursor()
			sql = "update student set name = '%s', marks='%d' where rno = '%d'"
			cursor.execute(sql % (vname, vmarks, vrno))
			if cursor.rowcount > 0:
				showinfo("Success","Record updated")
				con.commit()
			else:
				showerror("Retry","Record does not exist")
			upd_window_ent_rno.delete(0, END)
			upd_window_ent_name.delete(0, END)
			upd_window_ent_marks.delete(0, END)
			upd_window_ent_rno.focus()			
		except Exception as e:
			showerror("Issue", e)
			con.rollback()
		finally:
			if con is not None:
				con.close()
def fn8():
	upd_window.withdraw()
	main_window.deiconify()	

def fn9():
	main_window.withdraw()
	del_window.deiconify()

def fn10():
	con = None		
	rno = del_window_ent_rno.get()
	if rno == '':
		showerror("Warning","Roll cannot be blank.")
		del_window_ent_rno.focus()
	elif not rno.isdigit():
		showerror("Warning","Roll has to be numeric.")
		del_window_ent_rno.delete(0,END)
		del_window_ent_rno.focus()
	else:
		try:
			con = connect("sms.db")
			cursor = con.cursor()
			sql = "delete from student where rno ='%d'"
			rno = del_window_ent_rno.get()
			cursor.execute(sql % int(rno))
			if cursor.rowcount > 0:
				showinfo("Success","record deleted")
				con.commit()	
			else:
				showerror("Failure","record does not exists")
			del_window_ent_rno.delete(0, END)
			del_window_ent_rno.focus()
		except Exception as e:
			showerror("Issue", e)
		finally:
			if con is not None:
				con.close()		

def fn11():
	del_window.withdraw()
	main_window.deiconify()	

def fn12():
	con = None
	try:
		con = connect("sms.db")
		cursor = con.cursor()
		sql = "select * from student"
		cursor.execute(sql)
		rno = []
		marks = []
		name = []
		row = cursor.fetchone()
		while row is not None:
			rno.append(row[0])
			name.append(row[1])
			marks.append(row[2])
			row = cursor.fetchone()
		x = np.arange(len(name))
		y = np.arange(len(marks))
		plt.bar(name, marks, color=['red', 'green', 'blue'])
		plt.ylabel("marks")
		plt.title("Batch Information")
		plt.xticks(x, name)
		plt.show()
	except Exception as e:
		showerror("Issue", e)
	finally:
		if con is not None:
			con.close()
							
# - - MAIN WINDOW - - - - - - - - - -
main_window = Tk()
main_window.title("S.M.S ")
main_window.geometry("600x500+400+100")
main_window.configure(bg='honeydew2')


f = ('Calibri', 18, 'bold')
f1 = ('Calibri', 18)
main_window_btn_add = Button(main_window, text="Add", width=10, font=f, relief='solid', borderwidth=1, command=fn1)
main_window_btn_view = Button(main_window, text="View", width=10, font=f, relief='solid', borderwidth=1, command=fn3)
main_window_btn_update = Button(main_window, text="Update", width=10, font=f, relief='solid', borderwidth=1, command=fn6)
main_window_btn_delete = Button(main_window, text="Delete", width=10, font=f, relief='solid', borderwidth=1, command=fn9)
main_window_btn_charts = Button(main_window, text="Charts", width=10, font=f, relief='solid', borderwidth=1, command=fn12)
main_window_lbl_lt = Label(main_window, text=("Location: "+ city + "\t\tTemp: " + str(temp)), font=f1, relief='solid', borderwidth=1)
main_window_lbl_qotd = Label(main_window, text=("QOTD: "+ msg), font=f1, relief='solid', borderwidth=1, wraplength=600)

main_window_btn_add.pack(pady=10)
main_window_btn_view.pack(pady=10)
main_window_btn_update.pack(pady=10)
main_window_btn_delete.pack(pady=10)
main_window_btn_charts.pack(pady=10)
main_window_lbl_lt.pack(pady=10)
main_window_lbl_qotd.pack(pady=10)

#  - -  ADD WINDOW - - - - - - - - - -
add_window = Toplevel(main_window)
add_window.title("Add St.")
add_window.geometry("700x500+400+100")
add_window.configure(bg='lavender')

add_window_lbl_rno = Label(add_window, text="enter rno:", font=f)
add_window_ent_rno = Entry(add_window, bd=5, font=f)
add_window_lbl_name = Label(add_window, text="enter name:", font=f)
add_window_ent_name = Entry(add_window, bd=5, font=f)
add_window_lbl_marks = Label(add_window, text="enter marks:", font=f)
add_window_ent_marks = Entry(add_window, bd=5, font=f)
add_window_btn_save = Button(add_window, text="Save", width=10, font=f, command=fn5)
add_window_btn_back = Button(add_window, text="Back", width=10, font=f, command=fn2)

add_window_lbl_rno.pack(pady=10)
add_window_ent_rno.pack(pady=10)
add_window_lbl_name.pack(pady=10)
add_window_ent_name.pack(pady=10)
add_window_lbl_marks.pack(pady=10)
add_window_ent_marks.pack(pady=10)
add_window_btn_save.pack(pady=10)
add_window_btn_back.pack(pady=10)

add_window.withdraw()

#  - -  VIEW WINDOW - - - - - - - - - -
view_window = Toplevel(main_window)
view_window.title("View St.")
view_window.geometry("700x500+400+100")
view_window.configure(bg='yellow')

view_window_st_data = ScrolledText(view_window, width=50, height=20)
view_window_btn_back = Button(view_window, text="Back", width=10, font=f, command=fn4)

view_window_st_data.pack(pady=10)
view_window_btn_back.pack(pady=10)

view_window.withdraw()

#  - -  UPDATE WINDOW - - - - - - - - - -
upd_window = Toplevel(main_window)
upd_window.title("Update St.")
upd_window.geometry("700x500+400+100")
upd_window.configure(bg='peach puff')

upd_window_lbl_rno = Label(upd_window, text="enter rno:", font=f)
upd_window_ent_rno = Entry(upd_window, bd=5, font=f)
upd_window_lbl_name = Label(upd_window, text="enter name:", font=f)
upd_window_ent_name = Entry(upd_window, bd=5, font=f)
upd_window_lbl_marks = Label(upd_window, text="enter marks:", font=f)
upd_window_ent_marks = Entry(upd_window, bd=5, font=f)
upd_window_btn_save = Button(upd_window, text="Save", width=10, font=f, command=fn7)
upd_window_btn_back = Button(upd_window, text="Back", width=10, font=f, command=fn8)

upd_window_lbl_rno.pack(pady=10)
upd_window_ent_rno.pack(pady=10)
upd_window_lbl_name.pack(pady=10)
upd_window_ent_name.pack(pady=10)
upd_window_lbl_marks.pack(pady=10)
upd_window_ent_marks.pack(pady=10)
upd_window_btn_save.pack(pady=10)
upd_window_btn_back.pack(pady=10)

upd_window.withdraw()

#  - -  DELETE WINDOW - - - - - - - - - -
del_window = Toplevel(main_window)
del_window.title("Delete St.")
del_window.geometry("700x500+400+100")
del_window.configure(bg='LightSteelBlue1')

del_window_lbl_rno = Label(del_window, text="enter rno:", font=f)
del_window_ent_rno = Entry(del_window, bd=5, font=f)
del_window_btn_save = Button(del_window, text="Save", width=10, font=f, command=fn10)
del_window_btn_back = Button(del_window, text="Back", width=10, font=f, command=fn11)

del_window_lbl_rno.pack(pady=10)
del_window_ent_rno.pack(pady=10)
del_window_btn_save.pack(pady=10)
del_window_btn_back.pack(pady=10)

del_window.withdraw()

main_window.mainloop()