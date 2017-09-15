from tkinter import*
from tkinter import messagebox
import random,sys

root = Tk()
root.geometry("500x500")
root.title("Mayın Tarlası v1.2")
root.resizable(0,0)
class Gui:
	bu = {}
	sayac = 0
	fra = Frame(background="#e1edc2", height=500, width=500)
	fra.place(x=0,y=0)
	frame = Frame(background="#b7ff00", height=400, width=400)
	frame.place(x=57,y=50)
	Button(text="( ͡° ͜ʖ ͡°)", width=7, height= 1 ,command = lambda: Gui() ).pack()
	var = IntVar()
	var.set(0)
	def __init__(self):
		self.sayi1 = self.rand()
		print(self.sayi1)
		#[print(i) for i in self.sayi1]

		self.yarat()


	def rand(self):
		return random.sample(range(100), 16)


	def yarat(self):
		for i in range(10):
			for j in range(10):
				self.bu[i,j] = Button(self.frame, height=2, width=4, text="✪", command= lambda x=i, y=j: self.bas(x,y))
				self.bu[i,j].bind("<Button-3>", lambda a,x=i, y=j  :self.bayrak(x,y))
				self.bu[i,j].grid(row=i, column=j)

	def bayrak(self,x,y):
		if self.bu[x,y]["text"] == "✪":
			self.bu[x,y]["text"] = "!!"

		elif self.bu[x,y]["text"] == "!!":
			self.bu[x,y]["text"] = "✪"
		
		
	def bas(self,x,y):
		if self.bu[x,y]["text"] == "!!":
			pass;
		else:
			self.sayac +=1
			if self.sayac == 84:
				messagebox.showinfo("Kazandınız", "Oyun Bitti\nTebrikler")
				sys.exit()
			print(x,y)
			#self.bu[x,y].grid_forget()
			self.bu[x,y]["state"] = "disabled"
			self.bu[x,y]["text"] = 0
			
			if int(str(x)+ str(y)) in self.sayi1:
				
				self.bu[x,y]["text"] = "X"
				self.bu[x,y]["bg"] = "red"
				messagebox.showerror("Kaybettiniz", "Oyun Bitti")
				Gui()



			else:
				if x == 0:
					if y==0:				
						if int(str(x+1)+ str(y)) in self.sayi1:
							va = self.bu[x,y]["text"] 
							self.var.set(int(va)+1)
							self.bu[x,y]["text"] = self.var.get()
							self.var.set(0)						
						if int(str(x)+ str(y+1)) in self.sayi1:
							va = self.bu[x,y]["text"]
							self.var.set(int(va)+1)
							self.bu[x,y]["text"] = self.var.get()
							self.var.set(0)
						if int(str(x+1)+ str(y+1)) in self.sayi1:
							va = self.bu[x,y]["text"]
							self.var.set(int(va)+1)
							self.bu[x,y]["text"] = self.var.get()
							self.var.set(0)

					elif y!=9:
						if int(str(x)+ str(y+1)) in self.sayi1:
							va = self.bu[x,y]["text"]
							self.var.set(int(va)+1)
							self.bu[x,y]["text"] = self.var.get()
							self.var.set(0)

						if int(str(x)+ str(y-1)) in self.sayi1:
							va = self.bu[x,y]["text"]
							self.var.set(int(va)+1)
							self.bu[x,y]["text"] = self.var.get()
							self.var.set(0)

						if int(str(x+1)+ str(y)) in self.sayi1:
							va = self.bu[x,y]["text"]
							self.var.set(int(va)+1)
							self.bu[x,y]["text"] = self.var.get()
							self.var.set(0)

						if int(str(x+1)+ str(y+1)) in self.sayi1:
							va = self.bu[x,y]["text"]
							self.var.set(int(va)+1)
							self.bu[x,y]["text"] = self.var.get()
							self.var.set(0)

						if int(str(x+1)+ str(y-1)) in self.sayi1:
							va = self.bu[x,y]["text"]
							self.var.set(int(va)+1)
							self.bu[x,y]["text"] = self.var.get()
							self.var.set(0)

				if x == 9:
					if y==0:
						if int(str(x)+ str(y+1)) in self.sayi1:
							va = self.bu[x,y]["text"] 
							self.var.set(int(va)+1)
							self.bu[x,y]["text"] = self.var.get()
							self.var.set(0)
						if int(str(x-1)+ str(y)) in self.sayi1:
							va = self.bu[x,y]["text"] 
							self.var.set(int(va)+1)
							self.bu[x,y]["text"] = self.var.get()
							self.var.set(0)
						if int(str(x-1)+ str(y+1)) in self.sayi1:
							va = self.bu[x,y]["text"] 
							self.var.set(int(va)+1)
							self.bu[x,y]["text"] = self.var.get()
							self.var.set(0)
					elif y !=9:
						if int(str(x)+ str(y+1)) in self.sayi1:
							va = self.bu[x,y]["text"] 
							self.var.set(int(va)+1)
							self.bu[x,y]["text"] = self.var.get()
							self.var.set(0)
						if int(str(x)+ str(y-1)) in self.sayi1:
							va = self.bu[x,y]["text"] 
							self.var.set(int(va)+1)
							self.bu[x,y]["text"] = self.var.get()
							self.var.set(0)
						if int(str(x-1)+ str(y)) in self.sayi1:
							va = self.bu[x,y]["text"] 
							self.var.set(int(va)+1)
							self.bu[x,y]["text"] = self.var.get()
							self.var.set(0)
						if int(str(x-1)+ str(y+1)) in self.sayi1:
							va = self.bu[x,y]["text"] 
							self.var.set(int(va)+1)
							self.bu[x,y]["text"] = self.var.get()
							self.var.set(0)
						if int(str(x-1)+ str(y-1)) in self.sayi1:
							va = self.bu[x,y]["text"] 
							self.var.set(int(va)+1)
							self.bu[x,y]["text"] = self.var.get()
							self.var.set(0)


			
				if x == 0:
					if y==9:
						if int(str(x)+ str(y-1)) in self.sayi1:
							va = self.bu[x,y]["text"] 
							self.var.set(int(va)+1)
							self.bu[x,y]["text"] = self.var.get()
							self.var.set(0)
						if int(str(x+1)+ str(y)) in self.sayi1:
							va = self.bu[x,y]["text"] 
							self.var.set(int(va)+1)
							self.bu[x,y]["text"] = self.var.get()
							self.var.set(0)
						if int(str(x+1)+ str(y-1)) in self.sayi1:
							va = self.bu[x,y]["text"] 
							self.var.set(int(va)+1)
							self.bu[x,y]["text"] = self.var.get()
							self.var.set(0)
					
				if x == 9:
					if y==9:
						if int(str(x)+ str(y-1)) in self.sayi1:
							va = self.bu[x,y]["text"] 
							self.var.set(int(va)+1)
							self.bu[x,y]["text"] = self.var.get()
							self.var.set(0)
						if int(str(x-1)+ str(y)) in self.sayi1:
							va = self.bu[x,y]["text"] 
							self.var.set(int(va)+1)
							self.bu[x,y]["text"] = self.var.get()
							self.var.set(0)
						if int(str(x-1)+ str(y-1)) in self.sayi1:
							va = self.bu[x,y]["text"] 
							self.var.set(int(va)+1)
							self.bu[x,y]["text"] = self.var.get()
							self.var.set(0)
				if y==0:
					if x!=0:
						if x!=9:
							if int(str(x)+ str(y+1)) in self.sayi1:
								va = self.bu[x,y]["text"]
								self.var.set(int(va)+1)
								self.bu[x,y]["text"] = self.var.get()
								self.var.set(0)
							if int(str(x+1)+ str(y)) in self.sayi1:
								va = self.bu[x,y]["text"]
								self.var.set(int(va)+1)
								self.bu[x,y]["text"] = self.var.get()
								self.var.set(0)
							if int(str(x-1)+ str(y)) in self.sayi1:
								va = self.bu[x,y]["text"]
								self.var.set(int(va)+1)
								self.bu[x,y]["text"] = self.var.get()
								self.var.set(0)
							if int(str(x-1)+ str(y+1)) in self.sayi1:
								va = self.bu[x,y]["text"]
								self.var.set(int(va)+1)
								self.bu[x,y]["text"] = self.var.get()
								self.var.set(0)
							if int(str(x+1)+ str(y+1)) in self.sayi1:
								va = self.bu[x,y]["text"]
								self.var.set(int(va)+1)
								self.bu[x,y]["text"] = self.var.get()
								self.var.set(0)
				if y==9:
					if x!=0:
						if x!=9:
							if int(str(x)+ str(y-1)) in self.sayi1:
								va = self.bu[x,y]["text"]
								self.var.set(int(va)+1)
								self.bu[x,y]["text"] = self.var.get()
								self.var.set(0)
							if int(str(x+1)+ str(y)) in self.sayi1:
								va = self.bu[x,y]["text"]
								self.var.set(int(va)+1)
								self.bu[x,y]["text"] = self.var.get()
								self.var.set(0)
							if int(str(x-1)+ str(y)) in self.sayi1:
								va = self.bu[x,y]["text"]
								self.var.set(int(va)+1)
								self.bu[x,y]["text"] = self.var.get()
								self.var.set(0)
							if int(str(x-1)+ str(y-1)) in self.sayi1:
								va = self.bu[x,y]["text"]
								self.var.set(int(va)+1)
								self.bu[x,y]["text"] = self.var.get()
								self.var.set(0)
							if int(str(x+1)+ str(y-1)) in self.sayi1:
								va = self.bu[x,y]["text"]
								self.var.set(int(va)+1)
								self.bu[x,y]["text"] = self.var.get()
								self.var.set(0)
				if x !=0:
					if x !=9:
						if y !=0:
							if y !=9:
								if int(str(x) + str(y - 1)) in self.sayi1:
									va = self.bu[x, y]["text"]
									self.var.set(int(va) + 1)
									self.bu[x, y]["text"] = self.var.get()
									self.var.set(0)
								if int(str(x) + str(y+1)) in self.sayi1:
									va = self.bu[x, y]["text"]
									self.var.set(int(va) + 1)
									self.bu[x, y]["text"] = self.var.get()
									self.var.set(0)
								if int(str(x - 1) + str(y)) in self.sayi1:
									va = self.bu[x, y]["text"]
									self.var.set(int(va) + 1)
									self.bu[x, y]["text"] = self.var.get()
									self.var.set(0)
								if int(str(x - 1) + str(y - 1)) in self.sayi1:
									va = self.bu[x, y]["text"]
									self.var.set(int(va) + 1)
									self.bu[x, y]["text"] = self.var.get()
									self.var.set(0)
								if int(str(x - 1) + str(y + 1)) in self.sayi1:
									va = self.bu[x, y]["text"]
									self.var.set(int(va) + 1)
									self.bu[x, y]["text"] = self.var.get()
									self.var.set(0)

								if int(str(x + 1) + str(y)) in self.sayi1:
									va = self.bu[x, y]["text"]
									self.var.set(int(va) + 1)
									self.bu[x, y]["text"] = self.var.get()
									self.var.set(0)

								if int(str(x + 1) + str(y + 1)) in self.sayi1:
									va = self.bu[x, y]["text"]
									self.var.set(int(va) + 1)
									self.bu[x, y]["text"] = self.var.get()
									self.var.set(0)

								if int(str(x + 1) + str(y - 1)) in self.sayi1:
									va = self.bu[x, y]["text"]
									self.var.set(int(va) + 1)
									self.bu[x, y]["text"] = self.var.get()
									self.var.set(0)


				






							


				
Gui()


root.mainloop()
