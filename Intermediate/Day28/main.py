from tkinter import *
import  math
from click import command

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
	canvas.after_cancel(timer)
	canvas.itemconfig(timer_text, text= "00: 00")
	label.config(text="Timer", fg= GREEN)
	check_box.config(text= "")
	global  reps
	reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
	global reps
	reps +=1
	work_sec = WORK_MIN * 60
	short_break_sec = SHORT_BREAK_MIN * 60
	long_break_sec = LONG_BREAK_MIN * 60
	if reps % 8 == 0:
		count_down(long_break_sec)
		label.config(text="Long Break", fg= RED)
	elif reps % 2 == 0:
		count_down(short_break_sec)
		label.config(text= "Short Break",  fg= PINK)
	else:
		count_down(work_sec)
		label.config(text= "Working" , fg= GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
	count_min = math.floor(count/60)
	count_sec = count % 60
	if count_sec  < 10:
		count_sec = f"0{count_sec}"
	canvas.itemconfig(timer_text, text = f"{count_min}: {count_sec}")
	if count > 0:
		global timer
		timer =  canvas.after(1000, count_down , count-1)
	else:
		start_timer()
		marks = ""
		work_session = math.floor(reps/2)
		for _ in range(work_session):
			marks+= "🗸"
		check_box.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pmodoro")
window.config(padx=100, pady= 50, bg=YELLOW)

canvas = Canvas(width=200 , height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image= tomato_img)
timer_text = canvas.create_text(103,112, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1 )
label = Label(text="Timer",  bg=YELLOW,  fg=GREEN ,highlightthickness=0 ,  font=(FONT_NAME, 50 , "bold"))
label.grid(column=1, row=0 )
start_button = Button(text="Start", highlightthickness=0 ,bg="white", command= start_timer)
start_button.grid(column=0, row=2 )
reset_button = Button(text="Reset", highlightthickness=0,bg="white" , command= reset_timer)
reset_button.grid(column=2,row=2)
check_box = Label(highlightthickness=0  ,bg=YELLOW, fg= GREEN , font=("bold"))
check_box.grid(column=1, row=3)



window.mainloop()