import ctypes
from ctypes import wintypes

#typedef struct _wfsversion
#{
#    WORD            wVersion;
#    WORD            wLowVersion;
#    WORD            wHighVersion;
#    CHAR            szDescription[WFSDDESCRIPTION_LEN+1];
#    CHAR            szSystemStatus[WFSDSYSSTATUS_LEN+1];
#} WFSVERSION, * LPWFSVERSION;


class WFSVERSION(ctypes.Structure):
    _fields_ = [
        ("wVersion", ctypes.c_ushort),
        ("wLowVersion", ctypes.c_ushort),
        ("wHighVersion", ctypes.c_ushort),
        ("szDescription", ctypes.c_char * 100),
        ("szSystemStatus", ctypes.c_char * 100)
    ]


lib_msxfs = ctypes.CDLL("../LIB/DLL/msxfs.dll")
lib_spsiu = ctypes.CDLL("../LIB/DLL/spsiu.dll")

#1 Startup
xfs_version = WFSVERSION()

hResult = lib_msxfs.WFSStartUp(wintypes.DWORD(0x00030003), ctypes.byref(xfs_version))
print("hResult {}".format(hResult))
print("wVersion {}".format(xfs_version.wVersion))
print("wLowVersion {}".format(xfs_version.wLowVersion))
print("wHighVersion {}".format(xfs_version.wHighVersion))
print("szDescription {}".format(xfs_version.szDescription))
print("szSystemStatus {}".format(xfs_version.szSystemStatus))


#2 WFPOpen 
sp_version = WFSVERSION()
hService = ctypes.c_ushort(0)
logicalName = wintypes.LPSTR("Sensores".encode('utf-8'))
appId = wintypes.LPSTR("BRXFSTEST".encode('utf-8'))
WFS_DEFAULT_HAPP = ctypes.c_int(0)
traceLevel = wintypes.DWORD(0)
timeOut = wintypes.DWORD(5000)
srvcVersion = wintypes.DWORD(0x00030303)

hResult = lib_msxfs.WFSOpen(
        logicalName,
        WFS_DEFAULT_HAPP,
        appId,
        traceLevel,
        timeOut,
        srvcVersion,
        ctypes.byref(xfs_version),
        ctypes.byref(sp_version),
        ctypes.byref(hService) 
    )

# fecha o servico aberto acima
lib_spsiu.WFPClose(hService)

