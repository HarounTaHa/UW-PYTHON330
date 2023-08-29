import socket


class Stream:

    def __init__(self, stream):
        self._stream = stream

    def process(self):
        """
        :return: int
        """

        count = 0  # How many two-digit numbers the `process` method has added
        # together.
        total = 0  # The running total of sums.

        while count < 10 and total < 200:
            digits = self._stream.read(2)
            if len(digits) < 2:
                break

            count += 1

            n = int(digits)
            total += n

        return count


def get_constants(prefix):
    """filtered mapping of socket module constants to their names"""
    return {
        getattr(socket, name): name
        for name in dir(socket) if name.startswith(prefix)
    }


def get_address_info(host, port):
    families = get_constants('AF_INET')
    types = get_constants('SOCK_STREAM')
    protocols = get_constants('IPPROTO_IP')
    for response in socket.getaddrinfo(host, port):
        family, s_type, protocol, name, address = response
        print('family: {}'.format(families[family]))
        print('type: {}'.format(types[s_type]))
        print('protocol: {}'.format(protocols[protocol]))
        print('canonical name: {}'.format(name))
        print('socket address: {}'.format(address))
        print('')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    number = Stream(open('text.txt', 'r')).process()
    print(number)
    socket.getaddrinfo('info.cern.ch', 'http')
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_IP)
    client.connect(('188.184.100.182', 80))
    msg = "GET / HTTP/1.1\r\n"
    msg += "Host: info.cern.ch\r\n\r\n"
    msg = msg.encode('utf8')
    client.sendall(msg)
    response = client.recv(64)
    print(response)
    response = client.recv(64)
    print(response)

