from core import *

def main():
    transactions = get_eleitores()
    merkletree = Tree(transactions)
    print("Root Hash.....: " + merkletree.root.hash)

# entry point
if __name__ == "__main__":
    main()
