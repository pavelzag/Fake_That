import semver

from maestro import __version__

ver = semver.VersionInfo.parse(__version__)
print(ver.major)
