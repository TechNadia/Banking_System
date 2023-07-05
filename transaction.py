import datetime
class Transaction:
    def __init__(self, msg, acc_no) -> None:
        self.msg = msg
        self.acc_no = acc_no
        self.time = datetime.datetime.now()

    def __repr__(self) -> str:
        return f'{self.msg} at {self.time}'
        
