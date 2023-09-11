import platform

def is_windows() -> bool:
    if platform.system() == "Windows":
        if platform.release() != "10":
            print("This might not be Windows 10/11. Proceed with caution.")
            
        return True
    
    return False

def is_ubuntu() -> bool:
    pass
    # TODO: platform module is deprecated for this task, use the distro module instead or sys.package
    
if __name__ == "__main__":
    is_windows()