import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry  # Necesario para el DatePicker

# -------------------------------
# Clase principal de la aplicación
# -------------------------------
class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("600x400")

        # Frame principal para organizar la interfaz
        frame_principal = tk.Frame(self.root)
        frame_principal.pack(fill="both", expand=True, padx=10, pady=10)

        # -------------------------------
        # Sección: TreeView (lista de eventos)
        # -------------------------------
        frame_lista = tk.LabelFrame(frame_principal, text="Eventos Programados")
        frame_lista.pack(fill="both", expand=True, padx=5, pady=5)

        self.tree = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack(fill="both", expand=True)

        # -------------------------------
        # Sección: Entrada de datos
        # -------------------------------
        frame_entrada = tk.LabelFrame(frame_principal, text="Agregar Nuevo Evento")
        frame_entrada.pack(fill="x", padx=5, pady=5)

        tk.Label(frame_entrada, text="Fecha:").grid(row=0, column=0, padx=5, pady=5)
        self.fecha_entry = DateEntry(frame_entrada, width=12, background="darkblue", foreground="white", borderwidth=2)
        self.fecha_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_entrada, text="Hora:").grid(row=0, column=2, padx=5, pady=5)
        self.hora_entry = tk.Entry(frame_entrada)
        self.hora_entry.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(frame_entrada, text="Descripción:").grid(row=1, column=0, padx=5, pady=5)
        self.desc_entry = tk.Entry(frame_entrada, width=40)
        self.desc_entry.grid(row=1, column=1, columnspan=3, padx=5, pady=5)

        # -------------------------------
        # Sección: Botones de acción
        # -------------------------------
        frame_botones = tk.Frame(frame_principal)
        frame_botones.pack(fill="x", padx=5, pady=5)

        btn_agregar = tk.Button(frame_botones, text="Agregar Evento", command=self.agregar_evento)
        btn_agregar.pack(side="left", padx=5)

        btn_eliminar = tk.Button(frame_botones, text="Eliminar Evento Seleccionado", command=self.eliminar_evento)
        btn_eliminar.pack(side="left", padx=5)

        btn_salir = tk.Button(frame_botones, text="Salir", command=self.root.quit)
        btn_salir.pack(side="right", padx=5)

    # -------------------------------
    # Funciones de manejo de eventos
    # -------------------------------
    def agregar_evento(self):
        fecha = self.fecha_entry.get()
        hora = self.hora_entry.get()
        descripcion = self.desc_entry.get()

        if not hora or not descripcion:
            messagebox.showwarning("Campos Vacíos", "Por favor complete todos los campos.")
            return

        self.tree.insert("", "end", values=(fecha, hora, descripcion))
        self.hora_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)

    def eliminar_evento(self):
        seleccionado = self.tree.selection()
        if not seleccionado:
            messagebox.showwarning("Selección Vacía", "Debe seleccionar un evento para eliminar.")
            return

        confirmacion = messagebox.askyesno("Confirmar Eliminación", "¿Está seguro de eliminar el evento seleccionado?")
        if confirmacion:
            self.tree.delete(seleccionado)

# -------------------------------
# Ejecución de la aplicación
# -------------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()