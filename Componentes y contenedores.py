import tkinter as tk
from tkinter import ttk
from tkinter import messagebox



class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")

        # Crear el contenedor principal
        self.main_container = ttk.Frame(self.root, padding="10")
        self.main_container.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Crear la lista de eventos
        self.event_list = ttk.Treeview(self.main_container, columns=("Date", "Time", "Description"), show="headings")
        self.event_list.heading("Date", text="Date")
        self.event_list.heading("Time", text="Time")
        self.event_list.heading("Description", text="Description")
        self.event_list.grid(row=0, column=0, padx=10, pady=10, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Crear campos de entrada
        self.date_entry = ttk.Entry(self.main_container)
        self.time_entry = ttk.Entry(self.main_container)
        self.desc_entry = ttk.Entry(self.main_container)

        # Crear etiquetas
        ttk.Label(self.main_container, text="Date:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.date_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)
        ttk.Label(self.main_container, text="Time:").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.time_entry.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)
        ttk.Label(self.main_container, text="Description:").grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
        self.desc_entry.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)

        # Crear botones
        ttk.Button(self.main_container, text="Agregar Evento", command=self.add_event).grid(row=4, column=0, padx=5,
                                                                                            pady=5, sticky=tk.W)
        ttk.Button(self.main_container, text="Eliminar Evento Seleccionado", command=self.delete_selected_event).grid(
            row=4, column=1, padx=5, pady=5, sticky=tk.W)
        ttk.Button(self.main_container, text="Salir", command=self.root.quit).grid(row=4, column=2, padx=5, pady=5,
                                                                                   sticky=tk.W)

    def add_event(self):
        date = self.date_entry.get()
        time = self.time_entry.get()
        description = self.desc_entry.get()

        if date and time and description:
            self.event_list.insert("", "end", values=(date, time, description))
            self.date_entry.delete(0, tk.END)
            self.time_entry.delete(0, tk.END)
            self.desc_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Campos Incompletos", "Por favor, complete todos los campos.")

    def delete_selected_event(self):
        selected_item = self.event_list.selection()
        if selected_item:
            confirmed = messagebox.askyesno("Eliminar Evento",
                                            "¿Está seguro que desea eliminar el evento seleccionado?")
            if confirmed:
                self.event_list.delete(selected_item)
        else:
            messagebox.showwarning("Evento no seleccionado", "Por favor, seleccione un evento para eliminar.")


def main():
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
