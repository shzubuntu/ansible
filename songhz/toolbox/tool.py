import nmap
import telnetlib

class Network:
    def __init__(self,host_net=None):
        self.host_net=host_net
        self.hosts_up=[]
        self.hosts_ssh=[]
        self.hosts_other=[]
        self.scanhosts(host_net)

    def get_hosts_up(self):
        #return self.hosts_up
        return self.hosts_up

    def get_hosts_ssh(self):
        #return self.hosts_ssh
        return self.hosts_ssh

    def get_hosts_other(self):
        #return self.hosts_other
        return self.hosts_other

    def scanhosts(self,host_net):
        host_net=self.host_net
        nm = nmap.PortScanner()
        nm.scan(hosts=host_net, arguments='-n -sP -PE -PA')
        self.hosts_up= nm.all_hosts()
        for ip in self.hosts_up:
            try:
                tm = telnetlib.Telnet(host=ip, port='22', timeout=4)
                info = tm.read_until("\n", timeout=5)
                self.hosts_ssh.append(ip)
            except:
                self.hosts_other.append(ip)

if __name__ == "__main__":
    net = "192.168.31.0/24"
    network = Network(net);
    network.get_hosts_up();
    network.get_hosts_ssh();
    network.get_hosts_other();
