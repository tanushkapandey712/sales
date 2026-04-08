import numpy as np
import tkinter as tk
arr=np.array([[1200,1500,1700,1600],
[1000, 1100, 1050, 1150],
[2000, 2100, 1900, 2200],
[800,  900,  950,  1000]])
a=arr.sum()
def sale():
    result_label.config(text=f"Total sales:{a}\n")
def trending():
    trend=arr.argmax(axis=0)
    text = ""
    for i in range(0,4):
      text+=f"trending product on day {i+1}:product {trend[i]}\n"
      result_label.config(text=text)
def low():
    least=arr.sum(axis=1)
    less=least.argmin()
    text = ""
    text+=f"least selling product: product {less+1}\n"
    result_label.config(text=text)

def bt():
    best=(arr.sum(axis=1)).argmax()
    text = ""
    text+=f"best selling product: product {best+1}\n"
    result_label.config(text=text)
l=np.array([sale,trending,bt,low])
p=np.array(["Total sales","Trending Products","Best Selling","Least Selling"])
root=tk.Tk()
for i in range(0,4):
    button=tk.Button(root, text=p[i], command=l[i],bg='black',fg='white',font=("Arial,16"),padx=10,pady=5)
    button.pack(pady=20)
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=15)

root.mainloop()