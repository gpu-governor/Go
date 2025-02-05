# import required libraries
import tkinter
import tkinter.messagebox
import pickle
from quotes import random_quote 

def add_tasks():
    task= entry_task.get()
    if task!="":
        listbox_tasks.insert(tkinter.END,task)
        entry_task.delete(0,tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="warning!",message="you must enter a task.")

def delete_tasks():
    try:
        task_index=listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="warning!",message="you must select a task.")
        
def load_tasks():
    try:
        tasks=pickle.load(open("tasks.dat","rb"))
        listbox_tasks.delete(0,tkinter.END)
        for task in tasks:
            listbox_tasks.insert(tkinter.END,task)
    except:
        tkinter.messagebox.showwarning(title="warning!",message="cannot find task.dat.")
def save_tasks():
    tasks=listbox_tasks.get(0,listbox_tasks.size())
    # print(tasks)
    pickle.dump(tasks,open("tasks.dat","wb"))
    
    
# main program window
root =tkinter.Tk()
root.title("Todo list")
root.geometry("450x350")

# create gui
quote_label=tkinter.Message(root,text=random_quote,font=("Arial", 16), width=300, anchor=tkinter.CENTER, justify=tkinter.CENTER)
quote_label.pack()

frame_tasks=tkinter.Frame(root)
frame_tasks.pack()

listbox_tasks=tkinter.Listbox(frame_tasks,height=3,width=50)
listbox_tasks.pack(side=tkinter.LEFT)


scrollbar_tasks=tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task=tkinter.Entry(root, width=50)
entry_task.pack()

button_add_tasks=tkinter.Button(root, text="Add task",width=48, command=add_tasks)
button_add_tasks.pack()

button_delete_tasks=tkinter.Button(root, text="delete task",width=48, command=delete_tasks)
button_delete_tasks.pack()

button_load_tasks=tkinter.Button(root, text="load task",width=48, command=load_tasks)
button_load_tasks.pack()

button_save_tasks=tkinter.Button(root, text="save task",width=48, command=save_tasks)
button_save_tasks.pack()

# main loop
root.mainloop()
