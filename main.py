#The Python program takes a packet capture file (packet.pcap) as input, processes the network 
#traffic data contained within, and extracts source and destination IP addresses 
#By Pranav K. Rao

import dpkt    #python module that allows simple packet parsing
import socket  #used to communicate and send small messages across network
import pygeoip #allows you to retrieve geographic information from IP address

gi = pygeoip.GeoIP('GeoLiteCity.dat') #.dat file is database that matches all IP address

#this is the function that maps and organizes the .KML file
def retKML(dstip, srcip):
    dst = gi.record_by_name(dstip)
    src = gi.record_by_name(srcip)
    try:
        dstlongitude = dst['longitude'] #longitutde
        dstlatitude = dst['latitude']   
        srclongitude = src['longitude']
        srclatitude = src['latitude']
        kml = (
            '<Placemark>\n'
            '<name>%s</name>\n'
            '<extrude>1</extrude>\n'
            '<tessellate>1</tessellate>\n'
            '<styleUrl>#transGeo</styleUrl>\n'
            '<LineString>\n'
            '<coordinates>%6f,%6f\n%6f,%6f</coordinates>\n'
            '</LineString>\n'
            '</Placemark>\n'
        ) % (dstip, dstlongitude, dstlatitude, srclongitude, srclatitude)
        return kml
    except:
        return ''

#This function is for extracting the data in the packet capture file, like source and destination
def plotIPs(pcap, srcip):
    kmlPts = ''
    for (ts, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data #extract the IP address
            src = socket.inet_ntoa(ip.src) #extract the source(which is manually inputed)
            dst = socket.inet_ntoa(ip.dst) #extract the destinations
            KML = retKML(dst, srcip)
            kmlPts = kmlPts + KML
        except:
            pass
    return kmlPts

#main function
def main():
    f = open('packet.pcap', 'rb') #allows the file to be read in binary format
    pcap = dpkt.pcap.Reader(f) 

    #this formating the KML Files: Which are a a format used to display geographical data; color, witdth
    kmlheader = '<?xml version="1.0" encoding="UTF-8"?> \n<kml xmlns="http://www.opengis.net/kml/2.2">\n<Document>\n' \
                '<Style id="transGeo">' \
                '<LineStyle>' \
                '<width>1.5</width>' \
                '<color>501400E6</color>' \
                '</LineStyle>' \
                '</Style>'
    kmlfooter = '</Document>\n</kml>\n'

    #calling the .KML document format function and in this case statically adding the source IP 
    kmldoc = kmlheader + plotIPs(pcap, '108.44.218.129') + kmlfooter

    #outputing to a .kml file 
    with open('output.kml', 'w') as kmlfile:
        kmlfile.write(kmldoc)


if __name__ == '__main__':
    main()