import argparse

def main():
    parser = argparse.ArgumentParser(description="My CLI Tool")
    parser.add_argument("name", help="The person's name")
    
    args = parser.parse_args()
    
    greeting = f"Hello, {args.name}!"
    print(greeting)

if __name__ == "__main__":
    main()