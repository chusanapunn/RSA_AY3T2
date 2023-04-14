import tkinter as tk
import math
import pybase64 
import NewLogic as NL

def GUI():
    def display(): 

        #get p,q input
        p = myentry1.get()
        q = myentry2.get()

        #convert input to int
        p = int(p)
        q = int(q)

        #check if it is prime
        check_p = NL.prime_check(p)
        check_q = NL.prime_check(q)
        #If not
        if((check_p==False)or(check_q==False)):
           quit()


        window =tk.Toplevel(root)
        # find n RSA modulus
        n=NL.n_value(p,q)
        # Eulers Toitent Function 
        r=NL.r_value(p,q)
        print(n,r)
    #Creating Window
    root = tk.Tk()
    


    #Window Size 
    root.geometry("600x600+50+50")

    #Window Title
    root.title("RSA GUI")

    #Main Label 
    label = tk.Label(root, text = "CryptoCipher" , font = ("Ubuntu", 30))
    label.pack(padx = 20, pady = 20)


    #Frame 
    my_frame = tk.Frame(root)
    my_frame.pack(pady = 20)



    #Entry Labels 
    enc_label = tk.Label(root, text = "Please Enter Prime Values for N and Q", font = ("Helvetica",10))
    enc_label.pack(padx = 10, pady = 10)
        
    #Entry 
    myentry1 = tk.Entry(root)
    myentry2 = tk.Entry(root)

    myentry1 = tk.Entry(root,font = ("Helvetica", 18), width = 15)
    myentry1.pack(pady = 10)

    myentry2 = tk.Entry(root,font = ("Helvetica", 18), width = 15)
    myentry2.pack(pady = 10)

       
    #Submit Buttons 
    enc_button = tk.Button(root, text="Submit", command=display)
    enc_button.pack(side = "bottom")
    root.mainloop()





GUI()