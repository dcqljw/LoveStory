import time


class IdGenerator:
    def __init__(self, datacenter_id=1122, worker_id=1122):
        self.datacenter_id = datacenter_id
        self.worker_id = worker_id
        self.sequence = 0
        self.last_timestamp = -1

    def generate_id(self):
        timestamp = int(time.time() * 1000)
        if timestamp < self.last_timestamp:
            raise Exception("Clock moved backwards. Refusing to generate id for {} milliseconds".format(
                self.last_timestamp - timestamp))
        if timestamp == self.last_timestamp:
            self.sequence = (self.sequence + 1) & 4095
            if self.sequence == 0:
                timestamp = self.wait_for_next_millis()
        else:
            self.sequence = 0
        self.last_timestamp = timestamp
        return (self.datacenter_id << 12) | (self.worker_id << 12) | (timestamp << 12) | self.sequence

    def wait_for_next_millis(self):
        timestamp = int(time.time() * 1000)
        while timestamp <= self.last_timestamp:
            timestamp = int(time.time() * 1000)
        return timestamp


idGenerator = IdGenerator()

if __name__ == '__main__':
    print(idGenerator.generate_id())
