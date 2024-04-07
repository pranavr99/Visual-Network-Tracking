# Visual-Network-Tracking

This Python script reads packet capture data from a pcap file, extracts source and destination IP addresses, and generates a KML file for visualization of geolocated IPs.

## Requirements
- Python 3.x
- dpkt library
- pygeoip library

## Installation
1. Install Python 3.x from [python.org](https://www.python.org/downloads/).
2. Install required libraries using pip:
    ```
    pip install dpkt pygeoip
    ```

## Usage
1. Place your pcap file named `packet.pcap` in the same directory as the script.
2. Run the script:
    ```
    python geolocation_plotter.py
    ```
3. The script will generate an output KML file named `output.kml` in the same directory.

## Description
- `retKML(dstip, srcip)`: Retrieves latitude and longitude for given source and destination IP addresses and returns KML string for plotting.
- `plotIPs(pcap, srcip)`: Iterates through packets in pcap file, extracts source and destination IPs, and generates KML points for plotting.
- `main()`: Main function to read pcap file, generate KML header, call `plotIPs`, and write output to KML file.

## Notes
- This script utilizes the GeoLiteCity database (`GeoLiteCity.dat`) for IP geolocation.
- Ensure the pcap file contains relevant network traffic data for accurate plotting.
- Update the `srcip` parameter in `main()` function to plot IPs originating from a specific source.

## Disclaimer
- This script is provided for educational and informational purposes only. Usage of this script may be subject to legal restrictions. Ensure compliance with applicable laws and regulations when using this script.
