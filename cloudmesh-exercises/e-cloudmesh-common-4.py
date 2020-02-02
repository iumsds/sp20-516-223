# fa20-516-223 E.Cloudmesh.Common.4

from cloudmesh.common.Shell import Shell
from cloudmesh.common.StopWatch import StopWatch

StopWatch.start("cmshelp")
# Get cms help.
cms_help = Shell.cms("help")
print(cms_help)
StopWatch.stop("cmshelp")

# print(StopWatch.get("cmshelp"))

StopWatch.benchmark()
