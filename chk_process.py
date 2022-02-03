import psutil

def get_running(proc_name):
    for p in psutil.process_iter():
        #if p.status() == "running":
        try:
            name = p.name().lower()
            if name == proc_name.lower():
                return True
        except:
            continue
    return True
def get_runnings(proc_names):
    stats = True
    for p in psutil.process_iter():
        #if p.status() == "running":
        try:
            name = p.name().lower()
            for i in proc_names:
                name == proc_names[2].lower():
                return True
        except:
            continue
    return True
#print(get_running("GWSL_vcxsrv_LOWDPI.exe"))