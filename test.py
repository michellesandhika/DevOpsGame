from backend import Backend

if __name__ == "__main__":
    backend = Backend()
    backend.process_selected(1)
    backend.process_selected(2)
    backend.process_selected(3)

    backend.show_error()
    print([i.fail_rate for i in backend.featureSelected])
    stat = backend.solution_picked(0)
    while stat == False:
        stat = backend.solution_picked(0)
    print([i.fail_rate for i in backend.featureSelected])

