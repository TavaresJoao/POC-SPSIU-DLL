import ctypes
from ctypes import wintypes

lib_msxfs = ctypes.CDLL("../LIB/DLL/msxfs.dll")
# lib_spsiu = ctypes.CDLL("../LIB/DLL/spsiu.dll")


class WFSVERSION(ctypes.Structure):
    _fields_ = [
        ("wVersion", ctypes.c_ushort),
        ("wLowVersion", ctypes.c_ushort),
        ("wHighVersion", ctypes.c_ushort),
        ("szDescription", ctypes.c_char * 257),
        ("szSystemStatus", ctypes.c_char * 257)
    ]


def ShowHRsesultXfsVersion(hresult, _xfs_version):
    print("WFSStartUp Result: {}".format(hresult))
    print("Description: {}".format(_xfs_version.szDescription))
    print("SystemStatus: {}".format(_xfs_version.szSystemStatus))
    print("HighVersion: {}".format(hex(_xfs_version.wHighVersion)))
    print("LowVersion: {}".format(hex(_xfs_version.wLowVersion)))
    print("Version: {}\n".format(hex(_xfs_version.wVersion)))


def ShwWFSOpenResult(hresult, _hservice, _xfs_version, _sp_version):
    print("WFSOpen Result: {}".format(hresult))
    print("hService: {}".format(_hservice))

    print("\nXFS Version")
    print("\tDescription: {}".format(_xfs_version.szDescription))
    print("\tSystemStatus: {}".format(_xfs_version.szSystemStatus))
    print("\tHighVersion: {}".format(hex(_xfs_version.wHighVersion)))
    print("\tLowVersion: {}".format(hex(_xfs_version.wLowVersion)))
    print("\tVersion: {}".format(hex(_xfs_version.wVersion)))

    print("\nSP Version")
    print("\tDescription: {}".format(_sp_version.szDescription))
    print("\tSystemStatus: {}".format(_sp_version.szSystemStatus))
    print("\tHighVersion: {}".format(hex(_sp_version.wHighVersion)))
    print("\tLowVersion: {}".format(hex(_sp_version.wLowVersion)))
    print("\tVersion: {}".format(hex(_sp_version.wVersion)))


if __name__ == "__main__":
    xfs_version_start = WFSVERSION()
    xfs_version_open = WFSVERSION()
    sp_version = WFSVERSION()
    hService = ctypes.c_ushort()

    hResult = lib_msxfs.WFSStartUp(wintypes.DWORD(0x00030003), ctypes.byref(xfs_version_start))
    ShowHRsesultXfsVersion(hResult, xfs_version_start)

    sensores = wintypes.LPSTR("Sensores".encode('utf-8'))
    BRXFSTEST = wintypes.LPSTR("BRXFSTEST".encode('utf-8'))

    WFS_DEFAULT_HAPP = ctypes.c_int(0)
    traceLevel = wintypes.DWORD(0)
    timeout = wintypes.DWORD(5000)
    versionOpen = wintypes.DWORD(0x00030303)

    hResult = lib_msxfs.WFSOpen(
        sensores,
        WFS_DEFAULT_HAPP,
        BRXFSTEST,
        traceLevel,
        timeout,
        versionOpen,
        ctypes.byref(xfs_version_open),
        ctypes.byref(sp_version),
        ctypes.byref(hService)
    )

    ShwWFSOpenResult(hResult, hService, xfs_version_open, sp_version)

    lib_msxfs.WFSClose(hService)
