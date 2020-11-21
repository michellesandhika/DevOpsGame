from backend import Backend

if __name__ == "__main__":
    backend = Backend()
    backend.process_selected(1)
    backend.process_selected(2)
    backend.process_selected(3)

    print(backend.show_error())