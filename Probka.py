import tkinter as tk
from tkinter import messagebox, Toplevel
import sqlite3


# Main application class
class EnergyMonitorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Energy Monitor")
        self.root.geometry("600x400")

        # Menu
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)

        # Adding a file menu
        file_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Exit", command=self.root.quit)

        # Dashboard frame
        self.dashboard_frame = tk.Frame(self.root)
        self.dashboard_frame.pack(fill=tk.BOTH, expand=True)

        # Setup UI components
        self.setup_ui()

    def setup_ui(self):
        # Dashboard UI
        tk.Label(self.dashboard_frame, text="Main Dashboard", font=('Arial', 16)).pack(pady=20)

        # Buttons for different functionalities
        tk.Button(self.dashboard_frame, text="Device Management", command=self.manage_devices).pack(pady=10)
        tk.Button(self.dashboard_frame, text="Energy Consumption Analysis",
                  command=self.analyze_energy_consumption).pack(pady=10)
        tk.Button(self.dashboard_frame, text="Notifications and Alarms", command=self.notifications_alarms).pack(
            pady=10)
        tk.Button(self.dashboard_frame, text="Settings", command=self.settings).pack(pady=10)

    def manage_devices(self):
        messagebox.showinfo("Device Management", "Manage your devices here.")

    def analyze_energy_consumption(self):
        messagebox.showinfo("Energy Consumption Analysis", "Analyze your energy consumption patterns here.")

    def notifications_alarms(self):
        # Create a new window
        new_window = tk.Toplevel(self.root)
        new_window.title("Notifications and Alarms")
        new_window.geometry("400x200")

        # Display a message
        msg = "Otrzymuj powiadomienia w czasie rzeczywistym o awariach urządzeń lub nieprawidłowych wzorcach zużycia energii."
        tk.Label(new_window, text=msg, wraplength=380).pack(pady=20)

        # Optionally, fetch data from the database and display
        self.fetch_and_display_notifications(new_window)

    def fetch_and_display_notifications(self, window):
        # Connect to your database
        conn = sqlite3.connect('your_database.db')  # Adjust as needed
        cursor = conn.cursor()

        # Execute a query to fetch notifications
        cursor.execute("SELECT message FROM notifications WHERE status = 'unread'")
        notifications = cursor.fetchall()

        # Display notifications
        if notifications:
            for notification in notifications:
                tk.Label(window, text=notification[0], wraplength=380).pack()
        else:
            tk.Label(window, text="Brak nowych powiadomień.", wraplength=380).pack()

        # Close the database connection
        conn.close()
    def settings(self):
        messagebox.showinfo("Settings", "Configure your application settings here.")


# Run the application
root = tk.Tk()
app = EnergyMonitorApp(root)
root.mainloop()
