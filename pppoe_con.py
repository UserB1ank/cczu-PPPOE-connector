import wmi

c = wmi.WMI()
ncm = c.Win32_NetworkConnectionManager()
