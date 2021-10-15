def main():
    reader = [1, 2, 3, 4, 5]
    new_reader = map(lambda x: float(x), reader)
    print(list(reader))
    print(list(new_reader))
 

if __name__ == "__main__":
    main()
