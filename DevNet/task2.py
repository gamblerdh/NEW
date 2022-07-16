from ncclient import manager
import xml.dom.minidom

def get_config_info():
    m =  manager.connect(host="sandbox-iosxe-recomm-1.cisco.com",
                            port="830",
                            username="developer",
                            password="C1sco12345",
                            device_params={'name':"csr"})

    hostname_filter = '''
                        <filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
                            <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                            </native>
                        </filter>
                        '''
    xmlDom = xml.dom.minidom.parseString( str( m.get_config('running', hostname_filter)))
    result = xmlDom.toprettyxml( indent = "  " )
    return result