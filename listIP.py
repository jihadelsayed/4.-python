from ipaddr import IPAddress
import netifaces


# def get_all_ips(self):
#         """
#         Get a list that can be iterated over that includes every IP address currently
#         configured in this scanner.
#         :return: A list that can be iterated over that includes every IP address currently
#         configured in this scanner.
#         """
#         to_return = []
#         for address in self.ipv4_addresses:
#             to_return.append(ipaddress(address))
#         for range_start, range_end in self.ipv4_ranges:
#             to_return.append(IPRange(range_start, range_end))
#         for network in self.ipv4_networks:
#             to_return.append(ipaddress.ip_network(network))
#         return to_return 
def ipaddress_from_string(ip_address_string):
    """
    Parse an IPv4 or IPv6 address string and return an
    IPAddress instance.
    Remove the "embedded scope id" from IPv6 addresses (if there is
    one).

    :param str ip_address_string: The IP address string to be parsed.
    :returns: An ``ipaddr.IPAddress`` instance.
    """
    # There may be an embedded scope id in an IPv6 address. Discard
    # it. Eg fe80::f816:3eff:fe11:ca54%eth0
    parts = ip_address_string.rsplit('%', 1)
    ip_address_string = parts[0]
    return IPAddress(ip_address_string)

def get_all_ips():
    """
    Find all IPs for this machine.

    :return: ``set`` of IP addresses (``IPAddress``).
    """
    ips = set()
    interfaces = netifaces.interfaces()
    for interface in interfaces:
        addresses = netifaces.ifaddresses(interface)
        for address_family in (netifaces.AF_INET, netifaces.AF_INET6):
            family_addresses = addresses.get(address_family)
            if not family_addresses:
                continue
            for address in family_addresses:
                ips.add(ipaddress_from_string(address['addr']))
    return ips 