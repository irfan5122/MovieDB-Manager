#@Author : AHMED IRFAN N
# Making gui for movie database management
# Import module
from tkinter import*
from tkinter import ttk
import mysql.connector as sql
from tkinter import messagebox as msg
import csv
root = Tk()
#----------------------app initializing management---------------------------
conn = sql.connect(host='localhost',user='root',password='root',database='movies_series')
my_cur = conn.cursor()
my_cur.execute("select * from movies_seen")
#C:\Users\ASUS\Documents\user_documents\text_files\movie and series zone\
with open(r'movies_seen.csv','w',newline='') as data:
    writer_obj = csv.writer(data)
    for i in my_cur:
        writer_obj.writerow(i)
conn.close()
#----------------------------------------------------------------------------
root.config(bg='black')
root.title("Database manager")
root.geometry('870x300')
root.resizable(False,False)
def delete_tab():
	def delete():
		deletion_no = sno_store.get()
		entry_delete.delete(0,END)
		entry_delete.insert(0,0)
		print(deletion_no)
		if deletion_no == 0:
			msg.showinfo("No Input","Please Enter a value and continue")
		else:
			connector = sql.connect(host='localhost',user='root',password='root',database='movies_series')
			handle = connector.cursor()
			handle.execute(f"delete from movies_seen where sno={deletion_no}")
			connector.commit()
	window = Tk()
	window.title('Database manager')
	window.config(bg='black')
	window.geometry('700x150')
	lbl_delete = Label(window,text="Enter the Sno to be deleted : ",font=('ROG FONTS',18),bg='black',fg='cyan')
	lbl_delete.place(x=10,y=2)
	sno_store = IntVar(window)
	entry_delete = Entry(window,textvariable=sno_store,font=('ROG FONTS',18),width=5)
	entry_delete.place(x=550,y=2)
	btn_del = Button(window,text='delete',font=('ROG FONTS',20),bg='black',fg='cyan',command=delete)
	btn_del.place(x=300,y=50)
	window.mainloop()
def module_fetcher():
	root_2 = Tk()
	root_2.config(bg='black')
	root_2.title("Database manager")
	root_2.geometry('800x800')
	root_2.resizable(False,False)


	#-------scroll bar-----------------
	mainframe = Frame(root_2)
	mainframe.config(bg='black')
	mainframe.pack(fill=BOTH, expand=1)
	my_canvas = Canvas(mainframe)
	my_canvas.pack(sid=LEFT,fill=BOTH,expand=1)
	my_scrollbar = ttk.Scrollbar(mainframe,orient=VERTICAL,command=my_canvas.yview)
	my_scrollbar.pack(side=RIGHT,fill=Y)
	my_canvas.configure(yscrollcommand=my_scrollbar.set)
	my_canvas.bind('<Configure>',lambda e:my_canvas.configure(scrollregion = my_canvas.bbox("all")))
	second_frame = Frame(my_canvas)
	second_frame.config(bg='black')	
	my_canvas.create_window((0,0),window=second_frame,anchor="nw")
	#----------------------------------------------------------------------



	connector = sql.connect(host='localhost',user='root',password='root',database='movies_series')
	handle = connector.cursor()
	handle.execute("select * from movies_seen")
	for i in handle:
		lbl = Label(second_frame,text=f'{i}',font={'ROG FONTS',10},bg='black',fg='cyan')
		lbl.grid(column=0,pady=10,padx=10)
	root_2.mainloop()

def main():
	#-----------sql connection---------------

	connector = sql.connect(host='localhost',user='root',password='root',database='movies_series')
	handle = connector.cursor()
	handle.execute("select max(Sno) from movies_seen")
	movie_name_sql = movie_name_value.get()
	language_sql = language.get()
	Category_sql = ''
	if R1_R2_option.get() == 1:
		Category_sql+='Movie'
	else:
		Category_sql+='Series'
	year_sql = year.get()
	language_sql = language.get()
	count = 0
	for i in handle:
		for j in i:
			count+=j
	count+=1

	handle.execute(f"insert into movies_seen values({count},'{movie_name_sql}','{Category_sql}',{year_sql},'{language_sql}');")
	connector.commit()

#------------------------app-closing-management----------------

def on_close():
	conn = sql.connect(host='localhost',user='root',password='root',database='movies_series')
	my_cur = conn.cursor()
	my_cur.execute("select * from movies_seen")
	with open(r'movies_seen.csv','w',newline='') as data:
		writer_obj = csv.writer(data)
		for i in my_cur:
			writer_obj.writerow(i)
	root.destroy()


#---------------------------------------------------------------



movie_name_value = StringVar()
MovieName_lbl = Label(root,text="Enter the movie_name : ",bg='black',fg='cyan',font=('ROG FONTS',18))
MovieName_lbl.place(x=20,y=10)
MovieName_entry = Entry(root,bg='white',fg='black',font=('Time new roman',18),textvariable=movie_name_value)
MovieName_entry.place(x=500+50,y=10)
Category_lbl = Label(root,text="Select category : ",bg='black',fg='cyan',font=('ROG FONTS',18))
Category_lbl.place(x=20,y=60)
R1_R2_option = IntVar()
R1_R2_option.set(1)
R1 = Radiobutton(root,text='Movie',bg='black',fg='cyan',font=('ROG FONTS',15),variable=R1_R2_option,value=1)
R1.place(x=500+50,y=60)
R2 = Radiobutton(root,text='Series',bg='black',fg='cyan',font=('ROG FONTS',15),variable=R1_R2_option,value=2)
R2.place(x=630+50,y=60)
year_lbl = Label(root,text="Enter the release date : ",font=('ROG FONTS',18),bg='black',fg='cyan')
year_lbl.place(x=20,y=100)
year = IntVar()
year_entry = Entry(root,bg='white',fg='black',font=('Time new roman',18),textvariable=year,width=10)
year_entry.place(x=500+50,y=100)
language_lbl = Label(root,text="Enter the language : ",font=('ROG FONTS',18),bg='black',fg='cyan')
language = StringVar()
language.set("English")
language_lbl.place(x=20,y=140)



language_entry = OptionMenu(root,language,"English","Malayalam","Tamil","Hindi","Telungu","Korean","Japanese")
language_entry.config(bg='black',fg='cyan',font=('ROG FONTS',15))
language_entry["menu"].config(bg='black',fg='cyan',font=('Pangolin',15))
language_entry.place(x=500+50,y=140)
#language_entry.insert(0,'English')
b1 = Button(root,text='Submit',fg='cyan',bg='black',font=('ROG FONTS',20),command=main)
b1.place(x=300+80,y=200)

b2 = Button(root,text='open db',fg='red',bg='black',font=('ROG FONTS',20),command=module_fetcher)
b2.place(x=100+90,y=200)

lbl_credits = Label(root,text="Software by Ahmed Irfan N",bg='black',fg='pale green',font=('Pangolin',17))
lbl_credits.place(x=500+50,y=240)

b3 = Button(root,text='delete',fg='red',bg='black',font=('ROG FONTS',20),command=delete_tab)
b3.place(x=10,y=200)



#window closing management
root.protocol('WM_DELETE_WINDOW', on_close)
root.mainloop()






