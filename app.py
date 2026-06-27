import tkinter as tk
from tkinter import messagebox
import ctypes
import math
import os

# Подключение необходимых библиотек Windows для работы с цветом
gdi32 = ctypes.windll.gdi32
user32 = ctypes.windll.user32

VALID_KEYS = {
    "WLYR-A7B9-XM24-991A": "DESKTOP-F87ISRV",  # Сюда впиши имя ПК друга
    "WLYR-K3R8-PL77-024B": "KERNELOS-PC",
    "WLYR-N5E2-QQ11-846C": "DESKTOP-12CVRNV",
    "WLYR-Z9X4-VV88-305D": "LAPTOP-123",
    "WLYR-M1O7-BB33-741E": "DESKTOP-COMP",
    "WLYR-L6P2-FF55-192F": "TEST-PC",
    "WLYR-C8V3-GG44-558G": "OFFICE-PC",
    "WLYR-U4Y9-HH22-663H": "PC-HOME",
    "WLYR-T2I5-SS99-884K": "GAMING-PC",
    "WLYR-Q9W1-JJ66-115M": "ADMIN-PC"
}

LICENSE_FILE = "license.txt"

class ScreenAdjuster:
    def __init__(self, root):
        self.root = root
        self.root.title("22 By Walexyyr ⚡ PREMIUM")
        self.root.geometry("500x750")
        self.root.configure(bg="#0B0B0F")
        self.root.attributes("-topmost", True)
        
        self.accent_purple = "#A066FF"
        self.accent_cyan = "#00E5FF"
        self.bg_card = "#161622"
        self.text_main = "#FFFFFF"
        self.text_muted = "#8F8F9F"
        
        # Получаем контекст устройства для главного экрана
        self.hdc = user32.GetDC(0)
        self.orig_ramp = (ctypes.c_ushort * 768)()
        gdi32.GetDeviceGammaRamp(self.hdc, ctypes.byref(self.orig_ramp))
        
        self.current_pc_name = os.environ.get('COMPUTERNAME', '').strip().upper()
        
        self.profiles = {
            1: {"vib": 100, "sat": 100, "gamma": 100},
            2: {"vib": 100, "sat": 100, "gamma": 100},
            3: {"vib": 100, "sat": 100, "gamma": 100}
        }
        
        # Горячие клавиши для поля ввода ключа
        self.root.bind_class("Entry", "<Control-v>", lambda e: e.widget.event_generate("<<Paste>>"))
        self.root.bind_class("Entry", "<Control-c>", lambda e: e.widget.event_generate("<<Copy>>"))
        self.root.bind_class("Entry", "<Control-a>", lambda e: e.widget.event_generate("<<SelectAll>>"))
        
        if self.check_existing_license():
            self.build_main_interface()
        else:
            self.show_auth_screen()

    def check_existing_license(self):
        if os.path.exists(LICENSE_FILE):
            try:
                with open(LICENSE_FILE, "r") as f:
                    saved_data = f.read().strip().split("|")
                    if len(saved_data) == 2:
                        saved_key, saved_pc = saved_data
                        if saved_pc.upper() == self.current_pc_name:
                            return True
            except:
                pass
        return False

    def show_auth_screen(self):
        self.auth_frame = tk.Frame(self.root, bg="#0B0B0F")
        self.auth_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        tk.Label(self.auth_frame, text="22 By Walexyyr", font=("Segoe UI", 22, "bold"), fg=self.accent_purple, bg="#0B0B0F").pack(pady=10)
        tk.Label(self.auth_frame, text="ТРЕБУЕТСЯ АКТИВАЦИЯ ПРЕМЕНУМА", font=("Segoe UI", 9, "bold"), fg=self.text_muted, bg="#0B0B0F").pack(pady=(0, 20))
        
        self.key_entry = tk.Entry(self.auth_frame, font=("Consolas", 12), bg=self.bg_card, fg=self.accent_cyan, insertbackground=self.accent_cyan, bd=0, width=25, justify="center")
        self.key_entry.pack(pady=10, ipady=8)
        self.key_entry.insert(0, "ВВЕДИТЕ КЛЮЧ СЮДА")
        
        self.key_entry.bind("<FocusIn>", lambda e: self.key_entry.delete(0, tk.END) if self.key_entry.get() == "ВВЕДИТЕ КЛЮЧ СЮДА" else None)

        btn_act = tk.Button(self.auth_frame, text="АКТИВИРОВАТЬ", font=("Segoe UI", 10, "bold"), command=self.check_activation, bg=self.accent_purple, fg="#0B0B0F", activebackground=self.accent_cyan, bd=0, cursor="hand2", padx=30, pady=8)
        btn_act.pack(pady=15)

    def check_activation(self):
        user_key = self.key_entry.get().strip()
        if user_key in VALID_KEYS:
            allowed_pc = VALID_KEYS[user_key].strip().upper()
            if allowed_pc == self.current_pc_name:
                try:
                    with open(LICENSE_FILE, "w") as f:
                        f.write(f"{user_key}|{self.current_pc_name}")
                except:
                    pass
                self.auth_frame.destroy()
                self.build_main_interface()
            else:
                msg = f"Ключ создан для ПК '{allowed_pc}'.\nВаш ПК: '{self.current_pc_name}'"
                messagebox.showerror("Ошибка доступа", msg)
        else:
            messagebox.showerror("Ошибка", "Неверный ключ активации!")

    def build_main_interface(self):
        header_frame = tk.Frame(self.root, bg="#0B0B0F")
        header_frame.pack(pady=15, fill=tk.X)
        tk.Label(header_frame, text="22 By Walexyyr", font=("Segoe UI", 18, "bold"), fg=self.accent_purple, bg="#0B0B0F").pack()
        tk.Label(header_frame, text="PREMIUM EDITION ⚡ ACTIVE", font=("Segoe UI", 8, "bold"), fg=self.accent_cyan, bg="#0B0B0F").pack()

        prof_frame = tk.LabelFrame(self.root, text=" СЛОТЫ ДЛЯ ПРОФИЛЕЙ ", font=("Segoe UI", 9, "bold"), fg=self.accent_cyan, bg=self.bg_card, bd=1, relief=tk.SOLID)
        prof_frame.pack(pady=10, padx=25, fill=tk.X, ipady=8)
        
        slots_container = tk.Frame(prof_frame, bg=self.bg_card)
        slots_container.pack(fill=tk.X, padx=5, pady=5)

        s1 = tk.Frame(slots_container, bg=self.bg_card)
        s1.pack(side=tk.LEFT, expand=True, padx=5)
        tk.Label(s1, text="Saturation 2022 WP", font=("Segoe UI", 8, "bold"), fg=self.text_main, bg=self.bg_card).pack(pady=2)
        tk.Button(s1, text="Save", font=("Segoe UI", 8, "bold"), bg="#282A36", fg=self.accent_purple, bd=0, command=lambda: self.save_profile(1), width=9, pady=3).pack(side=tk.LEFT, padx=1)
        tk.Button(s1, text="Load", font=("Segoe UI", 8, "bold"), bg=self.accent_purple, fg="#0B0B0F", bd=0, command=lambda: self.load_profile(1), width=9, pady=3).pack(side=tk.LEFT, padx=1)

        s2 = tk.Frame(slots_container, bg=self.bg_card)
        s2.pack(side=tk.LEFT, expand=True, padx=5)
        tk.Label(s2, text="Для ночи", font=("Segoe UI", 8, "bold"), fg=self.text_main, bg=self.bg_card).pack(pady=2)
        tk.Button(s2, text="Save", font=("Segoe UI", 8, "bold"), bg="#282A36", fg=self.accent_cyan, bd=0, command=lambda: self.save_profile(2), width=9, pady=3).pack(side=tk.LEFT, padx=1)
        tk.Button(s2, text="Load", font=("Segoe UI", 8, "bold"), bg=self.accent_cyan, fg="#0B0B0F", bd=0, command=lambda: self.load_profile(2), width=9, pady=3).pack(side=tk.LEFT, padx=1)

        s3 = tk.Frame(slots_container, bg=self.bg_card)
        s3.pack(side=tk.LEFT, expand=True, padx=5)
        tk.Label(s3, text="Ваш личный", font=("Segoe UI", 8, "bold"), fg=self.text_main, bg=self.bg_card).pack(pady=2)
        tk.Button(s3, text="Save", font=("Segoe UI", 8, "bold"), bg="#282A36", fg=self.accent_purple, bd=0, command=lambda: self.save_profile(3), width=9, pady=3).pack(side=tk.LEFT, padx=1)
        tk.Button(s3, text="Load", font=("Segoe UI", 8, "bold"), bg=self.accent_purple, fg="#0B0B0F", bd=0, command=lambda: self.load_profile(3), width=9, pady=3).pack(side=tk.LEFT, padx=1)

        sliders_frame = tk.LabelFrame(self.root, text=" ТОНКАЯ НАСТРОЙКА КАРТИНКИ ", font=("Segoe UI", 9, "bold"), fg=self.accent_purple, bg=self.bg_card, bd=1, relief=tk.SOLID)
        sliders_frame.pack(pady=10, padx=25, fill=tk.BOTH, expand=True, ipady=10)

        sc_style = {"bg": self.bg_card, "fg": self.text_main, "troughcolor": self.accent_purple, "highlightbackground": self.bg_card, "bd": 0, "orient": tk.HORIZONTAL, "length": 380}

        tk.Label(sliders_frame, text="Цифровая сочность (Vibrance)", font=("Segoe UI", 10, "bold"), fg=self.text_muted, bg=self.bg_card).pack(pady=(15, 2))
        self.vib_scale = tk.Scale(sliders_frame, from_=50, to=250, command=self.apply_changes, **sc_style)
        self.vib_scale.set(100)
        self.vib_scale.pack(pady=5)
        
        tk.Label(sliders_frame, text="Глубокая насыщенность (Saturation)", font=("Segoe UI", 10, "bold"), fg=self.text_muted, bg=self.bg_card).pack(pady=(15, 2))
        self.sat_scale = tk.Scale(sliders_frame, from_=50, to=250, command=self.apply_changes, **sc_style)
        self.sat_scale.set(100)
        self.sat_scale.pack(pady=5)
        
        tk.Label(sliders_frame, text="Гамма экрана (Gamma)", font=("Segoe UI", 10, "bold"), fg=self.text_muted, bg=self.bg_card).pack(pady=(15, 2))
        self.gamma_scale = tk.Scale(sliders_frame, from_=30, to=220, command=self.apply_changes, **sc_style)
        self.gamma_scale.set(100)
        self.gamma_scale.pack(pady=5)
        
        self.btn_reset = tk.Button(self.root, text="СБРОСИТЬ ВСЕ НАСТРОЙКИ", font=("Segoe UI", 10, "bold"), command=self.reset_channels, bg="#FF5252", fg="#FFFFFF", activebackground="#D32F2F", bd=0, padx=30, pady=10, cursor="hand2")
        self.btn_reset.pack(pady=20)
        
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def save_profile(self, slot_id):
        names = {1: "Saturation 2022 WP", 2: "Для ночи", 3: "Ваш личный"}
        self.profiles[slot_id]["vib"] = self.vib_scale.get()
        self.profiles[slot_id]["sat"] = self.sat_scale.get()
        self.profiles[slot_id]["gamma"] = self.gamma_scale.get()
        messagebox.showinfo("Успех", f"Сохранено в {names[slot_id]}!")

    def load_profile(self, slot_id):
        p = self.profiles[slot_id]
        self.vib_scale.set(p["vib"])
        self.sat_scale.set(p["sat"])
        self.gamma_scale.set(p["gamma"])
        self.apply_changes()

    def apply_changes(self, *args):
        if not hasattr(self, 'vib_scale'): return 
        
        vib = self.vib_scale.get() / 100.0
        sat = self.sat_scale.get() / 100.0
        gamma_val = self.gamma_scale.get() / 100.0
        
        ramp = (ctypes.c_ushort * 768)()
        
        for i in range(256):
            val = i / 255.0
            g_v = 0.1 if gamma_val == 0 else gamma_val
            val_gamma = math.pow(val, 1.0 / g_v)
            
            if vib >= 1.0:
                r_f = 1.0 + (vib - 1.0) * 0.35
                g_f = 1.0 + (vib - 1.0) * 0.20
                b_f = 1.0 + (vib - 1.0) * 0.40
                
                r_val = val_gamma * r_f if val_gamma > 0.15 else val_gamma
                g_val = val_gamma * g_f if val_gamma > 0.15 else val_gamma
                b_val = val_gamma * b_f if val_gamma > 0.15 else val_gamma
                
                r_val = min(val_gamma, r_val) if val_gamma > 0.85 else r_val
                g_val = min(val_gamma, g_val) if val_gamma > 0.85 else g_val
                b_val = min(val_gamma, b_val) if val_gamma > 0.85 else b_val
            else:
                div = vib if vib > 0 else 0.1
                r_val = g_val = b_val = math.pow(val_gamma, 1.0 / div)

            if sat != 1.0:
                div_s = sat if sat > 0 else 0.1
                r_val = math.pow(max(0.0, min(1.0, r_val)), 1.0 / div_s)
                g_val = math.pow(max(0.0, min(1.0, g_val)), 1.0 / div_s)
                b_val = math.pow(max(0.0, min(1.0, b_val)), 1.0 / div_s)

            ramp[i] = int(max(0, min(65535, r_val * 65535)))
            ramp[256 + i] = int(max(0, min(65535, g_val * 65535)))
            ramp[512 + i] = int(max(0, min(65535, b_val * 65535)))
            
        # Обновленный вызов, форсирующий системное применение цвета
        gdi32.SetDeviceGammaRamp(self.hdc, ctypes.byref(ramp))
        # Принудительное обновление рабочего стола Windows (устраняет игнорирование драйверами)
        user32.RedrawWindow(0, None, None, 0x0100 | 0x0001 | 0x0004)

    def reset_channels(self):
        self.vib_scale.set(100)
        self.sat_scale.set(100)
        self.gamma_scale.set(100)
        gdi32.SetDeviceGammaRamp(self.hdc, ctypes.byref(self.orig_ramp))
        user32.RedrawWindow(0, None, None, 0x0100 | 0x0001 | 0x0004)

    def on_close(self):
        gdi32.SetDeviceGammaRamp(self.hdc, ctypes.byref(self.orig_ramp))
        user32.RedrawWindow(0, None, None, 0x0100 | 0x0001 | 0x0004)
        user32.ReleaseDC(0, self.hdc)
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ScreenAdjuster(root)
    root.mainloop()