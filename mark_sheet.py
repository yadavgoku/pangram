
class MarkSheet:
    def __init__(self):
        self.stu_data = [['akil' ,80] ,['arun' ,50] ,['john' ,90]]
    def get_marks(self):
        stu_name = input('Enter the name : ')

        for data in self.stu_data:

            if stu_name in data:
                print(data[0] ,':', data[1])
                flag = input("Do you want to remove the data ? Y/N : ")

                if flag is 'Y':
                    self.stu_data.remove(data)
                print(self.stu_data)

    def mark_list(self):
        print('70 Above')

        for data in self.stu_data:
            if  data[1] >= 70:

                print(data[0], ':', data[1])

    def descending_order(self):
        new_list = []
        c = 0
        for data in self.stu_data:
            new_list.append(data[1])
        s = set(new_list)

        print(s)



#MarkSheet().get_marks()
#MarkSheet().mark_list()
MarkSheet().descending_order()
