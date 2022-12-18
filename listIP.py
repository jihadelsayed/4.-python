def get_all_ips(self):
        """
        Get a list that can be iterated over that includes every IP address currently
        configured in this scanner.
        :return: A list that can be iterated over that includes every IP address currently
        configured in this scanner.
        """
        to_return = []
        for address in self.ipv4_addresses:
            to_return.append(IPAddress(address))
        for range_start, range_end in self.ipv4_ranges:
            to_return.append(IPRange(range_start, range_end))
        for network in self.ipv4_networks:
            to_return.append(IPNetwork(network))
        return to_return 