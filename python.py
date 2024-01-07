from tkinter import *
from tkinter import ttk
import requests




def data_get():
    city = city_name.get()
    api_key = "7b6bc17061bca8dd1a6c354d56d68f02"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    data = requests.get(url).json()
    W_label1.config(text=data["weather"][0]["main"])
    Wb_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(data["main"]["temp"] - 273.15))
    per_label1.config(text=data["main"]["pressure"])


win = Tk()
win.title("tushar patil")
win.config(bg="dark orange")
win.geometry('500x570')

name_label=Label(win,text="STORMSHIELD ",
                 font=("Algerian",35,"bold"))
name_label.place(x=25,y=50,height=50,width=450)

city_name = StringVar()
list_name=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com=ttk.Combobox(win,text="Tushar Weather App",values=list_name,
                 font=("Times New Roman",19,),textvariable=city_name)
com.place(x=25,y=120,height=50,width=450)


W_label=Label(win,text="Weather climate",
                 font=("Times New Roman",20))
W_label.place(x=25,y=260,height=50,width=210)
W_label1=Label(win,text="",
                 font=("Times New Roman",20))
W_label1.place(x=250,y=260,height=50,width=220)


Wb_label=Label(win,text=" description",
                 font=("Times New Roman",20))
Wb_label.place(x=25,y=330,height=50,width=210)
Wb_label1=Label(win,text="",
                 font=("Times New Roman",20))
Wb_label1.place(x=250,y=330,height=50,width=220)


temp_label=Label(win,text="Tempreture",
                 font=("Times New Roman",20))
temp_label.place(x=25,y=400,height=50,width=210)
temp_label1=Label(win,text="",
                 font=("Times New Roman",20))
temp_label1.place(x=250,y=400,height=50,width=240)


per_label=Label(win,text="pressure",
                 font=("Times New Roman",20))
per_label.place(x=25,y=470,height=50,width=210)
per_label1=Label(win,text="",
                 font=("Times New Roman",20))
per_label1.place(x=250,y=470,height=50,width=220)

done_button=Button(win,text="Done",
                 font=("Times New Roman",20,"bold"),command= data_get)
done_button.place(y=190,height=50,width=100,x=200)




win.mainloop()
