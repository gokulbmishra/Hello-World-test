# call_hello_gok.py
import hello_world  # Import the hello_world module

def call_main():
    """Wrapper function to call main from hello_world.py"""
    hello_world.main()

if __name__ == "__main__":
    call_main()
