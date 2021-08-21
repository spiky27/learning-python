#
# Example file for working with classes
#

class c1():
    def m1(self):
        print("c1::m1")

    def m2(self, s1):
        print("c1::m2 " + s1)

    def m3(self, s1):
        print("c1::m3 " + s1)

class c2(c1):
    def m1(self):
        c1.m1(self)
        print("c2::m1")

    def m2(self, s1):
        c1.m2(self,s1)
        print("c2::m2 " + s1)

    def m4(self, s1):
        print("c2::m4 " + s1)

def main():
   # c = c1()
   # c.m1()
   # c.m2("test")

    cc = c2()
    cc.m1()
    cc.m2("test")
    cc.m3("3rd func")
    cc.m4("4th func")


if __name__ == "__main__":
    main()
