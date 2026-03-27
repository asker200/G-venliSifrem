import customtkinter as ctk
import random
import string
import os
from tkinter import messagebox

ctk.set_appearance_mode("pink")
ctk.set_default_color_theme("blue")

class SifreUygulamasi(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Güvenilir Sifrem")
        self.geometry("400x500")

        self.label = ctk.CTkLabel(self, text="Güvenli Şifre Oluştur", font=("Arial", 20, "bold"))
        self.label.pack(pady=20)

        self.entry_platform = ctk.CTkEntry(self, placeholder_text="Ne şifresi? (örn: Instagram)", width=300)
        self.entry_platform.pack(pady=10)

        self.slider_label = ctk.CTkLabel(self, text="Şifre Uzunluğu: 12")
        self.slider_label.pack()
        
        self.slider = ctk.CTkSlider(self, from_=6, to=32, number_of_steps=26, command=self.slider_event)
        self.slider.set(12)
        self.slider.pack(pady=10)

        self.result_entry = ctk.CTkEntry(self, width=300, justify="center", fg_color="transparent", border_color="#1f538d")
        self.result_entry.pack(pady=20)

        self.btn_generate = ctk.CTkButton(self, text="Şifre Üret", command=self.generate_password)
        self.btn_generate.pack(pady=5)

        self.btn_copy = ctk.CTkButton(self, text="Kopyala", fg_color="#5D3FD3", hover_color="#4832a8", command=self.copy_to_clipboard)
        self.btn_copy.pack(pady=5)

        self.btn_save = ctk.CTkButton(self, text="Masaüstüne Kaydet", fg_color="green", hover_color="#228B22", command=self.save_password)
        self.btn_save.pack(pady=5)

    def slider_event(self, value):
        self.slider_label.configure(text=f"Şifre Uzunluğu: {int(value)}")

    def generate_password(self):
        length = int(self.slider.get())
        chars = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choice(chars) for _ in range(length))
        
        self.result_entry.delete(0, "end")
        self.result_entry.insert(0, password)

    def copy_to_clipboard(self):
        password = self.result_entry.get()
        if password:
            self.clipboard_clear()
            self.clipboard_append(password)
            messagebox.showinfo("Başarılı", "Şifre panoya kopyalandı!")
        else:
            messagebox.showwarning("Hata", "Önce bir şifre üretmelisiniz!")

    def save_password(self):
        platform = self.entry_platform.get()
        password = self.result_entry.get()

        if not platform or not password:
            messagebox.showwarning("Hata", "Lütfen bir platform adı girin ve şifre üretin!")
            return

        desktop = os.path.join(os.path.expanduser("~"), "Desktop")
        file_path = os.path.join(desktop, "sifrelerim.txt")

        try:
            with open(file_path, "a", encoding="utf-8") as f:
                f.write(f"Platform: {platform}\nŞifre: {password}\n{'-'*20}\n")
            messagebox.showinfo("Başarılı", "Şifre masaüstündeki 'sifrelerim.txt' dosyasına eklendi!")
        except Exception as e:
            messagebox.showerror("Hata", f"Kaydedilirken bir hata oluştu: {e}")

if __name__ == "__main__":
    app = SifreUygulamasi()
    app.mainloop()
