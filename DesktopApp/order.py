class MedicineOptions:
    def __init__(self):
        self.__medicines = ["Choose medicine:", "Analgin", "Elaksa piko", "Espumizan", "Nurofen", "Reparil gel"]
        self.__quantity = ["Choose number:", "1", "2", "3"]

    @property
    def get_medicine_options(self):
        return self.__medicines

    @property
    def get_quantity_options(self):
        return self.__quantity

    # def add(self, index, medicine):
    #     self.__medicines.insert(index, medicine)
    #
    # def remove(self, medicine):
    #     self.__medicines.remove(medicine)


class MedicineList:
    def __init__(self):
        self.__arr = []
        self.__size = 0

    @property
    def get_list(self):
        return self.__arr

    @property
    def get_size(self):
        return self.__size

    def clear(self):
        self.__arr.clear()
        self.__size = 0

    def add(self, data):
        self.__arr.append(data)

    def inc_size(self):
        self.__size += 1

    def dec_size(self):
        self.__size -= 1

    @staticmethod
    def encode(data, meds):
        el_idx = 1
        while el_idx < len(meds) and meds[el_idx] != data:
            el_idx += 1

        return chr(ord('a') + el_idx - 1)

    @staticmethod
    def decode(data, meds):
        meds.pop(0)
        return meds[ord(data) - ord('a')]


class DeviceList:
    def __init__(self):
        self.__arr = []

    def save(self, device, baud):
        self.__arr.clear()
        self.__arr.append(str(device))
        self.__arr.append(str(baud))

    def is_saved(self):
        if len(self.__arr) != 0:
            return 1

        return 0

    @property
    def get_list(self):
        return self.__arr
