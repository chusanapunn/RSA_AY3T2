import tkinter as tk
import math
import pybase64 
import NewLogic as NL

def GUI():
    def display(): 
        global d_name
        # result button function
        # display m message
        # If encryption, we want readable message
        def result():
            m=myEntry3.get()
            if (d_name=="Encryption"):
                mLabel=tk.Label(Detailwindow, text = "Your messages to encrpyt is \"" + str(m)+"\"", font = ("Ubuntu", 12))
                mLabel.pack(padx=4,pady=4)
                enc_msg=NL.encrypt(public,m)
                resLabel=tk.Label(Detailwindow, text = "Your encrpyted is " + str(enc_msg), font = ("Ubuntu", 12))
                resLabel.pack(padx=4,pady=4)
                resEntry=tk.Entry(Detailwindow,font = ("Ubuntu", 12))
                resEntry.pack(padx=4,pady=4)
                resEntry.insert(0,(str(enc_msg)).strip("[]"))
            # If decryption, we want secret encrpted message
            elif(d_name=="Decryption"):
                mLabel=tk.Label(Detailwindow, text = "Your encrypted messages to decrpyt is \"" + str(m)+"\"", font = ("Ubuntu", 12))
                mLabel.pack(padx=4,pady=4)
                dec_msg=NL.decrypt(private,m)
                resLabel=tk.Label(Detailwindow, text = "Your encrpyted is " + str(dec_msg), font = ("Ubuntu", 12))
                resLabel.pack(padx=4,pady=4)
                resEntry=tk.Entry(Detailwindow,font = ("Ubuntu", 12))
                resEntry.pack(padx=4,pady=4)
                resEntry.insert(0,str(dec_msg).strip("[]"))
            
        # get p,q input
        p = myentry1.get()
        q = myentry2.get()
        # convert input to int
        
        p = int(p)
        q = int(q)
        
        # check if it is prime
        check_p = NL.prime_check(p)
        check_q = NL.prime_check(q)

        # If not prime
        if((check_p==False)or(check_q==False)):
           quit()
        
        Detailwindow =tk.Toplevel(root)
        Detailwindow.title(d_name + " details")
        Detailwindow.geometry("600x800+50+50")

        # display Function title
        DetailMainLabel = tk.Label(Detailwindow, text = d_name , font = ("Ubuntu", 14))
        DetailMainLabel.pack(padx = 20, pady = 20)
        # find n RSA modulus
        n=NL.n_value(p,q)
        # Eulers Toitent Function 
        r=NL.r_value(p,q)

        # display n and r
        nvalLabel = tk.Label(Detailwindow, text = "[n] RSA modulus value is " + str(n) , font = ("Ubuntu", 12))
        nvalLabel.pack(padx = 4, pady = 4)
        rvalLabel = tk.Label(Detailwindow, text = "[r] Eulers Toitent value is " + str(r) , font = ("Ubuntu", 12))
        rvalLabel.pack(padx = 4, pady = 4)
    
        
        # find e value
        e=NL.value_calculation(r)
        # display e 
        evalLabel = tk.Label(Detailwindow, text = "[e] value is " + str(e) , font = ("Ubuntu", 12))
        evalLabel.pack(padx = 4, pady = 4)

        # display euclid algorithm calculation (Terminal)
        eu=NL.eugcd(e,r)
        euLabel=tk.Label(Detailwindow, text = "Euclid Algorithm calculation", font = ("Ubuntu", 12))
        euLabel.pack(padx = 4, pady = 4)

        # display d from multiplicative inverse & Euclid extended algorithm calculation (Terminal)
        eeLabel=tk.Label(Detailwindow, text = "Extended Euclidean Algorithm calculation", font = ("Ubuntu", 12))
        eeLabel.pack(padx = 4, pady = 4)
        d = NL.mult_inv(e,r)
        dLabel=tk.Label(Detailwindow, text = "[d] value is " + str(d) , font = ("Ubuntu", 12))
        dLabel.pack(padx = 4, pady = 4)

        # display pub/pri key from calculation above
        public = (e,n)
        private = (d,n)
        keyLabel=tk.Label(Detailwindow, text = "Private key is " + str(private)+", Public key is " + str(public) , font = ("Ubuntu", 12))
        keyLabel.pack(padx=4,pady=4)

        # get message/encrypted message input
        entry3Label=tk.Label(Detailwindow, text = "Enter your Messages/Encrpted messages", font = ("Ubuntu", 12))
        entry3Label.pack(padx = 4, pady = 4)
        myEntry3 = tk.Entry(Detailwindow,font = ("Helvetica", 18), width = 15)
        myEntry3.pack(pady = 10)
        # message submit button
        submit_button = tk.Button(Detailwindow, text="Submit", command=result, bg="#b7ded2", font = ("Helvetica",14))
        submit_button.pack(side="bottom",padx = 4,pady=4,fill="x")
        
        
        
    # Click on Encryption Button    
    
    def enc():
        global d_name
        d_name="Encryption"
        enc_button.configure(bg="#620606")
        dec_button.configure(bg="#90d2d8")
    # Click on Decryption Button    
    def dec():
        global d_name
        d_name="Decryption" 
        dec_button.configure(bg="#416269")
        enc_button.configure(bg="#f6a6b2")
    #Creating Window
    root = tk.Tk()
    
    #Window Size 
    root.geometry("500x500+50+50")

    #Window Title
    root.title("RSA Main GUI")

    #Main Label 
    Mainlabel = tk.Label(root, text = "CryptoCipher" , font = ("Ubuntu", 30))
    Mainlabel.pack(padx = 20, pady = 20)


    #Entry Labels 
    enc_label = tk.Label(root, text = "Please Enter Prime Values for P and Q", font = ("Helvetica",10))
    enc_label.pack(padx = 10, pady = 10)
        
    #Entry 
    myentry1 = tk.Entry(root)
    myentry2 = tk.Entry(root)

    inpp_label = tk.Label(root, text = "Input P" , font = ("Ubuntu", 14))
    inpp_label.pack(padx=4,pady=4)
    myentry1 = tk.Entry(root,font = ("Helvetica", 18), width = 15)
    myentry1.pack(pady = 10)

    inpq_label = tk.Label(root, text = "Input Q" , font = ("Ubuntu", 14))
    inpq_label.pack(padx=4,pady=4)
    myentry2 = tk.Entry(root,font = ("Helvetica", 18), width = 15)
    myentry2.pack(pady = 10)

    ende_frame=tk.Frame(root)
    sub_frame=tk.Frame(root)
    ende_frame.pack(side="top",fill="x")
    sub_frame.pack(side="bottom",fill="x")
       
    #Submit Buttons 
    enc_button = tk.Button(ende_frame, text="Encryption", command=enc, bg="#f6a6b2",height=2,width=12, font = ("Helvetica",14))
    enc_button.pack(side="left",padx = 20,pady=8)
    dec_button = tk.Button(ende_frame, text="Decryption", command=dec, bg="#90d2d8",height=2,width=12, font = ("Helvetica",14))
    dec_button.pack(side="right",padx = 20,pady=8)
    submit_button = tk.Button(sub_frame, text="Submit", command=display, bg="#b7ded2",height=2,width=24, font = ("Helvetica",14))
    submit_button.pack(side="bottom",padx = 24,pady=8,fill="x")
    root.mainloop()

GUI()