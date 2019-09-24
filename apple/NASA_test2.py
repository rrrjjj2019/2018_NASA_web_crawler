import tkinter as tk

window = tk.Tk()
window.title('rocket')
window.geometry('930x465')

canvas = tk.Canvas(window, bg = 'blue', height = 465, width = 930)
image_file = tk.PhotoImage(file = 'back.gif')
image = canvas.create_image(0, 0, anchor = 'nw', image = image_file)
canvas.pack()

window.mainloop()
