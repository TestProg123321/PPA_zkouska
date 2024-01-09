class Alpha:
    def __init__(self, data):
        self.data = data

class Beta:
    def __init__(self, d1, d2):
        self.d1 = d1
        self.d2 = d2

    def push(self):
        data = self.d1
        m = Alpha(data.data)
        print(data.data) #breakpoint
        return m
    

def main():
    main = Beta(Alpha([1,2]), Alpha([1, 3]))
    main.push()

main()
