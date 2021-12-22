class Minix1:
    def get_header(self):
        print("runing Minix1.get_headeer")
        ctx = super(Minix1, self).get_header()
        print("after call super().get_header in Minix1")
        ctx.append("minix1")
        return ctx

class Minix2:
    def get_header(self):
        print("runing Minix2.get_headeer")
        ctx = super(Minix2, self).get_header()
        print("after call super().get_header in Minix2")
        ctx.append("minix2")
        return ctx

class Header:
    header = []
    def get_header(self):
        print("runing Header.get_headeer")
        return self.header if self.header else []

class Final(Minix1, Minix2, Header):
    def get_header(self):
        return super(Final, self).get_header()


f = Final()
print(f.get_header())