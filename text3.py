# class Itarator:
#     def __init__(self,start,stop):
#         self.start=start+1
#         self.stop=stop
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.start-=1
#
#         if self.start>self.stop:
#             return self.start
#         raise StopIteration
#
#
# for elem in Itarator(10,-10):
#     print(elem)


# def try_generator(y):
#     n=y
#     yield n**2
#
#
# for i in range(1,11):
#     print(next(try_generator(i)))


# my_generator=(n**5 for n in range(100) if n//2)
# for i in my_generator:
#     print(i)
